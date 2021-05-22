# coding: utf-8

from model.serializable import SwaggerSerializable


class User(SwaggerSerializable):
    swagger_types = {
        'template_name': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'merchant_id': 'str',
        'user_email': 'str',
        'time_zone': 'str',
        'allow_terminal_setup': 'bool',
        'allow_payment_page_layout': 'bool',
        'allow_refund': 'bool',
        'allow_unreferenced_refunds': 'bool',
        'allow_virtual_terminal': 'bool',
        'allow_chp_on_vt': 'bool',
        'allow_user_setup': 'bool',
        'allow_open_batch': 'bool',
        'allow_closed_batch': 'bool',
        'allow_bulk_payments_results': 'bool',
        'allow_billing': 'bool',
        'locked_status': 'str',
        'active_status': 'str',
        'allow_preauth': 'bool',
        'allow_secure_cards': 'bool',
        'allow_subscriptions': 'bool',
        'allow_dashboard': 'bool',
        'allow_achjhtransactions': 'bool',
        'allow_achiptransactions': 'bool',
        'allow_partial_captures': 'bool',
        'allow_scheduled_report': 'bool',
        'allow_api_key_management': 'bool',
        'user_processing_terminals': 'list[str]'
    }

    attribute_map = {
        'template_name': 'templateName',
        'user_id': 'userId',
        'user_name': 'userName',
        'merchant_id': 'merchantId',
        'user_email': 'userEmail',
        'time_zone': 'timeZone',
        'allow_terminal_setup': 'allowTerminalSetup',
        'allow_payment_page_layout': 'allowPaymentPageLayout',
        'allow_refund': 'allowRefund',
        'allow_unreferenced_refunds': 'allowUnreferencedRefunds',
        'allow_virtual_terminal': 'allowVirtualTerminal',
        'allow_chp_on_vt': 'allowChpOnVt',
        'allow_user_setup': 'allowUserSetup',
        'allow_open_batch': 'allowOpenBatch',
        'allow_closed_batch': 'allowClosedBatch',
        'allow_bulk_payments_results': 'allowBulkPaymentsResults',
        'allow_billing': 'allowBilling',
        'locked_status': 'lockedStatus',
        'active_status': 'activeStatus',
        'allow_preauth': 'allowPreauth',
        'allow_secure_cards': 'allowSecureCards',
        'allow_subscriptions': 'allowSubscriptions',
        'allow_dashboard': 'allowDashboard',
        'allow_achjhtransactions': 'allowAchjhtransactions',
        'allow_achiptransactions': 'allowAchiptransactions',
        'allow_partial_captures': 'allowPartialCaptures',
        'allow_scheduled_report': 'allowScheduledReport',
        'allow_api_key_management': 'allowApiKeyManagement',
        'user_processing_terminals': 'userProcessingTerminals'
    }

    def __init__(self, template_name=None, user_id=None, user_name=None, merchant_id=None, user_email=None, time_zone=None, allow_terminal_setup=None, allow_payment_page_layout=None, allow_refund=None, allow_unreferenced_refunds=None, allow_virtual_terminal=None, allow_chp_on_vt=None, allow_user_setup=None, allow_open_batch=None, allow_closed_batch=None, allow_bulk_payments_results=None, allow_billing=None, locked_status=None, active_status=None, allow_preauth=None, allow_secure_cards=None, allow_subscriptions=None, allow_dashboard=None, allow_achjhtransactions=None, allow_achiptransactions=None, allow_partial_captures=None, allow_scheduled_report=None, allow_api_key_management=None, user_processing_terminals=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._template_name = None
        self._user_id = None
        self._user_name = None
        self._merchant_id = None
        self._user_email = None
        self._time_zone = None
        self._allow_terminal_setup = None
        self._allow_payment_page_layout = None
        self._allow_refund = None
        self._allow_unreferenced_refunds = None
        self._allow_virtual_terminal = None
        self._allow_chp_on_vt = None
        self._allow_user_setup = None
        self._allow_open_batch = None
        self._allow_closed_batch = None
        self._allow_bulk_payments_results = None
        self._allow_billing = None
        self._locked_status = None
        self._active_status = None
        self._allow_preauth = None
        self._allow_secure_cards = None
        self._allow_subscriptions = None
        self._allow_dashboard = None
        self._allow_achjhtransactions = None
        self._allow_achiptransactions = None
        self._allow_partial_captures = None
        self._allow_scheduled_report = None
        self._allow_api_key_management = None
        self._user_processing_terminals = None
        self.discriminator = None
        if template_name is not None:
            self.template_name = template_name
        if user_id is not None:
            self.user_id = user_id
        self.user_name = user_name
        self.merchant_id = merchant_id
        self.user_email = user_email
        self.time_zone = time_zone
        if allow_terminal_setup is not None:
            self.allow_terminal_setup = allow_terminal_setup
        if allow_payment_page_layout is not None:
            self.allow_payment_page_layout = allow_payment_page_layout
        if allow_refund is not None:
            self.allow_refund = allow_refund
        if allow_unreferenced_refunds is not None:
            self.allow_unreferenced_refunds = allow_unreferenced_refunds
        if allow_virtual_terminal is not None:
            self.allow_virtual_terminal = allow_virtual_terminal
        if allow_chp_on_vt is not None:
            self.allow_chp_on_vt = allow_chp_on_vt
        if allow_user_setup is not None:
            self.allow_user_setup = allow_user_setup
        if allow_open_batch is not None:
            self.allow_open_batch = allow_open_batch
        if allow_closed_batch is not None:
            self.allow_closed_batch = allow_closed_batch
        if allow_bulk_payments_results is not None:
            self.allow_bulk_payments_results = allow_bulk_payments_results
        if allow_billing is not None:
            self.allow_billing = allow_billing
        if locked_status is not None:
            self.locked_status = locked_status
        if active_status is not None:
            self.active_status = active_status
        if allow_preauth is not None:
            self.allow_preauth = allow_preauth
        if allow_secure_cards is not None:
            self.allow_secure_cards = allow_secure_cards
        if allow_subscriptions is not None:
            self.allow_subscriptions = allow_subscriptions
        if allow_dashboard is not None:
            self.allow_dashboard = allow_dashboard
        if allow_achjhtransactions is not None:
            self.allow_achjhtransactions = allow_achjhtransactions
        if allow_achiptransactions is not None:
            self.allow_achiptransactions = allow_achiptransactions
        if allow_partial_captures is not None:
            self.allow_partial_captures = allow_partial_captures
        if allow_scheduled_report is not None:
            self.allow_scheduled_report = allow_scheduled_report
        if allow_api_key_management is not None:
            self.allow_api_key_management = allow_api_key_management
        if user_processing_terminals is not None:
            self.user_processing_terminals = user_processing_terminals

    @property
    def template_name(self):
        """Gets the template_name of this User.  # noqa: E501


        :return: The template_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this User.


        :param template_name: The template_name of this User.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def user_id(self):
        """Gets the user_id of this User.  # noqa: E501


        :return: The user_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this User.


        :param user_id: The user_id of this User.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this User.  # noqa: E501


        :return: The user_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this User.


        :param user_name: The user_name of this User.  # noqa: E501
        :type: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def merchant_id(self):
        """Gets the merchant_id of this User.  # noqa: E501


        :return: The merchant_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this User.


        :param merchant_id: The merchant_id of this User.  # noqa: E501
        :type: str
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def user_email(self):
        """Gets the user_email of this User.  # noqa: E501


        :return: The user_email of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this User.


        :param user_email: The user_email of this User.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

    @property
    def time_zone(self):
        """Gets the time_zone of this User.  # noqa: E501

        User's preferred time-zone.  # noqa: E501

        :return: The time_zone of this User.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this User.

        User's preferred time-zone.  # noqa: E501

        :param time_zone: The time_zone of this User.  # noqa: E501
        :type: str
        """
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501
        allowed_values = ["Pacific/Midway", "Pacific/Honolulu", "Pacific/Marquesas", "America/Anchorage", "Pacific/Pitcairn", "America/Los_Angeles", "America/Tijuana", "America/Chihuahua", "America/Denver", "America/Phoenix", "America/Chicago", "America/Guatemala", "America/Mexico_City", "America/Regina", "America/Bogota", "America/Indiana/Indianapolis", "America/New_York", "America/Caracas", "America/Guyana", "America/Halifax", "America/La_Paz", "America/Manaus", "America/Santiago", "America/St_Johns", "America/Argentina/Buenos_Aires", "America/Godthab", "America/Montevideo", "America/Sao_Paulo", "Atlantic/South_Georgia", "Atlantic/Azores", "Atlantic/Cape_Verde", "Africa/Casablanca", "Africa/Monrovia", "Europe/London", "Africa/Algiers", "Africa/Windhoek", "Europe/Belgrade", "Europe/Berlin", "Europe/Brussels", "Europe/Warsaw", "Africa/Cairo", "Africa/Harare", "Asia/Amman", "Asia/Beirut", "Asia/Jerusalem", "Europe/Athens", "Europe/Helsinki", "Europe/Minsk", "Africa/Nairobi", "Asia/Baghdad", "Asia/Kuwait", "Europe/Moscow", "Asia/Tehran", "Asia/Baku", "Asia/Muscat", "Asia/Tbilisi", "Asia/Yerevan", "Asia/Kabul", "Asia/Karachi", "Asia/Tashkent", "Asia/Yekaterinburg", "Asia/Colombo", "Asia/Kolkata", "Asia/Kathmandu", "Asia/Dhaka", "Asia/Novosibirsk", "Asia/Rangoon", "Asia/Bangkok", "Asia/Krasnoyarsk", "Asia/Hong_Kong", "Asia/Irkutsk", "Asia/Kuala_Lumpur", "Asia/Taipei", "Australia/Perth", "Asia/Seoul", "Asia/Tokyo", "Asia/Yakutsk", "Australia/Adelaide", "Australia/Darwin", "Asia/Vladivostok", "Australia/Brisbane", "Australia/Hobart", "Australia/Sydney", "Pacific/Guam", "Australia/Lord_Howe", "Asia/Magadan", "Pacific/Norfolk", "Pacific/Auckland", "Pacific/Fiji", "Pacific/Tongatapu"]  # noqa: E501
        if time_zone not in allowed_values:
            raise ValueError(
                "Invalid value for `time_zone` ({0}), must be one of {1}"  # noqa: E501
                .format(time_zone, allowed_values)
            )

        self._time_zone = time_zone

    @property
    def allow_terminal_setup(self):
        """Gets the allow_terminal_setup of this User.  # noqa: E501


        :return: The allow_terminal_setup of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_terminal_setup

    @allow_terminal_setup.setter
    def allow_terminal_setup(self, allow_terminal_setup):
        """Sets the allow_terminal_setup of this User.


        :param allow_terminal_setup: The allow_terminal_setup of this User.  # noqa: E501
        :type: bool
        """

        self._allow_terminal_setup = allow_terminal_setup

    @property
    def allow_payment_page_layout(self):
        """Gets the allow_payment_page_layout of this User.  # noqa: E501


        :return: The allow_payment_page_layout of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_payment_page_layout

    @allow_payment_page_layout.setter
    def allow_payment_page_layout(self, allow_payment_page_layout):
        """Sets the allow_payment_page_layout of this User.


        :param allow_payment_page_layout: The allow_payment_page_layout of this User.  # noqa: E501
        :type: bool
        """

        self._allow_payment_page_layout = allow_payment_page_layout

    @property
    def allow_refund(self):
        """Gets the allow_refund of this User.  # noqa: E501


        :return: The allow_refund of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_refund

    @allow_refund.setter
    def allow_refund(self, allow_refund):
        """Sets the allow_refund of this User.


        :param allow_refund: The allow_refund of this User.  # noqa: E501
        :type: bool
        """

        self._allow_refund = allow_refund

    @property
    def allow_unreferenced_refunds(self):
        """Gets the allow_unreferenced_refunds of this User.  # noqa: E501


        :return: The allow_unreferenced_refunds of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_unreferenced_refunds

    @allow_unreferenced_refunds.setter
    def allow_unreferenced_refunds(self, allow_unreferenced_refunds):
        """Sets the allow_unreferenced_refunds of this User.


        :param allow_unreferenced_refunds: The allow_unreferenced_refunds of this User.  # noqa: E501
        :type: bool
        """

        self._allow_unreferenced_refunds = allow_unreferenced_refunds

    @property
    def allow_virtual_terminal(self):
        """Gets the allow_virtual_terminal of this User.  # noqa: E501


        :return: The allow_virtual_terminal of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_virtual_terminal

    @allow_virtual_terminal.setter
    def allow_virtual_terminal(self, allow_virtual_terminal):
        """Sets the allow_virtual_terminal of this User.


        :param allow_virtual_terminal: The allow_virtual_terminal of this User.  # noqa: E501
        :type: bool
        """

        self._allow_virtual_terminal = allow_virtual_terminal

    @property
    def allow_chp_on_vt(self):
        """Gets the allow_chp_on_vt of this User.  # noqa: E501


        :return: The allow_chp_on_vt of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_chp_on_vt

    @allow_chp_on_vt.setter
    def allow_chp_on_vt(self, allow_chp_on_vt):
        """Sets the allow_chp_on_vt of this User.


        :param allow_chp_on_vt: The allow_chp_on_vt of this User.  # noqa: E501
        :type: bool
        """

        self._allow_chp_on_vt = allow_chp_on_vt

    @property
    def allow_user_setup(self):
        """Gets the allow_user_setup of this User.  # noqa: E501


        :return: The allow_user_setup of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_user_setup

    @allow_user_setup.setter
    def allow_user_setup(self, allow_user_setup):
        """Sets the allow_user_setup of this User.


        :param allow_user_setup: The allow_user_setup of this User.  # noqa: E501
        :type: bool
        """

        self._allow_user_setup = allow_user_setup

    @property
    def allow_open_batch(self):
        """Gets the allow_open_batch of this User.  # noqa: E501


        :return: The allow_open_batch of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_open_batch

    @allow_open_batch.setter
    def allow_open_batch(self, allow_open_batch):
        """Sets the allow_open_batch of this User.


        :param allow_open_batch: The allow_open_batch of this User.  # noqa: E501
        :type: bool
        """

        self._allow_open_batch = allow_open_batch

    @property
    def allow_closed_batch(self):
        """Gets the allow_closed_batch of this User.  # noqa: E501


        :return: The allow_closed_batch of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_closed_batch

    @allow_closed_batch.setter
    def allow_closed_batch(self, allow_closed_batch):
        """Sets the allow_closed_batch of this User.


        :param allow_closed_batch: The allow_closed_batch of this User.  # noqa: E501
        :type: bool
        """

        self._allow_closed_batch = allow_closed_batch

    @property
    def allow_bulk_payments_results(self):
        """Gets the allow_bulk_payments_results of this User.  # noqa: E501


        :return: The allow_bulk_payments_results of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_bulk_payments_results

    @allow_bulk_payments_results.setter
    def allow_bulk_payments_results(self, allow_bulk_payments_results):
        """Sets the allow_bulk_payments_results of this User.


        :param allow_bulk_payments_results: The allow_bulk_payments_results of this User.  # noqa: E501
        :type: bool
        """

        self._allow_bulk_payments_results = allow_bulk_payments_results

    @property
    def allow_billing(self):
        """Gets the allow_billing of this User.  # noqa: E501


        :return: The allow_billing of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_billing

    @allow_billing.setter
    def allow_billing(self, allow_billing):
        """Sets the allow_billing of this User.


        :param allow_billing: The allow_billing of this User.  # noqa: E501
        :type: bool
        """

        self._allow_billing = allow_billing

    @property
    def locked_status(self):
        """Gets the locked_status of this User.  # noqa: E501


        :return: The locked_status of this User.  # noqa: E501
        :rtype: str
        """
        return self._locked_status

    @locked_status.setter
    def locked_status(self, locked_status):
        """Sets the locked_status of this User.


        :param locked_status: The locked_status of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "LOCKED_BY_TOO_MANY_ATTEMPTS", "LOCKED_BY_ADMIN", "LOCKED_BY_SELF"]  # noqa: E501
        if locked_status not in allowed_values:
            raise ValueError(
                "Invalid value for `locked_status` ({0}), must be one of {1}"  # noqa: E501
                .format(locked_status, allowed_values)
            )

        self._locked_status = locked_status

    @property
    def active_status(self):
        """Gets the active_status of this User.  # noqa: E501


        :return: The active_status of this User.  # noqa: E501
        :rtype: str
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this User.


        :param active_status: The active_status of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DESACTIVATED_BY_MERCHANT", "DESACTIVATED_BY_ADMIN", "MERCHANT_DESACTIVATED"]  # noqa: E501
        if active_status not in allowed_values:
            raise ValueError(
                "Invalid value for `active_status` ({0}), must be one of {1}"  # noqa: E501
                .format(active_status, allowed_values)
            )

        self._active_status = active_status

    @property
    def allow_preauth(self):
        """Gets the allow_preauth of this User.  # noqa: E501


        :return: The allow_preauth of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_preauth

    @allow_preauth.setter
    def allow_preauth(self, allow_preauth):
        """Sets the allow_preauth of this User.


        :param allow_preauth: The allow_preauth of this User.  # noqa: E501
        :type: bool
        """

        self._allow_preauth = allow_preauth

    @property
    def allow_secure_cards(self):
        """Gets the allow_secure_cards of this User.  # noqa: E501


        :return: The allow_secure_cards of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_secure_cards

    @allow_secure_cards.setter
    def allow_secure_cards(self, allow_secure_cards):
        """Sets the allow_secure_cards of this User.


        :param allow_secure_cards: The allow_secure_cards of this User.  # noqa: E501
        :type: bool
        """

        self._allow_secure_cards = allow_secure_cards

    @property
    def allow_subscriptions(self):
        """Gets the allow_subscriptions of this User.  # noqa: E501


        :return: The allow_subscriptions of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_subscriptions

    @allow_subscriptions.setter
    def allow_subscriptions(self, allow_subscriptions):
        """Sets the allow_subscriptions of this User.


        :param allow_subscriptions: The allow_subscriptions of this User.  # noqa: E501
        :type: bool
        """

        self._allow_subscriptions = allow_subscriptions

    @property
    def allow_dashboard(self):
        """Gets the allow_dashboard of this User.  # noqa: E501


        :return: The allow_dashboard of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_dashboard

    @allow_dashboard.setter
    def allow_dashboard(self, allow_dashboard):
        """Sets the allow_dashboard of this User.


        :param allow_dashboard: The allow_dashboard of this User.  # noqa: E501
        :type: bool
        """

        self._allow_dashboard = allow_dashboard

    @property
    def allow_achjhtransactions(self):
        """Gets the allow_achjhtransactions of this User.  # noqa: E501


        :return: The allow_achjhtransactions of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_achjhtransactions

    @allow_achjhtransactions.setter
    def allow_achjhtransactions(self, allow_achjhtransactions):
        """Sets the allow_achjhtransactions of this User.


        :param allow_achjhtransactions: The allow_achjhtransactions of this User.  # noqa: E501
        :type: bool
        """

        self._allow_achjhtransactions = allow_achjhtransactions

    @property
    def allow_achiptransactions(self):
        """Gets the allow_achiptransactions of this User.  # noqa: E501


        :return: The allow_achiptransactions of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_achiptransactions

    @allow_achiptransactions.setter
    def allow_achiptransactions(self, allow_achiptransactions):
        """Sets the allow_achiptransactions of this User.


        :param allow_achiptransactions: The allow_achiptransactions of this User.  # noqa: E501
        :type: bool
        """

        self._allow_achiptransactions = allow_achiptransactions

    @property
    def allow_partial_captures(self):
        """Gets the allow_partial_captures of this User.  # noqa: E501


        :return: The allow_partial_captures of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_partial_captures

    @allow_partial_captures.setter
    def allow_partial_captures(self, allow_partial_captures):
        """Sets the allow_partial_captures of this User.


        :param allow_partial_captures: The allow_partial_captures of this User.  # noqa: E501
        :type: bool
        """

        self._allow_partial_captures = allow_partial_captures

    @property
    def allow_scheduled_report(self):
        """Gets the allow_scheduled_report of this User.  # noqa: E501


        :return: The allow_scheduled_report of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_scheduled_report

    @allow_scheduled_report.setter
    def allow_scheduled_report(self, allow_scheduled_report):
        """Sets the allow_scheduled_report of this User.


        :param allow_scheduled_report: The allow_scheduled_report of this User.  # noqa: E501
        :type: bool
        """

        self._allow_scheduled_report = allow_scheduled_report

    @property
    def allow_api_key_management(self):
        """Gets the allow_api_key_management of this User.  # noqa: E501


        :return: The allow_api_key_management of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_api_key_management

    @allow_api_key_management.setter
    def allow_api_key_management(self, allow_api_key_management):
        """Sets the allow_api_key_management of this User.


        :param allow_api_key_management: The allow_api_key_management of this User.  # noqa: E501
        :type: bool
        """

        self._allow_api_key_management = allow_api_key_management

    @property
    def user_processing_terminals(self):
        """Gets the user_processing_terminals of this User.  # noqa: E501


        :return: The user_processing_terminals of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_processing_terminals

    @user_processing_terminals.setter
    def user_processing_terminals(self, user_processing_terminals):
        """Sets the user_processing_terminals of this User.


        :param user_processing_terminals: The user_processing_terminals of this User.  # noqa: E501
        :type: list[str]
        """

        self._user_processing_terminals = user_processing_terminals

