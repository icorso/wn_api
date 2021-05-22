# coding: utf-8

from model.serializable import SwaggerSerializable


class SurchargeSettings(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'percentage': 'float'
    }

    attribute_map = {
        'enable': 'enable',
        'percentage': 'percentage'
    }

    def __init__(self, enable=False, percentage=None):  # noqa: E501
        """SurchargeSettings - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._percentage = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if percentage is not None:
            self.percentage = percentage

    @property
    def enable(self):
        """Gets the enable of this SurchargeSettings.  # noqa: E501


        :return: The enable of this SurchargeSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this SurchargeSettings.


        :param enable: The enable of this SurchargeSettings.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def percentage(self):
        """Gets the percentage of this SurchargeSettings.  # noqa: E501


        :return: The percentage of this SurchargeSettings.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this SurchargeSettings.


        :param percentage: The percentage of this SurchargeSettings.  # noqa: E501
        :type: float
        """

        self._percentage = percentage
