# coding: utf-8
from model.serializable import SwaggerSerializable


class Terminal(SwaggerSerializable):
    swagger_types = {
        'payment_processor': 'str',
        'terminal_number': 'str',
        'deactivation_date': 'datetime',
        'secret': 'str',
        'template_name': 'str',
        'processing_rules': 'list[ProcessingRule]',
        'union_pay_processing': 'TerminalUnionPayProcessing',
        'volume_limits': 'TerminalVolumeLimits',
        'supported_cards': 'list[str]'
    }

    attribute_map = {
        'payment_processor': 'paymentProcessor',
        'terminal_number': 'terminalNumber',
        'deactivation_date': 'deactivationDate',
        'secret': 'secret',
        'template_name': 'templateName',
        'processing_rules': 'processingRules',
        'union_pay_processing': 'unionPayProcessing',
        'volume_limits': 'volumeLimits',
        'supported_cards': 'supportedCards'
    }

    def __init__(self, payment_processor=None, terminal_number=None, deactivation_date=None, secret=None, template_name=None, processing_rules=None, union_pay_processing=None, volume_limits=None, supported_cards=None):  # noqa: E501
        """Terminal - a model defined in Swagger"""  # noqa: E501
        self._payment_processor = None
        self._terminal_number = None
        self._deactivation_date = None
        self._secret = None
        self._template_name = None
        self._processing_rules = None
        self._union_pay_processing = None
        self._volume_limits = None
        self._supported_cards = None
        self.discriminator = None
        self.payment_processor = payment_processor
        if terminal_number is not None:
            self.terminal_number = terminal_number
        if deactivation_date is not None:
            self.deactivation_date = deactivation_date
        self.secret = secret
        if template_name is not None:
            self.template_name = template_name
        if processing_rules is not None:
            self.processing_rules = processing_rules
        if union_pay_processing is not None:
            self.union_pay_processing = union_pay_processing
        if volume_limits is not None:
            self.volume_limits = volume_limits
        if supported_cards is not None:
            self.supported_cards = supported_cards

    @property
    def payment_processor(self):
        """Gets the payment_processor of this Terminal.  # noqa: E501

        The financial entity that will process and authorise the operations performed by the terminal.  # noqa: E501

        :return: The payment_processor of this Terminal.  # noqa: E501
        :rtype: str
        """
        return self._payment_processor

    @payment_processor.setter
    def payment_processor(self, payment_processor):
        """Sets the payment_processor of this Terminal.

        The financial entity that will process and authorise the operations performed by the terminal.  # noqa: E501

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

        self._terminal_number = terminal_number

    @property
    def deactivation_date(self):
        """Gets the deactivation_date of this Terminal.  # noqa: E501

        Date when the terminal was deactivated.  # noqa: E501

        :return: The deactivation_date of this Terminal.  # noqa: E501
        :rtype: datetime
        """
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        """Sets the deactivation_date of this Terminal.

        Date when the terminal was deactivated.  # noqa: E501

        :param deactivation_date: The deactivation_date of this Terminal.  # noqa: E501
        :type: datetime
        """

        self._deactivation_date = deactivation_date

    @property
    def secret(self):
        """Gets the secret of this Terminal.  # noqa: E501

        The shared secret is used in digest verifications to verify the authenticity of requests.  # noqa: E501

        :return: The secret of this Terminal.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this Terminal.

        The shared secret is used in digest verifications to verify the authenticity of requests.  # noqa: E501

        :param secret: The secret of this Terminal.  # noqa: E501
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def template_name(self):
        """Gets the template_name of this Terminal.  # noqa: E501


        :return: The template_name of this Terminal.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this Terminal.


        :param template_name: The template_name of this Terminal.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

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
    def union_pay_processing(self):
        """Gets the union_pay_processing of this Terminal.  # noqa: E501


        :return: The union_pay_processing of this Terminal.  # noqa: E501
        :rtype: TerminalUnionPayProcessing
        """
        return self._union_pay_processing

    @union_pay_processing.setter
    def union_pay_processing(self, union_pay_processing):
        """Sets the union_pay_processing of this Terminal.


        :param union_pay_processing: The union_pay_processing of this Terminal.  # noqa: E501
        :type: TerminalUnionPayProcessing
        """

        self._union_pay_processing = union_pay_processing

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
