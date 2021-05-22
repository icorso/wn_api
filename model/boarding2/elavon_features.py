# coding: utf-8

from model.serializable import SwaggerSerializable


class ElavonFeatures(SwaggerSerializable):
    swagger_types = {
        'allow_partial_captures': 'bool',
        'allow_dashboard': 'bool',
        'allow_bulk_payments': 'bool',
        'allow_schedule_reports': 'bool',
        'allow_virtual_terminal_auto_order_id': 'bool',
        'enable_decryptx': 'bool',
        'enable_google_pay': 'bool',
        'enable_apple_pay': 'bool',
        'apple_store_name': 'str',
        'pay_link': 'PayLink',
        'shopify': 'Shopify',
        'secure_credentials': 'SecureCredentials'
    }

    attribute_map = {
        'allow_partial_captures': 'allowPartialCaptures',
        'allow_dashboard': 'allowDashboard',
        'allow_bulk_payments': 'allowBulkPayments',
        'allow_schedule_reports': 'allowScheduleReports',
        'allow_virtual_terminal_auto_order_id': 'allowVirtualTerminalAutoOrderId',
        'enable_decryptx': 'enableDecryptx',
        'enable_google_pay': 'enableGooglePay',
        'enable_apple_pay': 'enableApplePay',
        'apple_store_name': 'appleStoreName',
        'pay_link': 'payLink',
        'shopify': 'shopify',
        'secure_credentials': 'secureCredentials'
    }

    def __init__(self, allow_partial_captures=False, allow_dashboard=False, allow_bulk_payments=False, allow_schedule_reports=False, allow_virtual_terminal_auto_order_id=False, enable_decryptx=False, enable_google_pay=False, enable_apple_pay=False, apple_store_name=None, pay_link=None, shopify=None, secure_credentials=None):  # noqa: E501
        """ElavonFeatures - a model defined in Swagger"""  # noqa: E501
        self._allow_partial_captures = None
        self._allow_dashboard = None
        self._allow_bulk_payments = None
        self._allow_schedule_reports = None
        self._allow_virtual_terminal_auto_order_id = None
        self._enable_decryptx = None
        self._enable_google_pay = None
        self._enable_apple_pay = None
        self._apple_store_name = None
        self._pay_link = None
        self._shopify = None
        self._secure_credentials = None
        self.discriminator = None
        if allow_partial_captures is not None:
            self.allow_partial_captures = allow_partial_captures
        if allow_dashboard is not None:
            self.allow_dashboard = allow_dashboard
        if allow_bulk_payments is not None:
            self.allow_bulk_payments = allow_bulk_payments
        if allow_schedule_reports is not None:
            self.allow_schedule_reports = allow_schedule_reports
        if allow_virtual_terminal_auto_order_id is not None:
            self.allow_virtual_terminal_auto_order_id = allow_virtual_terminal_auto_order_id
        if enable_decryptx is not None:
            self.enable_decryptx = enable_decryptx
        if enable_google_pay is not None:
            self.enable_google_pay = enable_google_pay
        if enable_apple_pay is not None:
            self.enable_apple_pay = enable_apple_pay
        if apple_store_name is not None:
            self.apple_store_name = apple_store_name
        if pay_link is not None:
            self.pay_link = pay_link
        if shopify is not None:
            self.shopify = shopify
        if secure_credentials is not None:
            self.secure_credentials = secure_credentials

    @property
    def allow_partial_captures(self):
        """Gets the allow_partial_captures of this ElavonFeatures.  # noqa: E501


        :return: The allow_partial_captures of this ElavonFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_partial_captures

    @allow_partial_captures.setter
    def allow_partial_captures(self, allow_partial_captures):
        """Sets the allow_partial_captures of this ElavonFeatures.


        :param allow_partial_captures: The allow_partial_captures of this ElavonFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_partial_captures = allow_partial_captures

    @property
    def allow_dashboard(self):
        """Gets the allow_dashboard of this ElavonFeatures.  # noqa: E501


        :return: The allow_dashboard of this ElavonFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_dashboard

    @allow_dashboard.setter
    def allow_dashboard(self, allow_dashboard):
        """Sets the allow_dashboard of this ElavonFeatures.


        :param allow_dashboard: The allow_dashboard of this ElavonFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_dashboard = allow_dashboard

    @property
    def allow_bulk_payments(self):
        """Gets the allow_bulk_payments of this ElavonFeatures.  # noqa: E501


        :return: The allow_bulk_payments of this ElavonFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_bulk_payments

    @allow_bulk_payments.setter
    def allow_bulk_payments(self, allow_bulk_payments):
        """Sets the allow_bulk_payments of this ElavonFeatures.


        :param allow_bulk_payments: The allow_bulk_payments of this ElavonFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_bulk_payments = allow_bulk_payments

    @property
    def allow_schedule_reports(self):
        """Gets the allow_schedule_reports of this ElavonFeatures.  # noqa: E501


        :return: The allow_schedule_reports of this ElavonFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_schedule_reports

    @allow_schedule_reports.setter
    def allow_schedule_reports(self, allow_schedule_reports):
        """Sets the allow_schedule_reports of this ElavonFeatures.


        :param allow_schedule_reports: The allow_schedule_reports of this ElavonFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_schedule_reports = allow_schedule_reports

    @property
    def allow_virtual_terminal_auto_order_id(self):
        """Gets the allow_virtual_terminal_auto_order_id of this ElavonFeatures.  # noqa: E501


        :return: The allow_virtual_terminal_auto_order_id of this ElavonFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_virtual_terminal_auto_order_id

    @allow_virtual_terminal_auto_order_id.setter
    def allow_virtual_terminal_auto_order_id(self, allow_virtual_terminal_auto_order_id):
        """Sets the allow_virtual_terminal_auto_order_id of this ElavonFeatures.


        :param allow_virtual_terminal_auto_order_id: The allow_virtual_terminal_auto_order_id of this ElavonFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_virtual_terminal_auto_order_id = allow_virtual_terminal_auto_order_id

    @property
    def enable_decryptx(self):
        """Gets the enable_decryptx of this ElavonFeatures.  # noqa: E501


        :return: The enable_decryptx of this ElavonFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._enable_decryptx

    @enable_decryptx.setter
    def enable_decryptx(self, enable_decryptx):
        """Sets the enable_decryptx of this ElavonFeatures.


        :param enable_decryptx: The enable_decryptx of this ElavonFeatures.  # noqa: E501
        :type: bool
        """

        self._enable_decryptx = enable_decryptx

    @property
    def enable_google_pay(self):
        """Gets the enable_google_pay of this ElavonFeatures.  # noqa: E501


        :return: The enable_google_pay of this ElavonFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._enable_google_pay

    @enable_google_pay.setter
    def enable_google_pay(self, enable_google_pay):
        """Sets the enable_google_pay of this ElavonFeatures.


        :param enable_google_pay: The enable_google_pay of this ElavonFeatures.  # noqa: E501
        :type: bool
        """

        self._enable_google_pay = enable_google_pay

    @property
    def enable_apple_pay(self):
        """Gets the enable_apple_pay of this ElavonFeatures.  # noqa: E501


        :return: The enable_apple_pay of this ElavonFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._enable_apple_pay

    @enable_apple_pay.setter
    def enable_apple_pay(self, enable_apple_pay):
        """Sets the enable_apple_pay of this ElavonFeatures.


        :param enable_apple_pay: The enable_apple_pay of this ElavonFeatures.  # noqa: E501
        :type: bool
        """

        self._enable_apple_pay = enable_apple_pay

    @property
    def apple_store_name(self):
        """Gets the apple_store_name of this ElavonFeatures.  # noqa: E501


        :return: The apple_store_name of this ElavonFeatures.  # noqa: E501
        :rtype: str
        """
        return self._apple_store_name

    @apple_store_name.setter
    def apple_store_name(self, apple_store_name):
        """Sets the apple_store_name of this ElavonFeatures.


        :param apple_store_name: The apple_store_name of this ElavonFeatures.  # noqa: E501
        :type: str
        """

        self._apple_store_name = apple_store_name

    @property
    def pay_link(self):
        """Gets the pay_link of this ElavonFeatures.  # noqa: E501


        :return: The pay_link of this ElavonFeatures.  # noqa: E501
        :rtype: PayLink
        """
        return self._pay_link

    @pay_link.setter
    def pay_link(self, pay_link):
        """Sets the pay_link of this ElavonFeatures.


        :param pay_link: The pay_link of this ElavonFeatures.  # noqa: E501
        :type: PayLink
        """

        self._pay_link = pay_link

    @property
    def shopify(self):
        """Gets the shopify of this ElavonFeatures.  # noqa: E501


        :return: The shopify of this ElavonFeatures.  # noqa: E501
        :rtype: Shopify
        """
        return self._shopify

    @shopify.setter
    def shopify(self, shopify):
        """Sets the shopify of this ElavonFeatures.


        :param shopify: The shopify of this ElavonFeatures.  # noqa: E501
        :type: Shopify
        """

        self._shopify = shopify

    @property
    def secure_credentials(self):
        """Gets the secure_credentials of this ElavonFeatures.  # noqa: E501


        :return: The secure_credentials of this ElavonFeatures.  # noqa: E501
        :rtype: SecureCredentials
        """
        return self._secure_credentials

    @secure_credentials.setter
    def secure_credentials(self, secure_credentials):
        """Sets the secure_credentials of this ElavonFeatures.


        :param secure_credentials: The secure_credentials of this ElavonFeatures.  # noqa: E501
        :type: SecureCredentials
        """

        self._secure_credentials = secure_credentials

