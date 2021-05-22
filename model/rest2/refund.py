# coding: utf-8

from model.serializable import SwaggerSerializable


class Refund(SwaggerSerializable):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'unique_reference': 'str',
        'terminal': 'str',
        'operator': 'str',
        'order_id': 'str',
        'refund_reason': 'str',
        'customer_account': 'CustomerAccount',
        'security_check': 'SecurityCheck',
        'transaction_result': 'TransactionResult',
        'additional_data_fields': 'list[CustomField]',
        'emv_tags': 'list[EmvTag]',
        'receipts': 'list[TransactionReceipt]',
        'links': 'list[HypermediaLink]'
    }

    attribute_map = {
        'unique_reference': 'uniqueReference',
        'terminal': 'terminal',
        'operator': 'operator',
        'order_id': 'orderId',
        'refund_reason': 'refundReason',
        'customer_account': 'customerAccount',
        'security_check': 'securityCheck',
        'transaction_result': 'transactionResult',
        'additional_data_fields': 'additionalDataFields',
        'emv_tags': 'emvTags',
        'receipts': 'receipts',
        'links': 'links'
    }

    def __init__(self, unique_reference=None, terminal=None, operator=None, order_id=None, refund_reason=None, customer_account=None, security_check=None, transaction_result=None, additional_data_fields=None, emv_tags=None, receipts=None, links=None):  # noqa: E501
        """Refund - a model defined in Swagger"""  # noqa: E501
        self._unique_reference = None
        self._terminal = None
        self._operator = None
        self._order_id = None
        self._refund_reason = None
        self._customer_account = None
        self._security_check = None
        self._transaction_result = None
        self._additional_data_fields = None
        self._emv_tags = None
        self._receipts = None
        self._links = None
        self.discriminator = None
        self.unique_reference = unique_reference
        self.terminal = terminal
        if operator is not None:
            self.operator = operator
        self.order_id = order_id
        self.refund_reason = refund_reason
        self.customer_account = customer_account
        if security_check is not None:
            self.security_check = security_check
        if transaction_result is not None:
            self.transaction_result = transaction_result
        if additional_data_fields is not None:
            self.additional_data_fields = additional_data_fields
        if emv_tags is not None:
            self.emv_tags = emv_tags
        if receipts is not None:
            self.receipts = receipts
        if links is not None:
            self.links = links

    @property
    def unique_reference(self):
        """Gets the unique_reference of this Refund.  # noqa: E501

        Unique reference number assigned by the gateway that identifies the transaction on both platforms.  **Note:** Clients must be able to store this value in order to eventually perform follow up operation on existing transactions.  # noqa: E501

        :return: The unique_reference of this Refund.  # noqa: E501
        :rtype: str
        """
        return self._unique_reference

    @unique_reference.setter
    def unique_reference(self, unique_reference):
        """Sets the unique_reference of this Refund.

        Unique reference number assigned by the gateway that identifies the transaction on both platforms.  **Note:** Clients must be able to store this value in order to eventually perform follow up operation on existing transactions.  # noqa: E501

        :param unique_reference: The unique_reference of this Refund.  # noqa: E501
        :type: str
        """
        if unique_reference is None:
            raise ValueError("Invalid value for `unique_reference`, must not be `None`")  # noqa: E501

        self._unique_reference = unique_reference

    @property
    def terminal(self):
        """Gets the terminal of this Refund.  # noqa: E501

        The terminal number assigned by the gateway.  # noqa: E501

        :return: The terminal of this Refund.  # noqa: E501
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this Refund.

        The terminal number assigned by the gateway.  # noqa: E501

        :param terminal: The terminal of this Refund.  # noqa: E501
        :type: str
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def operator(self):
        """Gets the operator of this Refund.  # noqa: E501

        The operator who initiated the transaction.  # noqa: E501

        :return: The operator of this Refund.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Refund.

        The operator who initiated the transaction.  # noqa: E501

        :param operator: The operator of this Refund.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def order_id(self):
        """Gets the order_id of this Refund.  # noqa: E501

        A unique identifier for the order assigned by the merchant.  # noqa: E501

        :return: The order_id of this Refund.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Refund.

        A unique identifier for the order assigned by the merchant.  # noqa: E501

        :param order_id: The order_id of this Refund.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def refund_reason(self):
        """Gets the refund_reason of this Refund.  # noqa: E501

        The reason why the transaction is being refunded.  # noqa: E501

        :return: The refund_reason of this Refund.  # noqa: E501
        :rtype: str
        """
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, refund_reason):
        """Sets the refund_reason of this Refund.

        The reason why the transaction is being refunded.  # noqa: E501

        :param refund_reason: The refund_reason of this Refund.  # noqa: E501
        :type: str
        """
        if refund_reason is None:
            raise ValueError("Invalid value for `refund_reason`, must not be `None`")  # noqa: E501

        self._refund_reason = refund_reason

    @property
    def customer_account(self):
        """Gets the customer_account of this Refund.  # noqa: E501


        :return: The customer_account of this Refund.  # noqa: E501
        :rtype: CustomerAccount
        """
        return self._customer_account

    @customer_account.setter
    def customer_account(self, customer_account):
        """Sets the customer_account of this Refund.


        :param customer_account: The customer_account of this Refund.  # noqa: E501
        :type: CustomerAccount
        """
        if customer_account is None:
            raise ValueError("Invalid value for `customer_account`, must not be `None`")  # noqa: E501

        self._customer_account = customer_account

    @property
    def security_check(self):
        """Gets the security_check of this Refund.  # noqa: E501


        :return: The security_check of this Refund.  # noqa: E501
        :rtype: SecurityCheck
        """
        return self._security_check

    @security_check.setter
    def security_check(self, security_check):
        """Sets the security_check of this Refund.


        :param security_check: The security_check of this Refund.  # noqa: E501
        :type: SecurityCheck
        """

        self._security_check = security_check

    @property
    def transaction_result(self):
        """Gets the transaction_result of this Refund.  # noqa: E501


        :return: The transaction_result of this Refund.  # noqa: E501
        :rtype: TransactionResult
        """
        return self._transaction_result

    @transaction_result.setter
    def transaction_result(self, transaction_result):
        """Sets the transaction_result of this Refund.


        :param transaction_result: The transaction_result of this Refund.  # noqa: E501
        :type: TransactionResult
        """

        self._transaction_result = transaction_result

    @property
    def additional_data_fields(self):
        """Gets the additional_data_fields of this Refund.  # noqa: E501

        List of custom fields representing the additional information sent by the merchant and stored along with the transaction.  # noqa: E501

        :return: The additional_data_fields of this Refund.  # noqa: E501
        :rtype: list[CustomField]
        """
        return self._additional_data_fields

    @additional_data_fields.setter
    def additional_data_fields(self, additional_data_fields):
        """Sets the additional_data_fields of this Refund.

        List of custom fields representing the additional information sent by the merchant and stored along with the transaction.  # noqa: E501

        :param additional_data_fields: The additional_data_fields of this Refund.  # noqa: E501
        :type: list[CustomField]
        """

        self._additional_data_fields = additional_data_fields

    @property
    def emv_tags(self):
        """Gets the emv_tags of this Refund.  # noqa: E501

        List of tags returned for EMV transactions.  # noqa: E501

        :return: The emv_tags of this Refund.  # noqa: E501
        :rtype: list[EmvTag]
        """
        return self._emv_tags

    @emv_tags.setter
    def emv_tags(self, emv_tags):
        """Sets the emv_tags of this Refund.

        List of tags returned for EMV transactions.  # noqa: E501

        :param emv_tags: The emv_tags of this Refund.  # noqa: E501
        :type: list[EmvTag]
        """

        self._emv_tags = emv_tags

    @property
    def receipts(self):
        """Gets the receipts of this Refund.  # noqa: E501

        The customer and merchant receipt copies.  # noqa: E501

        :return: The receipts of this Refund.  # noqa: E501
        :rtype: list[TransactionReceipt]
        """
        return self._receipts

    @receipts.setter
    def receipts(self, receipts):
        """Sets the receipts of this Refund.

        The customer and merchant receipt copies.  # noqa: E501

        :param receipts: The receipts of this Refund.  # noqa: E501
        :type: list[TransactionReceipt]
        """

        self._receipts = receipts

    @property
    def links(self):
        """Gets the links of this Refund.  # noqa: E501

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :return: The links of this Refund.  # noqa: E501
        :rtype: list[HypermediaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Refund.

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :param links: The links of this Refund.  # noqa: E501
        :type: list[HypermediaLink]
        """

        self._links = links
