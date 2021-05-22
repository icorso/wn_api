# coding: utf-8

from model.serializable import SwaggerSerializable


class TerminalBankSettings(SwaggerSerializable):
    swagger_types = {
        'allow_multicurrency': 'bool',
        'allow_emcp': 'bool',
        'allow_edcc': 'bool',
        'base_currency': 'str',
        'supported_currencies': 'list[str]',
        'allow_moto': 'bool',
        'allow_internet': 'bool',
        'allow_chp': 'bool',
        'allow_recurring': 'bool',
        'allow_pre_auth': 'bool',
        'enable_automatic_settle': 'bool',
        'batch_time': 'str',
        'display_name': 'str',
        'force_unique_order_id': 'bool'
    }

    attribute_map = {
        'allow_multicurrency': 'allowMulticurrency',
        'allow_emcp': 'allowEmcp',
        'allow_edcc': 'allowEdcc',
        'base_currency': 'baseCurrency',
        'supported_currencies': 'supportedCurrencies',
        'allow_moto': 'allowMoto',
        'allow_internet': 'allowInternet',
        'allow_chp': 'allowChp',
        'allow_recurring': 'allowRecurring',
        'allow_pre_auth': 'allowPreAuth',
        'enable_automatic_settle': 'enableAutomaticSettle',
        'batch_time': 'batchTime',
        'display_name': 'displayName',
        'force_unique_order_id': 'forceUniqueOrderId'
    }

    def __init__(self, allow_multicurrency=None, allow_emcp=None, allow_edcc=None, base_currency=None, supported_currencies=None, allow_moto=None, allow_internet=None, allow_chp=None, allow_recurring=None, allow_pre_auth=None, enable_automatic_settle=None, batch_time=None, display_name=None, force_unique_order_id=None):  # noqa: E501
        """TerminalBankSettings - a model defined in Swagger"""  # noqa: E501
        self._allow_multicurrency = None
        self._allow_emcp = None
        self._allow_edcc = None
        self._base_currency = None
        self._supported_currencies = None
        self._allow_moto = None
        self._allow_internet = None
        self._allow_chp = None
        self._allow_recurring = None
        self._allow_pre_auth = None
        self._enable_automatic_settle = None
        self._batch_time = None
        self._display_name = None
        self._force_unique_order_id = None
        self.discriminator = None
        self.allow_multicurrency = allow_multicurrency
        self.allow_emcp = allow_emcp
        self.allow_edcc = allow_edcc
        if base_currency is not None:
            self.base_currency = base_currency
        if supported_currencies is not None:
            self.supported_currencies = supported_currencies
        self.allow_moto = allow_moto
        self.allow_internet = allow_internet
        self.allow_chp = allow_chp
        self.allow_recurring = allow_recurring
        self.allow_pre_auth = allow_pre_auth
        self.enable_automatic_settle = enable_automatic_settle
        if batch_time is not None:
            self.batch_time = batch_time
        if display_name is not None:
            self.display_name = display_name
        self.force_unique_order_id = force_unique_order_id

    @property
    def allow_multicurrency(self):
        """Gets the allow_multicurrency of this TerminalBankSettings.  # noqa: E501

        Indicates whether the terminal supports multi-currency processing.  # noqa: E501

        :return: The allow_multicurrency of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multicurrency

    @allow_multicurrency.setter
    def allow_multicurrency(self, allow_multicurrency):
        """Sets the allow_multicurrency of this TerminalBankSettings.

        Indicates whether the terminal supports multi-currency processing.  # noqa: E501

        :param allow_multicurrency: The allow_multicurrency of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if allow_multicurrency is None:
            raise ValueError("Invalid value for `allow_multicurrency`, must not be `None`")  # noqa: E501

        self._allow_multicurrency = allow_multicurrency

    @property
    def allow_emcp(self):
        """Gets the allow_emcp of this TerminalBankSettings.  # noqa: E501

        Indicates whether the terminal supports enhanced multi-currency processing.  # noqa: E501

        :return: The allow_emcp of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_emcp

    @allow_emcp.setter
    def allow_emcp(self, allow_emcp):
        """Sets the allow_emcp of this TerminalBankSettings.

        Indicates whether the terminal supports enhanced multi-currency processing.  # noqa: E501

        :param allow_emcp: The allow_emcp of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if allow_emcp is None:
            raise ValueError("Invalid value for `allow_emcp`, must not be `None`")  # noqa: E501

        self._allow_emcp = allow_emcp

    @property
    def allow_edcc(self):
        """Gets the allow_edcc of this TerminalBankSettings.  # noqa: E501

        Indicates whether the terminal supports dynamic currency conversion.  # noqa: E501

        :return: The allow_edcc of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_edcc

    @allow_edcc.setter
    def allow_edcc(self, allow_edcc):
        """Sets the allow_edcc of this TerminalBankSettings.

        Indicates whether the terminal supports dynamic currency conversion.  # noqa: E501

        :param allow_edcc: The allow_edcc of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if allow_edcc is None:
            raise ValueError("Invalid value for `allow_edcc`, must not be `None`")  # noqa: E501

        self._allow_edcc = allow_edcc

    @property
    def base_currency(self):
        """Gets the base_currency of this TerminalBankSettings.  # noqa: E501

        The terminal's base currency used for single currency transactions as well as MCP and DCC processing.  **Note:** Terminals where `allowMulticurrency` is enabled will not have a base currency.  # noqa: E501

        :return: The base_currency of this TerminalBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this TerminalBankSettings.

        The terminal's base currency used for single currency transactions as well as MCP and DCC processing.  **Note:** Terminals where `allowMulticurrency` is enabled will not have a base currency.  # noqa: E501

        :param base_currency: The base_currency of this TerminalBankSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if base_currency not in allowed_values:
            raise ValueError(
                "Invalid value for `base_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(base_currency, allowed_values)
            )

        self._base_currency = base_currency

    @property
    def supported_currencies(self):
        """Gets the supported_currencies of this TerminalBankSettings.  # noqa: E501

        List of currencies supported by the terminal for multi-currency processing of any kind.  # noqa: E501

        :return: The supported_currencies of this TerminalBankSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_currencies

    @supported_currencies.setter
    def supported_currencies(self, supported_currencies):
        """Sets the supported_currencies of this TerminalBankSettings.

        List of currencies supported by the terminal for multi-currency processing of any kind.  # noqa: E501

        :param supported_currencies: The supported_currencies of this TerminalBankSettings.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if not set(supported_currencies).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `supported_currencies` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(supported_currencies) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._supported_currencies = supported_currencies

    @property
    def allow_moto(self):
        """Gets the allow_moto of this TerminalBankSettings.  # noqa: E501

        Indicates whether the terminal is configured to process Mail Order / Telephone Order transactions.  # noqa: E501

        :return: The allow_moto of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_moto

    @allow_moto.setter
    def allow_moto(self, allow_moto):
        """Sets the allow_moto of this TerminalBankSettings.

        Indicates whether the terminal is configured to process Mail Order / Telephone Order transactions.  # noqa: E501

        :param allow_moto: The allow_moto of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if allow_moto is None:
            raise ValueError("Invalid value for `allow_moto`, must not be `None`")  # noqa: E501

        self._allow_moto = allow_moto

    @property
    def allow_internet(self):
        """Gets the allow_internet of this TerminalBankSettings.  # noqa: E501

        Indicates whether the terminal is configured to process Web-based transactions.  # noqa: E501

        :return: The allow_internet of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_internet

    @allow_internet.setter
    def allow_internet(self, allow_internet):
        """Sets the allow_internet of this TerminalBankSettings.

        Indicates whether the terminal is configured to process Web-based transactions.  # noqa: E501

        :param allow_internet: The allow_internet of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if allow_internet is None:
            raise ValueError("Invalid value for `allow_internet`, must not be `None`")  # noqa: E501

        self._allow_internet = allow_internet

    @property
    def allow_chp(self):
        """Gets the allow_chp of this TerminalBankSettings.  # noqa: E501

        Indicates whether the terminal is configured to process POS-based (Cardholder Present) transactions.  # noqa: E501

        :return: The allow_chp of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_chp

    @allow_chp.setter
    def allow_chp(self, allow_chp):
        """Sets the allow_chp of this TerminalBankSettings.

        Indicates whether the terminal is configured to process POS-based (Cardholder Present) transactions.  # noqa: E501

        :param allow_chp: The allow_chp of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if allow_chp is None:
            raise ValueError("Invalid value for `allow_chp`, must not be `None`")  # noqa: E501

        self._allow_chp = allow_chp

    @property
    def allow_recurring(self):
        """Gets the allow_recurring of this TerminalBankSettings.  # noqa: E501

        Indicates whether the terminal allows recurring payments.  # noqa: E501

        :return: The allow_recurring of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_recurring

    @allow_recurring.setter
    def allow_recurring(self, allow_recurring):
        """Sets the allow_recurring of this TerminalBankSettings.

        Indicates whether the terminal allows recurring payments.  # noqa: E501

        :param allow_recurring: The allow_recurring of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if allow_recurring is None:
            raise ValueError("Invalid value for `allow_recurring`, must not be `None`")  # noqa: E501

        self._allow_recurring = allow_recurring

    @property
    def allow_pre_auth(self):
        """Gets the allow_pre_auth of this TerminalBankSettings.  # noqa: E501

        Indicates whether the terminal allows pre-authorizations.<br />This type of transactions need to be complemented with a capture operation which can be done for a partial as well as a full amount.  # noqa: E501

        :return: The allow_pre_auth of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_pre_auth

    @allow_pre_auth.setter
    def allow_pre_auth(self, allow_pre_auth):
        """Sets the allow_pre_auth of this TerminalBankSettings.

        Indicates whether the terminal allows pre-authorizations.<br />This type of transactions need to be complemented with a capture operation which can be done for a partial as well as a full amount.  # noqa: E501

        :param allow_pre_auth: The allow_pre_auth of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if allow_pre_auth is None:
            raise ValueError("Invalid value for `allow_pre_auth`, must not be `None`")  # noqa: E501

        self._allow_pre_auth = allow_pre_auth

    @property
    def enable_automatic_settle(self):
        """Gets the enable_automatic_settle of this TerminalBankSettings.  # noqa: E501

        If enabled, the terminal's transactions will be automatically cleared and settled based on the cut-off time in `batchTime` property.  # noqa: E501

        :return: The enable_automatic_settle of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_automatic_settle

    @enable_automatic_settle.setter
    def enable_automatic_settle(self, enable_automatic_settle):
        """Sets the enable_automatic_settle of this TerminalBankSettings.

        If enabled, the terminal's transactions will be automatically cleared and settled based on the cut-off time in `batchTime` property.  # noqa: E501

        :param enable_automatic_settle: The enable_automatic_settle of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if enable_automatic_settle is None:
            raise ValueError("Invalid value for `enable_automatic_settle`, must not be `None`")  # noqa: E501

        self._enable_automatic_settle = enable_automatic_settle

    @property
    def batch_time(self):
        """Gets the batch_time of this TerminalBankSettings.  # noqa: E501

        Time, represented in the terminal's timezone, that defines the end-of-day closing for the terminal.<br />When in manual mode, merchants must send a `endOfDay` request in order to indicate that transactions performed prior to that moment are eligible to be cleared in the next settlement run.  # noqa: E501

        :return: The batch_time of this TerminalBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._batch_time

    @batch_time.setter
    def batch_time(self, batch_time):
        """Sets the batch_time of this TerminalBankSettings.

        Time, represented in the terminal's timezone, that defines the end-of-day closing for the terminal.<br />When in manual mode, merchants must send a `endOfDay` request in order to indicate that transactions performed prior to that moment are eligible to be cleared in the next settlement run.  # noqa: E501

        :param batch_time: The batch_time of this TerminalBankSettings.  # noqa: E501
        :type: str
        """

        self._batch_time = batch_time

    @property
    def display_name(self):
        """Gets the display_name of this TerminalBankSettings.  # noqa: E501

        Friendly name assigned by the merchant.  # noqa: E501

        :return: The display_name of this TerminalBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TerminalBankSettings.

        Friendly name assigned by the merchant.  # noqa: E501

        :param display_name: The display_name of this TerminalBankSettings.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def force_unique_order_id(self):
        """Gets the force_unique_order_id of this TerminalBankSettings.  # noqa: E501

        Indicates whether the terminal accepts duplicate order identifiers.<br />An order is considered a duplicate when there is already another approved transaction sitting in the open batch with the same identifier.  # noqa: E501

        :return: The force_unique_order_id of this TerminalBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._force_unique_order_id

    @force_unique_order_id.setter
    def force_unique_order_id(self, force_unique_order_id):
        """Sets the force_unique_order_id of this TerminalBankSettings.

        Indicates whether the terminal accepts duplicate order identifiers.<br />An order is considered a duplicate when there is already another approved transaction sitting in the open batch with the same identifier.  # noqa: E501

        :param force_unique_order_id: The force_unique_order_id of this TerminalBankSettings.  # noqa: E501
        :type: bool
        """
        if force_unique_order_id is None:
            raise ValueError("Invalid value for `force_unique_order_id`, must not be `None`")  # noqa: E501

        self._force_unique_order_id = force_unique_order_id
