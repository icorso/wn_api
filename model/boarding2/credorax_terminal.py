# coding: utf-8
from model.boarding2.terminal import Terminal
from model.serializable import SwaggerSerializable


class CredoraxTerminal(SwaggerSerializable):
    swagger_types = {
        'payment_processor': 'str',
        'terminal_number': 'str',
        'deactivation_date': 'datetime',
        'secret': 'str',
        'template_name': 'str',
        'union_pay_processing': 'TerminalUnionPayProcessing',
        'volume_limits': 'TerminalVolumeLimits',
        'supported_cards': 'list[str]',
        'bank_settings': 'CredoraxBankSettings',
        'terminal_location': 'TerminalLocationDetails',
        'terminal_features': 'CredoraxFeatures',
        'fraud_detection': 'CredoraxFraudDetection',
        'integration_settings': 'CredoraxIntegrationSettings',
        'receipt_notifications': 'TerminalReceiptNotifications',
        'ach_processing': 'TerminalAchJackHenryProcessing'
    }
    if hasattr(Terminal, "swagger_types"):
        swagger_types.update(Terminal.swagger_types)

    attribute_map = {
        'payment_processor': 'paymentProcessor',
        'terminal_number': 'terminalNumber',
        'deactivation_date': 'deactivationDate',
        'secret': 'secret',
        'template_name': 'templateName',
        'union_pay_processing': 'unionPayProcessing',
        'volume_limits': 'volumeLimits',
        'supported_cards': 'supportedCards',
        'bank_settings': 'bankSettings',
        'terminal_location': 'terminalLocation',
        'terminal_features': 'terminalFeatures',
        'fraud_detection': 'fraudDetection',
        'integration_settings': 'integrationSettings',
        'receipt_notifications': 'receiptNotifications',
        'ach_processing': 'achProcessing'
    }
    if hasattr(Terminal, "attribute_map"):
        attribute_map.update(Terminal.attribute_map)

    def __init__(self, payment_processor=None, terminal_number=None, deactivation_date=None, secret=None, template_name=None, union_pay_processing=None, volume_limits=None, supported_cards=None, bank_settings=None, terminal_location=None, terminal_features=None, fraud_detection=None, integration_settings=None, receipt_notifications=None, ach_processing=None, *args, **kwargs):  # noqa: E501
        """CredoraxTerminal - a model defined in Swagger"""  # noqa: E501
        self._payment_processor = None
        self._terminal_number = None
        self._deactivation_date = None
        self._secret = None
        self._template_name = None
        self._union_pay_processing = None
        self._volume_limits = None
        self._supported_cards = None
        self._bank_settings = None
        self._terminal_location = None
        self._terminal_features = None
        self._fraud_detection = None
        self._integration_settings = None
        self._receipt_notifications = None
        self._ach_processing = None
        self.discriminator = None
        self.payment_processor = payment_processor
        if terminal_number is not None:
            self.terminal_number = terminal_number
        if deactivation_date is not None:
            self.deactivation_date = deactivation_date
        self.secret = secret
        if template_name is not None:
            self.template_name = template_name
        if union_pay_processing is not None:
            self.union_pay_processing = union_pay_processing
        if volume_limits is not None:
            self.volume_limits = volume_limits
        if supported_cards is not None:
            self.supported_cards = supported_cards
        self.bank_settings = bank_settings
        self.terminal_location = terminal_location
        if terminal_features is not None:
            self.terminal_features = terminal_features
        if fraud_detection is not None:
            self.fraud_detection = fraud_detection
        if integration_settings is not None:
            self.integration_settings = integration_settings
        if receipt_notifications is not None:
            self.receipt_notifications = receipt_notifications
        if ach_processing is not None:
            self.ach_processing = ach_processing

    @property
    def payment_processor(self):
        """Gets the payment_processor of this CredoraxTerminal.  # noqa: E501

        The financial entity that will process and authorise the operations performed by the terminal.  # noqa: E501

        :return: The payment_processor of this CredoraxTerminal.  # noqa: E501
        :rtype: str
        """
        return self._payment_processor

    @payment_processor.setter
    def payment_processor(self, payment_processor):
        """Sets the payment_processor of this CredoraxTerminal.

        The financial entity that will process and authorise the operations performed by the terminal.  # noqa: E501

        :param payment_processor: The payment_processor of this CredoraxTerminal.  # noqa: E501
        :type: str
        """
        if payment_processor is None:
            raise ValueError("Invalid value for `payment_processor`, must not be `None`")  # noqa: E501

        self._payment_processor = payment_processor

    @property
    def terminal_number(self):
        """Gets the terminal_number of this CredoraxTerminal.  # noqa: E501

        Unique number assigned by the gateway.  # noqa: E501

        :return: The terminal_number of this CredoraxTerminal.  # noqa: E501
        :rtype: str
        """
        return self._terminal_number

    @terminal_number.setter
    def terminal_number(self, terminal_number):
        """Sets the terminal_number of this CredoraxTerminal.

        Unique number assigned by the gateway.  # noqa: E501

        :param terminal_number: The terminal_number of this CredoraxTerminal.  # noqa: E501
        :type: str
        """

        self._terminal_number = terminal_number

    @property
    def deactivation_date(self):
        """Gets the deactivation_date of this CredoraxTerminal.  # noqa: E501

        Date when the terminal was deactivated.  # noqa: E501

        :return: The deactivation_date of this CredoraxTerminal.  # noqa: E501
        :rtype: datetime
        """
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        """Sets the deactivation_date of this CredoraxTerminal.

        Date when the terminal was deactivated.  # noqa: E501

        :param deactivation_date: The deactivation_date of this CredoraxTerminal.  # noqa: E501
        :type: datetime
        """

        self._deactivation_date = deactivation_date

    @property
    def secret(self):
        """Gets the secret of this CredoraxTerminal.  # noqa: E501

        The shared secret is used in digest verifications to verify the authenticity of requests.  # noqa: E501

        :return: The secret of this CredoraxTerminal.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this CredoraxTerminal.

        The shared secret is used in digest verifications to verify the authenticity of requests.  # noqa: E501

        :param secret: The secret of this CredoraxTerminal.  # noqa: E501
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def template_name(self):
        """Gets the template_name of this CredoraxTerminal.  # noqa: E501


        :return: The template_name of this CredoraxTerminal.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this CredoraxTerminal.


        :param template_name: The template_name of this CredoraxTerminal.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def union_pay_processing(self):
        """Gets the union_pay_processing of this CredoraxTerminal.  # noqa: E501


        :return: The union_pay_processing of this CredoraxTerminal.  # noqa: E501
        :rtype: TerminalUnionPayProcessing
        """
        return self._union_pay_processing

    @union_pay_processing.setter
    def union_pay_processing(self, union_pay_processing):
        """Sets the union_pay_processing of this CredoraxTerminal.


        :param union_pay_processing: The union_pay_processing of this CredoraxTerminal.  # noqa: E501
        :type: TerminalUnionPayProcessing
        """

        self._union_pay_processing = union_pay_processing

    @property
    def volume_limits(self):
        """Gets the volume_limits of this CredoraxTerminal.  # noqa: E501


        :return: The volume_limits of this CredoraxTerminal.  # noqa: E501
        :rtype: TerminalVolumeLimits
        """
        return self._volume_limits

    @volume_limits.setter
    def volume_limits(self, volume_limits):
        """Sets the volume_limits of this CredoraxTerminal.


        :param volume_limits: The volume_limits of this CredoraxTerminal.  # noqa: E501
        :type: TerminalVolumeLimits
        """

        self._volume_limits = volume_limits

    @property
    def supported_cards(self):
        """Gets the supported_cards of this CredoraxTerminal.  # noqa: E501

        List of card brands supported by the terminal.  # noqa: E501

        :return: The supported_cards of this CredoraxTerminal.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_cards

    @supported_cards.setter
    def supported_cards(self, supported_cards):
        """Sets the supported_cards of this CredoraxTerminal.

        List of card brands supported by the terminal.  # noqa: E501

        :param supported_cards: The supported_cards of this CredoraxTerminal.  # noqa: E501
        :type: list[str]
        """

        self._supported_cards = supported_cards

    @property
    def bank_settings(self):
        """Gets the bank_settings of this CredoraxTerminal.  # noqa: E501


        :return: The bank_settings of this CredoraxTerminal.  # noqa: E501
        :rtype: CredoraxBankSettings
        """
        return self._bank_settings

    @bank_settings.setter
    def bank_settings(self, bank_settings):
        """Sets the bank_settings of this CredoraxTerminal.


        :param bank_settings: The bank_settings of this CredoraxTerminal.  # noqa: E501
        :type: CredoraxBankSettings
        """
        if bank_settings is None:
            raise ValueError("Invalid value for `bank_settings`, must not be `None`")  # noqa: E501

        self._bank_settings = bank_settings

    @property
    def terminal_location(self):
        """Gets the terminal_location of this CredoraxTerminal.  # noqa: E501


        :return: The terminal_location of this CredoraxTerminal.  # noqa: E501
        :rtype: TerminalLocationDetails
        """
        return self._terminal_location

    @terminal_location.setter
    def terminal_location(self, terminal_location):
        """Sets the terminal_location of this CredoraxTerminal.


        :param terminal_location: The terminal_location of this CredoraxTerminal.  # noqa: E501
        :type: TerminalLocationDetails
        """
        if terminal_location is None:
            raise ValueError("Invalid value for `terminal_location`, must not be `None`")  # noqa: E501

        self._terminal_location = terminal_location

    @property
    def terminal_features(self):
        """Gets the terminal_features of this CredoraxTerminal.  # noqa: E501


        :return: The terminal_features of this CredoraxTerminal.  # noqa: E501
        :rtype: CredoraxFeatures
        """
        return self._terminal_features

    @terminal_features.setter
    def terminal_features(self, terminal_features):
        """Sets the terminal_features of this CredoraxTerminal.


        :param terminal_features: The terminal_features of this CredoraxTerminal.  # noqa: E501
        :type: CredoraxFeatures
        """

        self._terminal_features = terminal_features

    @property
    def fraud_detection(self):
        """Gets the fraud_detection of this CredoraxTerminal.  # noqa: E501


        :return: The fraud_detection of this CredoraxTerminal.  # noqa: E501
        :rtype: CredoraxFraudDetection
        """
        return self._fraud_detection

    @fraud_detection.setter
    def fraud_detection(self, fraud_detection):
        """Sets the fraud_detection of this CredoraxTerminal.


        :param fraud_detection: The fraud_detection of this CredoraxTerminal.  # noqa: E501
        :type: CredoraxFraudDetection
        """

        self._fraud_detection = fraud_detection

    @property
    def integration_settings(self):
        """Gets the integration_settings of this CredoraxTerminal.  # noqa: E501


        :return: The integration_settings of this CredoraxTerminal.  # noqa: E501
        :rtype: CredoraxIntegrationSettings
        """
        return self._integration_settings

    @integration_settings.setter
    def integration_settings(self, integration_settings):
        """Sets the integration_settings of this CredoraxTerminal.


        :param integration_settings: The integration_settings of this CredoraxTerminal.  # noqa: E501
        :type: CredoraxIntegrationSettings
        """

        self._integration_settings = integration_settings

    @property
    def receipt_notifications(self):
        """Gets the receipt_notifications of this CredoraxTerminal.  # noqa: E501


        :return: The receipt_notifications of this CredoraxTerminal.  # noqa: E501
        :rtype: TerminalReceiptNotifications
        """
        return self._receipt_notifications

    @receipt_notifications.setter
    def receipt_notifications(self, receipt_notifications):
        """Sets the receipt_notifications of this CredoraxTerminal.


        :param receipt_notifications: The receipt_notifications of this CredoraxTerminal.  # noqa: E501
        :type: TerminalReceiptNotifications
        """

        self._receipt_notifications = receipt_notifications

    @property
    def ach_processing(self):
        """Gets the ach_processing of this CredoraxTerminal.  # noqa: E501


        :return: The ach_processing of this CredoraxTerminal.  # noqa: E501
        :rtype: TerminalAchJackHenryProcessing
        """
        return self._ach_processing

    @ach_processing.setter
    def ach_processing(self, ach_processing):
        """Sets the ach_processing of this CredoraxTerminal.


        :param ach_processing: The ach_processing of this CredoraxTerminal.  # noqa: E501
        :type: TerminalAchJackHenryProcessing
        """

        self._ach_processing = ach_processing
