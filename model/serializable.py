# coding: utf-8
import datetime
import json
import pprint
from copy import deepcopy

import six


class SwaggerSerializable(object):

    @classmethod
    def get_class(cls):
        return cls

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types

    def serialize(self):
        obj = deepcopy(self)
        return self.sanitize_for_serialization(obj)

    def sanitize_for_serialization(self, obj):
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in six.iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: self.sanitize_for_serialization(val) for key, val in six.iteritems(obj_dict)}

    def json(self, allow_nan=False, pretty_print=True):
        indent = 2 if pretty_print else None
        return json.dumps(self.serialize(), allow_nan=allow_nan, indent=indent, ensure_ascii=False)

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(self.get_class(), dict):
            for key, value in self.items():
                result[key] = value

        return result

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.get_class()):
            return False

        return self.__dict__ == other.__dict__

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __ne__(self, other):
        return not self == other
