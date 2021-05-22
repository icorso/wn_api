# coding: utf-8
from model.rest2.keyed_data_format import KeyedDataFormat
from model.serializable import SwaggerSerializable


class FullyEncryptedKeyedDataFormat(SwaggerSerializable):
    swagger_types = {
        'data_format': 'str',
        'device': 'EncryptionCapableDevice',
        'encrypted_data': 'str',
        'first_digit_of_pan': 'str'
    }
    if hasattr(KeyedDataFormat, "swagger_types"):
        swagger_types.update(KeyedDataFormat.swagger_types)

    attribute_map = {
        'data_format': 'dataFormat',
        'device': 'device',
        'encrypted_data': 'encryptedData',
        'first_digit_of_pan': 'firstDigitOfPan'
    }
    if hasattr(KeyedDataFormat, "attribute_map"):
        attribute_map.update(KeyedDataFormat.attribute_map)

    def __init__(self, data_format='PLAIN_TEXT', device=None, encrypted_data=None, first_digit_of_pan=None, *args, **kwargs):  # noqa: E501
        """FullyEncryptedKeyedDataFormat - a model defined in Swagger"""  # noqa: E501
        self._data_format = None
        self._device = None
        self._encrypted_data = None
        self._first_digit_of_pan = None
        self.discriminator = None
        if data_format is not None:
            self.data_format = data_format
        self.device = device
        self.encrypted_data = encrypted_data
        if first_digit_of_pan is not None:
            self.first_digit_of_pan = first_digit_of_pan

    @property
    def data_format(self):
        """Gets the data_format of this FullyEncryptedKeyedDataFormat.  # noqa: E501


        :return: The data_format of this FullyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this FullyEncryptedKeyedDataFormat.


        :param data_format: The data_format of this FullyEncryptedKeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._data_format = data_format

    @property
    def device(self):
        """Gets the device of this FullyEncryptedKeyedDataFormat.  # noqa: E501


        :return: The device of this FullyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: EncryptionCapableDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this FullyEncryptedKeyedDataFormat.


        :param device: The device of this FullyEncryptedKeyedDataFormat.  # noqa: E501
        :type: EncryptionCapableDevice
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def encrypted_data(self):
        """Gets the encrypted_data of this FullyEncryptedKeyedDataFormat.  # noqa: E501

        The full card data encrypted by the device.  # noqa: E501

        :return: The encrypted_data of this FullyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_data

    @encrypted_data.setter
    def encrypted_data(self, encrypted_data):
        """Sets the encrypted_data of this FullyEncryptedKeyedDataFormat.

        The full card data encrypted by the device.  # noqa: E501

        :param encrypted_data: The encrypted_data of this FullyEncryptedKeyedDataFormat.  # noqa: E501
        :type: str
        """
        if encrypted_data is None:
            raise ValueError("Invalid value for `encrypted_data`, must not be `None`")  # noqa: E501

        self._encrypted_data = encrypted_data

    @property
    def first_digit_of_pan(self):
        """Gets the first_digit_of_pan of this FullyEncryptedKeyedDataFormat.  # noqa: E501

        The first digit of the primary account number (PAN) / card number.  # noqa: E501

        :return: The first_digit_of_pan of this FullyEncryptedKeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._first_digit_of_pan

    @first_digit_of_pan.setter
    def first_digit_of_pan(self, first_digit_of_pan):
        """Sets the first_digit_of_pan of this FullyEncryptedKeyedDataFormat.

        The first digit of the primary account number (PAN) / card number.  # noqa: E501

        :param first_digit_of_pan: The first_digit_of_pan of this FullyEncryptedKeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._first_digit_of_pan = first_digit_of_pan
