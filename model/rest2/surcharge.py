# coding: utf-8

from model.serializable import SwaggerSerializable


class Surcharge(SwaggerSerializable):
    swagger_types = {
        'applied': 'bool',
        'amount': 'float',
        'percentage': 'float'
    }

    attribute_map = {
        'applied': 'applied',
        'amount': 'amount',
        'percentage': 'percentage'
    }

    def __init__(self, applied=None, amount=None, percentage=None):  # noqa: E501
        """Surcharge - a model defined in Swagger"""  # noqa: E501
        self._applied = None
        self._amount = None
        self._percentage = None
        self.discriminator = None
        if applied is not None:
            self.applied = applied
        if amount is not None:
            self.amount = amount
        if percentage is not None:
            self.percentage = percentage

    @property
    def applied(self):
        """Gets the applied of this Surcharge.  # noqa: E501

        Indicates whether or not a surcharge fee is applied to the total amount.  # noqa: E501

        :return: The applied of this Surcharge.  # noqa: E501
        :rtype: bool
        """
        return self._applied

    @applied.setter
    def applied(self, applied):
        """Sets the applied of this Surcharge.

        Indicates whether or not a surcharge fee is applied to the total amount.  # noqa: E501

        :param applied: The applied of this Surcharge.  # noqa: E501
        :type: bool
        """

        self._applied = applied

    @property
    def amount(self):
        """Gets the amount of this Surcharge.  # noqa: E501

        Surcharge amount. This field is only available in the response and it'll be populated whenever a surcharge fee is applied to the transaction.  # noqa: E501

        :return: The amount of this Surcharge.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Surcharge.

        Surcharge amount. This field is only available in the response and it'll be populated whenever a surcharge fee is applied to the transaction.  # noqa: E501

        :param amount: The amount of this Surcharge.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def percentage(self):
        """Gets the percentage of this Surcharge.  # noqa: E501

        Surcharge percentage. This field is only available in the response and it'll be populated whenever a surcharge fee is applied to the transaction.  # noqa: E501

        :return: The percentage of this Surcharge.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Surcharge.

        Surcharge percentage. This field is only available in the response and it'll be populated whenever a surcharge fee is applied to the transaction.  # noqa: E501

        :param percentage: The percentage of this Surcharge.  # noqa: E501
        :type: float
        """

        self._percentage = percentage
