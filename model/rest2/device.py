# coding: utf-8
from model.serializable import SwaggerSerializable


class Device(SwaggerSerializable):
    swagger_types = {
        'type': 'str',
        'category': 'str',
        'serial_number': 'str',
        'firmware_version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'category': 'category',
        'serial_number': 'serialNumber',
        'firmware_version': 'firmwareVersion'
    }

    def __init__(self, type=None, category='ATTENDED', serial_number=None, firmware_version=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._category = None
        self._serial_number = None
        self._firmware_version = None
        self.discriminator = None
        self.type = type
        if category is not None:
            self.category = category
        if serial_number is not None:
            self.serial_number = serial_number
        if firmware_version is not None:
            self.firmware_version = firmware_version

    @property
    def type(self):
        """Gets the type of this Device.  # noqa: E501

        Type/Model of the point-of-sale terminal.  # noqa: E501

        :return: The type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Device.

        Type/Model of the point-of-sale terminal.  # noqa: E501

        :param type: The type of this Device.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def category(self):
        """Gets the category of this Device.  # noqa: E501


        :return: The category of this Device.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Device.


        :param category: The category of this Device.  # noqa: E501
        :type: str
        """
        allowed_values = ["ATTENDED", "UNATTENDED"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def serial_number(self):
        """Gets the serial_number of this Device.  # noqa: E501

        Serial number of the point-of-sale terminal.  # noqa: E501

        :return: The serial_number of this Device.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this Device.

        Serial number of the point-of-sale terminal.  # noqa: E501

        :param serial_number: The serial_number of this Device.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def firmware_version(self):
        """Gets the firmware_version of this Device.  # noqa: E501

        Firmware version of the point-of-sale terminal.  # noqa: E501

        :return: The firmware_version of this Device.  # noqa: E501
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """Sets the firmware_version of this Device.

        Firmware version of the point-of-sale terminal.  # noqa: E501

        :param firmware_version: The firmware_version of this Device.  # noqa: E501
        :type: str
        """

        self._firmware_version = firmware_version
