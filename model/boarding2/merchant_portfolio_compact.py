# coding: utf-8

from model.serializable import SwaggerSerializable


class MerchantPortfolioCompact(SwaggerSerializable):
    swagger_types = {
        'merchant_portfolio_id': 'str',
        'name': 'str',
        'gateway': 'str',
        'contact_name': 'str',
        'contact_phone': 'str',
        'contact_email': 'str',
        'links': 'list[HypermediaLink]'
    }

    attribute_map = {
        'merchant_portfolio_id': 'merchantPortfolioId',
        'name': 'name',
        'gateway': 'gateway',
        'contact_name': 'contactName',
        'contact_phone': 'contactPhone',
        'contact_email': 'contactEmail',
        'links': 'links'
    }

    def __init__(self, merchant_portfolio_id=None, name=None, gateway=None, contact_name=None, contact_phone=None, contact_email=None, links=None):  # noqa: E501
        """MerchantPortfolioCompact - a model defined in Swagger"""  # noqa: E501
        self._merchant_portfolio_id = None
        self._name = None
        self._gateway = None
        self._contact_name = None
        self._contact_phone = None
        self._contact_email = None
        self._links = None
        self.discriminator = None
        if merchant_portfolio_id is not None:
            self.merchant_portfolio_id = merchant_portfolio_id
        if name is not None:
            self.name = name
        if gateway is not None:
            self.gateway = gateway
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_phone is not None:
            self.contact_phone = contact_phone
        if contact_email is not None:
            self.contact_email = contact_email
        if links is not None:
            self.links = links

    @property
    def merchant_portfolio_id(self):
        """Gets the merchant_portfolio_id of this MerchantPortfolioCompact.  # noqa: E501


        :return: The merchant_portfolio_id of this MerchantPortfolioCompact.  # noqa: E501
        :rtype: str
        """
        return self._merchant_portfolio_id

    @merchant_portfolio_id.setter
    def merchant_portfolio_id(self, merchant_portfolio_id):
        """Sets the merchant_portfolio_id of this MerchantPortfolioCompact.


        :param merchant_portfolio_id: The merchant_portfolio_id of this MerchantPortfolioCompact.  # noqa: E501
        :type: str
        """

        self._merchant_portfolio_id = merchant_portfolio_id

    @property
    def name(self):
        """Gets the name of this MerchantPortfolioCompact.  # noqa: E501


        :return: The name of this MerchantPortfolioCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MerchantPortfolioCompact.


        :param name: The name of this MerchantPortfolioCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def gateway(self):
        """Gets the gateway of this MerchantPortfolioCompact.  # noqa: E501


        :return: The gateway of this MerchantPortfolioCompact.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this MerchantPortfolioCompact.


        :param gateway: The gateway of this MerchantPortfolioCompact.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def contact_name(self):
        """Gets the contact_name of this MerchantPortfolioCompact.  # noqa: E501


        :return: The contact_name of this MerchantPortfolioCompact.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this MerchantPortfolioCompact.


        :param contact_name: The contact_name of this MerchantPortfolioCompact.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_phone(self):
        """Gets the contact_phone of this MerchantPortfolioCompact.  # noqa: E501


        :return: The contact_phone of this MerchantPortfolioCompact.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this MerchantPortfolioCompact.


        :param contact_phone: The contact_phone of this MerchantPortfolioCompact.  # noqa: E501
        :type: str
        """

        self._contact_phone = contact_phone

    @property
    def contact_email(self):
        """Gets the contact_email of this MerchantPortfolioCompact.  # noqa: E501


        :return: The contact_email of this MerchantPortfolioCompact.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this MerchantPortfolioCompact.


        :param contact_email: The contact_email of this MerchantPortfolioCompact.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def links(self):
        """Gets the links of this MerchantPortfolioCompact.  # noqa: E501

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :return: The links of this MerchantPortfolioCompact.  # noqa: E501
        :rtype: list[HypermediaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MerchantPortfolioCompact.

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :param links: The links of this MerchantPortfolioCompact.  # noqa: E501
        :type: list[HypermediaLink]
        """

        self._links = links

