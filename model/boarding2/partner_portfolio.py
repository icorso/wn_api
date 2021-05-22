# coding: utf-8

from model.serializable import SwaggerSerializable


class PartnerPortfolio(SwaggerSerializable):
    swagger_types = {
        'name': 'str',
        'contact_name': 'str',
        'contact_phone': 'str',
        'contact_email': 'str',
        'percentage': 'int',
        'bank_name': 'str',
        'bank_address': 'str',
        'bank_bic': 'str',
        'bank_iban': 'str',
        'bank_sort_code': 'str',
        'bank_account_number': 'str',
        'reporting_email_address': 'str',
        'deactivation_date': 'datetime',
        'gateway': 'str',
        'allow_pay_fac': 'bool',
        'pay_fac_bank': 'str',
        'pay_fac_identifier': 'str',
        'pay_fac_name': 'str',
        'partner_portfolio_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'contact_name': 'contactName',
        'contact_phone': 'contactPhone',
        'contact_email': 'contactEmail',
        'percentage': 'percentage',
        'bank_name': 'bankName',
        'bank_address': 'bankAddress',
        'bank_bic': 'bankBIC',
        'bank_iban': 'bankIBAN',
        'bank_sort_code': 'bankSortCode',
        'bank_account_number': 'bankAccountNumber',
        'reporting_email_address': 'reportingEmailAddress',
        'deactivation_date': 'deactivationDate',
        'gateway': 'gateway',
        'allow_pay_fac': 'allowPayFac',
        'pay_fac_bank': 'payFacBank',
        'pay_fac_identifier': 'payFacIdentifier',
        'pay_fac_name': 'payFacName',
        'partner_portfolio_id': 'partnerPortfolioId'
    }

    def __init__(self, name=None, contact_name=None, contact_phone=None, contact_email=None, percentage=None, bank_name=None, bank_address=None, bank_bic=None, bank_iban=None, bank_sort_code=None, bank_account_number=None, reporting_email_address=None, deactivation_date=None, gateway=None, allow_pay_fac=None, pay_fac_bank=None, pay_fac_identifier=None, pay_fac_name=None, partner_portfolio_id=None):  # noqa: E501
        """PartnerPortfolio - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._contact_name = None
        self._contact_phone = None
        self._contact_email = None
        self._percentage = None
        self._bank_name = None
        self._bank_address = None
        self._bank_bic = None
        self._bank_iban = None
        self._bank_sort_code = None
        self._bank_account_number = None
        self._reporting_email_address = None
        self._deactivation_date = None
        self._gateway = None
        self._allow_pay_fac = None
        self._pay_fac_bank = None
        self._pay_fac_identifier = None
        self._pay_fac_name = None
        self._partner_portfolio_id = None
        self.discriminator = None
        self.name = name
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        if percentage is not None:
            self.percentage = percentage
        if bank_name is not None:
            self.bank_name = bank_name
        if bank_address is not None:
            self.bank_address = bank_address
        if bank_bic is not None:
            self.bank_bic = bank_bic
        if bank_iban is not None:
            self.bank_iban = bank_iban
        if bank_sort_code is not None:
            self.bank_sort_code = bank_sort_code
        if bank_account_number is not None:
            self.bank_account_number = bank_account_number
        if reporting_email_address is not None:
            self.reporting_email_address = reporting_email_address
        if deactivation_date is not None:
            self.deactivation_date = deactivation_date
        if gateway is not None:
            self.gateway = gateway
        if allow_pay_fac is not None:
            self.allow_pay_fac = allow_pay_fac
        if pay_fac_bank is not None:
            self.pay_fac_bank = pay_fac_bank
        if pay_fac_identifier is not None:
            self.pay_fac_identifier = pay_fac_identifier
        if pay_fac_name is not None:
            self.pay_fac_name = pay_fac_name
        if partner_portfolio_id is not None:
            self.partner_portfolio_id = partner_portfolio_id

    @property
    def name(self):
        """Gets the name of this PartnerPortfolio.  # noqa: E501


        :return: The name of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartnerPortfolio.


        :param name: The name of this PartnerPortfolio.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def contact_name(self):
        """Gets the contact_name of this PartnerPortfolio.  # noqa: E501


        :return: The contact_name of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this PartnerPortfolio.


        :param contact_name: The contact_name of this PartnerPortfolio.  # noqa: E501
        :type: str
        """
        if contact_name is None:
            raise ValueError("Invalid value for `contact_name`, must not be `None`")  # noqa: E501

        self._contact_name = contact_name

    @property
    def contact_phone(self):
        """Gets the contact_phone of this PartnerPortfolio.  # noqa: E501


        :return: The contact_phone of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this PartnerPortfolio.


        :param contact_phone: The contact_phone of this PartnerPortfolio.  # noqa: E501
        :type: str
        """
        if contact_phone is None:
            raise ValueError("Invalid value for `contact_phone`, must not be `None`")  # noqa: E501

        self._contact_phone = contact_phone

    @property
    def contact_email(self):
        """Gets the contact_email of this PartnerPortfolio.  # noqa: E501


        :return: The contact_email of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this PartnerPortfolio.


        :param contact_email: The contact_email of this PartnerPortfolio.  # noqa: E501
        :type: str
        """
        if contact_email is None:
            raise ValueError("Invalid value for `contact_email`, must not be `None`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def percentage(self):
        """Gets the percentage of this PartnerPortfolio.  # noqa: E501


        :return: The percentage of this PartnerPortfolio.  # noqa: E501
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this PartnerPortfolio.


        :param percentage: The percentage of this PartnerPortfolio.  # noqa: E501
        :type: int
        """

        self._percentage = percentage

    @property
    def bank_name(self):
        """Gets the bank_name of this PartnerPortfolio.  # noqa: E501


        :return: The bank_name of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this PartnerPortfolio.


        :param bank_name: The bank_name of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def bank_address(self):
        """Gets the bank_address of this PartnerPortfolio.  # noqa: E501


        :return: The bank_address of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._bank_address

    @bank_address.setter
    def bank_address(self, bank_address):
        """Sets the bank_address of this PartnerPortfolio.


        :param bank_address: The bank_address of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._bank_address = bank_address

    @property
    def bank_bic(self):
        """Gets the bank_bic of this PartnerPortfolio.  # noqa: E501


        :return: The bank_bic of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._bank_bic

    @bank_bic.setter
    def bank_bic(self, bank_bic):
        """Sets the bank_bic of this PartnerPortfolio.


        :param bank_bic: The bank_bic of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._bank_bic = bank_bic

    @property
    def bank_iban(self):
        """Gets the bank_iban of this PartnerPortfolio.  # noqa: E501


        :return: The bank_iban of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._bank_iban

    @bank_iban.setter
    def bank_iban(self, bank_iban):
        """Sets the bank_iban of this PartnerPortfolio.


        :param bank_iban: The bank_iban of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._bank_iban = bank_iban

    @property
    def bank_sort_code(self):
        """Gets the bank_sort_code of this PartnerPortfolio.  # noqa: E501


        :return: The bank_sort_code of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._bank_sort_code

    @bank_sort_code.setter
    def bank_sort_code(self, bank_sort_code):
        """Sets the bank_sort_code of this PartnerPortfolio.


        :param bank_sort_code: The bank_sort_code of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._bank_sort_code = bank_sort_code

    @property
    def bank_account_number(self):
        """Gets the bank_account_number of this PartnerPortfolio.  # noqa: E501


        :return: The bank_account_number of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        """Sets the bank_account_number of this PartnerPortfolio.


        :param bank_account_number: The bank_account_number of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._bank_account_number = bank_account_number

    @property
    def reporting_email_address(self):
        """Gets the reporting_email_address of this PartnerPortfolio.  # noqa: E501


        :return: The reporting_email_address of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._reporting_email_address

    @reporting_email_address.setter
    def reporting_email_address(self, reporting_email_address):
        """Sets the reporting_email_address of this PartnerPortfolio.


        :param reporting_email_address: The reporting_email_address of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._reporting_email_address = reporting_email_address

    @property
    def deactivation_date(self):
        """Gets the deactivation_date of this PartnerPortfolio.  # noqa: E501


        :return: The deactivation_date of this PartnerPortfolio.  # noqa: E501
        :rtype: datetime
        """
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        """Sets the deactivation_date of this PartnerPortfolio.


        :param deactivation_date: The deactivation_date of this PartnerPortfolio.  # noqa: E501
        :type: datetime
        """

        self._deactivation_date = deactivation_date

    @property
    def gateway(self):
        """Gets the gateway of this PartnerPortfolio.  # noqa: E501


        :return: The gateway of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this PartnerPortfolio.


        :param gateway: The gateway of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def allow_pay_fac(self):
        """Gets the allow_pay_fac of this PartnerPortfolio.  # noqa: E501


        :return: The allow_pay_fac of this PartnerPortfolio.  # noqa: E501
        :rtype: bool
        """
        return self._allow_pay_fac

    @allow_pay_fac.setter
    def allow_pay_fac(self, allow_pay_fac):
        """Sets the allow_pay_fac of this PartnerPortfolio.


        :param allow_pay_fac: The allow_pay_fac of this PartnerPortfolio.  # noqa: E501
        :type: bool
        """

        self._allow_pay_fac = allow_pay_fac

    @property
    def pay_fac_bank(self):
        """Gets the pay_fac_bank of this PartnerPortfolio.  # noqa: E501


        :return: The pay_fac_bank of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._pay_fac_bank

    @pay_fac_bank.setter
    def pay_fac_bank(self, pay_fac_bank):
        """Sets the pay_fac_bank of this PartnerPortfolio.


        :param pay_fac_bank: The pay_fac_bank of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._pay_fac_bank = pay_fac_bank

    @property
    def pay_fac_identifier(self):
        """Gets the pay_fac_identifier of this PartnerPortfolio.  # noqa: E501


        :return: The pay_fac_identifier of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._pay_fac_identifier

    @pay_fac_identifier.setter
    def pay_fac_identifier(self, pay_fac_identifier):
        """Sets the pay_fac_identifier of this PartnerPortfolio.


        :param pay_fac_identifier: The pay_fac_identifier of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._pay_fac_identifier = pay_fac_identifier

    @property
    def pay_fac_name(self):
        """Gets the pay_fac_name of this PartnerPortfolio.  # noqa: E501


        :return: The pay_fac_name of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._pay_fac_name

    @pay_fac_name.setter
    def pay_fac_name(self, pay_fac_name):
        """Sets the pay_fac_name of this PartnerPortfolio.


        :param pay_fac_name: The pay_fac_name of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._pay_fac_name = pay_fac_name

    @property
    def partner_portfolio_id(self):
        """Gets the partner_portfolio_id of this PartnerPortfolio.  # noqa: E501


        :return: The partner_portfolio_id of this PartnerPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._partner_portfolio_id

    @partner_portfolio_id.setter
    def partner_portfolio_id(self, partner_portfolio_id):
        """Sets the partner_portfolio_id of this PartnerPortfolio.


        :param partner_portfolio_id: The partner_portfolio_id of this PartnerPortfolio.  # noqa: E501
        :type: str
        """

        self._partner_portfolio_id = partner_portfolio_id

