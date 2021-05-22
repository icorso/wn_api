# coding: utf-8

from model.serializable import SwaggerSerializable


class Terminal(SwaggerSerializable):
    swagger_types = {
        'payment_processor': 'str',
        'terminal_number': 'str',
        'merchant_details': 'MerchantDetails',
        'bank_settings': 'TerminalBankSettings',
        'terminal_location': 'TerminalLocationDetails',
        'terminal_features': 'TerminalFeatures',
        'fraud_detection': 'TerminalFraudDetection',
        'processing_rules': 'list[ProcessingRule]',
        'terminal_tips': 'list[TerminalTip]',
        'terminal_taxes': 'list[TerminalTax]',
        'terminal_custom_fields': 'list[TerminalCustomField]',
        'supported_cards': 'list[str]',
        'supported_device_types': 'list[str]',
        'volume_limits': 'TerminalVolumeLimits',
        'links': 'list[HypermediaLink]'
    }

    attribute_map = {
        'payment_processor': 'paymentProcessor',
        'terminal_number': 'terminalNumber',
        'merchant_details': 'merchantDetails',
        'bank_settings': 'bankSettings',
        'terminal_location': 'terminalLocation',
        'terminal_features': 'terminalFeatures',
        'fraud_detection': 'fraudDetection',
        'processing_rules': 'processingRules',
        'terminal_tips': 'terminalTips',
        'terminal_taxes': 'terminalTaxes',
        'terminal_custom_fields': 'terminalCustomFields',
        'supported_cards': 'supportedCards',
        'supported_device_types': 'supportedDeviceTypes',
        'volume_limits': 'volumeLimits',
        'links': 'links'
    }

    def __init__(self, payment_processor=None, terminal_number=None, merchant_details=None, bank_settings=None, terminal_location=None, terminal_features=None, fraud_detection=None, processing_rules=None, terminal_tips=None, terminal_taxes=None, terminal_custom_fields=None, supported_cards=None, supported_device_types=None, volume_limits=None, links=None):  # noqa: E501
        """Terminal - a model defined in Swagger"""  # noqa: E501
        self._payment_processor = None
        self._terminal_number = None
        self._merchant_details = None
        self._bank_settings = None
        self._terminal_location = None
        self._terminal_features = None
        self._fraud_detection = None
        self._processing_rules = None
        self._terminal_tips = None
        self._terminal_taxes = None
        self._terminal_custom_fields = None
        self._supported_cards = None
        self._supported_device_types = None
        self._volume_limits = None
        self._links = None
        self.discriminator = None
        self.payment_processor = payment_processor
        self.terminal_number = terminal_number
        if merchant_details is not None:
            self.merchant_details = merchant_details
        if bank_settings is not None:
            self.bank_settings = bank_settings
        if terminal_location is not None:
            self.terminal_location = terminal_location
        if terminal_features is not None:
            self.terminal_features = terminal_features
        if fraud_detection is not None:
            self.fraud_detection = fraud_detection
        if processing_rules is not None:
            self.processing_rules = processing_rules
        if terminal_tips is not None:
            self.terminal_tips = terminal_tips
        if terminal_taxes is not None:
            self.terminal_taxes = terminal_taxes
        if terminal_custom_fields is not None:
            self.terminal_custom_fields = terminal_custom_fields
        if supported_cards is not None:
            self.supported_cards = supported_cards
        if supported_device_types is not None:
            self.supported_device_types = supported_device_types
        if volume_limits is not None:
            self.volume_limits = volume_limits
        if links is not None:
            self.links = links

    @property
    def payment_processor(self):
        """Gets the payment_processor of this Terminal.  # noqa: E501

        The financial entity that will process and authorize the operations performed by the terminal.  # noqa: E501

        :return: The payment_processor of this Terminal.  # noqa: E501
        :rtype: str
        """
        return self._payment_processor

    @payment_processor.setter
    def payment_processor(self, payment_processor):
        """Sets the payment_processor of this Terminal.

        The financial entity that will process and authorize the operations performed by the terminal.  # noqa: E501

        :param payment_processor: The payment_processor of this Terminal.  # noqa: E501
        :type: str
        """
        if payment_processor is None:
            raise ValueError("Invalid value for `payment_processor`, must not be `None`")  # noqa: E501

        self._payment_processor = payment_processor

    @property
    def terminal_number(self):
        """Gets the terminal_number of this Terminal.  # noqa: E501

        Unique number assigned by the gateway.  # noqa: E501

        :return: The terminal_number of this Terminal.  # noqa: E501
        :rtype: str
        """
        return self._terminal_number

    @terminal_number.setter
    def terminal_number(self, terminal_number):
        """Sets the terminal_number of this Terminal.

        Unique number assigned by the gateway.  # noqa: E501

        :param terminal_number: The terminal_number of this Terminal.  # noqa: E501
        :type: str
        """
        if terminal_number is None:
            raise ValueError("Invalid value for `terminal_number`, must not be `None`")  # noqa: E501

        self._terminal_number = terminal_number

    @property
    def merchant_details(self):
        """Gets the merchant_details of this Terminal.  # noqa: E501


        :return: The merchant_details of this Terminal.  # noqa: E501
        :rtype: MerchantDetails
        """
        return self._merchant_details

    @merchant_details.setter
    def merchant_details(self, merchant_details):
        """Sets the merchant_details of this Terminal.


        :param merchant_details: The merchant_details of this Terminal.  # noqa: E501
        :type: MerchantDetails
        """

        self._merchant_details = merchant_details

    @property
    def bank_settings(self):
        """Gets the bank_settings of this Terminal.  # noqa: E501


        :return: The bank_settings of this Terminal.  # noqa: E501
        :rtype: TerminalBankSettings
        """
        return self._bank_settings

    @bank_settings.setter
    def bank_settings(self, bank_settings):
        """Sets the bank_settings of this Terminal.


        :param bank_settings: The bank_settings of this Terminal.  # noqa: E501
        :type: TerminalBankSettings
        """

        self._bank_settings = bank_settings

    @property
    def terminal_location(self):
        """Gets the terminal_location of this Terminal.  # noqa: E501


        :return: The terminal_location of this Terminal.  # noqa: E501
        :rtype: TerminalLocationDetails
        """
        return self._terminal_location

    @terminal_location.setter
    def terminal_location(self, terminal_location):
        """Sets the terminal_location of this Terminal.


        :param terminal_location: The terminal_location of this Terminal.  # noqa: E501
        :type: TerminalLocationDetails
        """

        self._terminal_location = terminal_location

    @property
    def terminal_features(self):
        """Gets the terminal_features of this Terminal.  # noqa: E501


        :return: The terminal_features of this Terminal.  # noqa: E501
        :rtype: TerminalFeatures
        """
        return self._terminal_features

    @terminal_features.setter
    def terminal_features(self, terminal_features):
        """Sets the terminal_features of this Terminal.


        :param terminal_features: The terminal_features of this Terminal.  # noqa: E501
        :type: TerminalFeatures
        """

        self._terminal_features = terminal_features

    @property
    def fraud_detection(self):
        """Gets the fraud_detection of this Terminal.  # noqa: E501


        :return: The fraud_detection of this Terminal.  # noqa: E501
        :rtype: TerminalFraudDetection
        """
        return self._fraud_detection

    @fraud_detection.setter
    def fraud_detection(self, fraud_detection):
        """Sets the fraud_detection of this Terminal.


        :param fraud_detection: The fraud_detection of this Terminal.  # noqa: E501
        :type: TerminalFraudDetection
        """

        self._fraud_detection = fraud_detection

    @property
    def processing_rules(self):
        """Gets the processing_rules of this Terminal.  # noqa: E501

        The list of rules that allows for changing the way transactions are processed by this terminal. Each rule has its own conditions which leads to a certain action when all of them are met.<br />For example, processing rules can be used to route transactions to other terminals in your account.  # noqa: E501

        :return: The processing_rules of this Terminal.  # noqa: E501
        :rtype: list[ProcessingRule]
        """
        return self._processing_rules

    @processing_rules.setter
    def processing_rules(self, processing_rules):
        """Sets the processing_rules of this Terminal.

        The list of rules that allows for changing the way transactions are processed by this terminal. Each rule has its own conditions which leads to a certain action when all of them are met.<br />For example, processing rules can be used to route transactions to other terminals in your account.  # noqa: E501

        :param processing_rules: The processing_rules of this Terminal.  # noqa: E501
        :type: list[ProcessingRule]
        """

        self._processing_rules = processing_rules

    @property
    def terminal_tips(self):
        """Gets the terminal_tips of this Terminal.  # noqa: E501

        The list of terminal's pre-configured tips.  # noqa: E501

        :return: The terminal_tips of this Terminal.  # noqa: E501
        :rtype: list[TerminalTip]
        """
        return self._terminal_tips

    @terminal_tips.setter
    def terminal_tips(self, terminal_tips):
        """Sets the terminal_tips of this Terminal.

        The list of terminal's pre-configured tips.  # noqa: E501

        :param terminal_tips: The terminal_tips of this Terminal.  # noqa: E501
        :type: list[TerminalTip]
        """

        self._terminal_tips = terminal_tips

    @property
    def terminal_taxes(self):
        """Gets the terminal_taxes of this Terminal.  # noqa: E501

        The list of terminal's supported taxes.  # noqa: E501

        :return: The terminal_taxes of this Terminal.  # noqa: E501
        :rtype: list[TerminalTax]
        """
        return self._terminal_taxes

    @terminal_taxes.setter
    def terminal_taxes(self, terminal_taxes):
        """Sets the terminal_taxes of this Terminal.

        The list of terminal's supported taxes.  # noqa: E501

        :param terminal_taxes: The terminal_taxes of this Terminal.  # noqa: E501
        :type: list[TerminalTax]
        """

        self._terminal_taxes = terminal_taxes

    @property
    def terminal_custom_fields(self):
        """Gets the terminal_custom_fields of this Terminal.  # noqa: E501

        List of additional data fields that can be used when performing transactions or storing secure credentials.<br />For more information about custom fields, see [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters#the_custom_fields).  # noqa: E501

        :return: The terminal_custom_fields of this Terminal.  # noqa: E501
        :rtype: list[TerminalCustomField]
        """
        return self._terminal_custom_fields

    @terminal_custom_fields.setter
    def terminal_custom_fields(self, terminal_custom_fields):
        """Sets the terminal_custom_fields of this Terminal.

        List of additional data fields that can be used when performing transactions or storing secure credentials.<br />For more information about custom fields, see [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters#the_custom_fields).  # noqa: E501

        :param terminal_custom_fields: The terminal_custom_fields of this Terminal.  # noqa: E501
        :type: list[TerminalCustomField]
        """

        self._terminal_custom_fields = terminal_custom_fields

    @property
    def supported_cards(self):
        """Gets the supported_cards of this Terminal.  # noqa: E501

        List of card brands supported by the terminal.  # noqa: E501

        :return: The supported_cards of this Terminal.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_cards

    @supported_cards.setter
    def supported_cards(self, supported_cards):
        """Sets the supported_cards of this Terminal.

        List of card brands supported by the terminal.  # noqa: E501

        :param supported_cards: The supported_cards of this Terminal.  # noqa: E501
        :type: list[str]
        """

        self._supported_cards = supported_cards

    @property
    def supported_device_types(self):
        """Gets the supported_device_types of this Terminal.  # noqa: E501

        List of POS device types supported by the terminal.  # noqa: E501

        :return: The supported_device_types of this Terminal.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_device_types

    @supported_device_types.setter
    def supported_device_types(self, supported_device_types):
        """Sets the supported_device_types of this Terminal.

        List of POS device types supported by the terminal.  # noqa: E501

        :param supported_device_types: The supported_device_types of this Terminal.  # noqa: E501
        :type: list[str]
        """

        self._supported_device_types = supported_device_types

    @property
    def volume_limits(self):
        """Gets the volume_limits of this Terminal.  # noqa: E501


        :return: The volume_limits of this Terminal.  # noqa: E501
        :rtype: TerminalVolumeLimits
        """
        return self._volume_limits

    @volume_limits.setter
    def volume_limits(self, volume_limits):
        """Sets the volume_limits of this Terminal.


        :param volume_limits: The volume_limits of this Terminal.  # noqa: E501
        :type: TerminalVolumeLimits
        """

        self._volume_limits = volume_limits

    @property
    def links(self):
        """Gets the links of this Terminal.  # noqa: E501

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :return: The links of this Terminal.  # noqa: E501
        :rtype: list[HypermediaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Terminal.

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :param links: The links of this Terminal.  # noqa: E501
        :type: list[HypermediaLink]
        """

        self._links = links
