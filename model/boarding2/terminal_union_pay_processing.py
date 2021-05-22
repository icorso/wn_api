# coding: utf-8
from model.serializable import SwaggerSerializable


class TerminalUnionPayProcessing(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'merchant_id': 'str',
        'merchant_name': 'str',
        'merchant_abbreviation': 'str',
        'merchant_category_code': 'str',
        'draft256_billing': 'Draft256Billing'
    }

    attribute_map = {
        'enable': 'enable',
        'merchant_id': 'merchantId',
        'merchant_name': 'merchantName',
        'merchant_abbreviation': 'merchantAbbreviation',
        'merchant_category_code': 'merchantCategoryCode',
        'draft256_billing': 'draft256Billing'
    }

    def __init__(self, enable=False, merchant_id=None, merchant_name=None, merchant_abbreviation=None, merchant_category_code=None, draft256_billing=None):  # noqa: E501
        self._enable = None
        self._merchant_id = None
        self._merchant_name = None
        self._merchant_abbreviation = None
        self._merchant_category_code = None
        self._draft256_billing = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if merchant_name is not None:
            self.merchant_name = merchant_name
        if merchant_abbreviation is not None:
            self.merchant_abbreviation = merchant_abbreviation
        if merchant_category_code is not None:
            self.merchant_category_code = merchant_category_code
        if draft256_billing is not None:
            self.draft256_billing = draft256_billing

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
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, merchant_name):
        self._merchant_name = merchant_name

    @property
    def merchant_abbreviation(self):
        return self._merchant_abbreviation

    @merchant_abbreviation.setter
    def merchant_abbreviation(self, merchant_abbreviation):
        self._merchant_abbreviation = merchant_abbreviation

    @property
    def merchant_category_code(self):
        return self._merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, merchant_category_code):
        self._merchant_category_code = merchant_category_code

    @property
    def draft256_billing(self):
        return self._draft256_billing

    @draft256_billing.setter
    def draft256_billing(self, draft256_billing):
        self._draft256_billing = draft256_billing

