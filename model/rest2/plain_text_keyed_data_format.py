# coding: utf-8
from model.rest2 import KeyedDataFormat
from model.serializable import SwaggerSerializable


class PlainTextKeyedDataFormat(SwaggerSerializable):
    swagger_types = {
        'data_format': 'str',
        'device': 'Device',
        'card_number': 'str',
        'expiry_date': 'str',
        'cvv': 'str',
        'issue_number': 'str'
    }
    if hasattr(KeyedDataFormat, "swagger_types"):
        swagger_types.update(KeyedDataFormat.swagger_types)

    attribute_map = {
        'data_format': 'dataFormat',
        'device': 'device',
        'card_number': 'cardNumber',
        'expiry_date': 'expiryDate',
        'cvv': 'cvv',
        'issue_number': 'issueNumber'
    }
    if hasattr(KeyedDataFormat, "attribute_map"):
        attribute_map.update(KeyedDataFormat.attribute_map)

    def __init__(self, data_format='PLAIN_TEXT', device=None, card_number=None, expiry_date=None, cvv=None, issue_number=None, *args, **kwargs):  # noqa: E501
        """PlainTextKeyedDataFormat - a model defined in Swagger"""  # noqa: E501
        self._data_format = None
        self._device = None
        self._card_number = None
        self._expiry_date = None
        self._cvv = None
        self._issue_number = None
        self.discriminator = None
        if data_format is not None:
            self.data_format = data_format
        if device is not None:
            self.device = device
        self.card_number = card_number
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if cvv is not None:
            self.cvv = cvv
        if issue_number is not None:
            self.issue_number = issue_number
        KeyedDataFormat.__init__(self, *args, **kwargs)

    @property
    def data_format(self):
        """Gets the data_format of this PlainTextKeyedDataFormat.  # noqa: E501


        :return: The data_format of this PlainTextKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this PlainTextKeyedDataFormat.


        :param data_format: The data_format of this PlainTextKeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._data_format = data_format

    @property
    def device(self):
        """Gets the device of this PlainTextKeyedDataFormat.  # noqa: E501


        :return: The device of this PlainTextKeyedDataFormat.  # noqa: E501
        :rtype: Device
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PlainTextKeyedDataFormat.


        :param device: The device of this PlainTextKeyedDataFormat.  # noqa: E501
        :type: Device
        """

        self._device = device

    @property
    def card_number(self):
        """Gets the card_number of this PlainTextKeyedDataFormat.  # noqa: E501

        The card number, as a string without any separators.  # noqa: E501

        :return: The card_number of this PlainTextKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this PlainTextKeyedDataFormat.

        The card number, as a string without any separators.  # noqa: E501

        :param card_number: The card_number of this PlainTextKeyedDataFormat.  # noqa: E501
        :type: str
        """
        if card_number is None:
            raise ValueError("Invalid value for `card_number`, must not be `None`")  # noqa: E501

        self._card_number = card_number

    @property
    def expiry_date(self):
        """Gets the expiry_date of this PlainTextKeyedDataFormat.  # noqa: E501

        The card's expiration date in the format `MMYY`. This field is mandatory in most cases except when performing electronic voucher transactions.  # noqa: E501

        :return: The expiry_date of this PlainTextKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this PlainTextKeyedDataFormat.

        The card's expiration date in the format `MMYY`. This field is mandatory in most cases except when performing electronic voucher transactions.  # noqa: E501

        :param expiry_date: The expiry_date of this PlainTextKeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._expiry_date = expiry_date

    @property
    def cvv(self):
        """Gets the cvv of this PlainTextKeyedDataFormat.  # noqa: E501

        The card's security code.  # noqa: E501

        :return: The cvv of this PlainTextKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """Sets the cvv of this PlainTextKeyedDataFormat.

        The card's security code.  # noqa: E501

        :param cvv: The cvv of this PlainTextKeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._cvv = cvv

    @property
    def issue_number(self):
        """Gets the issue_number of this PlainTextKeyedDataFormat.  # noqa: E501

        The card's issue number.  # noqa: E501

        :return: The issue_number of this PlainTextKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """Sets the issue_number of this PlainTextKeyedDataFormat.

        The card's issue number.  # noqa: E501

        :param issue_number: The issue_number of this PlainTextKeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._issue_number = issue_number
