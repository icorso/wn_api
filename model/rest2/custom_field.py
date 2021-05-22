# coding: utf-8
from model.serializable import SwaggerSerializable


class CustomField(SwaggerSerializable):
    swagger_types = {
        'value': 'str',
        'name': 'str'
    }

    attribute_map = {
        'value': 'value',
        'name': 'name'
    }

    def __init__(self, value=None, name=None):  # noqa: E501
        """CustomField - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._name = None
        self.discriminator = None
        self.value = value
        self.name = name

    @property
    def value(self):
        """Gets the value of this CustomField.  # noqa: E501


        :return: The value of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomField.


        :param value: The value of this CustomField.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def name(self):
        """Gets the name of this CustomField.  # noqa: E501


        :return: The name of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomField.


        :param name: The name of this CustomField.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name
