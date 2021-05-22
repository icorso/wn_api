# coding: utf-8
from model.serializable import SwaggerSerializable


class CustomerAccount(SwaggerSerializable):
    swagger_types = {
        'card_type': 'str',
        'cardholder_name': 'str',
        'masked_pan': 'str',
        'expiry_date': 'str',
        'entry_method': 'str'
    }

    attribute_map = {
        'card_type': 'cardType',
        'cardholder_name': 'cardholderName',
        'masked_pan': 'maskedPan',
        'expiry_date': 'expiryDate',
        'entry_method': 'entryMethod'
    }

    def __init__(self, card_type=None, cardholder_name=None, masked_pan=None, expiry_date=None, entry_method=None):  # noqa: E501
        """CustomerAccount - a model defined in Swagger"""  # noqa: E501
        self._card_type = None
        self._cardholder_name = None
        self._masked_pan = None
        self._expiry_date = None
        self._entry_method = None
        self.discriminator = None
        if card_type is not None:
            self.card_type = card_type
        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if masked_pan is not None:
            self.masked_pan = masked_pan
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if entry_method is not None:
            self.entry_method = entry_method

    @property
    def card_type(self):
        """Gets the card_type of this CustomerAccount.  # noqa: E501

        The brand of the card used in the transaction.  # noqa: E501

        :return: The card_type of this CustomerAccount.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this CustomerAccount.

        The brand of the card used in the transaction.  # noqa: E501

        :param card_type: The card_type of this CustomerAccount.  # noqa: E501
        :type: str
        """

        self._card_type = card_type

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this CustomerAccount.  # noqa: E501

        The cardholder's name as it appears on the card.  # noqa: E501

        :return: The cardholder_name of this CustomerAccount.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this CustomerAccount.

        The cardholder's name as it appears on the card.  # noqa: E501

        :param cardholder_name: The cardholder_name of this CustomerAccount.  # noqa: E501
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def masked_pan(self):
        """Gets the masked_pan of this CustomerAccount.  # noqa: E501

        The card number masked with the character `*`.<br />According to PCI DSS, only the first six and last four digits may be displayed. For example: `548010******5929`  # noqa: E501

        :return: The masked_pan of this CustomerAccount.  # noqa: E501
        :rtype: str
        """
        return self._masked_pan

    @masked_pan.setter
    def masked_pan(self, masked_pan):
        """Sets the masked_pan of this CustomerAccount.

        The card number masked with the character `*`.<br />According to PCI DSS, only the first six and last four digits may be displayed. For example: `548010******5929`  # noqa: E501

        :param masked_pan: The masked_pan of this CustomerAccount.  # noqa: E501
        :type: str
        """

        self._masked_pan = masked_pan

    @property
    def expiry_date(self):
        """Gets the expiry_date of this CustomerAccount.  # noqa: E501

        The card's expiration date in the format `MMYY`.  # noqa: E501

        :return: The expiry_date of this CustomerAccount.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this CustomerAccount.

        The card's expiration date in the format `MMYY`.  # noqa: E501

        :param expiry_date: The expiry_date of this CustomerAccount.  # noqa: E501
        :type: str
        """

        self._expiry_date = expiry_date

    @property
    def entry_method(self):
        """Gets the entry_method of this CustomerAccount.  # noqa: E501

        The method used to capture the customer's account details.  # noqa: E501

        :return: The entry_method of this CustomerAccount.  # noqa: E501
        :rtype: str
        """
        return self._entry_method

    @entry_method.setter
    def entry_method(self, entry_method):
        """Sets the entry_method of this CustomerAccount.

        The method used to capture the customer's account details.  # noqa: E501

        :param entry_method: The entry_method of this CustomerAccount.  # noqa: E501
        :type: str
        """

        self._entry_method = entry_method
