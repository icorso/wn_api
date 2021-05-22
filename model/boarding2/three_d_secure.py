# coding: utf-8
from model.serializable import SwaggerSerializable


class ThreeDSecure(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'merchant_id': 'str',
        'password': 'str',
        'supported_cards': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'merchant_id': 'merchantId',
        'password': 'password',
        'supported_cards': 'supportedCards'
    }

    def __init__(self, enable=False, merchant_id=None, password=None, supported_cards=None):  # noqa: E501
        self._enable = None
        self._merchant_id = None
        self._password = None
        self._supported_cards = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if password is not None:
            self.password = password
        if supported_cards is not None:
            self.supported_cards = supported_cards

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        self._merchant_id = merchant_id

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def supported_cards(self):
        return self._supported_cards

    @supported_cards.setter
    def supported_cards(self, supported_cards):
        self._supported_cards = supported_cards

