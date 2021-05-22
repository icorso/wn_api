# coding: utf-8
from model.serializable import SwaggerSerializable


class CapturePaymentRequest(SwaggerSerializable):
    swagger_types = {
        'operator': 'str',
        'capture_amount': 'float'
    }

    attribute_map = {
        'operator': 'operator',
        'capture_amount': 'captureAmount'
    }

    def __init__(self, operator=None, capture_amount=None):  # noqa: E501
        """CapturePaymentRequest - a model defined in Swagger"""  # noqa: E501
        self._operator = None
        self._capture_amount = None
        self.discriminator = None
        if operator is not None:
            self.operator = operator
        if capture_amount is not None:
            self.capture_amount = capture_amount

    @property
    def operator(self):
        """Gets the operator of this CapturePaymentRequest.  # noqa: E501

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :return: The operator of this CapturePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this CapturePaymentRequest.

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :param operator: The operator of this CapturePaymentRequest.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def capture_amount(self):
        """Gets the capture_amount of this CapturePaymentRequest.  # noqa: E501

        The amount to be captured. If not sent, the full amount of the transaction will be captured.  # noqa: E501

        :return: The capture_amount of this CapturePaymentRequest.  # noqa: E501
        :rtype: float
        """
        return self._capture_amount

    @capture_amount.setter
    def capture_amount(self, capture_amount):
        """Sets the capture_amount of this CapturePaymentRequest.

        The amount to be captured. If not sent, the full amount of the transaction will be captured.  # noqa: E501

        :param capture_amount: The capture_amount of this CapturePaymentRequest.  # noqa: E501
        :type: float
        """

        self._capture_amount = capture_amount
