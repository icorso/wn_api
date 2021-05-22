# coding: utf-8
from model.serializable import SwaggerSerializable


class SecureCredentials(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'enable_secure_card_validation': 'bool',
        'force_secure_card_validation': 'bool',
        'allow_hosted_page_storage': 'bool',
        'allow_hosted_page_automatic_storage': 'bool',
        'hosted_page_email_field_setup': 'str',
        'secure_credentials_receipt_url': 'str',
        'allow_subscriptions': 'bool',
        'subscription_max_missed_periods': 'int',
        'subscription_max_authorization_attempts': 'int',
        'subscription_max_days_waiting_for_payment': 'int',
        'subscription_notification_repeat_interval_in_days': 'int',
        'subscription_payment_notification_interval_in_days': 'int',
        'subscription_missed_periods_threshold_for_notification': 'int',
        'subscription_receipt_url': 'str',
        'subscription_notification_url': 'str',
        'account_updater': 'AccountUpdater'
    }

    attribute_map = {
        'enable': 'enable',
        'enable_secure_card_validation': 'enableSecureCardValidation',
        'force_secure_card_validation': 'forceSecureCardValidation',
        'allow_hosted_page_storage': 'allowHostedPageStorage',
        'allow_hosted_page_automatic_storage': 'allowHostedPageAutomaticStorage',
        'hosted_page_email_field_setup': 'hostedPageEmailFieldSetup',
        'secure_credentials_receipt_url': 'secureCredentialsReceiptUrl',
        'allow_subscriptions': 'allowSubscriptions',
        'subscription_max_missed_periods': 'subscriptionMaxMissedPeriods',
        'subscription_max_authorization_attempts': 'subscriptionMaxAuthorizationAttempts',
        'subscription_max_days_waiting_for_payment': 'subscriptionMaxDaysWaitingForPayment',
        'subscription_notification_repeat_interval_in_days': 'subscriptionNotificationRepeatIntervalInDays',
        'subscription_payment_notification_interval_in_days': 'subscriptionPaymentNotificationIntervalInDays',
        'subscription_missed_periods_threshold_for_notification': 'subscriptionMissedPeriodsThresholdForNotification',
        'subscription_receipt_url': 'subscriptionReceiptUrl',
        'subscription_notification_url': 'subscriptionNotificationUrl',
        'account_updater': 'accountUpdater'
    }

    def __init__(self, enable=False, enable_secure_card_validation=False, force_secure_card_validation=False, allow_hosted_page_storage=False, allow_hosted_page_automatic_storage=False, hosted_page_email_field_setup=None, secure_credentials_receipt_url=None, allow_subscriptions=False, subscription_max_missed_periods=2, subscription_max_authorization_attempts=1, subscription_max_days_waiting_for_payment=60, subscription_notification_repeat_interval_in_days=3, subscription_payment_notification_interval_in_days=30, subscription_missed_periods_threshold_for_notification=2, subscription_receipt_url=None, subscription_notification_url=None, account_updater=None):  # noqa: E501
        """SecureCredentials - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._enable_secure_card_validation = None
        self._force_secure_card_validation = None
        self._allow_hosted_page_storage = None
        self._allow_hosted_page_automatic_storage = None
        self._hosted_page_email_field_setup = None
        self._secure_credentials_receipt_url = None
        self._allow_subscriptions = None
        self._subscription_max_missed_periods = None
        self._subscription_max_authorization_attempts = None
        self._subscription_max_days_waiting_for_payment = None
        self._subscription_notification_repeat_interval_in_days = None
        self._subscription_payment_notification_interval_in_days = None
        self._subscription_missed_periods_threshold_for_notification = None
        self._subscription_receipt_url = None
        self._subscription_notification_url = None
        self._account_updater = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if enable_secure_card_validation is not None:
            self.enable_secure_card_validation = enable_secure_card_validation
        if force_secure_card_validation is not None:
            self.force_secure_card_validation = force_secure_card_validation
        if allow_hosted_page_storage is not None:
            self.allow_hosted_page_storage = allow_hosted_page_storage
        if allow_hosted_page_automatic_storage is not None:
            self.allow_hosted_page_automatic_storage = allow_hosted_page_automatic_storage
        if hosted_page_email_field_setup is not None:
            self.hosted_page_email_field_setup = hosted_page_email_field_setup
        if secure_credentials_receipt_url is not None:
            self.secure_credentials_receipt_url = secure_credentials_receipt_url
        if allow_subscriptions is not None:
            self.allow_subscriptions = allow_subscriptions
        if subscription_max_missed_periods is not None:
            self.subscription_max_missed_periods = subscription_max_missed_periods
        if subscription_max_authorization_attempts is not None:
            self.subscription_max_authorization_attempts = subscription_max_authorization_attempts
        if subscription_max_days_waiting_for_payment is not None:
            self.subscription_max_days_waiting_for_payment = subscription_max_days_waiting_for_payment
        if subscription_notification_repeat_interval_in_days is not None:
            self.subscription_notification_repeat_interval_in_days = subscription_notification_repeat_interval_in_days
        if subscription_payment_notification_interval_in_days is not None:
            self.subscription_payment_notification_interval_in_days = subscription_payment_notification_interval_in_days
        if subscription_missed_periods_threshold_for_notification is not None:
            self.subscription_missed_periods_threshold_for_notification = subscription_missed_periods_threshold_for_notification
        if subscription_receipt_url is not None:
            self.subscription_receipt_url = subscription_receipt_url
        if subscription_notification_url is not None:
            self.subscription_notification_url = subscription_notification_url
        if account_updater is not None:
            self.account_updater = account_updater

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def enable_secure_card_validation(self):
        return self._enable_secure_card_validation

    @enable_secure_card_validation.setter
    def enable_secure_card_validation(self, enable_secure_card_validation):
        self._enable_secure_card_validation = enable_secure_card_validation

    @property
    def force_secure_card_validation(self):
        return self._force_secure_card_validation

    @force_secure_card_validation.setter
    def force_secure_card_validation(self, force_secure_card_validation):
        self._force_secure_card_validation = force_secure_card_validation

    @property
    def allow_hosted_page_storage(self):
        return self._allow_hosted_page_storage

    @allow_hosted_page_storage.setter
    def allow_hosted_page_storage(self, allow_hosted_page_storage):
        self._allow_hosted_page_storage = allow_hosted_page_storage

    @property
    def allow_hosted_page_automatic_storage(self):
        return self._allow_hosted_page_automatic_storage

    @allow_hosted_page_automatic_storage.setter
    def allow_hosted_page_automatic_storage(self, allow_hosted_page_automatic_storage):
        self._allow_hosted_page_automatic_storage = allow_hosted_page_automatic_storage

    @property
    def hosted_page_email_field_setup(self):
        return self._hosted_page_email_field_setup

    @hosted_page_email_field_setup.setter
    def hosted_page_email_field_setup(self, hosted_page_email_field_setup):
        self._hosted_page_email_field_setup = hosted_page_email_field_setup

    @property
    def secure_credentials_receipt_url(self):
        return self._secure_credentials_receipt_url

    @secure_credentials_receipt_url.setter
    def secure_credentials_receipt_url(self, secure_credentials_receipt_url):
        self._secure_credentials_receipt_url = secure_credentials_receipt_url

    @property
    def allow_subscriptions(self):
        return self._allow_subscriptions

    @allow_subscriptions.setter
    def allow_subscriptions(self, allow_subscriptions):
        self._allow_subscriptions = allow_subscriptions

    @property
    def subscription_max_missed_periods(self):
        return self._subscription_max_missed_periods

    @subscription_max_missed_periods.setter
    def subscription_max_missed_periods(self, subscription_max_missed_periods):
        self._subscription_max_missed_periods = subscription_max_missed_periods

    @property
    def subscription_max_authorization_attempts(self):
        return self._subscription_max_authorization_attempts

    @subscription_max_authorization_attempts.setter
    def subscription_max_authorization_attempts(self, subscription_max_authorization_attempts):
        self._subscription_max_authorization_attempts = subscription_max_authorization_attempts

    @property
    def subscription_max_days_waiting_for_payment(self):
        return self._subscription_max_days_waiting_for_payment

    @subscription_max_days_waiting_for_payment.setter
    def subscription_max_days_waiting_for_payment(self, subscription_max_days_waiting_for_payment):
        self._subscription_max_days_waiting_for_payment = subscription_max_days_waiting_for_payment

    @property
    def subscription_notification_repeat_interval_in_days(self):
        return self._subscription_notification_repeat_interval_in_days

    @subscription_notification_repeat_interval_in_days.setter
    def subscription_notification_repeat_interval_in_days(self, subscription_notification_repeat_interval_in_days):
        self._subscription_notification_repeat_interval_in_days = subscription_notification_repeat_interval_in_days

    @property
    def subscription_payment_notification_interval_in_days(self):
        return self._subscription_payment_notification_interval_in_days

    @subscription_payment_notification_interval_in_days.setter
    def subscription_payment_notification_interval_in_days(self, subscription_payment_notification_interval_in_days):
        self._subscription_payment_notification_interval_in_days = subscription_payment_notification_interval_in_days

    @property
    def subscription_missed_periods_threshold_for_notification(self):
        return self._subscription_missed_periods_threshold_for_notification

    @subscription_missed_periods_threshold_for_notification.setter
    def subscription_missed_periods_threshold_for_notification(self, subscription_missed_periods_threshold_for_notification):
        self._subscription_missed_periods_threshold_for_notification = subscription_missed_periods_threshold_for_notification

    @property
    def subscription_receipt_url(self):
        return self._subscription_receipt_url

    @subscription_receipt_url.setter
    def subscription_receipt_url(self, subscription_receipt_url):
        self._subscription_receipt_url = subscription_receipt_url

    @property
    def subscription_notification_url(self):
        return self._subscription_notification_url

    @subscription_notification_url.setter
    def subscription_notification_url(self, subscription_notification_url):
        self._subscription_notification_url = subscription_notification_url

    @property
    def account_updater(self):
        return self._account_updater

    @account_updater.setter
    def account_updater(self, account_updater):
        self._account_updater = account_updater

