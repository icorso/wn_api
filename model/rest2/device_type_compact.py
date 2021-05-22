# coding: utf-8
from model.serializable import SwaggerSerializable


class DeviceTypeCompact(SwaggerSerializable):
    swagger_types = {
        'type': 'str',
        'manufacturer': 'str',
        'links': 'list[HypermediaLink]'
    }

    attribute_map = {
        'type': 'type',
        'manufacturer': 'manufacturer',
        'links': 'links'
    }

    def __init__(self, type=None, manufacturer=None, links=None):  # noqa: E501
        """DeviceTypeCompact - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._manufacturer = None
        self._links = None
        self.discriminator = None
        self.type = type
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if links is not None:
            self.links = links

    @property
    def type(self):
        """Gets the type of this DeviceTypeCompact.  # noqa: E501

        Type of device.  # noqa: E501

        :return: The type of this DeviceTypeCompact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceTypeCompact.

        Type of device.  # noqa: E501

        :param type: The type of this DeviceTypeCompact.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def manufacturer(self):
        """Gets the manufacturer of this DeviceTypeCompact.  # noqa: E501

        Company responsible for manufacturing the devices of this type.  # noqa: E501

        :return: The manufacturer of this DeviceTypeCompact.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this DeviceTypeCompact.

        Company responsible for manufacturing the devices of this type.  # noqa: E501

        :param manufacturer: The manufacturer of this DeviceTypeCompact.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def links(self):
        """Gets the links of this DeviceTypeCompact.  # noqa: E501

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :return: The links of this DeviceTypeCompact.  # noqa: E501
        :rtype: list[HypermediaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DeviceTypeCompact.

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :param links: The links of this DeviceTypeCompact.  # noqa: E501
        :type: list[HypermediaLink]
        """

        self._links = links
