# coding: utf-8
from model.serializable import SwaggerSerializable


class TsysSaratogaEnhancedData(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'enable_template_autofill': 'bool',
        'txn_data_level': 'str',
        'merchant_tax_id': 'str',
        'merchant_type_code': 'str',
        'preferred_shipping_address_mode': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'enable_template_autofill': 'enableTemplateAutofill',
        'txn_data_level': 'txnDataLevel',
        'merchant_tax_id': 'merchantTaxId',
        'merchant_type_code': 'merchantTypeCode',
        'preferred_shipping_address_mode': 'preferredShippingAddressMode'
    }

    def __init__(self, enable=False, enable_template_autofill=False, txn_data_level=None, merchant_tax_id=None, merchant_type_code=None, preferred_shipping_address_mode=None):  # noqa: E501
        self._enable = None
        self._enable_template_autofill = None
        self._txn_data_level = None
        self._merchant_tax_id = None
        self._merchant_type_code = None
        self._preferred_shipping_address_mode = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if enable_template_autofill is not None:
            self.enable_template_autofill = enable_template_autofill
        if txn_data_level is not None:
            self.txn_data_level = txn_data_level
        if merchant_tax_id is not None:
            self.merchant_tax_id = merchant_tax_id
        if merchant_type_code is not None:
            self.merchant_type_code = merchant_type_code
        if preferred_shipping_address_mode is not None:
            self.preferred_shipping_address_mode = preferred_shipping_address_mode

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def enable_template_autofill(self):
        return self._enable_template_autofill

    @enable_template_autofill.setter
    def enable_template_autofill(self, enable_template_autofill):
        self._enable_template_autofill = enable_template_autofill

    @property
    def txn_data_level(self):
        return self._txn_data_level

    @txn_data_level.setter
    def txn_data_level(self, txn_data_level):
        allowed_values = ["STANDARD", "LEVEL_II", "LEVEL_III"]  # noqa: E501
        if txn_data_level not in allowed_values:
            raise ValueError(
                "Invalid value for `txn_data_level` ({0}), must be one of {1}"  # noqa: E501
                .format(txn_data_level, allowed_values)
            )

        self._txn_data_level = txn_data_level

    @property
    def merchant_tax_id(self):
        return self._merchant_tax_id

    @merchant_tax_id.setter
    def merchant_tax_id(self, merchant_tax_id):
        self._merchant_tax_id = merchant_tax_id

    @property
    def merchant_type_code(self):
        return self._merchant_type_code

    @merchant_type_code.setter
    def merchant_type_code(self, merchant_type_code):
        self._merchant_type_code = merchant_type_code

    @property
    def preferred_shipping_address_mode(self):
        return self._preferred_shipping_address_mode

    @preferred_shipping_address_mode.setter
    def preferred_shipping_address_mode(self, preferred_shipping_address_mode):
        allowed_values = ["EXACT", "POSTAL"]  # noqa: E501
        if preferred_shipping_address_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `preferred_shipping_address_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(preferred_shipping_address_mode, allowed_values)
            )

        self._preferred_shipping_address_mode = preferred_shipping_address_mode

