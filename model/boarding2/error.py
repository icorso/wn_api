# coding: utf-8

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
        self._debug_identifier = debug_identifier

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")

        self._details = details
