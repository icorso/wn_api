# coding: utf-8
from model.serializable import SwaggerSerializable


class TransactionReceipt(SwaggerSerializable):
    swagger_types = {
        'copy': 'str',
        'header': 'str',
        'merchant_details': 'list[ReceiptOrderedInfo]',
        'transaction_data': 'list[ReceiptOrderedInfo]',
        'custom_fields': 'list[CustomField]',
        'icc_data': 'list[ReceiptOrderedInfo]',
        'footer': 'str',
        'terms_and_conditions': 'str'
    }

    attribute_map = {
        'copy': 'copy',
        'header': 'header',
        'merchant_details': 'merchantDetails',
        'transaction_data': 'transactionData',
        'custom_fields': 'customFields',
        'icc_data': 'iccData',
        'footer': 'footer',
        'terms_and_conditions': 'termsAndConditions'
    }

    def __init__(self, copy=None, header=None, merchant_details=None, transaction_data=None, custom_fields=None, icc_data=None, footer=None, terms_and_conditions=None):  # noqa: E501
        """TransactionReceipt - a model defined in Swagger"""  # noqa: E501
        self._copy = None
        self._header = None
        self._merchant_details = None
        self._transaction_data = None
        self._custom_fields = None
        self._icc_data = None
        self._footer = None
        self._terms_and_conditions = None
        self.discriminator = None
        self.copy = copy
        self.header = header
        self.merchant_details = merchant_details
        self.transaction_data = transaction_data
        self.custom_fields = custom_fields
        self.icc_data = icc_data
        self.footer = footer
        if terms_and_conditions is not None:
            self.terms_and_conditions = terms_and_conditions

    @property
    def copy(self):
        """Gets the copy of this TransactionReceipt.  # noqa: E501


        :return: The copy of this TransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._copy

    @copy.setter
    def copy(self, copy):
        """Sets the copy of this TransactionReceipt.


        :param copy: The copy of this TransactionReceipt.  # noqa: E501
        :type: str
        """
        if copy is None:
            raise ValueError("Invalid value for `copy`, must not be `None`")  # noqa: E501
        allowed_values = ["CARDHOLDER_COPY", "CARD_ACCEPTOR_COPY"]  # noqa: E501
        if copy not in allowed_values:
            raise ValueError(
                "Invalid value for `copy` ({0}), must be one of {1}"  # noqa: E501
                .format(copy, allowed_values)
            )

        self._copy = copy

    @property
    def header(self):
        """Gets the header of this TransactionReceipt.  # noqa: E501


        :return: The header of this TransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this TransactionReceipt.


        :param header: The header of this TransactionReceipt.  # noqa: E501
        :type: str
        """
        if header is None:
            raise ValueError("Invalid value for `header`, must not be `None`")  # noqa: E501

        self._header = header

    @property
    def merchant_details(self):
        """Gets the merchant_details of this TransactionReceipt.  # noqa: E501


        :return: The merchant_details of this TransactionReceipt.  # noqa: E501
        :rtype: list[ReceiptOrderedInfo]
        """
        return self._merchant_details

    @merchant_details.setter
    def merchant_details(self, merchant_details):
        """Sets the merchant_details of this TransactionReceipt.


        :param merchant_details: The merchant_details of this TransactionReceipt.  # noqa: E501
        :type: list[ReceiptOrderedInfo]
        """
        if merchant_details is None:
            raise ValueError("Invalid value for `merchant_details`, must not be `None`")  # noqa: E501

        self._merchant_details = merchant_details

    @property
    def transaction_data(self):
        """Gets the transaction_data of this TransactionReceipt.  # noqa: E501


        :return: The transaction_data of this TransactionReceipt.  # noqa: E501
        :rtype: list[ReceiptOrderedInfo]
        """
        return self._transaction_data

    @transaction_data.setter
    def transaction_data(self, transaction_data):
        """Sets the transaction_data of this TransactionReceipt.


        :param transaction_data: The transaction_data of this TransactionReceipt.  # noqa: E501
        :type: list[ReceiptOrderedInfo]
        """
        if transaction_data is None:
            raise ValueError("Invalid value for `transaction_data`, must not be `None`")  # noqa: E501

        self._transaction_data = transaction_data

    @property
    def custom_fields(self):
        """Gets the custom_fields of this TransactionReceipt.  # noqa: E501


        :return: The custom_fields of this TransactionReceipt.  # noqa: E501
        :rtype: list[CustomField]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this TransactionReceipt.


        :param custom_fields: The custom_fields of this TransactionReceipt.  # noqa: E501
        :type: list[CustomField]
        """
        if custom_fields is None:
            raise ValueError("Invalid value for `custom_fields`, must not be `None`")  # noqa: E501

        self._custom_fields = custom_fields

    @property
    def icc_data(self):
        """Gets the icc_data of this TransactionReceipt.  # noqa: E501


        :return: The icc_data of this TransactionReceipt.  # noqa: E501
        :rtype: list[ReceiptOrderedInfo]
        """
        return self._icc_data

    @icc_data.setter
    def icc_data(self, icc_data):
        """Sets the icc_data of this TransactionReceipt.


        :param icc_data: The icc_data of this TransactionReceipt.  # noqa: E501
        :type: list[ReceiptOrderedInfo]
        """
        if icc_data is None:
            raise ValueError("Invalid value for `icc_data`, must not be `None`")  # noqa: E501

        self._icc_data = icc_data

    @property
    def footer(self):
        """Gets the footer of this TransactionReceipt.  # noqa: E501


        :return: The footer of this TransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """Sets the footer of this TransactionReceipt.


        :param footer: The footer of this TransactionReceipt.  # noqa: E501
        :type: str
        """
        if footer is None:
            raise ValueError("Invalid value for `footer`, must not be `None`")  # noqa: E501

        self._footer = footer

    @property
    def terms_and_conditions(self):
        """Gets the terms_and_conditions of this TransactionReceipt.  # noqa: E501


        :return: The terms_and_conditions of this TransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, terms_and_conditions):
        """Sets the terms_and_conditions of this TransactionReceipt.


        :param terms_and_conditions: The terms_and_conditions of this TransactionReceipt.  # noqa: E501
        :type: str
        """

        self._terms_and_conditions = terms_and_conditions
