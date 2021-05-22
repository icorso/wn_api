# coding: utf-8
from model.serializable import SwaggerSerializable


class TransactionCompact(SwaggerSerializable):
    swagger_types = {
        'unique_reference': 'str',
        'terminal': 'str',
        'operator': 'str',
        'order_id': 'str',
        'date_time': 'datetime',
        'description': 'str',
        'customer_name': 'str',
        'masked_pan': 'str',
        'type': 'str',
        'result_code': 'str',
        'status': 'str',
        'currency': 'str',
        'amount': 'float',
        'links': 'list[HypermediaLink]'
    }

    attribute_map = {
        'unique_reference': 'uniqueReference',
        'terminal': 'terminal',
        'operator': 'operator',
        'order_id': 'orderId',
        'date_time': 'dateTime',
        'description': 'description',
        'customer_name': 'customerName',
        'masked_pan': 'maskedPan',
        'type': 'type',
        'result_code': 'resultCode',
        'status': 'status',
        'currency': 'currency',
        'amount': 'amount',
        'links': 'links'
    }

    def __init__(self, unique_reference=None, terminal=None, operator=None, order_id=None, date_time=None, description=None, customer_name=None, masked_pan=None, type=None, result_code=None, status=None, currency=None, amount=None, links=None):  # noqa: E501
        """TransactionCompact - a model defined in Swagger"""  # noqa: E501
        self._unique_reference = None
        self._terminal = None
        self._operator = None
        self._order_id = None
        self._date_time = None
        self._description = None
        self._customer_name = None
        self._masked_pan = None
        self._type = None
        self._result_code = None
        self._status = None
        self._currency = None
        self._amount = None
        self._links = None
        self.discriminator = None
        self.unique_reference = unique_reference
        self.terminal = terminal
        if operator is not None:
            self.operator = operator
        self.order_id = order_id
        if date_time is not None:
            self.date_time = date_time
        if description is not None:
            self.description = description
        if customer_name is not None:
            self.customer_name = customer_name
        if masked_pan is not None:
            self.masked_pan = masked_pan
        if type is not None:
            self.type = type
        if result_code is not None:
            self.result_code = result_code
        if status is not None:
            self.status = status
        self.currency = currency
        self.amount = amount
        if links is not None:
            self.links = links

    @property
    def unique_reference(self):
        """Gets the unique_reference of this TransactionCompact.  # noqa: E501

        Unique reference number assigned by the gateway that identifies the transaction on both platforms.  **Note:** Clients must be able to store this value in order to eventually perform follow up operation on existing transactions.  # noqa: E501

        :return: The unique_reference of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._unique_reference

    @unique_reference.setter
    def unique_reference(self, unique_reference):
        """Sets the unique_reference of this TransactionCompact.

        Unique reference number assigned by the gateway that identifies the transaction on both platforms.  **Note:** Clients must be able to store this value in order to eventually perform follow up operation on existing transactions.  # noqa: E501

        :param unique_reference: The unique_reference of this TransactionCompact.  # noqa: E501
        :type: str
        """
        if unique_reference is None:
            raise ValueError("Invalid value for `unique_reference`, must not be `None`")  # noqa: E501

        self._unique_reference = unique_reference

    @property
    def terminal(self):
        """Gets the terminal of this TransactionCompact.  # noqa: E501

        The terminal number assigned by the gateway.  # noqa: E501

        :return: The terminal of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this TransactionCompact.

        The terminal number assigned by the gateway.  # noqa: E501

        :param terminal: The terminal of this TransactionCompact.  # noqa: E501
        :type: str
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def operator(self):
        """Gets the operator of this TransactionCompact.  # noqa: E501

        The operator who initiated the transaction.  # noqa: E501

        :return: The operator of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this TransactionCompact.

        The operator who initiated the transaction.  # noqa: E501

        :param operator: The operator of this TransactionCompact.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def order_id(self):
        """Gets the order_id of this TransactionCompact.  # noqa: E501

        A unique identifier for the order assigned by the merchant.  # noqa: E501

        :return: The order_id of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this TransactionCompact.

        A unique identifier for the order assigned by the merchant.  # noqa: E501

        :param order_id: The order_id of this TransactionCompact.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def date_time(self):
        """Gets the date_time of this TransactionCompact.  # noqa: E501

        The processing date and time of the transaction represented as per [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.  # noqa: E501

        :return: The date_time of this TransactionCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this TransactionCompact.

        The processing date and time of the transaction represented as per [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.  # noqa: E501

        :param date_time: The date_time of this TransactionCompact.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def description(self):
        """Gets the description of this TransactionCompact.  # noqa: E501

        A brief description of the transaction.  # noqa: E501

        :return: The description of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionCompact.

        A brief description of the transaction.  # noqa: E501

        :param description: The description of this TransactionCompact.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def customer_name(self):
        """Gets the customer_name of this TransactionCompact.  # noqa: E501

        The card or account holder's name.  # noqa: E501

        :return: The customer_name of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this TransactionCompact.

        The card or account holder's name.  # noqa: E501

        :param customer_name: The customer_name of this TransactionCompact.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def masked_pan(self):
        """Gets the masked_pan of this TransactionCompact.  # noqa: E501

        The masked primary account number.  # noqa: E501

        :return: The masked_pan of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._masked_pan

    @masked_pan.setter
    def masked_pan(self, masked_pan):
        """Sets the masked_pan of this TransactionCompact.

        The masked primary account number.  # noqa: E501

        :param masked_pan: The masked_pan of this TransactionCompact.  # noqa: E501
        :type: str
        """

        self._masked_pan = masked_pan

    @property
    def type(self):
        """Gets the type of this TransactionCompact.  # noqa: E501

        The type of the generated transaction.  # noqa: E501

        :return: The type of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionCompact.

        The type of the generated transaction.  # noqa: E501

        :param type: The type of this TransactionCompact.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def result_code(self):
        """Gets the result_code of this TransactionCompact.  # noqa: E501

        Our platform maps result codes sent by different payment processors into a smaller set of codes as shown below. The original result code may be available in the `processorResultCode` field.  - **A**: Approved / Authorized. - **D**: Declined / Not Authorized. - **E**: Accepted for later processing, but result currently unknown. - **P**: Only a portion of the original amount requested was authorized. - **R**: Issuer has declined the transaction and indicated that the customer should contact their bank. - **C**: Issuer has declined the transaction and requested that the card be retained as it may have been reported as lost or stolen.  # noqa: E501

        :return: The result_code of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this TransactionCompact.

        Our platform maps result codes sent by different payment processors into a smaller set of codes as shown below. The original result code may be available in the `processorResultCode` field.  - **A**: Approved / Authorized. - **D**: Declined / Not Authorized. - **E**: Accepted for later processing, but result currently unknown. - **P**: Only a portion of the original amount requested was authorized. - **R**: Issuer has declined the transaction and indicated that the customer should contact their bank. - **C**: Issuer has declined the transaction and requested that the card be retained as it may have been reported as lost or stolen.  # noqa: E501

        :param result_code: The result_code of this TransactionCompact.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "D", "E", "P", "R", "C"]  # noqa: E501
        if result_code not in allowed_values:
            raise ValueError(
                "Invalid value for `result_code` ({0}), must be one of {1}"  # noqa: E501
                .format(result_code, allowed_values)
            )

        self._result_code = result_code

    @property
    def status(self):
        """Gets the status of this TransactionCompact.  # noqa: E501

        The current status of the generated transaction.  # noqa: E501

        :return: The status of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransactionCompact.

        The current status of the generated transaction.  # noqa: E501

        :param status: The status of this TransactionCompact.  # noqa: E501
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
    def currency(self):
        """Gets the currency of this TransactionCompact.  # noqa: E501

        The currency of the transaction. A 3-letter code as per the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) standard.  # noqa: E501

        :return: The currency of this TransactionCompact.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransactionCompact.

        The currency of the transaction. A 3-letter code as per the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) standard.  # noqa: E501

        :param currency: The currency of this TransactionCompact.  # noqa: E501
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
    def amount(self):
        """Gets the amount of this TransactionCompact.  # noqa: E501

        The amount authorized by the payment processor.  **Note:** For partial authorizations, this amount will be lower than the actual amount sent in the request.<br />**Note:** This amount will be negative for refund transactions to represent the return of settled funds back to the customer's account.  # noqa: E501

        :return: The amount of this TransactionCompact.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionCompact.

        The amount authorized by the payment processor.  **Note:** For partial authorizations, this amount will be lower than the actual amount sent in the request.<br />**Note:** This amount will be negative for refund transactions to represent the return of settled funds back to the customer's account.  # noqa: E501

        :param amount: The amount of this TransactionCompact.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def links(self):
        """Gets the links of this TransactionCompact.  # noqa: E501

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :return: The links of this TransactionCompact.  # noqa: E501
        :rtype: list[HypermediaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TransactionCompact.

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :param links: The links of this TransactionCompact.  # noqa: E501
        :type: list[HypermediaLink]
        """

        self._links = links
