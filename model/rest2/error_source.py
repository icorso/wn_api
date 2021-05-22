# coding: utf-8

import pprint

import six


class ErrorSource(object):
    swagger_types = {
        'location': 'str',
        'resource': 'str',
        '_property': 'str',
        'value': 'str',
        'expected': 'str'
    }

    attribute_map = {
        'location': 'location',
        'resource': 'resource',
        '_property': 'property',
        'value': 'value',
        'expected': 'expected'
    }

    def __init__(self, location=None, resource=None, _property=None, value=None, expected=None):
        self._location = None
        self._resource = None
        self.__property = None
        self._value = None
        self._expected = None
        self.discriminator = None
        self.location = location
        if resource is not None:
            self.resource = resource
        if _property is not None:
            self._property = _property
        if value is not None:
            self.value = value
        if expected is not None:
            self.expected = expected

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")
        allowed_values = ["HEADER", "BODY", "PATH", "QUERY"]
        if location not in allowed_values:
            raise ValueError("Invalid value for `location` ({0}), must be one of {1}".format(location, allowed_values))

        self._location = location

    @property
    def resource(self):
        return self._resource

    @resource.setter
    def resource(self, resource):
        self._resource = resource

    @property
    def _property(self):
        return self.__property

    @_property.setter
    def _property(self, _property):
        self.__property = _property

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def expected(self):
        return self._expected

    @expected.setter
    def expected(self, expected):
        self._expected = expected

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
        if issubclass(ErrorSource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def __eq__(self, other):
        if not isinstance(other, ErrorSource):
            return False

        return self.__dict__ == other.__dict__
