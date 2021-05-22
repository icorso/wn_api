# coding: utf-8
from model.serializable import SwaggerSerializable

import six


class Address(SwaggerSerializable):
    swagger_types = {
        'line1': 'str',
        'line2': 'str',
        'postal_code': 'str',
        'city': 'str',
        'state': 'str',
        'country': 'str'
    }

    attribute_map = {
        'line1': 'line1',
        'line2': 'line2',
        'postal_code': 'postalCode',
        'city': 'city',
        'state': 'state',
        'country': 'country'
    }

    def __init__(self, line1=None, line2=None, postal_code=None, city=None, state=None, country=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._line1 = None
        self._line2 = None
        self._postal_code = None
        self._city = None
        self._state = None
        self._country = None
        self.discriminator = None
        if line1 is not None:
            self.line1 = line1
        if line2 is not None:
            self.line2 = line2
        if postal_code is not None:
            self.postal_code = postal_code
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country

    @property
    def line1(self):
        """Gets the line1 of this Address.  # noqa: E501

        The first line of the address.<br />This field is used for AVS checks along with `city` and `postalCode`.  # noqa: E501

        :return: The line1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """Sets the line1 of this Address.

        The first line of the address.<br />This field is used for AVS checks along with `city` and `postalCode`.  # noqa: E501

        :param line1: The line1 of this Address.  # noqa: E501
        :type: str
        """

        self._line1 = line1

    @property
    def line2(self):
        """Gets the line2 of this Address.  # noqa: E501

        The second line of the address, if any.  # noqa: E501

        :return: The line2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """Sets the line2 of this Address.

        The second line of the address, if any.  # noqa: E501

        :param line2: The line2 of this Address.  # noqa: E501
        :type: str
        """

        self._line2 = line2

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501

        The address's ZIP or postal code.  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.

        The address's ZIP or postal code.  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        The city or town of the address.  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        The city or town of the address.  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Address.  # noqa: E501

        The state, county, province, or region.  # noqa: E501

        :return: The state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Address.

        The state, county, province, or region.  # noqa: E501

        :param state: The state of this Address.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501

        The two-letter country code defined by [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard.  # noqa: E501

        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.

        The two-letter country code defined by [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard.  # noqa: E501

        :param country: The country of this Address.  # noqa: E501
        :type: str
        """

        self._country = country
