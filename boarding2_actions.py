import datetime
import json
import re

import six
from faker import Factory

from actions import BaseSource
from model import boarding2
from model.boarding2 import AccessToken
from model.boarding2 import ProcessingRule
from model.boarding2 import ProcessingRuleInstruction
from model.boarding2 import ProcessingRulePredicate

fake = Factory.create()


class Boarding2Source(BaseSource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = self._session.url + self._path + '/api/v2/boarding'
        self._session.with_headers({'Content-Type': 'application/json', 'Accept': 'application/json'})

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def deserialize(self, response, response_type):
        """Deserializes response into an object.
        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.
        :return: deserialized object.
        """
        if not 200 <= response.status_code <= 299:
        # if response.status_code not in (200, 201):
            response_type = "Error"

        # fetch data from response object
        try:
            data = json.loads(response.content.decode('utf-8'))
        except ValueError:
            data = response.data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.
        :param data: dict, list or str.
        :param klass: class literal, or string of class name.
        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(boarding2, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise Exception(
                "Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datatime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise Exception("Failed to parse `{0}` as datetime object".format(string))

    def __hasattr(self, object, name):
            return name in object.__class__.__dict__

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        if not klass.swagger_types and not self.__hasattr(klass, 'get_real_child_model'):
            return data

        kwargs = {}
        if klass.swagger_types is not None:
            for attr, attr_type in six.iteritems(klass.swagger_types):
                if (data is not None and
                        klass.attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)

        if (isinstance(instance, dict) and
                klass.swagger_types is not None and
                isinstance(data, dict)):
            for key, value in data.items():
                if key not in klass.swagger_types:
                    instance[key] = value
        if self.__hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance

    def authenticate(self, boarding2_key=None, silence=True):
        url = self.url + '/authenticate'
        response = self._session.with_method('get').with_url(url).with_headers(
            {'Authorization': 'Basic %s' % boarding2_key}).request
        access_token = self.deserialize(response, AccessToken)
        if not silence:
            print('\n' + url)
            print(self._session.headers)
            print(access_token.json())
        return access_token

    def get_terminal(self, merchant_id, terminal_number, response_type, boarding2_key, silence=True):
        token = self.authenticate(boarding2_key).token
        url = self.url + '/merchants/{0}/terminals/{1}'.format(merchant_id, terminal_number)
        response = self._session.with_method('get').with_url(url).with_headers({'Authorization': 'Bearer %s' % token}).request
        terminal = self.deserialize(response, response_type)
        if not silence:
            print(url)
            print("\nGET TERMINAL RESPONSE:\n")
            print(terminal.json())
        return terminal

    def get_terminal_template(self, terminal_name, response_type, boarding2_key):
        token = self.authenticate(boarding2_key).token
        url = self.url + '/templates/terminals/{0}'.format(terminal_name)
        response = self._session.with_method('get').with_url(url).with_headers({'Authorization': 'Bearer %s' % token}).request
        terminal = self.deserialize(response, response_type)
        print(url)
        print("\nGET TERMINAL TEMPLATE RESPONSE:\n")
        print(terminal.json())
        return terminal

    def create_terminal(self, merchant_id, request, response_type, boarding2_key, silence=True):
        token = self.authenticate(boarding2_key).token
        url = self.url + '/merchants/{merchantId}/terminals'.format(merchantId=merchant_id)
        response = self._session.with_method('post').with_url(url).with_headers({'Authorization': 'Bearer %s' % token})\
            .with_data(request.json()).request
        terminal = self.deserialize(response, response_type)
        if not silence:
            print(url)
            print("\nCREATE TERMINAL REQUEST:\n")
            print(request.json())
            print("\nCREATE TERMINAL RESPONSE:\n")
            print(terminal.json())
        return terminal

    def update_terminal(self, merchant_id, terminal_number, request, response_type, boarding2_key, silence=True):
        token = self.authenticate(boarding2_key).token
        url = self.url + '/merchants/{0}/terminals/{1}'.format(merchant_id, terminal_number)
        response = self._session.with_method('put').with_url(url).with_headers({'Authorization': 'Bearer %s' % token})\
            .with_data(request.json()).request
        terminal = self.deserialize(response, response_type)
        if not silence:
            print(url)
            print("\nREQUEST:\n")
            print(request.json())
            print("\nRESPONSE:\n")
            print(terminal.json())
        return terminal

    def update_processing_rules(self, merchant_id, terminal_number, response_type, boarding2_key,
                                to_terminal, enable=True, value='CREDIT_DEBIT', silence=True):
        pr = ProcessingRule(enable=enable, conditions=[ProcessingRulePredicate(when='TENDER_TYPE', _is='EQUALS',
                            value=value)], then=ProcessingRuleInstruction(action='ROUTE_TO_TERMINAL',
                                                                          terminal_number=to_terminal))
        terminal = self.get_terminal(merchant_id=merchant_id, terminal_number=terminal_number,
                                     response_type=response_type, boarding2_key=boarding2_key)
        terminal.processing_rules = [pr]
        terminal.secret = 'someSecretPhrase'

        response = self.update_terminal(merchant_id=merchant_id, terminal_number=terminal_number, request=terminal,
                                        response_type=response_type, boarding2_key=boarding2_key, silence=True)

        if not silence:
            print("\nREQUEST:\n")
            print(terminal.json())
            print("\nRESPONSE:\n")
            print(response.json())
        return terminal

    def deactivate_terminal(self, merchant_id, terminal_number, response_type, boarding2_key, silence=True):
        token = self.authenticate(boarding2_key).token
        url = self.url + '/merchants/{0}/terminals/{1}/deactivate'.format(merchant_id, terminal_number)
        response = self._session.with_method('patch').with_url(url).with_headers({'Authorization': 'Bearer %s' % token}).request
        terminal = self.deserialize(response, response_type)
        if not silence:
            print(url)
            print("\nREQUEST:\n")
            print(terminal.json())
            print("\nRESPONSE:\n")
            print(terminal.json())
        return terminal

    def activate_terminal(self, merchant_id, terminal_number, response_type, boarding2_key, silence=True):
        token = self.authenticate(boarding2_key).token
        url = self.url + '/merchants/{0}/terminals/{1}/activate'.format(merchant_id, terminal_number)
        response = self._session.with_method('patch').with_url(url).with_headers({'Authorization': 'Bearer %s' % token}).request
        terminal = self.deserialize(response, response_type)
        if not silence:
            print(url)
            print("\nREQUEST:\n")
            print(terminal.json())
            print("\nRESPONSE:\n")
            print(terminal.json())
        return terminal

    def get_user(self, merchant_id, login, response_type, boarding2_key, silence=True):
        token = self.authenticate(boarding2_key).token
        url = self.url + '/merchants/{0}/users/{1}'.format(merchant_id, login)
        response = self._session.with_method('get').with_url(url).with_headers({'Authorization': 'Bearer %s' % token}).request
        terminal = self.deserialize(response, response_type)
        if not silence:
            print(url)
            print("\nGET USER RESPONSE:\n")
            print(terminal.json())
        return terminal
