# coding: utf-8

from model.serializable import SwaggerSerializable


class CredoraxFeatures(SwaggerSerializable):
    swagger_types = {
        'allow_dashboard': 'bool',
        'allow_bulk_payments': 'bool',
        'allow_schedule_reports': 'bool',
        'allow_virtual_terminal_auto_order_id': 'bool',
        'enable_decryptx': 'bool',
        'pay_link': 'PayLink',
        'shopify': 'Shopify',
        'secure_credentials': 'SecureCredentials',
        'dynamic_descriptor': 'CredoraxDynamicDescriptor'
    }

    attribute_map = {
        'allow_dashboard': 'allowDashboard',
        'allow_bulk_payments': 'allowBulkPayments',
        'allow_schedule_reports': 'allowScheduleReports',
        'allow_virtual_terminal_auto_order_id': 'allowVirtualTerminalAutoOrderId',
        'enable_decryptx': 'enableDecryptx',
        'pay_link': 'payLink',
        'shopify': 'shopify',
        'secure_credentials': 'secureCredentials',
        'dynamic_descriptor': 'dynamicDescriptor'
    }

    def __init__(self, allow_dashboard=False, allow_bulk_payments=False, allow_schedule_reports=False, allow_virtual_terminal_auto_order_id=None, enable_decryptx=False, pay_link=None, shopify=None, secure_credentials=None, dynamic_descriptor=None):  # noqa: E501
        """CredoraxFeatures - a model defined in Swagger"""  # noqa: E501
        self._allow_dashboard = None
        self._allow_bulk_payments = None
        self._allow_schedule_reports = None
        self._allow_virtual_terminal_auto_order_id = None
        self._enable_decryptx = None
        self._pay_link = None
        self._shopify = None
        self._secure_credentials = None
        self._dynamic_descriptor = None
        self.discriminator = None
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
        if pay_link is not None:
            self.pay_link = pay_link
        if shopify is not None:
            self.shopify = shopify
        if secure_credentials is not None:
            self.secure_credentials = secure_credentials
        if dynamic_descriptor is not None:
            self.dynamic_descriptor = dynamic_descriptor

    @property
    def allow_dashboard(self):
        """Gets the allow_dashboard of this CredoraxFeatures.  # noqa: E501


        :return: The allow_dashboard of this CredoraxFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_dashboard

    @allow_dashboard.setter
    def allow_dashboard(self, allow_dashboard):
        """Sets the allow_dashboard of this CredoraxFeatures.


        :param allow_dashboard: The allow_dashboard of this CredoraxFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_dashboard = allow_dashboard

    @property
    def allow_bulk_payments(self):
        """Gets the allow_bulk_payments of this CredoraxFeatures.  # noqa: E501


        :return: The allow_bulk_payments of this CredoraxFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_bulk_payments

    @allow_bulk_payments.setter
    def allow_bulk_payments(self, allow_bulk_payments):
        """Sets the allow_bulk_payments of this CredoraxFeatures.


        :param allow_bulk_payments: The allow_bulk_payments of this CredoraxFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_bulk_payments = allow_bulk_payments

    @property
    def allow_schedule_reports(self):
        """Gets the allow_schedule_reports of this CredoraxFeatures.  # noqa: E501


        :return: The allow_schedule_reports of this CredoraxFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_schedule_reports

    @allow_schedule_reports.setter
    def allow_schedule_reports(self, allow_schedule_reports):
        """Sets the allow_schedule_reports of this CredoraxFeatures.


        :param allow_schedule_reports: The allow_schedule_reports of this CredoraxFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_schedule_reports = allow_schedule_reports

    @property
    def allow_virtual_terminal_auto_order_id(self):
        """Gets the allow_virtual_terminal_auto_order_id of this CredoraxFeatures.  # noqa: E501


        :return: The allow_virtual_terminal_auto_order_id of this CredoraxFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_virtual_terminal_auto_order_id

    @allow_virtual_terminal_auto_order_id.setter
    def allow_virtual_terminal_auto_order_id(self, allow_virtual_terminal_auto_order_id):
        """Sets the allow_virtual_terminal_auto_order_id of this CredoraxFeatures.


        :param allow_virtual_terminal_auto_order_id: The allow_virtual_terminal_auto_order_id of this CredoraxFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_virtual_terminal_auto_order_id = allow_virtual_terminal_auto_order_id

    @property
    def enable_decryptx(self):
        """Gets the enable_decryptx of this CredoraxFeatures.  # noqa: E501


        :return: The enable_decryptx of this CredoraxFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._enable_decryptx

    @enable_decryptx.setter
    def enable_decryptx(self, enable_decryptx):
        """Sets the enable_decryptx of this CredoraxFeatures.


        :param enable_decryptx: The enable_decryptx of this CredoraxFeatures.  # noqa: E501
        :type: bool
        """

        self._enable_decryptx = enable_decryptx

    @property
    def pay_link(self):
        """Gets the pay_link of this CredoraxFeatures.  # noqa: E501


        :return: The pay_link of this CredoraxFeatures.  # noqa: E501
        :rtype: PayLink
        """
        return self._pay_link

    @pay_link.setter
    def pay_link(self, pay_link):
        """Sets the pay_link of this CredoraxFeatures.


        :param pay_link: The pay_link of this CredoraxFeatures.  # noqa: E501
        :type: PayLink
        """

        self._pay_link = pay_link

    @property
    def shopify(self):
        """Gets the shopify of this CredoraxFeatures.  # noqa: E501


        :return: The shopify of this CredoraxFeatures.  # noqa: E501
        :rtype: Shopify
        """
        return self._shopify

    @shopify.setter
    def shopify(self, shopify):
        """Sets the shopify of this CredoraxFeatures.


        :param shopify: The shopify of this CredoraxFeatures.  # noqa: E501
        :type: Shopify
        """

        self._shopify = shopify

    @property
    def secure_credentials(self):
        """Gets the secure_credentials of this CredoraxFeatures.  # noqa: E501


        :return: The secure_credentials of this CredoraxFeatures.  # noqa: E501
        :rtype: SecureCredentials
        """
        return self._secure_credentials

    @secure_credentials.setter
    def secure_credentials(self, secure_credentials):
        """Sets the secure_credentials of this CredoraxFeatures.


        :param secure_credentials: The secure_credentials of this CredoraxFeatures.  # noqa: E501
        :type: SecureCredentials
        """

        self._secure_credentials = secure_credentials

    @property
    def dynamic_descriptor(self):
        """Gets the dynamic_descriptor of this CredoraxFeatures.  # noqa: E501


        :return: The dynamic_descriptor of this CredoraxFeatures.  # noqa: E501
        :rtype: CredoraxDynamicDescriptor
        """
        return self._dynamic_descriptor

    @dynamic_descriptor.setter
    def dynamic_descriptor(self, dynamic_descriptor):
        """Sets the dynamic_descriptor of this CredoraxFeatures.


        :param dynamic_descriptor: The dynamic_descriptor of this CredoraxFeatures.  # noqa: E501
        :type: CredoraxDynamicDescriptor
        """

        self._dynamic_descriptor = dynamic_descriptor

