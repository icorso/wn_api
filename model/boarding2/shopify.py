# coding: utf-8
from model.serializable import SwaggerSerializable


class Shopify(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'password': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'password': 'password'
    }

    def __init__(self, enable=False, password=None):  # noqa: E501
        self._enable = None
        self._password = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if password is not None:
            self.password = password

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
