# coding: utf-8
from model.serializable import SwaggerSerializable


class FiServLocationDetails(SwaggerSerializable):
    swagger_types = {
        'card_acceptor_name': 'str',
        'country': 'str',
        'state': 'str',
        'city': 'str',
        'time_zone': 'str',
        'use_terminal_address': 'bool',
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'contact_phone': 'str'
    }

    attribute_map = {
        'card_acceptor_name': 'cardAcceptorName',
        'country': 'country',
        'state': 'state',
        'city': 'city',
        'time_zone': 'timeZone',
        'use_terminal_address': 'useTerminalAddress',
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'contact_phone': 'contactPhone'
    }

    def __init__(self, card_acceptor_name=None, country=None, state=None, city=None, time_zone=None, use_terminal_address=False, address1=None, address2=None, address3=None, contact_phone=None):
        self._card_acceptor_name = None
        self._country = None
        self._state = None
        self._city = None
        self._time_zone = None
        self._use_terminal_address = None
        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._contact_phone = None
        self.discriminator = None
        if card_acceptor_name is not None:
            self.card_acceptor_name = card_acceptor_name
        self.country = country
        if state is not None:
            self.state = state
        if city is not None:
            self.city = city
        self.time_zone = time_zone
        if use_terminal_address is not None:
            self.use_terminal_address = use_terminal_address
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if address3 is not None:
            self.address3 = address3
        if contact_phone is not None:
            self.contact_phone = contact_phone

    @property
    def card_acceptor_name(self):
        """Gets the card_acceptor_name of this FiServLocationDetails.  # noqa: E501


        :return: The card_acceptor_name of this FiServLocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._card_acceptor_name

    @card_acceptor_name.setter
    def card_acceptor_name(self, card_acceptor_name):
        """Sets the card_acceptor_name of this FiServLocationDetails.


        :param card_acceptor_name: The card_acceptor_name of this FiServLocationDetails.  # noqa: E501
        :type: str
        """

        self._card_acceptor_name = card_acceptor_name

    @property
    def country(self):
        """Gets the country of this FiServLocationDetails.  # noqa: E501

        The two-letter country code defined by [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard.  # noqa: E501

        :return: The country of this FiServLocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this FiServLocationDetails.

        The two-letter country code defined by [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard.  # noqa: E501

        :param country: The country of this FiServLocationDetails.  # noqa: E501
        :type: str
        """
        # allowed_values = ["AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX",
        # "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT",
        # "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU",
        # "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET",
        # "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP",
        # "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN",
        # "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW",
        # "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF",
        # "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ",
        # "NA", "NC", "NE", "NF", "NG", "NI", "NL", "false", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG",
        # "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB",
        # "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY",
        # "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA",
        # "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM",
        # "ZW"]
        self._country = country

    @property
    def state(self):
        """Gets the state of this FiServLocationDetails.  # noqa: E501

        The state code defined by [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) standard. This field only applies for American and Canadian terminals.  # noqa: E501

        :return: The state of this FiServLocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FiServLocationDetails.

        The state code defined by [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) standard. This field only applies for American and Canadian terminals.  # noqa: E501

        :param state: The state of this FiServLocationDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["CA-AB", "CA-BC", "CA-MB", "CA-NB", "CA-NL", "CA-NS", "CA-ON", "CA-PE", "CA-QC", "CA-SK", "CA-NT", "CA-NU", "CA-YT", "US-AL", "US-AK", "US-AZ", "US-AR", "US-CA", "US-CO", "US-CT", "US-DE", "US-FL", "US-GA", "US-HI", "US-ID", "US-IL", "US-IN", "US-IA", "US-KS", "US-KY", "US-LA", "US-ME", "US-MD", "US-MA", "US-MI", "US-MN", "US-MS", "US-MO", "US-MT", "US-NE", "US-NV", "US-NH", "US-NJ", "US-NM", "US-NY", "US-NC", "US-ND", "US-OH", "US-OK", "US-OR", "US-PA", "US-RI", "US-SC", "US-SD", "US-TN", "US-TX", "US-UT", "US-VT", "US-VA", "US-WA", "US-WV", "US-WI", "US-WY", "US-DC", "US-AS", "US-GU", "US-MP", "US-PR", "US-UM", "US-VI"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def city(self):
        """Gets the city of this FiServLocationDetails.  # noqa: E501


        :return: The city of this FiServLocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this FiServLocationDetails.


        :param city: The city of this FiServLocationDetails.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def time_zone(self):
        """Gets the time_zone of this FiServLocationDetails.  # noqa: E501

        Terminal's preferred time-zone.  # noqa: E501

        :return: The time_zone of this FiServLocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this FiServLocationDetails.

        Terminal's preferred time-zone.  # noqa: E501

        :param time_zone: The time_zone of this FiServLocationDetails.  # noqa: E501
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
    def use_terminal_address(self):
        """Gets the use_terminal_address of this FiServLocationDetails.  # noqa: E501


        :return: The use_terminal_address of this FiServLocationDetails.  # noqa: E501
        :rtype: bool
        """
        return self._use_terminal_address

    @use_terminal_address.setter
    def use_terminal_address(self, use_terminal_address):
        """Sets the use_terminal_address of this FiServLocationDetails.


        :param use_terminal_address: The use_terminal_address of this FiServLocationDetails.  # noqa: E501
        :type: bool
        """

        self._use_terminal_address = use_terminal_address

    @property
    def address1(self):
        """Gets the address1 of this FiServLocationDetails.  # noqa: E501


        :return: The address1 of this FiServLocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this FiServLocationDetails.


        :param address1: The address1 of this FiServLocationDetails.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this FiServLocationDetails.  # noqa: E501


        :return: The address2 of this FiServLocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this FiServLocationDetails.


        :param address2: The address2 of this FiServLocationDetails.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def address3(self):
        """Gets the address3 of this FiServLocationDetails.  # noqa: E501


        :return: The address3 of this FiServLocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this FiServLocationDetails.


        :param address3: The address3 of this FiServLocationDetails.  # noqa: E501
        :type: str
        """

        self._address3 = address3

    @property
    def contact_phone(self):
        """Gets the contact_phone of this FiServLocationDetails.  # noqa: E501


        :return: The contact_phone of this FiServLocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        """Sets the contact_phone of this FiServLocationDetails.


        :param contact_phone: The contact_phone of this FiServLocationDetails.  # noqa: E501
        :type: str
        """

        self._contact_phone = contact_phone

