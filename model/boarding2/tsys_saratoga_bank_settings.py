# coding: utf-8
from model.serializable import SwaggerSerializable


class TsysSaratogaBankSettings(SwaggerSerializable):
    swagger_types = {
        'group_bank_name': 'str',
        'allow_multicurrency': 'bool',
        'allow_emcp': 'bool',
        'allow_edcc': 'bool',
        'edcc_provider': 'str',
        'base_currency': 'str',
        'supported_currencies': 'list[str]',
        'allow_moto': 'bool',
        'allow_internet': 'bool',
        'allow_chp': 'bool',
        'default_terminal_type': 'str',
        'allow_recurring': 'bool',
        'allow_pre_auth': 'bool',
        'bank_merchant_id': 'str',
        'bank_terminal_id': 'str',
        'agent_bank_number': 'str',
        'agent_chain_number': 'str',
        'store_number': 'str',
        'terminal_id_number': 'str',
        'acq_institution_id_code': 'str',
        'mark_up_percentage': 'float',
        'customer_service_email': 'str',
        'customer_service_url': 'str',
        'enable_automatic_settle': 'bool',
        'batch_time': 'str',
        'display_name': 'str',
        'allow_edit_display_name': 'bool',
        'force_unique_order_id': 'bool'
    }

    attribute_map = {
        'group_bank_name': 'groupBankName',
        'allow_multicurrency': 'allowMulticurrency',
        'allow_emcp': 'allowEmcp',
        'allow_edcc': 'allowEdcc',
        'edcc_provider': 'edccProvider',
        'base_currency': 'baseCurrency',
        'supported_currencies': 'supportedCurrencies',
        'allow_moto': 'allowMoto',
        'allow_internet': 'allowInternet',
        'allow_chp': 'allowChp',
        'default_terminal_type': 'defaultTerminalType',
        'allow_recurring': 'allowRecurring',
        'allow_pre_auth': 'allowPreAuth',
        'bank_merchant_id': 'bankMerchantId',
        'bank_terminal_id': 'bankTerminalId',
        'agent_bank_number': 'agentBankNumber',
        'agent_chain_number': 'agentChainNumber',
        'store_number': 'storeNumber',
        'terminal_id_number': 'terminalIdNumber',
        'acq_institution_id_code': 'acqInstitutionIdCode',
        'mark_up_percentage': 'markUpPercentage',
        'customer_service_email': 'customerServiceEmail',
        'customer_service_url': 'customerServiceUrl',
        'enable_automatic_settle': 'enableAutomaticSettle',
        'batch_time': 'batchTime',
        'display_name': 'displayName',
        'allow_edit_display_name': 'allowEditDisplayName',
        'force_unique_order_id': 'forceUniqueOrderId'
    }

    def __init__(self, group_bank_name=None, allow_multicurrency=False, allow_emcp=False, allow_edcc=False, edcc_provider=None, base_currency=None, supported_currencies=None, allow_moto=True, allow_internet=False, allow_chp=False, default_terminal_type='MOTO', allow_recurring=True, allow_pre_auth=False, bank_merchant_id=None, bank_terminal_id=None, agent_bank_number=None, agent_chain_number=None, store_number=None, terminal_id_number=None, acq_institution_id_code=None, mark_up_percentage=None, customer_service_email=None, customer_service_url=None, enable_automatic_settle=True, batch_time=None, display_name=None, allow_edit_display_name=False, force_unique_order_id=True):  # noqa: E501
        self._group_bank_name = None
        self._allow_multicurrency = None
        self._allow_emcp = None
        self._allow_edcc = None
        self._edcc_provider = None
        self._base_currency = None
        self._supported_currencies = None
        self._allow_moto = None
        self._allow_internet = None
        self._allow_chp = None
        self._default_terminal_type = None
        self._allow_recurring = None
        self._allow_pre_auth = None
        self._bank_merchant_id = None
        self._bank_terminal_id = None
        self._agent_bank_number = None
        self._agent_chain_number = None
        self._store_number = None
        self._terminal_id_number = None
        self._acq_institution_id_code = None
        self._mark_up_percentage = None
        self._customer_service_email = None
        self._customer_service_url = None
        self._enable_automatic_settle = None
        self._batch_time = None
        self._display_name = None
        self._allow_edit_display_name = None
        self._force_unique_order_id = None
        self.discriminator = None
        self.group_bank_name = group_bank_name
        if allow_multicurrency is not None:
            self.allow_multicurrency = allow_multicurrency
        if allow_emcp is not None:
            self.allow_emcp = allow_emcp
        if allow_edcc is not None:
            self.allow_edcc = allow_edcc
        if edcc_provider is not None:
            self.edcc_provider = edcc_provider
        if base_currency is not None:
            self.base_currency = base_currency
        if supported_currencies is not None:
            self.supported_currencies = supported_currencies
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
        self.agent_bank_number = agent_bank_number
        self.agent_chain_number = agent_chain_number
        self.store_number = store_number
        self.terminal_id_number = terminal_id_number
        self.acq_institution_id_code = acq_institution_id_code
        if mark_up_percentage is not None:
            self.mark_up_percentage = mark_up_percentage
        if customer_service_email is not None:
            self.customer_service_email = customer_service_email
        if customer_service_url is not None:
            self.customer_service_url = customer_service_url
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
    def group_bank_name(self):
        return self._group_bank_name

    @group_bank_name.setter
    def group_bank_name(self, group_bank_name):
        if group_bank_name is None:
            raise ValueError("Invalid value for `group_bank_name`, must not be `None`")  # noqa: E501

        self._group_bank_name = group_bank_name

    @property
    def allow_multicurrency(self):
        return self._allow_multicurrency

    @allow_multicurrency.setter
    def allow_multicurrency(self, allow_multicurrency):
        self._allow_multicurrency = allow_multicurrency

    @property
    def allow_emcp(self):
        return self._allow_emcp

    @allow_emcp.setter
    def allow_emcp(self, allow_emcp):
        self._allow_emcp = allow_emcp

    @property
    def allow_edcc(self):
        return self._allow_edcc

    @allow_edcc.setter
    def allow_edcc(self, allow_edcc):
        self._allow_edcc = allow_edcc

    @property
    def edcc_provider(self):
        return self._edcc_provider

    @edcc_provider.setter
    def edcc_provider(self, edcc_provider):
        self._edcc_provider = edcc_provider

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
                "Invalid value for `base_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(base_currency, allowed_values)
            )

        self._base_currency = base_currency

    @property
    def supported_currencies(self):
        return self._supported_currencies

    @supported_currencies.setter
    def supported_currencies(self, supported_currencies):
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
        if not set(supported_currencies).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `supported_currencies` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(supported_currencies) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._supported_currencies = supported_currencies

    @property
    def allow_moto(self):
        return self._allow_moto

    @allow_moto.setter
    def allow_moto(self, allow_moto):
        self._allow_moto = allow_moto

    @property
    def allow_internet(self):
        return self._allow_internet

    @allow_internet.setter
    def allow_internet(self, allow_internet):
        self._allow_internet = allow_internet

    @property
    def allow_chp(self):
        return self._allow_chp

    @allow_chp.setter
    def allow_chp(self, allow_chp):
        self._allow_chp = allow_chp

    @property
    def default_terminal_type(self):
        return self._default_terminal_type

    @default_terminal_type.setter
    def default_terminal_type(self, default_terminal_type):
        allowed_values = ["MOTO", "CHP"]  # noqa: E501
        if default_terminal_type not in allowed_values:
            raise ValueError(
                "Invalid value for `default_terminal_type` ({0}), must be one of {1}"  # noqa: E501
                .format(default_terminal_type, allowed_values)
            )

        self._default_terminal_type = default_terminal_type

    @property
    def allow_recurring(self):
        return self._allow_recurring

    @allow_recurring.setter
    def allow_recurring(self, allow_recurring):
        self._allow_recurring = allow_recurring

    @property
    def allow_pre_auth(self):
        return self._allow_pre_auth

    @allow_pre_auth.setter
    def allow_pre_auth(self, allow_pre_auth):
        self._allow_pre_auth = allow_pre_auth

    @property
    def bank_merchant_id(self):
        return self._bank_merchant_id

    @bank_merchant_id.setter
    def bank_merchant_id(self, bank_merchant_id):
        if bank_merchant_id is None:
            raise ValueError("Invalid value for `bank_merchant_id`, must not be `None`")  # noqa: E501

        self._bank_merchant_id = bank_merchant_id

    @property
    def bank_terminal_id(self):
        return self._bank_terminal_id

    @bank_terminal_id.setter
    def bank_terminal_id(self, bank_terminal_id):
        if bank_terminal_id is None:
            raise ValueError("Invalid value for `bank_terminal_id`, must not be `None`")  # noqa: E501

        self._bank_terminal_id = bank_terminal_id

    @property
    def agent_bank_number(self):
        return self._agent_bank_number

    @agent_bank_number.setter
    def agent_bank_number(self, agent_bank_number):
        if agent_bank_number is None:
            raise ValueError("Invalid value for `agent_bank_number`, must not be `None`")  # noqa: E501

        self._agent_bank_number = agent_bank_number

    @property
    def agent_chain_number(self):
        return self._agent_chain_number

    @agent_chain_number.setter
    def agent_chain_number(self, agent_chain_number):
        if agent_chain_number is None:
            raise ValueError("Invalid value for `agent_chain_number`, must not be `None`")  # noqa: E501

        self._agent_chain_number = agent_chain_number

    @property
    def store_number(self):
        return self._store_number

    @store_number.setter
    def store_number(self, store_number):
        if store_number is None:
            raise ValueError("Invalid value for `store_number`, must not be `None`")  # noqa: E501

        self._store_number = store_number

    @property
    def terminal_id_number(self):
        return self._terminal_id_number

    @terminal_id_number.setter
    def terminal_id_number(self, terminal_id_number):
        if terminal_id_number is None:
            raise ValueError("Invalid value for `terminal_id_number`, must not be `None`")  # noqa: E501

        self._terminal_id_number = terminal_id_number

    @property
    def acq_institution_id_code(self):
        return self._acq_institution_id_code

    @acq_institution_id_code.setter
    def acq_institution_id_code(self, acq_institution_id_code):
        if acq_institution_id_code is None:
            raise ValueError("Invalid value for `acq_institution_id_code`, must not be `None`")  # noqa: E501

        self._acq_institution_id_code = acq_institution_id_code

    @property
    def mark_up_percentage(self):
        return self._mark_up_percentage

    @mark_up_percentage.setter
    def mark_up_percentage(self, mark_up_percentage):
        self._mark_up_percentage = mark_up_percentage

    @property
    def customer_service_email(self):
        return self._customer_service_email

    @customer_service_email.setter
    def customer_service_email(self, customer_service_email):
        self._customer_service_email = customer_service_email

    @property
    def customer_service_url(self):
        return self._customer_service_url

    @customer_service_url.setter
    def customer_service_url(self, customer_service_url):
        self._customer_service_url = customer_service_url

    @property
    def enable_automatic_settle(self):
        return self._enable_automatic_settle

    @enable_automatic_settle.setter
    def enable_automatic_settle(self, enable_automatic_settle):
        self._enable_automatic_settle = enable_automatic_settle

    @property
    def batch_time(self):
        return self._batch_time

    @batch_time.setter
    def batch_time(self, batch_time):
        self._batch_time = batch_time

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    @property
    def allow_edit_display_name(self):
        return self._allow_edit_display_name

    @allow_edit_display_name.setter
    def allow_edit_display_name(self, allow_edit_display_name):
        self._allow_edit_display_name = allow_edit_display_name

    @property
    def force_unique_order_id(self):
        return self._force_unique_order_id

    @force_unique_order_id.setter
    def force_unique_order_id(self, force_unique_order_id):
        self._force_unique_order_id = force_unique_order_id
