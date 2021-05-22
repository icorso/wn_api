# coding: utf-8

from model.serializable import SwaggerSerializable


class ReversePaymentRequest(SwaggerSerializable):
    swagger_types = {
        'operator': 'str',
        'reversal_amount': 'float',
        'reversal_reason': 'str',
        'customer_account': 'Payload',
        'ip_address': 'IpAddress'
    }

    attribute_map = {
        'operator': 'operator',
        'reversal_amount': 'reversalAmount',
        'reversal_reason': 'reversalReason',
        'customer_account': 'customerAccount',
        'ip_address': 'ipAddress'
    }

    def __init__(self, operator=None, reversal_amount=None, reversal_reason=None, customer_account=None, ip_address=None):  # noqa: E501
        """ReversePaymentRequest - a model defined in Swagger"""  # noqa: E501
        self._operator = None
        self._reversal_amount = None
        self._reversal_reason = None
        self._customer_account = None
        self._ip_address = None
        self.discriminator = None
        if operator is not None:
            self.operator = operator
        if reversal_amount is not None:
            self.reversal_amount = reversal_amount
        if reversal_reason is not None:
            self.reversal_reason = reversal_reason
        if customer_account is not None:
            self.customer_account = customer_account
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def operator(self):
        """Gets the operator of this ReversePaymentRequest.  # noqa: E501

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :return: The operator of this ReversePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ReversePaymentRequest.

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :param operator: The operator of this ReversePaymentRequest.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def reversal_amount(self):
        """Gets the reversal_amount of this ReversePaymentRequest.  # noqa: E501

        The amount to return to the customer's account.  **Note:** This field is not required for full amount cancellations.  # noqa: E501

        :return: The reversal_amount of this ReversePaymentRequest.  # noqa: E501
        :rtype: float
        """
        return self._reversal_amount

    @reversal_amount.setter
    def reversal_amount(self, reversal_amount):
        """Sets the reversal_amount of this ReversePaymentRequest.

        The amount to return to the customer's account.  **Note:** This field is not required for full amount cancellations.  # noqa: E501

        :param reversal_amount: The reversal_amount of this ReversePaymentRequest.  # noqa: E501
        :type: float
        """

        self._reversal_amount = reversal_amount

    @property
    def reversal_reason(self):
        """Gets the reversal_reason of this ReversePaymentRequest.  # noqa: E501

        The reason why the transaction is being cancelled.  # noqa: E501

        :return: The reversal_reason of this ReversePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._reversal_reason

    @reversal_reason.setter
    def reversal_reason(self, reversal_reason):
        """Sets the reversal_reason of this ReversePaymentRequest.

        The reason why the transaction is being cancelled.  # noqa: E501

        :param reversal_reason: The reversal_reason of this ReversePaymentRequest.  # noqa: E501
        :type: str
        """

        self._reversal_reason = reversal_reason

    @property
    def customer_account(self):
        """Gets the customer_account of this ReversePaymentRequest.  # noqa: E501


        :return: The customer_account of this ReversePaymentRequest.  # noqa: E501
        :rtype: Payload
        """
        return self._customer_account

    @customer_account.setter
    def customer_account(self, customer_account):
        """Sets the customer_account of this ReversePaymentRequest.


        :param customer_account: The customer_account of this ReversePaymentRequest.  # noqa: E501
        :type: Payload
        """

        self._customer_account = customer_account

    @property
    def ip_address(self):
        """Gets the ip_address of this ReversePaymentRequest.  # noqa: E501


        :return: The ip_address of this ReversePaymentRequest.  # noqa: E501
        :rtype: IpAddress
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ReversePaymentRequest.


        :param ip_address: The ip_address of this ReversePaymentRequest.  # noqa: E501
        :type: IpAddress
        """

        self._ip_address = ip_address
