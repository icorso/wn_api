# coding: utf-8
from model.boarding2.terminal import Terminal
from model.serializable import SwaggerSerializable


class TsysSierraTerminal(SwaggerSerializable):
    swagger_types = {
        'payment_processor': 'str',
        'terminal_number': 'str',
        'deactivation_date': 'datetime',
        'secret': 'str',
        'template_name': 'str',
        'union_pay_processing': 'TerminalUnionPayProcessing',
        'volume_limits': 'TerminalVolumeLimits',
        'supported_cards': 'list[str]',
        'bank_settings': 'TsysSierraBankSettings',
        'terminal_location': 'TsysSierraLocationDetails',
        'terminal_features': 'TsysSierraFeatures',
        'fraud_detection': 'TsysSierraFraudDetection',
        'integration_settings': 'TsysSierraIntegrationSettings',
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
        return self._payment_processor

    @payment_processor.setter
    def payment_processor(self, payment_processor):
        if payment_processor is None:
            raise ValueError("Invalid value for `payment_processor`, must not be `None`")

        self._payment_processor = payment_processor

    @property
    def terminal_number(self):
        return self._terminal_number

    @terminal_number.setter
    def terminal_number(self, terminal_number):
        self._terminal_number = terminal_number

    @property
    def deactivation_date(self):
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        self._deactivation_date = deactivation_date

    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, secret):
        self._secret = secret

    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        self._template_name = template_name

    @property
    def union_pay_processing(self):
        return self._union_pay_processing

    @union_pay_processing.setter
    def union_pay_processing(self, union_pay_processing):
        self._union_pay_processing = union_pay_processing

    @property
    def volume_limits(self):
        return self._volume_limits

    @volume_limits.setter
    def volume_limits(self, volume_limits):
        self._volume_limits = volume_limits

    @property
    def supported_cards(self):
        return self._supported_cards

    @supported_cards.setter
    def supported_cards(self, supported_cards):
        self._supported_cards = supported_cards

    @property
    def bank_settings(self):
        return self._bank_settings

    @bank_settings.setter
    def bank_settings(self, bank_settings):
        if bank_settings is None:
            raise ValueError("Invalid value for `bank_settings`, must not be `None`")

        self._bank_settings = bank_settings

    @property
    def terminal_location(self):
        return self._terminal_location

    @terminal_location.setter
    def terminal_location(self, terminal_location):
        if terminal_location is None:
            raise ValueError("Invalid value for `terminal_location`, must not be `None`")

        self._terminal_location = terminal_location

    @property
    def terminal_features(self):
        return self._terminal_features

    @terminal_features.setter
    def terminal_features(self, terminal_features):
        self._terminal_features = terminal_features

    @property
    def fraud_detection(self):
        return self._fraud_detection

    @fraud_detection.setter
    def fraud_detection(self, fraud_detection):
        self._fraud_detection = fraud_detection

    @property
    def integration_settings(self):
        return self._integration_settings

    @integration_settings.setter
    def integration_settings(self, integration_settings):
        self._integration_settings = integration_settings

    @property
    def receipt_notifications(self):
        return self._receipt_notifications

    @receipt_notifications.setter
    def receipt_notifications(self, receipt_notifications):
        self._receipt_notifications = receipt_notifications

    @property
    def ach_processing(self):
        return self._ach_processing

    @ach_processing.setter
    def ach_processing(self, ach_processing):
        self._ach_processing = ach_processing
