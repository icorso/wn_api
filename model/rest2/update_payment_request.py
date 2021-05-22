# coding: utf-8

from model.serializable import SwaggerSerializable


class UpdatePaymentRequest(SwaggerSerializable):

    swagger_types = {
        'operator': 'str',
        'total_amount': 'float',
        'customer': 'CustomerUpdatableData',
        'order_breakdown': 'OrderBreakdownUpdatableData',
        'status': 'str',
        'cardholder_signature': 'str'
    }

    attribute_map = {
        'operator': 'operator',
        'total_amount': 'totalAmount',
        'customer': 'customer',
        'order_breakdown': 'orderBreakdown',
        'status': 'status',
        'cardholder_signature': 'cardholderSignature'
    }

    def __init__(self, operator=None, total_amount=None, customer=None, order_breakdown=None, status=None, cardholder_signature=None):  # noqa: E501
        """UpdatePaymentRequest - a model defined in Swagger"""  # noqa: E501
        self._operator = None
        self._total_amount = None
        self._customer = None
        self._order_breakdown = None
        self._status = None
        self._cardholder_signature = None
        self.discriminator = None
        if operator is not None:
            self.operator = operator
        if total_amount is not None:
            self.total_amount = total_amount
        if customer is not None:
            self.customer = customer
        if order_breakdown is not None:
            self.order_breakdown = order_breakdown
        if status is not None:
            self.status = status
        if cardholder_signature is not None:
            self.cardholder_signature = cardholder_signature

    @property
    def operator(self):
        """Gets the operator of this UpdatePaymentRequest.  # noqa: E501

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :return: The operator of this UpdatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this UpdatePaymentRequest.

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :param operator: The operator of this UpdatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def total_amount(self):
        """Gets the total_amount of this UpdatePaymentRequest.  # noqa: E501

        It allows clients to update the transaction's total amount.  # noqa: E501

        :return: The total_amount of this UpdatePaymentRequest.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this UpdatePaymentRequest.

        It allows clients to update the transaction's total amount.  # noqa: E501

        :param total_amount: The total_amount of this UpdatePaymentRequest.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def customer(self):
        """Gets the customer of this UpdatePaymentRequest.  # noqa: E501


        :return: The customer of this UpdatePaymentRequest.  # noqa: E501
        :rtype: CustomerUpdatableData
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this UpdatePaymentRequest.


        :param customer: The customer of this UpdatePaymentRequest.  # noqa: E501
        :type: CustomerUpdatableData
        """

        self._customer = customer

    @property
    def order_breakdown(self):
        """Gets the order_breakdown of this UpdatePaymentRequest.  # noqa: E501


        :return: The order_breakdown of this UpdatePaymentRequest.  # noqa: E501
        :rtype: OrderBreakdownUpdatableData
        """
        return self._order_breakdown

    @order_breakdown.setter
    def order_breakdown(self, order_breakdown):
        """Sets the order_breakdown of this UpdatePaymentRequest.


        :param order_breakdown: The order_breakdown of this UpdatePaymentRequest.  # noqa: E501
        :type: OrderBreakdownUpdatableData
        """

        self._order_breakdown = order_breakdown

    @property
    def status(self):
        """Gets the status of this UpdatePaymentRequest.  # noqa: E501

        It allows clients to update the transaction's status.  # noqa: E501

        :return: The status of this UpdatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdatePaymentRequest.

        It allows clients to update the transaction's status.  # noqa: E501

        :param status: The status of this UpdatePaymentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["READY", "PENDING", "VOID", "DECLINED", "COMPLETE", "REFERRAL", "PICKUP", "REVERSAL", "SENT", "ADMIN", "EXPIRED", "ACCEPTED", "REVIEW", "OTHER"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def cardholder_signature(self):
        """Gets the cardholder_signature of this UpdatePaymentRequest.  # noqa: E501

        It allows clients to perform a late signature capture for approved cardholder present transactions.  **Note:** Once a signature is stored for a specific transaction it cannot be replace or deleted.  # noqa: E501

        :return: The cardholder_signature of this UpdatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_signature

    @cardholder_signature.setter
    def cardholder_signature(self, cardholder_signature):
        """Sets the cardholder_signature of this UpdatePaymentRequest.

        It allows clients to perform a late signature capture for approved cardholder present transactions.  **Note:** Once a signature is stored for a specific transaction it cannot be replace or deleted.  # noqa: E501

        :param cardholder_signature: The cardholder_signature of this UpdatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._cardholder_signature = cardholder_signature
