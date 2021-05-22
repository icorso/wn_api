# coding: utf-8
from model.serializable import SwaggerSerializable


class TsysSaratogaDynamicDescriptor(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'prefix': 'str',
        'default_descriptor': 'str',
        'merchant_name': 'str',
        'merchant_phone': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'prefix': 'prefix',
        'default_descriptor': 'defaultDescriptor',
        'merchant_name': 'merchantName',
        'merchant_phone': 'merchantPhone'
    }

    def __init__(self, enable=False, prefix=None, default_descriptor=None, merchant_name=None, merchant_phone=None):  # noqa: E501
        self._enable = None
        self._prefix = None
        self._default_descriptor = None
        self._merchant_name = None
        self._merchant_phone = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if prefix is not None:
            self.prefix = prefix
        if default_descriptor is not None:
            self.default_descriptor = default_descriptor
        if merchant_name is not None:
            self.merchant_name = merchant_name
        if merchant_phone is not None:
            self.merchant_phone = merchant_phone

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        self._prefix = prefix

    @property
    def default_descriptor(self):
        return self._default_descriptor

    @default_descriptor.setter
    def default_descriptor(self, default_descriptor):
        self._default_descriptor = default_descriptor

    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, merchant_name):
        self._merchant_name = merchant_name

    @property
    def merchant_phone(self):
        return self._merchant_phone

    @merchant_phone.setter
    def merchant_phone(self, merchant_phone):
        self._merchant_phone = merchant_phone

