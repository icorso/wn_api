# coding: utf-8
from model.serializable import SwaggerSerializable


class TerminalLocationDetails(SwaggerSerializable):
    swagger_types = {
        'country': 'str',
        'time_zone': 'str',
        'use_terminal_address': 'bool',
        'city': 'str',
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'contact_phone': 'str'
    }

    attribute_map = {
        'country': 'country',
        'time_zone': 'timeZone',
        'use_terminal_address': 'useTerminalAddress',
        'city': 'city',
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'contact_phone': 'contactPhone'
    }

    def __init__(self, country=None, time_zone=None, use_terminal_address=False, city=None, address1=None, address2=None, address3=None, contact_phone=None):  # noqa: E501
        self._country = None
        self._time_zone = None
        self._use_terminal_address = None
        self._city = None
        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._contact_phone = None
        self.discriminator = None
        self.country = country
        self.time_zone = time_zone
        if use_terminal_address is not None:
            self.use_terminal_address = use_terminal_address
        if city is not None:
            self.city = city
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if address3 is not None:
            self.address3 = address3
        if contact_phone is not None:
            self.contact_phone = contact_phone

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501
        allowed_values = ["AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX",
                          "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ",
                          "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK",
                          "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM",
                          "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR",
                          "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS",
                          "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN",
                          "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN",
                          "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV",
                          "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ",
                          "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI",
                          "NL", "false", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM",
                          "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC",
                          "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV",
                          "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR",
                          "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI",
                          "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"]
        if country not in allowed_values:
            raise ValueError(
                "Invalid value for `country` ({0}), must be one of {1}"  # noqa: E501
                .format(country, allowed_values)
            )

        self._country = country

    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")
        allowed_values = ["Pacific/Midway", "Pacific/Honolulu", "Pacific/Marquesas", "America/Anchorage",
                          "Pacific/Pitcairn", "America/Los_Angeles", "America/Tijuana", "America/Chihuahua",
                          "America/Denver", "America/Phoenix", "America/Chicago", "America/Guatemala",
                          "America/Mexico_City", "America/Regina", "America/Bogota", "America/Indiana/Indianapolis",
                          "America/New_York", "America/Caracas", "America/Guyana", "America/Halifax", "America/La_Paz",
                          "America/Manaus", "America/Santiago", "America/St_Johns", "America/Argentina/Buenos_Aires",
                          "America/Godthab", "America/Montevideo", "America/Sao_Paulo", "Atlantic/South_Georgia",
                          "Atlantic/Azores", "Atlantic/Cape_Verde", "Africa/Casablanca", "Africa/Monrovia",
                          "Europe/London", "Africa/Algiers", "Africa/Windhoek", "Europe/Belgrade", "Europe/Berlin",
                          "Europe/Brussels", "Europe/Warsaw", "Africa/Cairo", "Africa/Harare", "Asia/Amman",
                          "Asia/Beirut", "Asia/Jerusalem", "Europe/Athens", "Europe/Helsinki", "Europe/Minsk",
                          "Africa/Nairobi", "Asia/Baghdad", "Asia/Kuwait", "Europe/Moscow", "Asia/Tehran",
                          "Asia/Baku", "Asia/Muscat", "Asia/Tbilisi", "Asia/Yerevan", "Asia/Kabul", "Asia/Karachi",
                          "Asia/Tashkent", "Asia/Yekaterinburg", "Asia/Colombo", "Asia/Kolkata", "Asia/Kathmandu",
                          "Asia/Dhaka", "Asia/Novosibirsk", "Asia/Rangoon", "Asia/Bangkok", "Asia/Krasnoyarsk",
                          "Asia/Hong_Kong", "Asia/Irkutsk", "Asia/Kuala_Lumpur", "Asia/Taipei", "Australia/Perth",
                          "Asia/Seoul", "Asia/Tokyo", "Asia/Yakutsk", "Australia/Adelaide", "Australia/Darwin",
                          "Asia/Vladivostok", "Australia/Brisbane", "Australia/Hobart", "Australia/Sydney",
                          "Pacific/Guam", "Australia/Lord_Howe", "Asia/Magadan", "Pacific/Norfolk", "Pacific/Auckland",
                          "Pacific/Fiji", "Pacific/Tongatapu"]
        if time_zone not in allowed_values:
            raise ValueError(
                "Invalid value for `time_zone` ({0}), must be one of {1}"  # noqa: E501
                .format(time_zone, allowed_values)
            )

        self._time_zone = time_zone

    @property
    def use_terminal_address(self):
        return self._use_terminal_address

    @use_terminal_address.setter
    def use_terminal_address(self, use_terminal_address):
        self._use_terminal_address = use_terminal_address

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def address1(self):
        return self._address1

    @address1.setter
    def address1(self, address1):
        self._address1 = address1

    @property
    def address2(self):
        return self._address2

    @address2.setter
    def address2(self, address2):
        self._address2 = address2

    @property
    def address3(self):
        return self._address3

    @address3.setter
    def address3(self, address3):
        self._address3 = address3

    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        self._contact_phone = contact_phone

