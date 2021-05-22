# coding: utf-8

from model.serializable import SwaggerSerializable


class EncryptionCapableDevice(SwaggerSerializable):
    swagger_types = {
        'type': 'str',
        'data_ksn': 'str',
        'serial_number': 'str',
        'category': 'str'
    }

    attribute_map = {
        'type': 'type',
        'data_ksn': 'dataKsn',
        'serial_number': 'serialNumber',
        'category': 'category'
    }

    def __init__(self, type=None, data_ksn=None, serial_number=None, category='ATTENDED'):  # noqa: E501
        """EncryptionCapableDevice - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._data_ksn = None
        self._serial_number = None
        self._category = None
        self.discriminator = None
        self.type = type
        self.data_ksn = data_ksn
        if serial_number is not None:
            self.serial_number = serial_number
        if category is not None:
            self.category = category

    @property
    def type(self):
        """Gets the type of this EncryptionCapableDevice.  # noqa: E501


        :return: The type of this EncryptionCapableDevice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EncryptionCapableDevice.


        :param type: The type of this EncryptionCapableDevice.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def data_ksn(self):
        """Gets the data_ksn of this EncryptionCapableDevice.  # noqa: E501


        :return: The data_ksn of this EncryptionCapableDevice.  # noqa: E501
        :rtype: str
        """
        return self._data_ksn

    @data_ksn.setter
    def data_ksn(self, data_ksn):
        """Sets the data_ksn of this EncryptionCapableDevice.


        :param data_ksn: The data_ksn of this EncryptionCapableDevice.  # noqa: E501
        :type: str
        """
        if data_ksn is None:
            raise ValueError("Invalid value for `data_ksn`, must not be `None`")  # noqa: E501

        self._data_ksn = data_ksn

    @property
    def serial_number(self):
        """Gets the serial_number of this EncryptionCapableDevice.  # noqa: E501


        :return: The serial_number of this EncryptionCapableDevice.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this EncryptionCapableDevice.


        :param serial_number: The serial_number of this EncryptionCapableDevice.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def category(self):
        """Gets the category of this EncryptionCapableDevice.  # noqa: E501


        :return: The category of this EncryptionCapableDevice.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this EncryptionCapableDevice.


        :param category: The category of this EncryptionCapableDevice.  # noqa: E501
        :type: str
        """
        allowed_values = ["ATTENDED", "UNATTENDED"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category
