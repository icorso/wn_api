# coding: utf-8

import six

from model.serializable import SwaggerSerializable


class ErrorDetail(SwaggerSerializable):
    swagger_types = {
        'error_code': 'str',
        'error_message': 'str',
        'about': 'str',
        'source': 'ErrorSource'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'about': 'about',
        'source': 'source'
    }

    def __init__(self, error_code=None, error_message=None, about=None, source=None):
        self._error_code = None
        self._error_message = None
        self._about = None
        self._source = None
        self.discriminator = None
        self.error_code = error_code
        self.error_message = error_message
        if about is not None:
            self.about = about
        if source is not None:
            self.source = source

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")

        self._error_code = error_code

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")

        self._error_message = error_message

    @property
    def about(self):
        return self._about

    @about.setter
    def about(self, about):
        self._about = about

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        self._source = source

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
        if issubclass(ErrorDetail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def __eq__(self, other):
        if not isinstance(other, ErrorDetail):
            return False

        return self.__dict__ == other.__dict__
