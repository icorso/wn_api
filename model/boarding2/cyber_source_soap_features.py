# coding: utf-8

from model.serializable import SwaggerSerializable


class CyberSourceSoapFeatures(SwaggerSerializable):
    swagger_types = {
        'allow_acquiring': 'bool',
        'allow_dashboard': 'bool',
        'allow_bulk_payments': 'bool',
        'allow_schedule_reports': 'bool',
        'allow_virtual_terminal_auto_order_id': 'bool',
        'enable_decryptx': 'bool',
        'pay_link': 'PayLink',
        'secure_credentials': 'SecureCredentials'
    }

    attribute_map = {
        'allow_acquiring': 'allowAcquiring',
        'allow_dashboard': 'allowDashboard',
        'allow_bulk_payments': 'allowBulkPayments',
        'allow_schedule_reports': 'allowScheduleReports',
        'allow_virtual_terminal_auto_order_id': 'allowVirtualTerminalAutoOrderId',
        'enable_decryptx': 'enableDecryptx',
        'pay_link': 'payLink',
        'secure_credentials': 'secureCredentials'
    }

    def __init__(self, allow_acquiring=False, allow_dashboard=False, allow_bulk_payments=False, allow_schedule_reports=False, allow_virtual_terminal_auto_order_id=False, enable_decryptx=False, pay_link=None, secure_credentials=None):  # noqa: E501
        """CyberSourceSoapFeatures - a model defined in Swagger"""  # noqa: E501
        self._allow_acquiring = None
        self._allow_dashboard = None
        self._allow_bulk_payments = None
        self._allow_schedule_reports = None
        self._allow_virtual_terminal_auto_order_id = None
        self._enable_decryptx = None
        self._pay_link = None
        self._secure_credentials = None
        self.discriminator = None
        if allow_acquiring is not None:
            self.allow_acquiring = allow_acquiring
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
        if secure_credentials is not None:
            self.secure_credentials = secure_credentials

    @property
    def allow_acquiring(self):
        """Gets the allow_acquiring of this CyberSourceSoapFeatures.  # noqa: E501


        :return: The allow_acquiring of this CyberSourceSoapFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_acquiring

    @allow_acquiring.setter
    def allow_acquiring(self, allow_acquiring):
        """Sets the allow_acquiring of this CyberSourceSoapFeatures.


        :param allow_acquiring: The allow_acquiring of this CyberSourceSoapFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_acquiring = allow_acquiring

    @property
    def allow_dashboard(self):
        """Gets the allow_dashboard of this CyberSourceSoapFeatures.  # noqa: E501


        :return: The allow_dashboard of this CyberSourceSoapFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_dashboard

    @allow_dashboard.setter
    def allow_dashboard(self, allow_dashboard):
        """Sets the allow_dashboard of this CyberSourceSoapFeatures.


        :param allow_dashboard: The allow_dashboard of this CyberSourceSoapFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_dashboard = allow_dashboard

    @property
    def allow_bulk_payments(self):
        """Gets the allow_bulk_payments of this CyberSourceSoapFeatures.  # noqa: E501


        :return: The allow_bulk_payments of this CyberSourceSoapFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_bulk_payments

    @allow_bulk_payments.setter
    def allow_bulk_payments(self, allow_bulk_payments):
        """Sets the allow_bulk_payments of this CyberSourceSoapFeatures.


        :param allow_bulk_payments: The allow_bulk_payments of this CyberSourceSoapFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_bulk_payments = allow_bulk_payments

    @property
    def allow_schedule_reports(self):
        """Gets the allow_schedule_reports of this CyberSourceSoapFeatures.  # noqa: E501


        :return: The allow_schedule_reports of this CyberSourceSoapFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_schedule_reports

    @allow_schedule_reports.setter
    def allow_schedule_reports(self, allow_schedule_reports):
        """Sets the allow_schedule_reports of this CyberSourceSoapFeatures.


        :param allow_schedule_reports: The allow_schedule_reports of this CyberSourceSoapFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_schedule_reports = allow_schedule_reports

    @property
    def allow_virtual_terminal_auto_order_id(self):
        """Gets the allow_virtual_terminal_auto_order_id of this CyberSourceSoapFeatures.  # noqa: E501


        :return: The allow_virtual_terminal_auto_order_id of this CyberSourceSoapFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_virtual_terminal_auto_order_id

    @allow_virtual_terminal_auto_order_id.setter
    def allow_virtual_terminal_auto_order_id(self, allow_virtual_terminal_auto_order_id):
        """Sets the allow_virtual_terminal_auto_order_id of this CyberSourceSoapFeatures.


        :param allow_virtual_terminal_auto_order_id: The allow_virtual_terminal_auto_order_id of this CyberSourceSoapFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_virtual_terminal_auto_order_id = allow_virtual_terminal_auto_order_id

    @property
    def enable_decryptx(self):
        """Gets the enable_decryptx of this CyberSourceSoapFeatures.  # noqa: E501


        :return: The enable_decryptx of this CyberSourceSoapFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._enable_decryptx

    @enable_decryptx.setter
    def enable_decryptx(self, enable_decryptx):
        """Sets the enable_decryptx of this CyberSourceSoapFeatures.


        :param enable_decryptx: The enable_decryptx of this CyberSourceSoapFeatures.  # noqa: E501
        :type: bool
        """

        self._enable_decryptx = enable_decryptx

    @property
    def pay_link(self):
        """Gets the pay_link of this CyberSourceSoapFeatures.  # noqa: E501


        :return: The pay_link of this CyberSourceSoapFeatures.  # noqa: E501
        :rtype: PayLink
        """
        return self._pay_link

    @pay_link.setter
    def pay_link(self, pay_link):
        """Sets the pay_link of this CyberSourceSoapFeatures.


        :param pay_link: The pay_link of this CyberSourceSoapFeatures.  # noqa: E501
        :type: PayLink
        """

        self._pay_link = pay_link

    @property
    def secure_credentials(self):
        """Gets the secure_credentials of this CyberSourceSoapFeatures.  # noqa: E501


        :return: The secure_credentials of this CyberSourceSoapFeatures.  # noqa: E501
        :rtype: SecureCredentials
        """
        return self._secure_credentials

    @secure_credentials.setter
    def secure_credentials(self, secure_credentials):
        """Sets the secure_credentials of this CyberSourceSoapFeatures.


        :param secure_credentials: The secure_credentials of this CyberSourceSoapFeatures.  # noqa: E501
        :type: SecureCredentials
        """

        self._secure_credentials = secure_credentials

