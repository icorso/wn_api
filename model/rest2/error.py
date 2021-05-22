# coding: utf-8

import six

from model.serializable import SwaggerSerializable


class Error(SwaggerSerializable):
    swagger_types = {
        'debug_identifier': 'str',
        'details': 'list[ErrorDetail]'
    }

    attribute_map = {
        'debug_identifier': 'debugIdentifier',
        'details': 'details'
    }

    def __init__(self, debug_identifier=None, details=None):
        self._debug_identifier = None
        self._details = None
        self.discriminator = None
        self.debug_identifier = debug_identifier
        self.details = details

    @property
    def debug_identifier(self):
        return self._debug_identifier

    @debug_identifier.setter
    def debug_identifier(self, debug_identifier):
        if debug_identifier is None:
            raise ValueError("Invalid value for `debug_identifier`, must not be `None`")

        self._debug_identifier = debug_identifier

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")

        self._details = details

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
        if issubclass(Error, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def __eq__(self, other):
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__
