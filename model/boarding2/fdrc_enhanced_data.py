# coding: utf-8

from model.serializable import SwaggerSerializable


class FdrcEnhancedData(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'enable_template_autofill': 'bool',
        'txn_data_level': 'str',
        'merchant_tax_id': 'str',
        'preferred_shipping_address_mode': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'enable_template_autofill': 'enableTemplateAutofill',
        'txn_data_level': 'txnDataLevel',
        'merchant_tax_id': 'merchantTaxId',
        'preferred_shipping_address_mode': 'preferredShippingAddressMode'
    }

    def __init__(self, enable=False, enable_template_autofill=False, txn_data_level=None, merchant_tax_id=None, preferred_shipping_address_mode=None):  # noqa: E501
        self._enable = None
        self._enable_template_autofill = None
        self._txn_data_level = None
        self._merchant_tax_id = None
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
        if preferred_shipping_address_mode is not None:
            self.preferred_shipping_address_mode = preferred_shipping_address_mode

    @property
    def enable(self):
        """Gets the enable of this FdrcEnhancedData.  # noqa: E501


        :return: The enable of this FdrcEnhancedData.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this FdrcEnhancedData.


        :param enable: The enable of this FdrcEnhancedData.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def enable_template_autofill(self):
        """Gets the enable_template_autofill of this FdrcEnhancedData.  # noqa: E501


        :return: The enable_template_autofill of this FdrcEnhancedData.  # noqa: E501
        :rtype: bool
        """
        return self._enable_template_autofill

    @enable_template_autofill.setter
    def enable_template_autofill(self, enable_template_autofill):
        """Sets the enable_template_autofill of this FdrcEnhancedData.


        :param enable_template_autofill: The enable_template_autofill of this FdrcEnhancedData.  # noqa: E501
        :type: bool
        """

        self._enable_template_autofill = enable_template_autofill

    @property
    def txn_data_level(self):
        """Gets the txn_data_level of this FdrcEnhancedData.  # noqa: E501


        :return: The txn_data_level of this FdrcEnhancedData.  # noqa: E501
        :rtype: str
        """
        return self._txn_data_level

    @txn_data_level.setter
    def txn_data_level(self, txn_data_level):
        """Sets the txn_data_level of this FdrcEnhancedData.


        :param txn_data_level: The txn_data_level of this FdrcEnhancedData.  # noqa: E501
        :type: str
        """
        allowed_values = ["STANDARD", "LEVEL_II", "LEVEL_III"]  # noqa: E501
        if txn_data_level not in allowed_values:
            raise ValueError(
                "Invalid value for `txn_data_level` ({0}), must be one of {1}"  # noqa: E501
                .format(txn_data_level, allowed_values)
            )

        self._txn_data_level = txn_data_level

    @property
    def merchant_tax_id(self):
        """Gets the merchant_tax_id of this FdrcEnhancedData.  # noqa: E501


        :return: The merchant_tax_id of this FdrcEnhancedData.  # noqa: E501
        :rtype: str
        """
        return self._merchant_tax_id

    @merchant_tax_id.setter
    def merchant_tax_id(self, merchant_tax_id):
        """Sets the merchant_tax_id of this FdrcEnhancedData.


        :param merchant_tax_id: The merchant_tax_id of this FdrcEnhancedData.  # noqa: E501
        :type: str
        """

        self._merchant_tax_id = merchant_tax_id

    @property
    def preferred_shipping_address_mode(self):
        """Gets the preferred_shipping_address_mode of this FdrcEnhancedData.  # noqa: E501


        :return: The preferred_shipping_address_mode of this FdrcEnhancedData.  # noqa: E501
        :rtype: str
        """
        return self._preferred_shipping_address_mode

    @preferred_shipping_address_mode.setter
    def preferred_shipping_address_mode(self, preferred_shipping_address_mode):
        """Sets the preferred_shipping_address_mode of this FdrcEnhancedData.


        :param preferred_shipping_address_mode: The preferred_shipping_address_mode of this FdrcEnhancedData.  # noqa: E501
        :type: str
        """
        allowed_values = ["EXACT", "POSTAL"]  # noqa: E501
        if preferred_shipping_address_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `preferred_shipping_address_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(preferred_shipping_address_mode, allowed_values)
            )

        self._preferred_shipping_address_mode = preferred_shipping_address_mode

