# coding: utf-8
from model.serializable import SwaggerSerializable


class AuthorizeNetBankSettings(SwaggerSerializable):
    swagger_types = {
        'allow_multicurrency': 'bool',
        'base_currency': 'str',
        'supported_currencies': 'list[str]',
        'allow_moto': 'bool',
        'allow_internet': 'bool',
        'allow_recurring': 'bool',
        'api_login_id': 'str',
        'transaction_key': 'str',
        'enable_automatic_settle': 'bool',
        'batch_time': 'str',
        'display_name': 'str',
        'allow_edit_display_name': 'bool',
        'force_unique_order_id': 'bool'
    }

    attribute_map = {
        'allow_multicurrency': 'allowMulticurrency',
        'base_currency': 'baseCurrency',
        'supported_currencies': 'supportedCurrencies',
        'allow_moto': 'allowMoto',
        'allow_internet': 'allowInternet',
        'allow_recurring': 'allowRecurring',
        'api_login_id': 'apiLoginId',
        'transaction_key': 'transactionKey',
        'enable_automatic_settle': 'enableAutomaticSettle',
        'batch_time': 'batchTime',
        'display_name': 'displayName',
        'allow_edit_display_name': 'allowEditDisplayName',
        'force_unique_order_id': 'forceUniqueOrderId'
    }

    def __init__(self, allow_multicurrency=False, base_currency=None, supported_currencies=None, allow_moto=True, allow_internet=False, allow_recurring=True, api_login_id=None, transaction_key=None, enable_automatic_settle=True, batch_time=None, display_name=None, allow_edit_display_name=False, force_unique_order_id=True):  # noqa: E501
        """AuthorizeNetBankSettings - a model defined in Swagger"""  # noqa: E501
        self._allow_multicurrency = None
        self._base_currency = None
        self._supported_currencies = None
        self._allow_moto = None
        self._allow_internet = None
        self._allow_recurring = None
        self._api_login_id = None
        self._transaction_key = None
        self._enable_automatic_settle = None
        self._batch_time = None
        self._display_name = None
        self._allow_edit_display_name = None
        self._force_unique_order_id = None
        self.discriminator = None
        if allow_multicurrency is not None:
            self.allow_multicurrency = allow_multicurrency
        if base_currency is not None:
            self.base_currency = base_currency
        if supported_currencies is not None:
            self.supported_currencies = supported_currencies
        if allow_moto is not None:
            self.allow_moto = allow_moto
        if allow_internet is not None:
            self.allow_internet = allow_internet
        if allow_recurring is not None:
            self.allow_recurring = allow_recurring
        self.api_login_id = api_login_id
        self.transaction_key = transaction_key
        if enable_automatic_settle is not None:
            self.enable_automatic_settle = enable_automatic_settle
        if batch_time is not None:
            self.batch_time = batch_time
        if display_name is not None:
            self.display_name = display_name
        if allow_edit_display_name is not None:
            self.allow_edit_display_name = allow_edit_display_name
        if force_unique_order_id is not None:
            self.force_unique_order_id = force_unique_order_id

    @property
    def allow_multicurrency(self):
        """Gets the allow_multicurrency of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The allow_multicurrency of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multicurrency

    @allow_multicurrency.setter
    def allow_multicurrency(self, allow_multicurrency):
        """Sets the allow_multicurrency of this AuthorizeNetBankSettings.


        :param allow_multicurrency: The allow_multicurrency of this AuthorizeNetBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_multicurrency = allow_multicurrency

    @property
    def base_currency(self):
        """Gets the base_currency of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The base_currency of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this AuthorizeNetBankSettings.


        :param base_currency: The base_currency of this AuthorizeNetBankSettings.  # noqa: E501
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
        """Gets the supported_currencies of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The supported_currencies of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_currencies

    @supported_currencies.setter
    def supported_currencies(self, supported_currencies):
        """Sets the supported_currencies of this AuthorizeNetBankSettings.


        :param supported_currencies: The supported_currencies of this AuthorizeNetBankSettings.  # noqa: E501
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
        """Gets the allow_moto of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The allow_moto of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_moto

    @allow_moto.setter
    def allow_moto(self, allow_moto):
        """Sets the allow_moto of this AuthorizeNetBankSettings.


        :param allow_moto: The allow_moto of this AuthorizeNetBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_moto = allow_moto

    @property
    def allow_internet(self):
        """Gets the allow_internet of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The allow_internet of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_internet

    @allow_internet.setter
    def allow_internet(self, allow_internet):
        """Sets the allow_internet of this AuthorizeNetBankSettings.


        :param allow_internet: The allow_internet of this AuthorizeNetBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_internet = allow_internet

    @property
    def allow_recurring(self):
        """Gets the allow_recurring of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The allow_recurring of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_recurring

    @allow_recurring.setter
    def allow_recurring(self, allow_recurring):
        """Sets the allow_recurring of this AuthorizeNetBankSettings.


        :param allow_recurring: The allow_recurring of this AuthorizeNetBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_recurring = allow_recurring

    @property
    def api_login_id(self):
        """Gets the api_login_id of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The api_login_id of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._api_login_id

    @api_login_id.setter
    def api_login_id(self, api_login_id):
        """Sets the api_login_id of this AuthorizeNetBankSettings.


        :param api_login_id: The api_login_id of this AuthorizeNetBankSettings.  # noqa: E501
        :type: str
        """
        if api_login_id is None:
            raise ValueError("Invalid value for `api_login_id`, must not be `None`")  # noqa: E501

        self._api_login_id = api_login_id

    @property
    def transaction_key(self):
        """Gets the transaction_key of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The transaction_key of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._transaction_key

    @transaction_key.setter
    def transaction_key(self, transaction_key):
        """Sets the transaction_key of this AuthorizeNetBankSettings.


        :param transaction_key: The transaction_key of this AuthorizeNetBankSettings.  # noqa: E501
        :type: str
        """
        if transaction_key is None:
            raise ValueError("Invalid value for `transaction_key`, must not be `None`")  # noqa: E501

        self._transaction_key = transaction_key

    @property
    def enable_automatic_settle(self):
        """Gets the enable_automatic_settle of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The enable_automatic_settle of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_automatic_settle

    @enable_automatic_settle.setter
    def enable_automatic_settle(self, enable_automatic_settle):
        """Sets the enable_automatic_settle of this AuthorizeNetBankSettings.


        :param enable_automatic_settle: The enable_automatic_settle of this AuthorizeNetBankSettings.  # noqa: E501
        :type: bool
        """

        self._enable_automatic_settle = enable_automatic_settle

    @property
    def batch_time(self):
        """Gets the batch_time of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The batch_time of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._batch_time

    @batch_time.setter
    def batch_time(self, batch_time):
        """Sets the batch_time of this AuthorizeNetBankSettings.


        :param batch_time: The batch_time of this AuthorizeNetBankSettings.  # noqa: E501
        :type: str
        """

        self._batch_time = batch_time

    @property
    def display_name(self):
        """Gets the display_name of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The display_name of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AuthorizeNetBankSettings.


        :param display_name: The display_name of this AuthorizeNetBankSettings.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def allow_edit_display_name(self):
        """Gets the allow_edit_display_name of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The allow_edit_display_name of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_edit_display_name

    @allow_edit_display_name.setter
    def allow_edit_display_name(self, allow_edit_display_name):
        """Sets the allow_edit_display_name of this AuthorizeNetBankSettings.


        :param allow_edit_display_name: The allow_edit_display_name of this AuthorizeNetBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_edit_display_name = allow_edit_display_name

    @property
    def force_unique_order_id(self):
        """Gets the force_unique_order_id of this AuthorizeNetBankSettings.  # noqa: E501


        :return: The force_unique_order_id of this AuthorizeNetBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._force_unique_order_id

    @force_unique_order_id.setter
    def force_unique_order_id(self, force_unique_order_id):
        """Sets the force_unique_order_id of this AuthorizeNetBankSettings.


        :param force_unique_order_id: The force_unique_order_id of this AuthorizeNetBankSettings.  # noqa: E501
        :type: bool
        """

        self._force_unique_order_id = force_unique_order_id
