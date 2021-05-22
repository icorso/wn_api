# coding: utf-8

from model.serializable import SwaggerSerializable


class MerchantCustomSettings(SwaggerSerializable):
    swagger_types = {
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):  # noqa: E501
        """MerchantCustomSettings - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._value = None
        self.discriminator = None
        self.name = name
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this MerchantCustomSettings.  # noqa: E501


        :return: The name of this MerchantCustomSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MerchantCustomSettings.


        :param name: The name of this MerchantCustomSettings.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this MerchantCustomSettings.  # noqa: E501


        :return: The value of this MerchantCustomSettings.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MerchantCustomSettings.


        :param value: The value of this MerchantCustomSettings.  # noqa: E501
        :type: str
        """

        self._value = value

