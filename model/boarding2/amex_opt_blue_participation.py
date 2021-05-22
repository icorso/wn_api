# coding: utf-8
from model.serializable import SwaggerSerializable


class AmexOptBlueParticipation(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'merchant_street_address': 'str',
        'industry_service_establishment': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'merchant_street_address': 'merchantStreetAddress',
        'industry_service_establishment': 'industryServiceEstablishment'
    }

    def __init__(self, enable=False, merchant_street_address=None, industry_service_establishment=None):  # noqa: E501
        """AmexOptBlueParticipation - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._merchant_street_address = None
        self._industry_service_establishment = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if merchant_street_address is not None:
            self.merchant_street_address = merchant_street_address
        if industry_service_establishment is not None:
            self.industry_service_establishment = industry_service_establishment

    @property
    def enable(self):
        """Gets the enable of this AmexOptBlueParticipation.  # noqa: E501


        :return: The enable of this AmexOptBlueParticipation.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AmexOptBlueParticipation.


        :param enable: The enable of this AmexOptBlueParticipation.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def merchant_street_address(self):
        """Gets the merchant_street_address of this AmexOptBlueParticipation.  # noqa: E501


        :return: The merchant_street_address of this AmexOptBlueParticipation.  # noqa: E501
        :rtype: str
        """
        return self._merchant_street_address

    @merchant_street_address.setter
    def merchant_street_address(self, merchant_street_address):
        """Sets the merchant_street_address of this AmexOptBlueParticipation.


        :param merchant_street_address: The merchant_street_address of this AmexOptBlueParticipation.  # noqa: E501
        :type: str
        """

        self._merchant_street_address = merchant_street_address

    @property
    def industry_service_establishment(self):
        """Gets the industry_service_establishment of this AmexOptBlueParticipation.  # noqa: E501


        :return: The industry_service_establishment of this AmexOptBlueParticipation.  # noqa: E501
        :rtype: str
        """
        return self._industry_service_establishment

    @industry_service_establishment.setter
    def industry_service_establishment(self, industry_service_establishment):
        """Sets the industry_service_establishment of this AmexOptBlueParticipation.


        :param industry_service_establishment: The industry_service_establishment of this AmexOptBlueParticipation.  # noqa: E501
        :type: str
        """

        self._industry_service_establishment = industry_service_establishment
