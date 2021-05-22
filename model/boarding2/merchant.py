# coding: utf-8

from model.serializable import SwaggerSerializable


class Merchant(SwaggerSerializable):
    swagger_types = {
        'template_name': 'str',
        'website': 'str',
        'city': 'str',
        'mcc': 'str',
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'pricing_type': 'str',
        'country': 'str',
        'merchant_portfolio_unique_id': 'str',
        'partner_portfolio_unique_id': 'str',
        'deactivation_date': 'datetime',
        'merchant_id': 'str',
        'gateway_host': 'str',
        'dba_name': 'str',
        'contact': 'str',
        'phone': 'str',
        'email': 'str',
        'time_zone': 'str',
        'merchant_pricing': 'MerchantPricing',
        'merchant_general_setup': 'MerchantGeneralSetup',
        'merchant_custom_settings': 'list[MerchantCustomSettings]'
    }

    attribute_map = {
        'template_name': 'templateName',
        'website': 'website',
        'city': 'city',
        'mcc': 'mcc',
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'pricing_type': 'pricingType',
        'country': 'country',
        'merchant_portfolio_unique_id': 'merchantPortfolioUniqueId',
        'partner_portfolio_unique_id': 'partnerPortfolioUniqueId',
        'deactivation_date': 'deactivationDate',
        'merchant_id': 'merchantId',
        'gateway_host': 'gatewayHost',
        'dba_name': 'dbaName',
        'contact': 'contact',
        'phone': 'phone',
        'email': 'email',
        'time_zone': 'timeZone',
        'merchant_pricing': 'merchantPricing',
        'merchant_general_setup': 'merchantGeneralSetup',
        'merchant_custom_settings': 'merchantCustomSettings'
    }

    def __init__(self, template_name=None, website=None, city=None, mcc=None, address1=None, address2=None, address3=None, pricing_type=None, country=None, merchant_portfolio_unique_id=None, partner_portfolio_unique_id=None, deactivation_date=None, merchant_id=None, gateway_host=None, dba_name=None, contact=None, phone=None, email=None, time_zone=None, merchant_pricing=None, merchant_general_setup=None, merchant_custom_settings=None):  # noqa: E501
        """Merchant - a model defined in Swagger"""  # noqa: E501
        self._template_name = None
        self._website = None
        self._city = None
        self._mcc = None
        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._pricing_type = None
        self._country = None
        self._merchant_portfolio_unique_id = None
        self._partner_portfolio_unique_id = None
        self._deactivation_date = None
        self._merchant_id = None
        self._gateway_host = None
        self._dba_name = None
        self._contact = None
        self._phone = None
        self._email = None
        self._time_zone = None
        self._merchant_pricing = None
        self._merchant_general_setup = None
        self._merchant_custom_settings = None
        self.discriminator = None
        if template_name is not None:
            self.template_name = template_name
        if website is not None:
            self.website = website
        self.city = city
        self.mcc = mcc
        self.address1 = address1
        self.address2 = address2
        if address3 is not None:
            self.address3 = address3
        if pricing_type is not None:
            self.pricing_type = pricing_type
        self.country = country
        if merchant_portfolio_unique_id is not None:
            self.merchant_portfolio_unique_id = merchant_portfolio_unique_id
        if partner_portfolio_unique_id is not None:
            self.partner_portfolio_unique_id = partner_portfolio_unique_id
        if deactivation_date is not None:
            self.deactivation_date = deactivation_date
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if gateway_host is not None:
            self.gateway_host = gateway_host
        self.dba_name = dba_name
        self.contact = contact
        self.phone = phone
        self.email = email
        self.time_zone = time_zone
        if merchant_pricing is not None:
            self.merchant_pricing = merchant_pricing
        if merchant_general_setup is not None:
            self.merchant_general_setup = merchant_general_setup
        if merchant_custom_settings is not None:
            self.merchant_custom_settings = merchant_custom_settings

    @property
    def template_name(self):
        """Gets the template_name of this Merchant.  # noqa: E501


        :return: The template_name of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this Merchant.


        :param template_name: The template_name of this Merchant.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def website(self):
        """Gets the website of this Merchant.  # noqa: E501


        :return: The website of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Merchant.


        :param website: The website of this Merchant.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def city(self):
        """Gets the city of this Merchant.  # noqa: E501


        :return: The city of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Merchant.


        :param city: The city of this Merchant.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def mcc(self):
        """Gets the mcc of this Merchant.  # noqa: E501


        :return: The mcc of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._mcc

    @mcc.setter
    def mcc(self, mcc):
        """Sets the mcc of this Merchant.


        :param mcc: The mcc of this Merchant.  # noqa: E501
        :type: str
        """
        if mcc is None:
            raise ValueError("Invalid value for `mcc`, must not be `None`")  # noqa: E501

        self._mcc = mcc

    @property
    def address1(self):
        """Gets the address1 of this Merchant.  # noqa: E501


        :return: The address1 of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Merchant.


        :param address1: The address1 of this Merchant.  # noqa: E501
        :type: str
        """
        if address1 is None:
            raise ValueError("Invalid value for `address1`, must not be `None`")  # noqa: E501

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Merchant.  # noqa: E501


        :return: The address2 of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Merchant.


        :param address2: The address2 of this Merchant.  # noqa: E501
        :type: str
        """
        if address2 is None:
            raise ValueError("Invalid value for `address2`, must not be `None`")  # noqa: E501

        self._address2 = address2

    @property
    def address3(self):
        """Gets the address3 of this Merchant.  # noqa: E501


        :return: The address3 of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this Merchant.


        :param address3: The address3 of this Merchant.  # noqa: E501
        :type: str
        """

        self._address3 = address3

    @property
    def pricing_type(self):
        """Gets the pricing_type of this Merchant.  # noqa: E501


        :return: The pricing_type of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._pricing_type

    @pricing_type.setter
    def pricing_type(self, pricing_type):
        """Sets the pricing_type of this Merchant.


        :param pricing_type: The pricing_type of this Merchant.  # noqa: E501
        :type: str
        """
        allowed_values = ["MERCHANT_LEVEL", "TERMINAL_LEVEL"]  # noqa: E501
        if pricing_type not in allowed_values:
            raise ValueError(
                "Invalid value for `pricing_type` ({0}), must be one of {1}"  # noqa: E501
                .format(pricing_type, allowed_values)
            )

        self._pricing_type = pricing_type

    @property
    def country(self):
        """Gets the country of this Merchant.  # noqa: E501

        The two-letter country code defined by [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard.  # noqa: E501

        :return: The country of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Merchant.

        The two-letter country code defined by [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard.  # noqa: E501

        :param country: The country of this Merchant.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501
        allowed_values = ["AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "false", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"]  # noqa: E501
        if country not in allowed_values:
            raise ValueError(
                "Invalid value for `country` ({0}), must be one of {1}"  # noqa: E501
                .format(country, allowed_values)
            )

        self._country = country

    @property
    def merchant_portfolio_unique_id(self):
        """Gets the merchant_portfolio_unique_id of this Merchant.  # noqa: E501


        :return: The merchant_portfolio_unique_id of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._merchant_portfolio_unique_id

    @merchant_portfolio_unique_id.setter
    def merchant_portfolio_unique_id(self, merchant_portfolio_unique_id):
        """Sets the merchant_portfolio_unique_id of this Merchant.


        :param merchant_portfolio_unique_id: The merchant_portfolio_unique_id of this Merchant.  # noqa: E501
        :type: str
        """

        self._merchant_portfolio_unique_id = merchant_portfolio_unique_id

    @property
    def partner_portfolio_unique_id(self):
        """Gets the partner_portfolio_unique_id of this Merchant.  # noqa: E501


        :return: The partner_portfolio_unique_id of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._partner_portfolio_unique_id

    @partner_portfolio_unique_id.setter
    def partner_portfolio_unique_id(self, partner_portfolio_unique_id):
        """Sets the partner_portfolio_unique_id of this Merchant.


        :param partner_portfolio_unique_id: The partner_portfolio_unique_id of this Merchant.  # noqa: E501
        :type: str
        """

        self._partner_portfolio_unique_id = partner_portfolio_unique_id

    @property
    def deactivation_date(self):
        """Gets the deactivation_date of this Merchant.  # noqa: E501


        :return: The deactivation_date of this Merchant.  # noqa: E501
        :rtype: datetime
        """
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        """Sets the deactivation_date of this Merchant.


        :param deactivation_date: The deactivation_date of this Merchant.  # noqa: E501
        :type: datetime
        """

        self._deactivation_date = deactivation_date

    @property
    def merchant_id(self):
        """Gets the merchant_id of this Merchant.  # noqa: E501


        :return: The merchant_id of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this Merchant.


        :param merchant_id: The merchant_id of this Merchant.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def gateway_host(self):
        """Gets the gateway_host of this Merchant.  # noqa: E501


        :return: The gateway_host of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._gateway_host

    @gateway_host.setter
    def gateway_host(self, gateway_host):
        """Sets the gateway_host of this Merchant.


        :param gateway_host: The gateway_host of this Merchant.  # noqa: E501
        :type: str
        """

        self._gateway_host = gateway_host

    @property
    def dba_name(self):
        """Gets the dba_name of this Merchant.  # noqa: E501


        :return: The dba_name of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._dba_name

    @dba_name.setter
    def dba_name(self, dba_name):
        """Sets the dba_name of this Merchant.


        :param dba_name: The dba_name of this Merchant.  # noqa: E501
        :type: str
        """
        if dba_name is None:
            raise ValueError("Invalid value for `dba_name`, must not be `None`")  # noqa: E501

        self._dba_name = dba_name

    @property
    def contact(self):
        """Gets the contact of this Merchant.  # noqa: E501


        :return: The contact of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Merchant.


        :param contact: The contact of this Merchant.  # noqa: E501
        :type: str
        """
        if contact is None:
            raise ValueError("Invalid value for `contact`, must not be `None`")  # noqa: E501

        self._contact = contact

    @property
    def phone(self):
        """Gets the phone of this Merchant.  # noqa: E501


        :return: The phone of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Merchant.


        :param phone: The phone of this Merchant.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this Merchant.  # noqa: E501


        :return: The email of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Merchant.


        :param email: The email of this Merchant.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def time_zone(self):
        """Gets the time_zone of this Merchant.  # noqa: E501

        Merchant's preferred time-zone.  # noqa: E501

        :return: The time_zone of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Merchant.

        Merchant's preferred time-zone.  # noqa: E501

        :param time_zone: The time_zone of this Merchant.  # noqa: E501
        :type: str
        """
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501
        allowed_values = ["Pacific/Midway", "Pacific/Honolulu", "Pacific/Marquesas", "America/Anchorage", "Pacific/Pitcairn", "America/Los_Angeles", "America/Tijuana", "America/Chihuahua", "America/Denver", "America/Phoenix", "America/Chicago", "America/Guatemala", "America/Mexico_City", "America/Regina", "America/Bogota", "America/Indiana/Indianapolis", "America/New_York", "America/Caracas", "America/Guyana", "America/Halifax", "America/La_Paz", "America/Manaus", "America/Santiago", "America/St_Johns", "America/Argentina/Buenos_Aires", "America/Godthab", "America/Montevideo", "America/Sao_Paulo", "Atlantic/South_Georgia", "Atlantic/Azores", "Atlantic/Cape_Verde", "Africa/Casablanca", "Africa/Monrovia", "Europe/London", "Africa/Algiers", "Africa/Windhoek", "Europe/Belgrade", "Europe/Berlin", "Europe/Brussels", "Europe/Warsaw", "Africa/Cairo", "Africa/Harare", "Asia/Amman", "Asia/Beirut", "Asia/Jerusalem", "Europe/Athens", "Europe/Helsinki", "Europe/Minsk", "Africa/Nairobi", "Asia/Baghdad", "Asia/Kuwait", "Europe/Moscow", "Asia/Tehran", "Asia/Baku", "Asia/Muscat", "Asia/Tbilisi", "Asia/Yerevan", "Asia/Kabul", "Asia/Karachi", "Asia/Tashkent", "Asia/Yekaterinburg", "Asia/Colombo", "Asia/Kolkata", "Asia/Kathmandu", "Asia/Dhaka", "Asia/Novosibirsk", "Asia/Rangoon", "Asia/Bangkok", "Asia/Krasnoyarsk", "Asia/Hong_Kong", "Asia/Irkutsk", "Asia/Kuala_Lumpur", "Asia/Taipei", "Australia/Perth", "Asia/Seoul", "Asia/Tokyo", "Asia/Yakutsk", "Australia/Adelaide", "Australia/Darwin", "Asia/Vladivostok", "Australia/Brisbane", "Australia/Hobart", "Australia/Sydney", "Pacific/Guam", "Australia/Lord_Howe", "Asia/Magadan", "Pacific/Norfolk", "Pacific/Auckland", "Pacific/Fiji", "Pacific/Tongatapu"]  # noqa: E501
        if time_zone not in allowed_values:
            raise ValueError(
                "Invalid value for `time_zone` ({0}), must be one of {1}"  # noqa: E501
                .format(time_zone, allowed_values)
            )

        self._time_zone = time_zone

    @property
    def merchant_pricing(self):
        """Gets the merchant_pricing of this Merchant.  # noqa: E501


        :return: The merchant_pricing of this Merchant.  # noqa: E501
        :rtype: MerchantPricing
        """
        return self._merchant_pricing

    @merchant_pricing.setter
    def merchant_pricing(self, merchant_pricing):
        """Sets the merchant_pricing of this Merchant.


        :param merchant_pricing: The merchant_pricing of this Merchant.  # noqa: E501
        :type: MerchantPricing
        """

        self._merchant_pricing = merchant_pricing

    @property
    def merchant_general_setup(self):
        """Gets the merchant_general_setup of this Merchant.  # noqa: E501


        :return: The merchant_general_setup of this Merchant.  # noqa: E501
        :rtype: MerchantGeneralSetup
        """
        return self._merchant_general_setup

    @merchant_general_setup.setter
    def merchant_general_setup(self, merchant_general_setup):
        """Sets the merchant_general_setup of this Merchant.


        :param merchant_general_setup: The merchant_general_setup of this Merchant.  # noqa: E501
        :type: MerchantGeneralSetup
        """

        self._merchant_general_setup = merchant_general_setup

    @property
    def merchant_custom_settings(self):
        """Gets the merchant_custom_settings of this Merchant.  # noqa: E501


        :return: The merchant_custom_settings of this Merchant.  # noqa: E501
        :rtype: list[MerchantCustomSettings]
        """
        return self._merchant_custom_settings

    @merchant_custom_settings.setter
    def merchant_custom_settings(self, merchant_custom_settings):
        """Sets the merchant_custom_settings of this Merchant.


        :param merchant_custom_settings: The merchant_custom_settings of this Merchant.  # noqa: E501
        :type: list[MerchantCustomSettings]
        """

        self._merchant_custom_settings = merchant_custom_settings

