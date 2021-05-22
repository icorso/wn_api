# coding: utf-8
from model.serializable import SwaggerSerializable


class TerminalAchJackHenryProcessing(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'location_id': 'str',
        'merchant_id': 'str',
        'group_bank_name': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'location_id': 'locationId',
        'merchant_id': 'merchantId',
        'group_bank_name': 'groupBankName'
    }

    def __init__(self, enable=False, location_id=None, merchant_id=None, group_bank_name=None):  # noqa: E501
        """TerminalAchJackHenryProcessing - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._location_id = None
        self._merchant_id = None
        self._group_bank_name = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if location_id is not None:
            self.location_id = location_id
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if group_bank_name is not None:
            self.group_bank_name = group_bank_name

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def location_id(self):
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        self._location_id = location_id

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        self._merchant_id = merchant_id

    @property
    def group_bank_name(self):
        return self._group_bank_name

    @group_bank_name.setter
    def group_bank_name(self, group_bank_name):
        self._group_bank_name = group_bank_name

