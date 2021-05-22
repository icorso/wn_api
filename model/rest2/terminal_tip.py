# coding: utf-8

from model.serializable import SwaggerSerializable


class TerminalTip(SwaggerSerializable):
    swagger_types = {
        'unique_reference': 'str',
        'type': 'str',
        'amount': 'float',
        'currency': 'str',
        'percentage': 'float'
    }

    attribute_map = {
        'unique_reference': 'uniqueReference',
        'type': 'type',
        'amount': 'amount',
        'currency': 'currency',
        'percentage': 'percentage'
    }

    def __init__(self, unique_reference=None, type=None, amount=None, currency=None, percentage=None):  # noqa: E501
        """TerminalTip - a model defined in Swagger"""  # noqa: E501
        self._unique_reference = None
        self._type = None
        self._amount = None
        self._currency = None
        self._percentage = None
        self.discriminator = None
        if unique_reference is not None:
            self.unique_reference = unique_reference
        self.type = type
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if percentage is not None:
            self.percentage = percentage

    @property
    def unique_reference(self):
        """Gets the unique_reference of this TerminalTip.  # noqa: E501

        Unique reference number assigned by the gateway. This field must be used when trying to update an existing terminal's tip.  # noqa: E501

        :return: The unique_reference of this TerminalTip.  # noqa: E501
        :rtype: str
        """
        return self._unique_reference

    @unique_reference.setter
    def unique_reference(self, unique_reference):
        """Sets the unique_reference of this TerminalTip.

        Unique reference number assigned by the gateway. This field must be used when trying to update an existing terminal's tip.  # noqa: E501

        :param unique_reference: The unique_reference of this TerminalTip.  # noqa: E501
        :type: str
        """

        self._unique_reference = unique_reference

    @property
    def type(self):
        """Gets the type of this TerminalTip.  # noqa: E501


        :return: The type of this TerminalTip.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TerminalTip.


        :param type: The type of this TerminalTip.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["PERCENTAGE", "FIXED_AMOUNT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def amount(self):
        """Gets the amount of this TerminalTip.  # noqa: E501

        This field must used when the tip is of type `FIXED_AMOUNT`. Otherwise, refer to the `percentage` property instead.  # noqa: E501

        :return: The amount of this TerminalTip.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TerminalTip.

        This field must used when the tip is of type `FIXED_AMOUNT`. Otherwise, refer to the `percentage` property instead.  # noqa: E501

        :param amount: The amount of this TerminalTip.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this TerminalTip.  # noqa: E501

        Currency associated with the tip. A 3-letter code as per the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) standard.<br />This is specially useful for multi-currency terminals in order to provide a different set of tips for each supported currency.  # noqa: E501

        :return: The currency of this TerminalTip.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TerminalTip.

        Currency associated with the tip. A 3-letter code as per the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) standard.<br />This is specially useful for multi-currency terminals in order to provide a different set of tips for each supported currency.  # noqa: E501

        :param currency: The currency of this TerminalTip.  # noqa: E501
        :type: str
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def percentage(self):
        """Gets the percentage of this TerminalTip.  # noqa: E501

        This field must used when the tip is of type `PERCENTAGE`. Otherwise, refer to the `amount` property instead.  # noqa: E501

        :return: The percentage of this TerminalTip.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this TerminalTip.

        This field must used when the tip is of type `PERCENTAGE`. Otherwise, refer to the `amount` property instead.  # noqa: E501

        :param percentage: The percentage of this TerminalTip.  # noqa: E501
        :type: float
        """

        self._percentage = percentage
