# coding: utf-8

from model.serializable import SwaggerSerializable


class PaymentFacilitator(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'sub_merchant_name': 'str',
        'sub_merchant_identifier': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'sub_merchant_name': 'subMerchantName',
        'sub_merchant_identifier': 'subMerchantIdentifier'
    }

    def __init__(self, enable=False, sub_merchant_name=None, sub_merchant_identifier=None):  # noqa: E501
        """PaymentFacilitator - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._sub_merchant_name = None
        self._sub_merchant_identifier = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if sub_merchant_name is not None:
            self.sub_merchant_name = sub_merchant_name
        if sub_merchant_identifier is not None:
            self.sub_merchant_identifier = sub_merchant_identifier

    @property
    def enable(self):
        """Gets the enable of this PaymentFacilitator.  # noqa: E501


        :return: The enable of this PaymentFacilitator.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PaymentFacilitator.


        :param enable: The enable of this PaymentFacilitator.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def sub_merchant_name(self):
        """Gets the sub_merchant_name of this PaymentFacilitator.  # noqa: E501


        :return: The sub_merchant_name of this PaymentFacilitator.  # noqa: E501
        :rtype: str
        """
        return self._sub_merchant_name

    @sub_merchant_name.setter
    def sub_merchant_name(self, sub_merchant_name):
        """Sets the sub_merchant_name of this PaymentFacilitator.


        :param sub_merchant_name: The sub_merchant_name of this PaymentFacilitator.  # noqa: E501
        :type: str
        """

        self._sub_merchant_name = sub_merchant_name

    @property
    def sub_merchant_identifier(self):
        """Gets the sub_merchant_identifier of this PaymentFacilitator.  # noqa: E501


        :return: The sub_merchant_identifier of this PaymentFacilitator.  # noqa: E501
        :rtype: str
        """
        return self._sub_merchant_identifier

    @sub_merchant_identifier.setter
    def sub_merchant_identifier(self, sub_merchant_identifier):
        """Sets the sub_merchant_identifier of this PaymentFacilitator.


        :param sub_merchant_identifier: The sub_merchant_identifier of this PaymentFacilitator.  # noqa: E501
        :type: str
        """

        self._sub_merchant_identifier = sub_merchant_identifier

