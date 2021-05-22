# coding: utf-8


from model.rest2.payment_request import PaymentRequest
from model.serializable import SwaggerSerializable


class MotoPaymentRequest(SwaggerSerializable):
    swagger_types = {
        'channel': 'str',
        'terminal': 'str',
        'operator': 'str',
        'order': 'Order',
        'customer': 'Customer',
        'customer_account': 'Payload',
        'credential_on_file': 'CredentialOnFile',
        'ip_address': 'IpAddress',
        'auto_capture': 'bool',
        'process_as_sale': 'bool',
        'offline_processing': 'OfflineProcessing',
        'additional_data_fields': 'list[CustomField]'
    }
    if hasattr(PaymentRequest, "swagger_types"):
        swagger_types.update(PaymentRequest.swagger_types)

    attribute_map = {
        'channel': 'channel',
        'terminal': 'terminal',
        'operator': 'operator',
        'order': 'order',
        'customer': 'customer',
        'customer_account': 'customerAccount',
        'credential_on_file': 'credentialOnFile',
        'ip_address': 'ipAddress',
        'auto_capture': 'autoCapture',
        'process_as_sale': 'processAsSale',
        'offline_processing': 'offlineProcessing',
        'additional_data_fields': 'additionalDataFields'
    }
    if hasattr(PaymentRequest, "attribute_map"):
        attribute_map.update(PaymentRequest.attribute_map)

    def __init__(self, channel=None, terminal=None, operator=None, order=None, customer=None, customer_account=None, credential_on_file=None, ip_address=None, auto_capture=True, process_as_sale=False, offline_processing=None, additional_data_fields=None, *args, **kwargs):  # noqa: E501
        """MotoPaymentRequest - a model defined in Swagger"""  # noqa: E501
        self._channel = None
        self._terminal = None
        self._operator = None
        self._order = None
        self._customer = None
        self._customer_account = None
        self._credential_on_file = None
        self._ip_address = None
        self._auto_capture = None
        self._process_as_sale = None
        self._offline_processing = None
        self._additional_data_fields = None
        self.discriminator = None
        if channel is not None:
            self.channel = channel
        self.terminal = terminal
        if operator is not None:
            self.operator = operator
        self.order = order
        if customer is not None:
            self.customer = customer
        self.customer_account = customer_account
        if credential_on_file is not None:
            self.credential_on_file = credential_on_file
        if ip_address is not None:
            self.ip_address = ip_address
        if auto_capture is not None:
            self.auto_capture = auto_capture
        if process_as_sale is not None:
            self.process_as_sale = process_as_sale
        if offline_processing is not None:
            self.offline_processing = offline_processing
        if additional_data_fields is not None:
            self.additional_data_fields = additional_data_fields

    @property
    def channel(self):
        """Gets the channel of this MotoPaymentRequest.  # noqa: E501


        :return: The channel of this MotoPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this MotoPaymentRequest.


        :param channel: The channel of this MotoPaymentRequest.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def terminal(self):
        """Gets the terminal of this MotoPaymentRequest.  # noqa: E501

        The terminal number assigned by the gateway.  # noqa: E501

        :return: The terminal of this MotoPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this MotoPaymentRequest.

        The terminal number assigned by the gateway.  # noqa: E501

        :param terminal: The terminal of this MotoPaymentRequest.  # noqa: E501
        :type: str
        """
        self._terminal = terminal

    @property
    def operator(self):
        """Gets the operator of this MotoPaymentRequest.  # noqa: E501

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :return: The operator of this MotoPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this MotoPaymentRequest.

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :param operator: The operator of this MotoPaymentRequest.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def order(self):
        """Gets the order of this MotoPaymentRequest.  # noqa: E501


        :return: The order of this MotoPaymentRequest.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this MotoPaymentRequest.


        :param order: The order of this MotoPaymentRequest.  # noqa: E501
        :type: Order
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

    @property
    def customer(self):
        """Gets the customer of this MotoPaymentRequest.  # noqa: E501


        :return: The customer of this MotoPaymentRequest.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this MotoPaymentRequest.


        :param customer: The customer of this MotoPaymentRequest.  # noqa: E501
        :type: Customer
        """

        self._customer = customer

    @property
    def customer_account(self):
        """Gets the customer_account of this MotoPaymentRequest.  # noqa: E501


        :return: The customer_account of this MotoPaymentRequest.  # noqa: E501
        :rtype: Payload
        """
        return self._customer_account

    @customer_account.setter
    def customer_account(self, customer_account):
        """Sets the customer_account of this MotoPaymentRequest.


        :param customer_account: The customer_account of this MotoPaymentRequest.  # noqa: E501
        :type: Payload
        """
        if customer_account is None:
            raise ValueError("Invalid value for `customer_account`, must not be `None`")  # noqa: E501

        self._customer_account = customer_account

    @property
    def credential_on_file(self):
        """Gets the credential_on_file of this MotoPaymentRequest.  # noqa: E501


        :return: The credential_on_file of this MotoPaymentRequest.  # noqa: E501
        :rtype: CredentialOnFile
        """
        return self._credential_on_file

    @credential_on_file.setter
    def credential_on_file(self, credential_on_file):
        """Sets the credential_on_file of this MotoPaymentRequest.


        :param credential_on_file: The credential_on_file of this MotoPaymentRequest.  # noqa: E501
        :type: CredentialOnFile
        """

        self._credential_on_file = credential_on_file

    @property
    def ip_address(self):
        """Gets the ip_address of this MotoPaymentRequest.  # noqa: E501


        :return: The ip_address of this MotoPaymentRequest.  # noqa: E501
        :rtype: IpAddress
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this MotoPaymentRequest.


        :param ip_address: The ip_address of this MotoPaymentRequest.  # noqa: E501
        :type: IpAddress
        """

        self._ip_address = ip_address

    @property
    def auto_capture(self):
        """Gets the auto_capture of this MotoPaymentRequest.  # noqa: E501

        It indicates whether the amount of the transaction should be automatically and fully captured.  - `true` : the gateway will automatically set the transaction to `READY` making it eligible for the next settlement run. - `false`: a pre-authorization will be performed if your account has the \"Allow Pre-Auth\" feature enabled. Otherwise, a regular transaction will be created with `PENDING` status. Either way, an additional call to the [Capture a Payment](#operation/capturePayment) operation is required to capture the final amount and flag the transaction as ready for the next settlement run.  # noqa: E501

        :return: The auto_capture of this MotoPaymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_capture

    @auto_capture.setter
    def auto_capture(self, auto_capture):
        """Sets the auto_capture of this MotoPaymentRequest.

        It indicates whether the amount of the transaction should be automatically and fully captured.  - `true` : the gateway will automatically set the transaction to `READY` making it eligible for the next settlement run. - `false`: a pre-authorization will be performed if your account has the \"Allow Pre-Auth\" feature enabled. Otherwise, a regular transaction will be created with `PENDING` status. Either way, an additional call to the [Capture a Payment](#operation/capturePayment) operation is required to capture the final amount and flag the transaction as ready for the next settlement run.  # noqa: E501

        :param auto_capture: The auto_capture of this MotoPaymentRequest.  # noqa: E501
        :type: bool
        """

        self._auto_capture = auto_capture

    @property
    def process_as_sale(self):
        """Gets the process_as_sale of this MotoPaymentRequest.  # noqa: E501

        Indicates whether the transaction should be processed as a Sale. A Sale transaction is characterized by its `COMPLETE` status due to the fact that authorization and settlement operations are performed at the same time. This means that this kind of transaction is not subject to changes or late adjustments even while sitting in the open batch.  **Note:** The `autoCapture` indicator must be set to TRUE to process a Sale.  # noqa: E501

        :return: The process_as_sale of this MotoPaymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._process_as_sale

    @process_as_sale.setter
    def process_as_sale(self, process_as_sale):
        """Sets the process_as_sale of this MotoPaymentRequest.

        Indicates whether the transaction should be processed as a Sale. A Sale transaction is characterized by its `COMPLETE` status due to the fact that authorization and settlement operations are performed at the same time. This means that this kind of transaction is not subject to changes or late adjustments even while sitting in the open batch.  **Note:** The `autoCapture` indicator must be set to TRUE to process a Sale.  # noqa: E501

        :param process_as_sale: The process_as_sale of this MotoPaymentRequest.  # noqa: E501
        :type: bool
        """

        self._process_as_sale = process_as_sale

    @property
    def offline_processing(self):
        """Gets the offline_processing of this MotoPaymentRequest.  # noqa: E501


        :return: The offline_processing of this MotoPaymentRequest.  # noqa: E501
        :rtype: OfflineProcessing
        """
        return self._offline_processing

    @offline_processing.setter
    def offline_processing(self, offline_processing):
        """Sets the offline_processing of this MotoPaymentRequest.


        :param offline_processing: The offline_processing of this MotoPaymentRequest.  # noqa: E501
        :type: OfflineProcessing
        """

        self._offline_processing = offline_processing

    @property
    def additional_data_fields(self):
        """Gets the additional_data_fields of this MotoPaymentRequest.  # noqa: E501

        List of custom fields which are used to add extra information to transactions. Their values are going to be stored and used for the requests sent to the terminal's receipt and validation webhooks.<br />For more information, visit the section [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters) of our knowledge base.  # noqa: E501

        :return: The additional_data_fields of this MotoPaymentRequest.  # noqa: E501
        :rtype: list[CustomField]
        """
        return self._additional_data_fields

    @additional_data_fields.setter
    def additional_data_fields(self, additional_data_fields):
        """Sets the additional_data_fields of this MotoPaymentRequest.

        List of custom fields which are used to add extra information to transactions. Their values are going to be stored and used for the requests sent to the terminal's receipt and validation webhooks.<br />For more information, visit the section [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters) of our knowledge base.  # noqa: E501

        :param additional_data_fields: The additional_data_fields of this MotoPaymentRequest.  # noqa: E501
        :type: list[CustomField]
        """

        self._additional_data_fields = additional_data_fields
