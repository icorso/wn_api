# coding: utf-8
from model.serializable import SwaggerSerializable


class TerminalAchProcessing(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool'
    }

    attribute_map = {
        'enable': 'enable'
    }

    def __init__(self, enable=False):  # noqa: E501
        self._enable = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

