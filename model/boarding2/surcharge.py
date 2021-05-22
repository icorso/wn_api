# coding: utf-8
from model.serializable import SwaggerSerializable


class Surcharge(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'percent': 'float'
    }

    attribute_map = {
        'enable': 'enable',
        'percent': 'percent'
    }

    def __init__(self, enable=False, percent=None):  # noqa: E501
        """Surcharge - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._percent = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if percent is not None:
            self.percent = percent

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, percent):
        self._percent = percent
