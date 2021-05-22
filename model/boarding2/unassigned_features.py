# coding: utf-8

from model.serializable import SwaggerSerializable


class UnassignedFeatures(SwaggerSerializable):
    swagger_types = {
        'allow_acquiring': 'bool',
        'allow_schedule_reports': 'bool',
        'allow_virtual_terminal_auto_order_id': 'bool',
        'pay_link': 'PayLink',
        'secure_credentials': 'SecureCredentials'
    }

    attribute_map = {
        'allow_acquiring': 'allowAcquiring',
        'allow_schedule_reports': 'allowScheduleReports',
        'allow_virtual_terminal_auto_order_id': 'allowVirtualTerminalAutoOrderId',
        'pay_link': 'payLink',
        'secure_credentials': 'secureCredentials'
    }

    def __init__(self, allow_acquiring=False, allow_schedule_reports=False, allow_virtual_terminal_auto_order_id=False, pay_link=None, secure_credentials=None):  # noqa: E501
        """UnassignedFeatures - a model defined in Swagger"""  # noqa: E501
        self._allow_acquiring = None
        self._allow_schedule_reports = None
        self._allow_virtual_terminal_auto_order_id = None
        self._pay_link = None
        self._secure_credentials = None
        self.discriminator = None
        if allow_acquiring is not None:
            self.allow_acquiring = allow_acquiring
        if allow_schedule_reports is not None:
            self.allow_schedule_reports = allow_schedule_reports
        if allow_virtual_terminal_auto_order_id is not None:
            self.allow_virtual_terminal_auto_order_id = allow_virtual_terminal_auto_order_id
        if pay_link is not None:
            self.pay_link = pay_link
        if secure_credentials is not None:
            self.secure_credentials = secure_credentials

    @property
    def allow_acquiring(self):
        """Gets the allow_acquiring of this UnassignedFeatures.  # noqa: E501


        :return: The allow_acquiring of this UnassignedFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_acquiring

    @allow_acquiring.setter
    def allow_acquiring(self, allow_acquiring):
        """Sets the allow_acquiring of this UnassignedFeatures.


        :param allow_acquiring: The allow_acquiring of this UnassignedFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_acquiring = allow_acquiring

    @property
    def allow_schedule_reports(self):
        """Gets the allow_schedule_reports of this UnassignedFeatures.  # noqa: E501


        :return: The allow_schedule_reports of this UnassignedFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_schedule_reports

    @allow_schedule_reports.setter
    def allow_schedule_reports(self, allow_schedule_reports):
        """Sets the allow_schedule_reports of this UnassignedFeatures.


        :param allow_schedule_reports: The allow_schedule_reports of this UnassignedFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_schedule_reports = allow_schedule_reports

    @property
    def allow_virtual_terminal_auto_order_id(self):
        """Gets the allow_virtual_terminal_auto_order_id of this UnassignedFeatures.  # noqa: E501


        :return: The allow_virtual_terminal_auto_order_id of this UnassignedFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_virtual_terminal_auto_order_id

    @allow_virtual_terminal_auto_order_id.setter
    def allow_virtual_terminal_auto_order_id(self, allow_virtual_terminal_auto_order_id):
        """Sets the allow_virtual_terminal_auto_order_id of this UnassignedFeatures.


        :param allow_virtual_terminal_auto_order_id: The allow_virtual_terminal_auto_order_id of this UnassignedFeatures.  # noqa: E501
        :type: bool
        """

        self._allow_virtual_terminal_auto_order_id = allow_virtual_terminal_auto_order_id

    @property
    def pay_link(self):
        """Gets the pay_link of this UnassignedFeatures.  # noqa: E501


        :return: The pay_link of this UnassignedFeatures.  # noqa: E501
        :rtype: PayLink
        """
        return self._pay_link

    @pay_link.setter
    def pay_link(self, pay_link):
        """Sets the pay_link of this UnassignedFeatures.


        :param pay_link: The pay_link of this UnassignedFeatures.  # noqa: E501
        :type: PayLink
        """

        self._pay_link = pay_link

    @property
    def secure_credentials(self):
        """Gets the secure_credentials of this UnassignedFeatures.  # noqa: E501


        :return: The secure_credentials of this UnassignedFeatures.  # noqa: E501
        :rtype: SecureCredentials
        """
        return self._secure_credentials

    @secure_credentials.setter
    def secure_credentials(self, secure_credentials):
        """Sets the secure_credentials of this UnassignedFeatures.


        :param secure_credentials: The secure_credentials of this UnassignedFeatures.  # noqa: E501
        :type: SecureCredentials
        """

        self._secure_credentials = secure_credentials

