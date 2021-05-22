# coding: utf-8
from model.serializable import SwaggerSerializable


class TerminalCompact(SwaggerSerializable):
    swagger_types = {
        'payment_processor': 'str',
        'terminal_number': 'str',
        'display_name': 'str',
        'base_currency': 'str',
        'time_zone': 'str',
        'links': 'list[HypermediaLink]'
    }

    attribute_map = {
        'payment_processor': 'paymentProcessor',
        'terminal_number': 'terminalNumber',
        'display_name': 'displayName',
        'base_currency': 'baseCurrency',
        'time_zone': 'timeZone',
        'links': 'links'
    }

    def __init__(self, payment_processor=None, terminal_number=None, display_name=None, base_currency=None, time_zone=None, links=None):  # noqa: E501
        self._payment_processor = None
        self._terminal_number = None
        self._display_name = None
        self._base_currency = None
        self._time_zone = None
        self._links = None
        self.discriminator = None
        if payment_processor is not None:
            self.payment_processor = payment_processor
        if terminal_number is not None:
            self.terminal_number = terminal_number
        if display_name is not None:
            self.display_name = display_name
        if base_currency is not None:
            self.base_currency = base_currency
        if time_zone is not None:
            self.time_zone = time_zone
        if links is not None:
            self.links = links

    @property
    def payment_processor(self):
        return self._payment_processor

    @payment_processor.setter
    def payment_processor(self, payment_processor):
        self._payment_processor = payment_processor

    @property
    def terminal_number(self):
        return self._terminal_number

    @terminal_number.setter
    def terminal_number(self, terminal_number):
        self._terminal_number = terminal_number

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    @property
    def base_currency(self):
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT",
                          "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD",
                          "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP",
                          "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP",
                          "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
                          "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW",
                          "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD",
                          "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV",
                          "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP",
                          "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK",
                          "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS",
                          "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI",
                          "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR",
                          "ZMW", "ZWL"]
        if base_currency not in allowed_values:
            raise ValueError(
                "Invalid value for `base_currency` ({0}), must be one of {1}"
                .format(base_currency, allowed_values)
            )

        self._base_currency = base_currency

    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        self._time_zone = time_zone

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

