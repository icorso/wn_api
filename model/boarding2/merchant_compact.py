# coding: utf-8

from model.serializable import SwaggerSerializable


class MerchantCompact(SwaggerSerializable):
    swagger_types = {
        'merchant_id': 'str',
        'dba_name': 'str',
        'gateway_host': 'str',
        'contact_name': 'str',
        'contact_phone': 'str',
        'contact_email': 'str',
        'links': 'list[HypermediaLink]'
    }

    attribute_map = {
        'merchant_id': 'merchantId',
        'dba_name': 'dbaName',
        'gateway_host': 'gatewayHost',
        'contact_name': 'contactName',
        'contact_phone': 'contactPhone',
        'contact_email': 'contactEmail',
        'links': 'links'
    }

    def __init__(self, merchant_id=None, dba_name=None, gateway_host=None, contact_name=None, contact_phone=None, contact_email=None, links=None):  # noqa: E501
        """MerchantCompact - a model defined in Swagger"""  # noqa: E501
        self._merchant_id = None
        self._dba_name = None
        self._gateway_host = None
        self._contact_name = None
        self._contact_phone = None
        self._contact_email = None
        self._links = None
        self.discriminator = None
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if dba_name is not None:
            self.dba_name = dba_name
        if gateway_host is not None:
            self.gateway_host = gateway_host
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_phone is not None:
            self.contact_phone = contact_phone
        if contact_email is not None:
            self.contact_email = contact_email
        if links is not None:
            self.links = links

    @property
    def merchant_id(self):
        """Gets the merchant_id of this MerchantCompact.  # noqa: E501


        :return: The merchant_id of this MerchantCompact.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this MerchantCompact.


        :param merchant_id: The merchant_id of this MerchantCompact.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def dba_name(self):
        """Gets the dba_name of this MerchantCompact.  # noqa: E501


        :return: The dba_name of this MerchantCompact.  # noqa: E501
        :rtype: str
        """
        return self._dba_name

    @dba_name.setter
    def dba_name(self, dba_name):
        """Sets the dba_name of this MerchantCompact.


        :param dba_name: The dba_name of this MerchantCompact.  # noqa: E501
        :type: str
        """

        self._dba_name = dba_name

    @property
    def gateway_host(self):
        """Gets the gateway_host of this MerchantCompact.  # noqa: E501


        :return: The gateway_host of this MerchantCompact.  # noqa: E501
        :rtype: str
        """
        return self._gateway_host

    @gateway_host.setter
    def gateway_host(self, gateway_host):
        """Sets the gateway_host of this MerchantCompact.


        :param gateway_host: The gateway_host of this MerchantCompact.  # noqa: E501
        :type: str
        """

        self._gateway_host = gateway_host

    @property
    def contact_name(self):
        """Gets the contact_name of this MerchantCompact.  # noqa: E501


        :return: The contact_name of this MerchantCompact.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this MerchantCompact.


        :param contact_name: The contact_name of this MerchantCompact.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_phone(self):
        """Gets the contact_phone of this MerchantCompact.  # noqa: E501


        :return: The contact_phone of this MerchantCompact.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this MerchantCompact.


        :param contact_phone: The contact_phone of this MerchantCompact.  # noqa: E501
        :type: str
        """

        self._contact_phone = contact_phone

    @property
    def contact_email(self):
        """Gets the contact_email of this MerchantCompact.  # noqa: E501


        :return: The contact_email of this MerchantCompact.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this MerchantCompact.


        :param contact_email: The contact_email of this MerchantCompact.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def links(self):
        """Gets the links of this MerchantCompact.  # noqa: E501

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :return: The links of this MerchantCompact.  # noqa: E501
        :rtype: list[HypermediaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MerchantCompact.

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :param links: The links of this MerchantCompact.  # noqa: E501
        :type: list[HypermediaLink]
        """

        self._links = links

