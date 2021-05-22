# coding: utf-8
from model.rest2.keyed_data_format import KeyedDataFormat
from model.serializable import SwaggerSerializable


class PartiallyEncryptedKeyedDataFormat(SwaggerSerializable):
    swagger_types = {
        'data_format': 'str',
        'device': 'EncryptionCapableDevice',
        'encrypted_pan': 'str',
        'masked_pan': 'str',
        'expiry_date': 'str',
        'cvv': 'str',
        'issue_number': 'str'
    }
    if hasattr(KeyedDataFormat, "swagger_types"):
        swagger_types.update(KeyedDataFormat.swagger_types)

    attribute_map = {
        'data_format': 'dataFormat',
        'device': 'device',
        'encrypted_pan': 'encryptedPan',
        'masked_pan': 'maskedPan',
        'expiry_date': 'expiryDate',
        'cvv': 'cvv',
        'issue_number': 'issueNumber'
    }
    if hasattr(KeyedDataFormat, "attribute_map"):
        attribute_map.update(KeyedDataFormat.attribute_map)

    def __init__(self, data_format='PLAIN_TEXT', device=None, encrypted_pan=None, masked_pan=None, expiry_date=None, cvv=None, issue_number=None, *args, **kwargs):  # noqa: E501
        """PartiallyEncryptedKeyedDataFormat - a model defined in Swagger"""  # noqa: E501
        self._data_format = None
        self._device = None
        self._encrypted_pan = None
        self._masked_pan = None
        self._expiry_date = None
        self._cvv = None
        self._issue_number = None
        self.discriminator = None
        if data_format is not None:
            self.data_format = data_format
        self.device = device
        self.encrypted_pan = encrypted_pan
        self.masked_pan = masked_pan
        self.expiry_date = expiry_date
        if cvv is not None:
            self.cvv = cvv
        if issue_number is not None:
            self.issue_number = issue_number
        KeyedDataFormat.__init__(self, *args, **kwargs)

    @property
    def data_format(self):
        """Gets the data_format of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501


        :return: The data_format of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this PartiallyEncryptedKeyedDataFormat.


        :param data_format: The data_format of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._data_format = data_format

    @property
    def device(self):
        """Gets the device of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501


        :return: The device of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: EncryptionCapableDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PartiallyEncryptedKeyedDataFormat.


        :param device: The device of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :type: EncryptionCapableDevice
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def encrypted_pan(self):
        """Gets the encrypted_pan of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501

        The primary account number (PAN) / card number encrypted by the device.  # noqa: E501

        :return: The encrypted_pan of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_pan

    @encrypted_pan.setter
    def encrypted_pan(self, encrypted_pan):
        """Sets the encrypted_pan of this PartiallyEncryptedKeyedDataFormat.

        The primary account number (PAN) / card number encrypted by the device.  # noqa: E501

        :param encrypted_pan: The encrypted_pan of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :type: str
        """
        if encrypted_pan is None:
            raise ValueError("Invalid value for `encrypted_pan`, must not be `None`")  # noqa: E501

        self._encrypted_pan = encrypted_pan

    @property
    def masked_pan(self):
        """Gets the masked_pan of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501

        The card number masked with the character `*`.<br />According to PCI DSS, only the first six and last four digits may be displayed. For example: `548010******5929`  # noqa: E501

        :return: The masked_pan of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._masked_pan

    @masked_pan.setter
    def masked_pan(self, masked_pan):
        """Sets the masked_pan of this PartiallyEncryptedKeyedDataFormat.

        The card number masked with the character `*`.<br />According to PCI DSS, only the first six and last four digits may be displayed. For example: `548010******5929`  # noqa: E501

        :param masked_pan: The masked_pan of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :type: str
        """
        if masked_pan is None:
            raise ValueError("Invalid value for `masked_pan`, must not be `None`")  # noqa: E501

        self._masked_pan = masked_pan

    @property
    def expiry_date(self):
        """Gets the expiry_date of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501

        The card's expiration date in the format `MMYY`.  # noqa: E501

        :return: The expiry_date of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this PartiallyEncryptedKeyedDataFormat.

        The card's expiration date in the format `MMYY`.  # noqa: E501

        :param expiry_date: The expiry_date of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :type: str
        """
        if expiry_date is None:
            raise ValueError("Invalid value for `expiry_date`, must not be `None`")  # noqa: E501

        self._expiry_date = expiry_date

    @property
    def cvv(self):
        """Gets the cvv of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501

        The card's security code.  # noqa: E501

        :return: The cvv of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """Sets the cvv of this PartiallyEncryptedKeyedDataFormat.

        The card's security code.  # noqa: E501

        :param cvv: The cvv of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._cvv = cvv

    @property
    def issue_number(self):
        """Gets the issue_number of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501

        The card's issue number.  # noqa: E501

        :return: The issue_number of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """Sets the issue_number of this PartiallyEncryptedKeyedDataFormat.

        The card's issue number.  # noqa: E501

        :param issue_number: The issue_number of this PartiallyEncryptedKeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._issue_number = issue_number
