# coding: utf-8
from model.rest2.refund_request import RefundRequest
from model.serializable import SwaggerSerializable


class MotoRefundRequest(SwaggerSerializable):
    swagger_types = {
        'channel': 'str',
        'terminal': 'str',
        'operator': 'str',
        'order_id': 'str',
        'currency': 'str',
        'refund_amount': 'float',
        'refund_reason': 'str',
        'customer': 'Customer',
        'customer_account': 'Payload',
        'ip_address': 'IpAddress',
        'additional_data_fields': 'list[CustomField]'
    }
    if hasattr(RefundRequest, "swagger_types"):
        swagger_types.update(RefundRequest.swagger_types)

    attribute_map = {
        'channel': 'channel',
        'terminal': 'terminal',
        'operator': 'operator',
        'order_id': 'orderId',
        'currency': 'currency',
        'refund_amount': 'refundAmount',
        'refund_reason': 'refundReason',
        'customer': 'customer',
        'customer_account': 'customerAccount',
        'ip_address': 'ipAddress',
        'additional_data_fields': 'additionalDataFields'
    }
    if hasattr(RefundRequest, "attribute_map"):
        attribute_map.update(RefundRequest.attribute_map)

    def __init__(self, channel=None, terminal=None, operator=None, order_id=None, currency=None, refund_amount=None, refund_reason=None, customer=None, customer_account=None, ip_address=None, additional_data_fields=None, *args, **kwargs):  # noqa: E501
        """MotoRefundRequest - a model defined in Swagger"""  # noqa: E501
        self._channel = None
        self._terminal = None
        self._operator = None
        self._order_id = None
        self._currency = None
        self._refund_amount = None
        self._refund_reason = None
        self._customer = None
        self._customer_account = None
        self._ip_address = None
        self._additional_data_fields = None
        self.discriminator = None
        if channel is not None:
            self.channel = channel
        self.terminal = terminal
        if operator is not None:
            self.operator = operator
        self.order_id = order_id
        self.currency = currency
        self.refund_amount = refund_amount
        self.refund_reason = refund_reason
        if customer is not None:
            self.customer = customer
        self.customer_account = customer_account
        if ip_address is not None:
            self.ip_address = ip_address
        if additional_data_fields is not None:
            self.additional_data_fields = additional_data_fields
        RefundRequest.__init__(self, *args, **kwargs)

    @property
    def channel(self):
        """Gets the channel of this MotoRefundRequest.  # noqa: E501


        :return: The channel of this MotoRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this MotoRefundRequest.


        :param channel: The channel of this MotoRefundRequest.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def terminal(self):
        """Gets the terminal of this MotoRefundRequest.  # noqa: E501

        The terminal number assigned by the gateway.  # noqa: E501

        :return: The terminal of this MotoRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this MotoRefundRequest.

        The terminal number assigned by the gateway.  # noqa: E501

        :param terminal: The terminal of this MotoRefundRequest.  # noqa: E501
        :type: str
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def operator(self):
        """Gets the operator of this MotoRefundRequest.  # noqa: E501

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :return: The operator of this MotoRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this MotoRefundRequest.

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :param operator: The operator of this MotoRefundRequest.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def order_id(self):
        """Gets the order_id of this MotoRefundRequest.  # noqa: E501

        A unique identifier for the order assigned by the merchant.  # noqa: E501

        :return: The order_id of this MotoRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this MotoRefundRequest.

        A unique identifier for the order assigned by the merchant.  # noqa: E501

        :param order_id: The order_id of this MotoRefundRequest.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def currency(self):
        """Gets the currency of this MotoRefundRequest.  # noqa: E501

        The currency of the transaction. A 3-letter code as per the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) standard.  # noqa: E501

        :return: The currency of this MotoRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MotoRefundRequest.

        The currency of the transaction. A 3-letter code as per the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) standard.  # noqa: E501

        :param currency: The currency of this MotoRefundRequest.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def refund_amount(self):
        """Gets the refund_amount of this MotoRefundRequest.  # noqa: E501

        The total amount to be refunded.  # noqa: E501

        :return: The refund_amount of this MotoRefundRequest.  # noqa: E501
        :rtype: float
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """Sets the refund_amount of this MotoRefundRequest.

        The total amount to be refunded.  # noqa: E501

        :param refund_amount: The refund_amount of this MotoRefundRequest.  # noqa: E501
        :type: float
        """
        if refund_amount is None:
            raise ValueError("Invalid value for `refund_amount`, must not be `None`")  # noqa: E501

        self._refund_amount = refund_amount

    @property
    def refund_reason(self):
        """Gets the refund_reason of this MotoRefundRequest.  # noqa: E501

        The reason why the refund is being performed.  # noqa: E501

        :return: The refund_reason of this MotoRefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, refund_reason):
        """Sets the refund_reason of this MotoRefundRequest.

        The reason why the refund is being performed.  # noqa: E501

        :param refund_reason: The refund_reason of this MotoRefundRequest.  # noqa: E501
        :type: str
        """
        if refund_reason is None:
            raise ValueError("Invalid value for `refund_reason`, must not be `None`")  # noqa: E501

        self._refund_reason = refund_reason

    @property
    def customer(self):
        """Gets the customer of this MotoRefundRequest.  # noqa: E501


        :return: The customer of this MotoRefundRequest.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this MotoRefundRequest.


        :param customer: The customer of this MotoRefundRequest.  # noqa: E501
        :type: Customer
        """

        self._customer = customer

    @property
    def customer_account(self):
        """Gets the customer_account of this MotoRefundRequest.  # noqa: E501


        :return: The customer_account of this MotoRefundRequest.  # noqa: E501
        :rtype: Payload
        """
        return self._customer_account

    @customer_account.setter
    def customer_account(self, customer_account):
        """Sets the customer_account of this MotoRefundRequest.


        :param customer_account: The customer_account of this MotoRefundRequest.  # noqa: E501
        :type: Payload
        """
        if customer_account is None:
            raise ValueError("Invalid value for `customer_account`, must not be `None`")  # noqa: E501

        self._customer_account = customer_account

    @property
    def ip_address(self):
        """Gets the ip_address of this MotoRefundRequest.  # noqa: E501


        :return: The ip_address of this MotoRefundRequest.  # noqa: E501
        :rtype: IpAddress
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this MotoRefundRequest.


        :param ip_address: The ip_address of this MotoRefundRequest.  # noqa: E501
        :type: IpAddress
        """

        self._ip_address = ip_address

    @property
    def additional_data_fields(self):
        """Gets the additional_data_fields of this MotoRefundRequest.  # noqa: E501

        List of custom fields which are used to add extra information to transactions. Their values are going to be stored and used for the requests sent to the terminal's receipt and validation webhooks.<br />To understand more visit the section regarding [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters).  # noqa: E501

        :return: The additional_data_fields of this MotoRefundRequest.  # noqa: E501
        :rtype: list[CustomField]
        """
        return self._additional_data_fields

    @additional_data_fields.setter
    def additional_data_fields(self, additional_data_fields):
        """Sets the additional_data_fields of this MotoRefundRequest.

        List of custom fields which are used to add extra information to transactions. Their values are going to be stored and used for the requests sent to the terminal's receipt and validation webhooks.<br />To understand more visit the section regarding [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters).  # noqa: E501

        :param additional_data_fields: The additional_data_fields of this MotoRefundRequest.  # noqa: E501
        :type: list[CustomField]
        """

        self._additional_data_fields = additional_data_fields
