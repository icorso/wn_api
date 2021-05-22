# coding: utf-8

from model.serializable import SwaggerSerializable


class RefundPaymentRequest(SwaggerSerializable):
    swagger_types = {
        'operator': 'str',
        'refund_amount': 'float',
        'refund_reason': 'str',
    }

    attribute_map = {
        'operator': 'operator',
        'refund_amount': 'refundAmount',
        'refund_reason': 'refundReason',
    }

    def __init__(self, auto_ready=None, operator=None, refund_amount=None, refund_reason=None):  # noqa: E501
        """RefundPaymentRequest - a model defined in Swagger"""  # noqa: E501
        self._operator = None
        self._refund_amount = None
        self._refund_reason = None
        self.discriminator = None
        if operator is not None:
            self.operator = operator
        self.refund_amount = refund_amount
        self.refund_reason = refund_reason

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        self._operator = operator

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        if refund_amount is None:
            raise ValueError("Invalid value for `refund_amount`, must not be `None`")  # noqa: E501

        self._refund_amount = refund_amount

    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, refund_reason):
        if refund_reason is None:
            raise ValueError("Invalid value for `refund_reason`, must not be `None`")  # noqa: E501

        self._refund_reason = refund_reason
