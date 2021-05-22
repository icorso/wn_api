# coding: utf-8

from model.serializable import SwaggerSerializable


class VacpG2GBankSettings(SwaggerSerializable):
    swagger_types = {
        'base_currency': 'str',
        'allow_moto': 'bool',
        'allow_internet': 'bool',
        'allow_chp': 'bool',
        'default_terminal_type': 'str',
        'allow_recurring': 'bool',
        'allow_pre_auth': 'bool',
        'bank_merchant_id': 'str',
        'bank_terminal_id': 'str',
        'transaction_key': 'str',
        'third_party_certification_number': 'str',
        'terminal_capability': 'str',
        'enable_automatic_settle': 'bool',
        'batch_time': 'str',
        'display_name': 'str',
        'allow_edit_display_name': 'bool',
        'force_unique_order_id': 'bool'
    }

    attribute_map = {
        'base_currency': 'baseCurrency',
        'allow_moto': 'allowMoto',
        'allow_internet': 'allowInternet',
        'allow_chp': 'allowChp',
        'default_terminal_type': 'defaultTerminalType',
        'allow_recurring': 'allowRecurring',
        'allow_pre_auth': 'allowPreAuth',
        'bank_merchant_id': 'bankMerchantId',
        'bank_terminal_id': 'bankTerminalId',
        'transaction_key': 'transactionKey',
        'third_party_certification_number': 'thirdPartyCertificationNumber',
        'terminal_capability': 'terminalCapability',
        'enable_automatic_settle': 'enableAutomaticSettle',
        'batch_time': 'batchTime',
        'display_name': 'displayName',
        'allow_edit_display_name': 'allowEditDisplayName',
        'force_unique_order_id': 'forceUniqueOrderId'
    }

    def __init__(self, base_currency=None, allow_moto=True, allow_internet=False, allow_chp=False, default_terminal_type='MOTO', allow_recurring=True, allow_pre_auth=False, bank_merchant_id=None, bank_terminal_id=None, transaction_key=None, third_party_certification_number=None, terminal_capability=None, enable_automatic_settle=True, batch_time=None, display_name=None, allow_edit_display_name=False, force_unique_order_id=True):  # noqa: E501
        """VacpG2GBankSettings - a model defined in Swagger"""  # noqa: E501
        self._base_currency = None
        self._allow_moto = None
        self._allow_internet = None
        self._allow_chp = None
        self._default_terminal_type = None
        self._allow_recurring = None
        self._allow_pre_auth = None
        self._bank_merchant_id = None
        self._bank_terminal_id = None
        self._transaction_key = None
        self._third_party_certification_number = None
        self._terminal_capability = None
        self._enable_automatic_settle = None
        self._batch_time = None
        self._display_name = None
        self._allow_edit_display_name = None
        self._force_unique_order_id = None
        self.discriminator = None
        self.base_currency = base_currency
        if allow_moto is not None:
            self.allow_moto = allow_moto
        if allow_internet is not None:
            self.allow_internet = allow_internet
        if allow_chp is not None:
            self.allow_chp = allow_chp
        if default_terminal_type is not None:
            self.default_terminal_type = default_terminal_type
        if allow_recurring is not None:
            self.allow_recurring = allow_recurring
        if allow_pre_auth is not None:
            self.allow_pre_auth = allow_pre_auth
        self.bank_merchant_id = bank_merchant_id
        self.bank_terminal_id = bank_terminal_id
        self.transaction_key = transaction_key
        self.third_party_certification_number = third_party_certification_number
        self.terminal_capability = terminal_capability
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
    def base_currency(self):
        """Gets the base_currency of this VacpG2GBankSettings.  # noqa: E501


        :return: The base_currency of this VacpG2GBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this VacpG2GBankSettings.


        :param base_currency: The base_currency of this VacpG2GBankSettings.  # noqa: E501
        :type: str
        """
        if base_currency is None:
            raise ValueError("Invalid value for `base_currency`, must not be `None`")  # noqa: E501
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if base_currency not in allowed_values:
            raise ValueError(
                "Invalid value for `base_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(base_currency, allowed_values)
            )

        self._base_currency = base_currency

    @property
    def allow_moto(self):
        """Gets the allow_moto of this VacpG2GBankSettings.  # noqa: E501


        :return: The allow_moto of this VacpG2GBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_moto

    @allow_moto.setter
    def allow_moto(self, allow_moto):
        """Sets the allow_moto of this VacpG2GBankSettings.


        :param allow_moto: The allow_moto of this VacpG2GBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_moto = allow_moto

    @property
    def allow_internet(self):
        """Gets the allow_internet of this VacpG2GBankSettings.  # noqa: E501


        :return: The allow_internet of this VacpG2GBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_internet

    @allow_internet.setter
    def allow_internet(self, allow_internet):
        """Sets the allow_internet of this VacpG2GBankSettings.


        :param allow_internet: The allow_internet of this VacpG2GBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_internet = allow_internet

    @property
    def allow_chp(self):
        """Gets the allow_chp of this VacpG2GBankSettings.  # noqa: E501


        :return: The allow_chp of this VacpG2GBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_chp

    @allow_chp.setter
    def allow_chp(self, allow_chp):
        """Sets the allow_chp of this VacpG2GBankSettings.


        :param allow_chp: The allow_chp of this VacpG2GBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_chp = allow_chp

    @property
    def default_terminal_type(self):
        """Gets the default_terminal_type of this VacpG2GBankSettings.  # noqa: E501


        :return: The default_terminal_type of this VacpG2GBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_terminal_type

    @default_terminal_type.setter
    def default_terminal_type(self, default_terminal_type):
        """Sets the default_terminal_type of this VacpG2GBankSettings.


        :param default_terminal_type: The default_terminal_type of this VacpG2GBankSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["MOTO", "CHP"]  # noqa: E501
        if default_terminal_type not in allowed_values:
            raise ValueError(
                "Invalid value for `default_terminal_type` ({0}), must be one of {1}"  # noqa: E501
                .format(default_terminal_type, allowed_values)
            )

        self._default_terminal_type = default_terminal_type

    @property
    def allow_recurring(self):
        """Gets the allow_recurring of this VacpG2GBankSettings.  # noqa: E501


        :return: The allow_recurring of this VacpG2GBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_recurring

    @allow_recurring.setter
    def allow_recurring(self, allow_recurring):
        """Sets the allow_recurring of this VacpG2GBankSettings.


        :param allow_recurring: The allow_recurring of this VacpG2GBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_recurring = allow_recurring

    @property
    def allow_pre_auth(self):
        """Gets the allow_pre_auth of this VacpG2GBankSettings.  # noqa: E501


        :return: The allow_pre_auth of this VacpG2GBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_pre_auth

    @allow_pre_auth.setter
    def allow_pre_auth(self, allow_pre_auth):
        """Sets the allow_pre_auth of this VacpG2GBankSettings.


        :param allow_pre_auth: The allow_pre_auth of this VacpG2GBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_pre_auth = allow_pre_auth

    @property
    def bank_merchant_id(self):
        """Gets the bank_merchant_id of this VacpG2GBankSettings.  # noqa: E501


        :return: The bank_merchant_id of this VacpG2GBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._bank_merchant_id

    @bank_merchant_id.setter
    def bank_merchant_id(self, bank_merchant_id):
        """Sets the bank_merchant_id of this VacpG2GBankSettings.


        :param bank_merchant_id: The bank_merchant_id of this VacpG2GBankSettings.  # noqa: E501
        :type: str
        """
        if bank_merchant_id is None:
            raise ValueError("Invalid value for `bank_merchant_id`, must not be `None`")  # noqa: E501

        self._bank_merchant_id = bank_merchant_id

    @property
    def bank_terminal_id(self):
        """Gets the bank_terminal_id of this VacpG2GBankSettings.  # noqa: E501


        :return: The bank_terminal_id of this VacpG2GBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._bank_terminal_id

    @bank_terminal_id.setter
    def bank_terminal_id(self, bank_terminal_id):
        """Sets the bank_terminal_id of this VacpG2GBankSettings.


        :param bank_terminal_id: The bank_terminal_id of this VacpG2GBankSettings.  # noqa: E501
        :type: str
        """
        if bank_terminal_id is None:
            raise ValueError("Invalid value for `bank_terminal_id`, must not be `None`")  # noqa: E501

        self._bank_terminal_id = bank_terminal_id

    @property
    def transaction_key(self):
        """Gets the transaction_key of this VacpG2GBankSettings.  # noqa: E501


        :return: The transaction_key of this VacpG2GBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._transaction_key

    @transaction_key.setter
    def transaction_key(self, transaction_key):
        """Sets the transaction_key of this VacpG2GBankSettings.


        :param transaction_key: The transaction_key of this VacpG2GBankSettings.  # noqa: E501
        :type: str
        """
        if transaction_key is None:
            raise ValueError("Invalid value for `transaction_key`, must not be `None`")  # noqa: E501

        self._transaction_key = transaction_key

    @property
    def third_party_certification_number(self):
        """Gets the third_party_certification_number of this VacpG2GBankSettings.  # noqa: E501


        :return: The third_party_certification_number of this VacpG2GBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._third_party_certification_number

    @third_party_certification_number.setter
    def third_party_certification_number(self, third_party_certification_number):
        """Sets the third_party_certification_number of this VacpG2GBankSettings.


        :param third_party_certification_number: The third_party_certification_number of this VacpG2GBankSettings.  # noqa: E501
        :type: str
        """
        if third_party_certification_number is None:
            raise ValueError("Invalid value for `third_party_certification_number`, must not be `None`")  # noqa: E501

        self._third_party_certification_number = third_party_certification_number

    @property
    def terminal_capability(self):
        """Gets the terminal_capability of this VacpG2GBankSettings.  # noqa: E501


        :return: The terminal_capability of this VacpG2GBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._terminal_capability

    @terminal_capability.setter
    def terminal_capability(self, terminal_capability):
        """Sets the terminal_capability of this VacpG2GBankSettings.


        :param terminal_capability: The terminal_capability of this VacpG2GBankSettings.  # noqa: E501
        :type: str
        """
        if terminal_capability is None:
            raise ValueError("Invalid value for `terminal_capability`, must not be `None`")  # noqa: E501
        allowed_values = ["MAG_STRIPE_READ_ONLY", "MAG_STRIPE_AND_MANUAL_ENTRY", "MANUAL_ENTRY_ONLY", "EMV_INCLUDE_PROXIMITY", "EMV_DOES_NOT_INCLUDE_CONTACT"]  # noqa: E501
        if terminal_capability not in allowed_values:
            raise ValueError(
                "Invalid value for `terminal_capability` ({0}), must be one of {1}"  # noqa: E501
                .format(terminal_capability, allowed_values)
            )

        self._terminal_capability = terminal_capability

    @property
    def enable_automatic_settle(self):
        """Gets the enable_automatic_settle of this VacpG2GBankSettings.  # noqa: E501


        :return: The enable_automatic_settle of this VacpG2GBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_automatic_settle

    @enable_automatic_settle.setter
    def enable_automatic_settle(self, enable_automatic_settle):
        """Sets the enable_automatic_settle of this VacpG2GBankSettings.


        :param enable_automatic_settle: The enable_automatic_settle of this VacpG2GBankSettings.  # noqa: E501
        :type: bool
        """

        self._enable_automatic_settle = enable_automatic_settle

    @property
    def batch_time(self):
        """Gets the batch_time of this VacpG2GBankSettings.  # noqa: E501


        :return: The batch_time of this VacpG2GBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._batch_time

    @batch_time.setter
    def batch_time(self, batch_time):
        """Sets the batch_time of this VacpG2GBankSettings.


        :param batch_time: The batch_time of this VacpG2GBankSettings.  # noqa: E501
        :type: str
        """

        self._batch_time = batch_time

    @property
    def display_name(self):
        """Gets the display_name of this VacpG2GBankSettings.  # noqa: E501


        :return: The display_name of this VacpG2GBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this VacpG2GBankSettings.


        :param display_name: The display_name of this VacpG2GBankSettings.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def allow_edit_display_name(self):
        """Gets the allow_edit_display_name of this VacpG2GBankSettings.  # noqa: E501


        :return: The allow_edit_display_name of this VacpG2GBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_edit_display_name

    @allow_edit_display_name.setter
    def allow_edit_display_name(self, allow_edit_display_name):
        """Sets the allow_edit_display_name of this VacpG2GBankSettings.


        :param allow_edit_display_name: The allow_edit_display_name of this VacpG2GBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_edit_display_name = allow_edit_display_name

    @property
    def force_unique_order_id(self):
        """Gets the force_unique_order_id of this VacpG2GBankSettings.  # noqa: E501


        :return: The force_unique_order_id of this VacpG2GBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._force_unique_order_id

    @force_unique_order_id.setter
    def force_unique_order_id(self, force_unique_order_id):
        """Sets the force_unique_order_id of this VacpG2GBankSettings.


        :param force_unique_order_id: The force_unique_order_id of this VacpG2GBankSettings.  # noqa: E501
        :type: bool
        """

        self._force_unique_order_id = force_unique_order_id
