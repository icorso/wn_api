# coding: utf-8
from model.serializable import SwaggerSerializable


class FiServBankSettings(SwaggerSerializable):
    swagger_types = {
        'base_currency': 'str',
        'allow_chp': 'bool',
        'default_terminal_type': 'str',
        'card_acceptor_id': 'str',
        'card_acceptor_terminal_id': 'str',
        'fns_number': 'str',
        'enable_automatic_settle': 'bool',
        'batch_time': 'str',
        'display_name': 'str',
        'allow_edit_display_name': 'bool',
        'force_unique_order_id': 'bool'
    }

    attribute_map = {
        'base_currency': 'baseCurrency',
        'allow_chp': 'allowChp',
        'default_terminal_type': 'defaultTerminalType',
        'card_acceptor_id': 'cardAcceptorId',
        'card_acceptor_terminal_id': 'cardAcceptorTerminalId',
        'fns_number': 'fnsNumber',
        'enable_automatic_settle': 'enableAutomaticSettle',
        'batch_time': 'batchTime',
        'display_name': 'displayName',
        'allow_edit_display_name': 'allowEditDisplayName',
        'force_unique_order_id': 'forceUniqueOrderId'
    }

    def __init__(self, base_currency=None, allow_chp=True, default_terminal_type=None, card_acceptor_id=None, card_acceptor_terminal_id=None, fns_number=None, enable_automatic_settle=True, batch_time=None, display_name=None, allow_edit_display_name=False, force_unique_order_id=True):
        self._base_currency = None
        self._allow_chp = None
        self._default_terminal_type = None
        self._card_acceptor_id = None
        self._card_acceptor_terminal_id = None
        self._fns_number = None
        self._enable_automatic_settle = None
        self._batch_time = None
        self._display_name = None
        self._allow_edit_display_name = None
        self._force_unique_order_id = None
        self.discriminator = None
        self.base_currency = base_currency
        if allow_chp is not None:
            self.allow_chp = allow_chp
        if default_terminal_type is not None:
            self.default_terminal_type = default_terminal_type
        self.card_acceptor_id = card_acceptor_id
        self.card_acceptor_terminal_id = card_acceptor_terminal_id
        self.fns_number = fns_number
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
        """Gets the base_currency of this FiServBankSettings.  # noqa: E501


        :return: The base_currency of this FiServBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this FiServBankSettings.


        :param base_currency: The base_currency of this FiServBankSettings.  # noqa: E501
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
    def allow_chp(self):
        """Gets the allow_chp of this FiServBankSettings.  # noqa: E501


        :return: The allow_chp of this FiServBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_chp

    @allow_chp.setter
    def allow_chp(self, allow_chp):
        """Sets the allow_chp of this FiServBankSettings.


        :param allow_chp: The allow_chp of this FiServBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_chp = allow_chp

    @property
    def default_terminal_type(self):
        """Gets the default_terminal_type of this FiServBankSettings.  # noqa: E501

        CHP  # noqa: E501

        :return: The default_terminal_type of this FiServBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_terminal_type

    @default_terminal_type.setter
    def default_terminal_type(self, default_terminal_type):
        """Sets the default_terminal_type of this FiServBankSettings.

        CHP  # noqa: E501

        :param default_terminal_type: The default_terminal_type of this FiServBankSettings.  # noqa: E501
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
    def card_acceptor_id(self):
        """Gets the card_acceptor_id of this FiServBankSettings.  # noqa: E501


        :return: The card_acceptor_id of this FiServBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._card_acceptor_id

    @card_acceptor_id.setter
    def card_acceptor_id(self, card_acceptor_id):
        """Sets the card_acceptor_id of this FiServBankSettings.


        :param card_acceptor_id: The card_acceptor_id of this FiServBankSettings.  # noqa: E501
        :type: str
        """
        self._card_acceptor_id = card_acceptor_id

    @property
    def card_acceptor_terminal_id(self):
        """Gets the card_acceptor_terminal_id of this FiServBankSettings.  # noqa: E501


        :return: The card_acceptor_terminal_id of this FiServBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._card_acceptor_terminal_id

    @card_acceptor_terminal_id.setter
    def card_acceptor_terminal_id(self, card_acceptor_terminal_id):
        """Sets the card_acceptor_terminal_id of this FiServBankSettings.


        :param card_acceptor_terminal_id: The card_acceptor_terminal_id of this FiServBankSettings.  # noqa: E501
        :type: str
        """
        self._card_acceptor_terminal_id = card_acceptor_terminal_id

    @property
    def fns_number(self):
        """Gets the fns_number of this FiServBankSettings.  # noqa: E501


        :return: The fns_number of this FiServBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._fns_number

    @fns_number.setter
    def fns_number(self, fns_number):
        self._fns_number = fns_number

    @property
    def enable_automatic_settle(self):
        """Gets the enable_automatic_settle of this FiServBankSettings.  # noqa: E501


        :return: The enable_automatic_settle of this FiServBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_automatic_settle

    @enable_automatic_settle.setter
    def enable_automatic_settle(self, enable_automatic_settle):
        """Sets the enable_automatic_settle of this FiServBankSettings.


        :param enable_automatic_settle: The enable_automatic_settle of this FiServBankSettings.  # noqa: E501
        :type: bool
        """

        self._enable_automatic_settle = enable_automatic_settle

    @property
    def batch_time(self):
        """Gets the batch_time of this FiServBankSettings.  # noqa: E501


        :return: The batch_time of this FiServBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._batch_time

    @batch_time.setter
    def batch_time(self, batch_time):
        """Sets the batch_time of this FiServBankSettings.


        :param batch_time: The batch_time of this FiServBankSettings.  # noqa: E501
        :type: str
        """

        self._batch_time = batch_time

    @property
    def display_name(self):
        """Gets the display_name of this FiServBankSettings.  # noqa: E501


        :return: The display_name of this FiServBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FiServBankSettings.


        :param display_name: The display_name of this FiServBankSettings.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def allow_edit_display_name(self):
        """Gets the allow_edit_display_name of this FiServBankSettings.  # noqa: E501


        :return: The allow_edit_display_name of this FiServBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_edit_display_name

    @allow_edit_display_name.setter
    def allow_edit_display_name(self, allow_edit_display_name):
        """Sets the allow_edit_display_name of this FiServBankSettings.


        :param allow_edit_display_name: The allow_edit_display_name of this FiServBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_edit_display_name = allow_edit_display_name

    @property
    def force_unique_order_id(self):
        """Gets the force_unique_order_id of this FiServBankSettings.  # noqa: E501


        :return: The force_unique_order_id of this FiServBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._force_unique_order_id

    @force_unique_order_id.setter
    def force_unique_order_id(self, force_unique_order_id):
        """Sets the force_unique_order_id of this FiServBankSettings.


        :param force_unique_order_id: The force_unique_order_id of this FiServBankSettings.  # noqa: E501
        :type: bool
        """

        self._force_unique_order_id = force_unique_order_id

