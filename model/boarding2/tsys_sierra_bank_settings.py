# coding: utf-8

from model.serializable import SwaggerSerializable


class TsysSierraBankSettings(SwaggerSerializable):
    swagger_types = {
        'base_currency': 'str',
        'allow_moto': 'bool',
        'allow_internet': 'bool',
        'allow_chp': 'bool',
        'default_terminal_type': 'str',
        'allow_recurring': 'bool',
        'allow_pre_auth': 'bool',
        'dst_observed': 'bool',
        'bank_merchant_id': 'str',
        'bank_terminal_id': 'str',
        'agent_bank_number': 'str',
        'agent_chain_number': 'str',
        'store_number': 'str',
        'terminal_id_number': 'str',
        'authentication_code': 'str',
        'acquirer_bin': 'str',
        'merchant_aba_number': 'str',
        'merchant_settlement_agent_number': 'str',
        'sharing_group': 'str',
        'food_and_consumer_id': 'str',
        'industry_code': 'str',
        'language_indicator': 'str',
        'reimbursement_attribute': 'str',
        'enable_automatic_settle': 'bool',
        'batch_time': 'str',
        'display_name': 'str',
        'allow_edit_display_name': 'bool',
        'force_unique_order_id': 'bool',
        'cardholder_service_phone_number': 'str'
    }

    attribute_map = {
        'base_currency': 'baseCurrency',
        'allow_moto': 'allowMoto',
        'allow_internet': 'allowInternet',
        'allow_chp': 'allowChp',
        'default_terminal_type': 'defaultTerminalType',
        'allow_recurring': 'allowRecurring',
        'allow_pre_auth': 'allowPreAuth',
        'dst_observed': 'dstObserved',
        'bank_merchant_id': 'bankMerchantId',
        'bank_terminal_id': 'bankTerminalId',
        'agent_bank_number': 'agentBankNumber',
        'agent_chain_number': 'agentChainNumber',
        'store_number': 'storeNumber',
        'terminal_id_number': 'terminalIdNumber',
        'authentication_code': 'authenticationCode',
        'acquirer_bin': 'acquirerBin',
        'merchant_aba_number': 'merchantAbaNumber',
        'merchant_settlement_agent_number': 'merchantSettlementAgentNumber',
        'sharing_group': 'sharingGroup',
        'food_and_consumer_id': 'foodAndConsumerId',
        'industry_code': 'industryCode',
        'language_indicator': 'languageIndicator',
        'reimbursement_attribute': 'reimbursementAttribute',
        'enable_automatic_settle': 'enableAutomaticSettle',
        'batch_time': 'batchTime',
        'display_name': 'displayName',
        'allow_edit_display_name': 'allowEditDisplayName',
        'force_unique_order_id': 'forceUniqueOrderId',
        'cardholder_service_phone_number': 'cardholderServicePhoneNumber'
    }

    def __init__(self, base_currency=None, allow_moto=True, allow_internet=False, allow_chp=False, default_terminal_type='MOTO', allow_recurring=True, allow_pre_auth=False, dst_observed=False, bank_merchant_id=None, bank_terminal_id=None, agent_bank_number=None, agent_chain_number=None, store_number=None, terminal_id_number=None, authentication_code=None, acquirer_bin=None, merchant_aba_number=None, merchant_settlement_agent_number=None, sharing_group=None, food_and_consumer_id=None, industry_code=None, language_indicator=None, reimbursement_attribute=None, enable_automatic_settle=True, batch_time=None, display_name=None, allow_edit_display_name=False, force_unique_order_id=True, cardholder_service_phone_number=None):  # noqa: E501
        """TsysSierraBankSettings - a model defined in Swagger"""  # noqa: E501
        self._base_currency = None
        self._allow_moto = None
        self._allow_internet = None
        self._allow_chp = None
        self._default_terminal_type = None
        self._allow_recurring = None
        self._allow_pre_auth = None
        self._dst_observed = None
        self._bank_merchant_id = None
        self._bank_terminal_id = None
        self._agent_bank_number = None
        self._agent_chain_number = None
        self._store_number = None
        self._terminal_id_number = None
        self._authentication_code = None
        self._acquirer_bin = None
        self._merchant_aba_number = None
        self._merchant_settlement_agent_number = None
        self._sharing_group = None
        self._food_and_consumer_id = None
        self._industry_code = None
        self._language_indicator = None
        self._reimbursement_attribute = None
        self._enable_automatic_settle = None
        self._batch_time = None
        self._display_name = None
        self._allow_edit_display_name = None
        self._force_unique_order_id = None
        self._cardholder_service_phone_number = None
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
        if dst_observed is not None:
            self.dst_observed = dst_observed
        self.bank_merchant_id = bank_merchant_id
        self.bank_terminal_id = bank_terminal_id
        self.agent_bank_number = agent_bank_number
        self.agent_chain_number = agent_chain_number
        self.store_number = store_number
        self.terminal_id_number = terminal_id_number
        self.authentication_code = authentication_code
        self.acquirer_bin = acquirer_bin
        if merchant_aba_number is not None:
            self.merchant_aba_number = merchant_aba_number
        if merchant_settlement_agent_number is not None:
            self.merchant_settlement_agent_number = merchant_settlement_agent_number
        if sharing_group is not None:
            self.sharing_group = sharing_group
        if food_and_consumer_id is not None:
            self.food_and_consumer_id = food_and_consumer_id
        self.industry_code = industry_code
        self.language_indicator = language_indicator
        self.reimbursement_attribute = reimbursement_attribute
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
        if cardholder_service_phone_number is not None:
            self.cardholder_service_phone_number = cardholder_service_phone_number

    @property
    def base_currency(self):
        """Gets the base_currency of this TsysSierraBankSettings.  # noqa: E501


        :return: The base_currency of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this TsysSierraBankSettings.


        :param base_currency: The base_currency of this TsysSierraBankSettings.  # noqa: E501
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
        """Gets the allow_moto of this TsysSierraBankSettings.  # noqa: E501


        :return: The allow_moto of this TsysSierraBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_moto

    @allow_moto.setter
    def allow_moto(self, allow_moto):
        """Sets the allow_moto of this TsysSierraBankSettings.


        :param allow_moto: The allow_moto of this TsysSierraBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_moto = allow_moto

    @property
    def allow_internet(self):
        """Gets the allow_internet of this TsysSierraBankSettings.  # noqa: E501


        :return: The allow_internet of this TsysSierraBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_internet

    @allow_internet.setter
    def allow_internet(self, allow_internet):
        """Sets the allow_internet of this TsysSierraBankSettings.


        :param allow_internet: The allow_internet of this TsysSierraBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_internet = allow_internet

    @property
    def allow_chp(self):
        """Gets the allow_chp of this TsysSierraBankSettings.  # noqa: E501


        :return: The allow_chp of this TsysSierraBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_chp

    @allow_chp.setter
    def allow_chp(self, allow_chp):
        """Sets the allow_chp of this TsysSierraBankSettings.


        :param allow_chp: The allow_chp of this TsysSierraBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_chp = allow_chp

    @property
    def default_terminal_type(self):
        """Gets the default_terminal_type of this TsysSierraBankSettings.  # noqa: E501


        :return: The default_terminal_type of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_terminal_type

    @default_terminal_type.setter
    def default_terminal_type(self, default_terminal_type):
        """Sets the default_terminal_type of this TsysSierraBankSettings.


        :param default_terminal_type: The default_terminal_type of this TsysSierraBankSettings.  # noqa: E501
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
        """Gets the allow_recurring of this TsysSierraBankSettings.  # noqa: E501


        :return: The allow_recurring of this TsysSierraBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_recurring

    @allow_recurring.setter
    def allow_recurring(self, allow_recurring):
        """Sets the allow_recurring of this TsysSierraBankSettings.


        :param allow_recurring: The allow_recurring of this TsysSierraBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_recurring = allow_recurring

    @property
    def allow_pre_auth(self):
        """Gets the allow_pre_auth of this TsysSierraBankSettings.  # noqa: E501


        :return: The allow_pre_auth of this TsysSierraBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_pre_auth

    @allow_pre_auth.setter
    def allow_pre_auth(self, allow_pre_auth):
        """Sets the allow_pre_auth of this TsysSierraBankSettings.


        :param allow_pre_auth: The allow_pre_auth of this TsysSierraBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_pre_auth = allow_pre_auth

    @property
    def dst_observed(self):
        """Gets the dst_observed of this TsysSierraBankSettings.  # noqa: E501


        :return: The dst_observed of this TsysSierraBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._dst_observed

    @dst_observed.setter
    def dst_observed(self, dst_observed):
        """Sets the dst_observed of this TsysSierraBankSettings.


        :param dst_observed: The dst_observed of this TsysSierraBankSettings.  # noqa: E501
        :type: bool
        """

        self._dst_observed = dst_observed

    @property
    def bank_merchant_id(self):
        """Gets the bank_merchant_id of this TsysSierraBankSettings.  # noqa: E501


        :return: The bank_merchant_id of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._bank_merchant_id

    @bank_merchant_id.setter
    def bank_merchant_id(self, bank_merchant_id):
        """Sets the bank_merchant_id of this TsysSierraBankSettings.


        :param bank_merchant_id: The bank_merchant_id of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if bank_merchant_id is None:
            raise ValueError("Invalid value for `bank_merchant_id`, must not be `None`")  # noqa: E501

        self._bank_merchant_id = bank_merchant_id

    @property
    def bank_terminal_id(self):
        """Gets the bank_terminal_id of this TsysSierraBankSettings.  # noqa: E501


        :return: The bank_terminal_id of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._bank_terminal_id

    @bank_terminal_id.setter
    def bank_terminal_id(self, bank_terminal_id):
        """Sets the bank_terminal_id of this TsysSierraBankSettings.


        :param bank_terminal_id: The bank_terminal_id of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if bank_terminal_id is None:
            raise ValueError("Invalid value for `bank_terminal_id`, must not be `None`")  # noqa: E501

        self._bank_terminal_id = bank_terminal_id

    @property
    def agent_bank_number(self):
        """Gets the agent_bank_number of this TsysSierraBankSettings.  # noqa: E501


        :return: The agent_bank_number of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._agent_bank_number

    @agent_bank_number.setter
    def agent_bank_number(self, agent_bank_number):
        """Sets the agent_bank_number of this TsysSierraBankSettings.


        :param agent_bank_number: The agent_bank_number of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if agent_bank_number is None:
            raise ValueError("Invalid value for `agent_bank_number`, must not be `None`")  # noqa: E501

        self._agent_bank_number = agent_bank_number

    @property
    def agent_chain_number(self):
        """Gets the agent_chain_number of this TsysSierraBankSettings.  # noqa: E501


        :return: The agent_chain_number of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._agent_chain_number

    @agent_chain_number.setter
    def agent_chain_number(self, agent_chain_number):
        """Sets the agent_chain_number of this TsysSierraBankSettings.


        :param agent_chain_number: The agent_chain_number of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if agent_chain_number is None:
            raise ValueError("Invalid value for `agent_chain_number`, must not be `None`")  # noqa: E501

        self._agent_chain_number = agent_chain_number

    @property
    def store_number(self):
        """Gets the store_number of this TsysSierraBankSettings.  # noqa: E501


        :return: The store_number of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._store_number

    @store_number.setter
    def store_number(self, store_number):
        """Sets the store_number of this TsysSierraBankSettings.


        :param store_number: The store_number of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if store_number is None:
            raise ValueError("Invalid value for `store_number`, must not be `None`")  # noqa: E501

        self._store_number = store_number

    @property
    def terminal_id_number(self):
        """Gets the terminal_id_number of this TsysSierraBankSettings.  # noqa: E501


        :return: The terminal_id_number of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._terminal_id_number

    @terminal_id_number.setter
    def terminal_id_number(self, terminal_id_number):
        """Sets the terminal_id_number of this TsysSierraBankSettings.


        :param terminal_id_number: The terminal_id_number of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if terminal_id_number is None:
            raise ValueError("Invalid value for `terminal_id_number`, must not be `None`")  # noqa: E501

        self._terminal_id_number = terminal_id_number

    @property
    def authentication_code(self):
        """Gets the authentication_code of this TsysSierraBankSettings.  # noqa: E501


        :return: The authentication_code of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_code

    @authentication_code.setter
    def authentication_code(self, authentication_code):
        """Sets the authentication_code of this TsysSierraBankSettings.


        :param authentication_code: The authentication_code of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if authentication_code is None:
            raise ValueError("Invalid value for `authentication_code`, must not be `None`")  # noqa: E501

        self._authentication_code = authentication_code

    @property
    def acquirer_bin(self):
        """Gets the acquirer_bin of this TsysSierraBankSettings.  # noqa: E501


        :return: The acquirer_bin of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._acquirer_bin

    @acquirer_bin.setter
    def acquirer_bin(self, acquirer_bin):
        """Sets the acquirer_bin of this TsysSierraBankSettings.


        :param acquirer_bin: The acquirer_bin of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if acquirer_bin is None:
            raise ValueError("Invalid value for `acquirer_bin`, must not be `None`")  # noqa: E501

        self._acquirer_bin = acquirer_bin

    @property
    def merchant_aba_number(self):
        """Gets the merchant_aba_number of this TsysSierraBankSettings.  # noqa: E501


        :return: The merchant_aba_number of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._merchant_aba_number

    @merchant_aba_number.setter
    def merchant_aba_number(self, merchant_aba_number):
        """Sets the merchant_aba_number of this TsysSierraBankSettings.


        :param merchant_aba_number: The merchant_aba_number of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """

        self._merchant_aba_number = merchant_aba_number

    @property
    def merchant_settlement_agent_number(self):
        """Gets the merchant_settlement_agent_number of this TsysSierraBankSettings.  # noqa: E501


        :return: The merchant_settlement_agent_number of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._merchant_settlement_agent_number

    @merchant_settlement_agent_number.setter
    def merchant_settlement_agent_number(self, merchant_settlement_agent_number):
        """Sets the merchant_settlement_agent_number of this TsysSierraBankSettings.


        :param merchant_settlement_agent_number: The merchant_settlement_agent_number of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """

        self._merchant_settlement_agent_number = merchant_settlement_agent_number

    @property
    def sharing_group(self):
        """Gets the sharing_group of this TsysSierraBankSettings.  # noqa: E501


        :return: The sharing_group of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._sharing_group

    @sharing_group.setter
    def sharing_group(self, sharing_group):
        """Sets the sharing_group of this TsysSierraBankSettings.


        :param sharing_group: The sharing_group of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """

        self._sharing_group = sharing_group

    @property
    def food_and_consumer_id(self):
        """Gets the food_and_consumer_id of this TsysSierraBankSettings.  # noqa: E501


        :return: The food_and_consumer_id of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._food_and_consumer_id

    @food_and_consumer_id.setter
    def food_and_consumer_id(self, food_and_consumer_id):
        """Sets the food_and_consumer_id of this TsysSierraBankSettings.


        :param food_and_consumer_id: The food_and_consumer_id of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """

        self._food_and_consumer_id = food_and_consumer_id

    @property
    def industry_code(self):
        """Gets the industry_code of this TsysSierraBankSettings.  # noqa: E501


        :return: The industry_code of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._industry_code

    @industry_code.setter
    def industry_code(self, industry_code):
        """Sets the industry_code of this TsysSierraBankSettings.


        :param industry_code: The industry_code of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if industry_code is None:
            raise ValueError("Invalid value for `industry_code`, must not be `None`")  # noqa: E501
        allowed_values = ["UNKNOWN", "AUTORENTAL", "FINANCIAL", "MARKETING", "FOOD", "GROCERY", "HOTEL", "LIMITED", "OIL", "PASSENGER", "RETAIL"]  # noqa: E501
        if industry_code not in allowed_values:
            raise ValueError(
                "Invalid value for `industry_code` ({0}), must be one of {1}"  # noqa: E501
                .format(industry_code, allowed_values)
            )

        self._industry_code = industry_code

    @property
    def language_indicator(self):
        """Gets the language_indicator of this TsysSierraBankSettings.  # noqa: E501


        :return: The language_indicator of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._language_indicator

    @language_indicator.setter
    def language_indicator(self, language_indicator):
        """Sets the language_indicator of this TsysSierraBankSettings.


        :param language_indicator: The language_indicator of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if language_indicator is None:
            raise ValueError("Invalid value for `language_indicator`, must not be `None`")  # noqa: E501
        allowed_values = ["ENGLISH"]  # noqa: E501
        if language_indicator not in allowed_values:
            raise ValueError(
                "Invalid value for `language_indicator` ({0}), must be one of {1}"  # noqa: E501
                .format(language_indicator, allowed_values)
            )

        self._language_indicator = language_indicator

    @property
    def reimbursement_attribute(self):
        """Gets the reimbursement_attribute of this TsysSierraBankSettings.  # noqa: E501


        :return: The reimbursement_attribute of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._reimbursement_attribute

    @reimbursement_attribute.setter
    def reimbursement_attribute(self, reimbursement_attribute):
        """Sets the reimbursement_attribute of this TsysSierraBankSettings.


        :param reimbursement_attribute: The reimbursement_attribute of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """
        if reimbursement_attribute is None:
            raise ValueError("Invalid value for `reimbursement_attribute`, must not be `None`")  # noqa: E501
        allowed_values = ["ATTRIBUTE_0", "ATTRIBUTE_W", "ATTRIBUTE_X", "ATTRIBUTE_Y", "ATTRIBUTE_Z"]  # noqa: E501
        if reimbursement_attribute not in allowed_values:
            raise ValueError(
                "Invalid value for `reimbursement_attribute` ({0}), must be one of {1}"  # noqa: E501
                .format(reimbursement_attribute, allowed_values)
            )

        self._reimbursement_attribute = reimbursement_attribute

    @property
    def enable_automatic_settle(self):
        """Gets the enable_automatic_settle of this TsysSierraBankSettings.  # noqa: E501


        :return: The enable_automatic_settle of this TsysSierraBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_automatic_settle

    @enable_automatic_settle.setter
    def enable_automatic_settle(self, enable_automatic_settle):
        """Sets the enable_automatic_settle of this TsysSierraBankSettings.


        :param enable_automatic_settle: The enable_automatic_settle of this TsysSierraBankSettings.  # noqa: E501
        :type: bool
        """

        self._enable_automatic_settle = enable_automatic_settle

    @property
    def batch_time(self):
        """Gets the batch_time of this TsysSierraBankSettings.  # noqa: E501


        :return: The batch_time of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._batch_time

    @batch_time.setter
    def batch_time(self, batch_time):
        """Sets the batch_time of this TsysSierraBankSettings.


        :param batch_time: The batch_time of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """

        self._batch_time = batch_time

    @property
    def display_name(self):
        """Gets the display_name of this TsysSierraBankSettings.  # noqa: E501


        :return: The display_name of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TsysSierraBankSettings.


        :param display_name: The display_name of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def allow_edit_display_name(self):
        """Gets the allow_edit_display_name of this TsysSierraBankSettings.  # noqa: E501


        :return: The allow_edit_display_name of this TsysSierraBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_edit_display_name

    @allow_edit_display_name.setter
    def allow_edit_display_name(self, allow_edit_display_name):
        """Sets the allow_edit_display_name of this TsysSierraBankSettings.


        :param allow_edit_display_name: The allow_edit_display_name of this TsysSierraBankSettings.  # noqa: E501
        :type: bool
        """

        self._allow_edit_display_name = allow_edit_display_name

    @property
    def force_unique_order_id(self):
        """Gets the force_unique_order_id of this TsysSierraBankSettings.  # noqa: E501


        :return: The force_unique_order_id of this TsysSierraBankSettings.  # noqa: E501
        :rtype: bool
        """
        return self._force_unique_order_id

    @force_unique_order_id.setter
    def force_unique_order_id(self, force_unique_order_id):
        """Sets the force_unique_order_id of this TsysSierraBankSettings.


        :param force_unique_order_id: The force_unique_order_id of this TsysSierraBankSettings.  # noqa: E501
        :type: bool
        """

        self._force_unique_order_id = force_unique_order_id

    @property
    def cardholder_service_phone_number(self):
        """Gets the cardholder_service_phone_number of this TsysSierraBankSettings.  # noqa: E501


        :return: The cardholder_service_phone_number of this TsysSierraBankSettings.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_service_phone_number

    @cardholder_service_phone_number.setter
    def cardholder_service_phone_number(self, cardholder_service_phone_number):
        """Sets the cardholder_service_phone_number of this TsysSierraBankSettings.


        :param cardholder_service_phone_number: The cardholder_service_phone_number of this TsysSierraBankSettings.  # noqa: E501
        :type: str
        """

        self._cardholder_service_phone_number = cardholder_service_phone_number

