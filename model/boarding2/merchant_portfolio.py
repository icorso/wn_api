# coding: utf-8

from model.serializable import SwaggerSerializable


class MerchantPortfolio(SwaggerSerializable):
    swagger_types = {
        'name': 'str',
        'merchant_portfolio_id': 'str',
        'contact_name': 'str',
        'contact_phone': 'str',
        'contact_email': 'str',
        'deactivation_date': 'datetime',
        'enable_secure_card_uniqueness': 'bool',
        'enable_secure_card_auto_sharing': 'bool',
        'share_cards_from_deactivated_terminals': 'bool',
        'enable_secure_card_auto_registration': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'merchant_portfolio_id': 'merchantPortfolioId',
        'contact_name': 'contactName',
        'contact_phone': 'contactPhone',
        'contact_email': 'contactEmail',
        'deactivation_date': 'deactivationDate',
        'enable_secure_card_uniqueness': 'enableSecureCardUniqueness',
        'enable_secure_card_auto_sharing': 'enableSecureCardAutoSharing',
        'share_cards_from_deactivated_terminals': 'shareCardsFromDeactivatedTerminals',
        'enable_secure_card_auto_registration': 'enableSecureCardAutoRegistration'
    }

    def __init__(self, name=None, merchant_portfolio_id=None, contact_name=None, contact_phone=None, contact_email=None, deactivation_date=None, enable_secure_card_uniqueness=None, enable_secure_card_auto_sharing=None, share_cards_from_deactivated_terminals=None, enable_secure_card_auto_registration=None):  # noqa: E501
        """MerchantPortfolio - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._merchant_portfolio_id = None
        self._contact_name = None
        self._contact_phone = None
        self._contact_email = None
        self._deactivation_date = None
        self._enable_secure_card_uniqueness = None
        self._enable_secure_card_auto_sharing = None
        self._share_cards_from_deactivated_terminals = None
        self._enable_secure_card_auto_registration = None
        self.discriminator = None
        self.name = name
        if merchant_portfolio_id is not None:
            self.merchant_portfolio_id = merchant_portfolio_id
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        if deactivation_date is not None:
            self.deactivation_date = deactivation_date
        if enable_secure_card_uniqueness is not None:
            self.enable_secure_card_uniqueness = enable_secure_card_uniqueness
        if enable_secure_card_auto_sharing is not None:
            self.enable_secure_card_auto_sharing = enable_secure_card_auto_sharing
        if share_cards_from_deactivated_terminals is not None:
            self.share_cards_from_deactivated_terminals = share_cards_from_deactivated_terminals
        if enable_secure_card_auto_registration is not None:
            self.enable_secure_card_auto_registration = enable_secure_card_auto_registration

    @property
    def name(self):
        """Gets the name of this MerchantPortfolio.  # noqa: E501


        :return: The name of this MerchantPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MerchantPortfolio.


        :param name: The name of this MerchantPortfolio.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def merchant_portfolio_id(self):
        """Gets the merchant_portfolio_id of this MerchantPortfolio.  # noqa: E501


        :return: The merchant_portfolio_id of this MerchantPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._merchant_portfolio_id

    @merchant_portfolio_id.setter
    def merchant_portfolio_id(self, merchant_portfolio_id):
        """Sets the merchant_portfolio_id of this MerchantPortfolio.


        :param merchant_portfolio_id: The merchant_portfolio_id of this MerchantPortfolio.  # noqa: E501
        :type: str
        """

        self._merchant_portfolio_id = merchant_portfolio_id

    @property
    def contact_name(self):
        """Gets the contact_name of this MerchantPortfolio.  # noqa: E501


        :return: The contact_name of this MerchantPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this MerchantPortfolio.


        :param contact_name: The contact_name of this MerchantPortfolio.  # noqa: E501
        :type: str
        """
        if contact_name is None:
            raise ValueError("Invalid value for `contact_name`, must not be `None`")  # noqa: E501

        self._contact_name = contact_name

    @property
    def contact_phone(self):
        """Gets the contact_phone of this MerchantPortfolio.  # noqa: E501


        :return: The contact_phone of this MerchantPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this MerchantPortfolio.


        :param contact_phone: The contact_phone of this MerchantPortfolio.  # noqa: E501
        :type: str
        """
        if contact_phone is None:
            raise ValueError("Invalid value for `contact_phone`, must not be `None`")  # noqa: E501

        self._contact_phone = contact_phone

    @property
    def contact_email(self):
        """Gets the contact_email of this MerchantPortfolio.  # noqa: E501


        :return: The contact_email of this MerchantPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this MerchantPortfolio.


        :param contact_email: The contact_email of this MerchantPortfolio.  # noqa: E501
        :type: str
        """
        if contact_email is None:
            raise ValueError("Invalid value for `contact_email`, must not be `None`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def deactivation_date(self):
        """Gets the deactivation_date of this MerchantPortfolio.  # noqa: E501


        :return: The deactivation_date of this MerchantPortfolio.  # noqa: E501
        :rtype: datetime
        """
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        """Sets the deactivation_date of this MerchantPortfolio.


        :param deactivation_date: The deactivation_date of this MerchantPortfolio.  # noqa: E501
        :type: datetime
        """

        self._deactivation_date = deactivation_date

    @property
    def enable_secure_card_uniqueness(self):
        """Gets the enable_secure_card_uniqueness of this MerchantPortfolio.  # noqa: E501


        :return: The enable_secure_card_uniqueness of this MerchantPortfolio.  # noqa: E501
        :rtype: bool
        """
        return self._enable_secure_card_uniqueness

    @enable_secure_card_uniqueness.setter
    def enable_secure_card_uniqueness(self, enable_secure_card_uniqueness):
        """Sets the enable_secure_card_uniqueness of this MerchantPortfolio.


        :param enable_secure_card_uniqueness: The enable_secure_card_uniqueness of this MerchantPortfolio.  # noqa: E501
        :type: bool
        """

        self._enable_secure_card_uniqueness = enable_secure_card_uniqueness

    @property
    def enable_secure_card_auto_sharing(self):
        """Gets the enable_secure_card_auto_sharing of this MerchantPortfolio.  # noqa: E501


        :return: The enable_secure_card_auto_sharing of this MerchantPortfolio.  # noqa: E501
        :rtype: bool
        """
        return self._enable_secure_card_auto_sharing

    @enable_secure_card_auto_sharing.setter
    def enable_secure_card_auto_sharing(self, enable_secure_card_auto_sharing):
        """Sets the enable_secure_card_auto_sharing of this MerchantPortfolio.


        :param enable_secure_card_auto_sharing: The enable_secure_card_auto_sharing of this MerchantPortfolio.  # noqa: E501
        :type: bool
        """

        self._enable_secure_card_auto_sharing = enable_secure_card_auto_sharing

    @property
    def share_cards_from_deactivated_terminals(self):
        """Gets the share_cards_from_deactivated_terminals of this MerchantPortfolio.  # noqa: E501


        :return: The share_cards_from_deactivated_terminals of this MerchantPortfolio.  # noqa: E501
        :rtype: bool
        """
        return self._share_cards_from_deactivated_terminals

    @share_cards_from_deactivated_terminals.setter
    def share_cards_from_deactivated_terminals(self, share_cards_from_deactivated_terminals):
        """Sets the share_cards_from_deactivated_terminals of this MerchantPortfolio.


        :param share_cards_from_deactivated_terminals: The share_cards_from_deactivated_terminals of this MerchantPortfolio.  # noqa: E501
        :type: bool
        """

        self._share_cards_from_deactivated_terminals = share_cards_from_deactivated_terminals

    @property
    def enable_secure_card_auto_registration(self):
        """Gets the enable_secure_card_auto_registration of this MerchantPortfolio.  # noqa: E501


        :return: The enable_secure_card_auto_registration of this MerchantPortfolio.  # noqa: E501
        :rtype: bool
        """
        return self._enable_secure_card_auto_registration

    @enable_secure_card_auto_registration.setter
    def enable_secure_card_auto_registration(self, enable_secure_card_auto_registration):
        """Sets the enable_secure_card_auto_registration of this MerchantPortfolio.


        :param enable_secure_card_auto_registration: The enable_secure_card_auto_registration of this MerchantPortfolio.  # noqa: E501
        :type: bool
        """

        self._enable_secure_card_auto_registration = enable_secure_card_auto_registration

