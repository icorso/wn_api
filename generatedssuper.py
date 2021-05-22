# coding=utf-8
import base64
import datetime as datetime_
import hashlib
import json
import logging
import re as re_
import sys

from lxml import etree

from constants import Currency
from utils import logger


class GeneratedsSuper(object):
    multicurrency = False
    currency = None
    decimal_format = '%.6f'
    terminal_id = None

    def __recursive_dict(self, element):
        if element.text is None and len(element.attrib):
            return element.tag, element.attrib
        return element.tag, dict(map(self.__recursive_dict, element)) or element.text

    def xml(self, is_hashable=True):
        if is_hashable:
            self.update_hash_field()
        if hasattr(self, 'CURRENCY'):
            self.decimal_format = '%.{minorunits}f'.format(minorunits=Currency[self.CURRENCY].minorunits)

        ET = self.to_etree()
        if 'boarding' in str(self) or 'rest' in str(self):  # camel-case name for boarding and rest xml
            ET.tag = ET.tag.title()
        xml = etree.tostring(ET, pretty_print=True, xml_declaration=True, encoding='utf-8').decode('utf-8')
        return xml

    def json(self, indent=2, is_hashable=True):
        if is_hashable:
            self.update_hash_field()
        parsed_etree = self.__recursive_dict(self.to_etree())
        return json.dumps(parsed_etree[1], indent=indent)

    def to_hash(self, hash_fields):
        from decimal import Decimal
        hash_array = []

        if not self.multicurrency:
            try:
                if 'ADDSTOREDSUBSCRIPTION' not in str(self):
                    hash_fields.remove('CURRENCY')
            except ValueError:
                pass

        for field in hash_fields:
            attr = getattr(self, field)
            if attr is not None and attr != '':
                if hasattr(attr, 'hashes') and not isinstance(attr, list):
                    hash_array.extend(attr.hashes)
                    if attr.__class__.__name__ == 'refundReferenced':
                        hash_array.extend(['REFERENCED'])
                    if attr.__class__.__name__ == 'refundUnreferenced':
                        hash_array.extend(['UNREFERENCED'])
                else:
                    if field == 'AMOUNT':
                        try:
                            self.currency = self.CURRENCY  # format amount decimal field according to request's currency
                            self.decimal_format = '%.' + str(Currency[self.currency].minorunits) + 'f'
                        except (AttributeError, KeyError):
                            self.decimal_format = '%.2f'
                        attr = self.decimal_format % attr
                    if field == 'amount' and (isinstance(attr, Decimal) or isinstance(attr, float)):
                        try:
                            self.currency = self.amount.get_currency()
                        except AttributeError:
                            pass
                        attr = round(attr * pow(10, Currency[self.currency].minorunits))
                    if isinstance(attr, datetime_.date):
                        attr = str(attr).replace(' ', 'T')

                    if field == 'percentage':  # percentage tip
                        attr = round((attr * 100) * pow(10, Currency[self.currency].minorunits))

                    if isinstance(attr, list):
                        for l in attr:
                            i = 0
                            for h in l.hashes:
                                if field == 'tax':
                                    if i == 1:  # percentage subfield
                                        h = str(int(h) * 10000)
                                hash_array.append(h)
                                i += 1
                        attr = None

                    if attr:
                        hash_array.append(str(attr))
        return hash_array

    def generate_hash(self):
        hash_string = (':' if 'rest' in str(self) else '') + self.hash_string

        if hasattr(self, 'secret'):
            hash_string += ':' + str(self.secret)
        else:
            setattr(self, 'secret', 'someSecretPhrase')
            hash_string += ':' + str(self.secret)
        m = hashlib.sha512()
        m.update(str.encode(hash_string))
        return m.hexdigest()

    def update_hash_field(self):
        h = self.generate_hash()
        if hasattr(self, 'HASH'):     # upper case for xml
            self.HASH = h
        elif hasattr(self, 'hash'):   # lower case for rest
            try:
                import model.rest as r
                self.hash = r.hash()
                self.hash.messageDigestAlgorithm = r.messageDigestAlgorithm.SHA__512
                self.hash.digest = h
            except AttributeError:
                raise Exception('Hash field must be an instance of hash class. See model/rest.py for more details')
        else:
            logger.warning(logging.INFO, 'No hash or digest field')

    def with_secret(self, secret: str):
        setattr(self, 'secret', secret)
        return self

    def with_field(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self

    def without_field(self, *args):
        for i in args:
            if hasattr(self, i):
                setattr(self, i, None)
        return self

    def is_multicurrency(self, multicurrency: bool):
        """Function to setup terminal multicurrency
        :param multicurrency: bool
        :return: self: Super class filled with multicurrency attribute
                 True when any value set, False only when set 'False'
        """
        if multicurrency:
            self.multicurrency = multicurrency
        return self

    tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')

    class _FixedOffsetTZ(datetime_.tzinfo):
        def __init__(self, offset, name):
            self.__offset = datetime_.timedelta(minutes=offset)
            self.__name = name

        def utcoffset(self, dt):
            return self.__offset

        def tzname(self, dt):
            return self.__name

        def dst(self, dt):
            return None

    def gds_format_string(self, input_data, input_name=''):
        return input_data

    def gds_validate_string(self, input_data, node=None, input_name=''):
        if not input_data:
            return ''
        else:
            return input_data

    def gds_format_base64(self, input_data, input_name=''):
        return base64.b64encode(input_data)

    def gds_validate_base64(self, input_data, node=None, input_name=''):
        return input_data

    def gds_format_integer(self, input_data, input_name=''):
        return '%d' % input_data

    def gds_validate_integer(self, input_data, node=None, input_name=''):
        return input_data

    def gds_format_integer_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)

    def gds_validate_integer_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                int(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of integers')
        return values

    def gds_format_float(self, input_data, input_name=''):
        return '%.5f' % input_data

    def gds_validate_float(self, input_data, node=None, input_name=''):
        return input_data

    def gds_format_float_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)

    def gds_validate_float_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of floats')
        return values

    def gds_format_double(self, input_data, input_name=''):
        # return '%.3f' % input_data
        return self.decimal_format % input_data

    def gds_validate_double(self, input_data, node=None, input_name=''):
        return input_data

    def gds_format_double_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)

    def gds_validate_double_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of doubles')
        return values

    def gds_format_boolean(self, input_data, input_name=''):
        return ('%s' % input_data).lower()

    def gds_validate_boolean(self, input_data, node=None, input_name=''):
        return input_data

    def gds_format_boolean_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)

    def gds_validate_boolean_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            if value not in ('true', '1', 'false', '0',):
                raise_parse_error(
                    node,
                    'Requires sequence of booleans '
                    '("true", "1", "false", "0")')
        return values

    def gds_validate_datetime(self, input_data, node=None, input_name=''):
        return input_data

    def gds_format_datetime(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue

    @classmethod
    def gds_parse_datetime(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        time_parts = input_data.split('.')
        if len(time_parts) > 1:
            micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
            input_data = '%s.%s' % (time_parts[0], micro_seconds,)
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt

    def gds_validate_date(self, input_data, node=None, input_name=''):
        return input_data

    def gds_format_date(self, input_data, input_name=''):
        _svalue = '%04d-%02d-%02d' % (
            input_data.year,
            input_data.month,
            input_data.day,
        )
        try:
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(
                            hours, minutes)
        except AttributeError:
            pass
        return _svalue

    @classmethod
    def gds_parse_date(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
        dt = dt.replace(tzinfo=tz)
        return dt.date()

    def gds_validate_time(self, input_data, node=None, input_name=''):
        return input_data

    def gds_format_time(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%02d:%02d:%02d' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%02d:%02d:%02d.%s' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue

    def gds_validate_simple_patterns(self, patterns, target):
        # pat is a list of lists of strings/patterns.  We should:
        # - AND the outer elements
        # - OR the inner elements
        found1 = True
        for patterns1 in patterns:
            found2 = False
            for patterns2 in patterns1:
                if re_.search(patterns2, target) is not None:
                    found2 = True
                    break
            if not found2:
                found1 = False
                break
        return found1

    @classmethod
    def gds_parse_time(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split('.')) > 1:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt.time()

    def gds_str_lower(self, instring):
        return instring.lower()

    def get_path_(self, node):
        path_list = []
        self.get_path_list_(node, path_list)
        path_list.reverse()
        path = '/'.join(path_list)
        return path

    Tag_strip_pattern_ = re_.compile(r'\{.*\}')

    def get_path_list_(self, node, path_list):
        if node is None:
            return
        tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
        if tag:
            path_list.append(tag)
        self.get_path_list_(node.getparent(), path_list)

    def get_class_obj_(self, node, default_class=None):
        class_obj1 = default_class
        if 'xsi' in node.nsmap:
            classname = node.get('{%s}type' % node.nsmap['xsi'])
            if classname is not None:
                names = classname.split(':')
                if len(names) == 2:
                    classname = names[1]
                class_obj2 = globals().get(classname)
                if class_obj2 is not None:
                    class_obj1 = class_obj2
        return class_obj1

    def gds_build_any(self, node, type_name=None):
        return None

    @classmethod
    def gds_reverse_node_mapping(cls, mapping):
        return dict(((v, k) for k, v in mapping.iteritems()))

    @staticmethod
    def gds_encode(instring):
        if sys.version_info.major == 2:
            return instring.encode(ExternalEncoding)
        else:
            return instring

    @staticmethod
    def convert_unicode(instring):
        if isinstance(instring, str):
            result = quote_xml(instring)
        elif sys.version_info.major == 2 and isinstance(instring, unicode):
            result = quote_xml(instring).encode('utf8')
        else:
            result = GeneratedsSuper.gds_encode(str(instring))
        return result

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


def getSubclassFromModule_(module, class_):
    '''Get the subclass of a class from a specific module.'''
    name = class_.__name__ + 'Sub'
    if hasattr(module, name):
        return getattr(module, name)
    else:
        return None
