import json
import re
from xml.dom.minidom import parseString

from lxml import etree
from xmltodict import parse, unparse


class Serializable(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # hack to fix _json.so make_encoder serialize properly
        self.__setitem__('dummy', 1)

        for k, v in kwargs.items():
            setattr(self, k, v)

    def _myattrs(self):
        return [
            (x, self._repr(getattr(self, x)))
            for x in self.__dir__()
            if x not in Serializable().__dir__()
        ]

    def _repr(self, value):
        # return value
        if isinstance(value, (str, int, float, list, tuple, dict)):
            return value
        else:
            return repr(value)

    def __repr__(self):
        return '<%s.%s object at %s>' % (
            self.__class__.__module__,
            self.__class__.__name__,
            hex(id(self))
        )

    def keys(self):
        return iter([x[0] for x in self._myattrs()])

    def values(self):
        return iter([x[1] for x in self._myattrs()])

    def items(self):
        return iter(self._myattrs())

    def to_json(self, allow_nan=False, pretty_print=True):
        indent = 2 if pretty_print else None
        return json.dumps(self, default=lambda o: o.__dict__, allow_nan=allow_nan, indent=indent)

    def from_json(self, json_string: str):
        self.__dict__ = json.loads(json_string)
        return self

    def to_xml(self, pretty_print=True, custom_root=None, namespace=None, no_header=False):
        header = '<?xml version="1.0" encoding="utf-8"?>\n' if pretty_print else '<?xml version="1.0" encoding="utf-8"?>'
        root = self.__class__.__name__ if not custom_root else custom_root
        if namespace:
            self.__dict__.update({'@xmlns': namespace})
        xml = parseString(unparse({root: self.__dict__}))
        xml = xml.toprettyxml(encoding='utf-8') if pretty_print else xml.toxml(encoding='utf-8')
        xml = xml.decode('utf-8')
        if no_header:
            xml = xml.replace(header, '')

        return xml

    def from_xml(self, xml_string: str):
        self.__dict__ = parse(xml_string)[self.__class__.__name__]
        return self


class HppSerializable(Serializable):
    def __init__(self, source):
        super().__init__()
        if type(source) == bytes:
            source = source.decode('utf-8')

            if 'Merchant -- Error' not in source:
                b = etree.HTML(source)
                body = b[1]
                children = list(body)
                for c in children:
                    a = c.text.split(' : ')
                    setattr(self, a[0], a[1])
            else:
                setattr(self, 'ERROR', re.findall('<font class="bold">(.*?)</font>', source)[0])
