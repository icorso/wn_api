# coding: utf-8

from model.serializable import SwaggerSerializable


class SearchCredentialTransactionsRequest(SwaggerSerializable):
    swagger_types = {
        'terminal': 'str',
        'operator': 'str',
        'ip_address': 'IpAddress',
        'customer_account': 'Payload'
    }

    attribute_map = {
        'terminal': 'terminal',
        'operator': 'operator',
        'ip_address': 'ipAddress',
        'customer_account': 'customerAccount'
    }

    def __init__(self, terminal=None, operator=None, ip_address=None, customer_account=None):  # noqa: E501
        """SearchCredentialTransactionsRequest - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._operator = None
        self._ip_address = None
        self._customer_account = None
        self.discriminator = None
        self.terminal = terminal
        if operator is not None:
            self.operator = operator
        if ip_address is not None:
            self.ip_address = ip_address
        self.customer_account = customer_account

    @property
    def terminal(self):
        """Gets the terminal of this SearchCredentialTransactionsRequest.  # noqa: E501

        The terminal number assigned by the gateway. This field indicates the terminal that owns the credentials, even though, it is possible to share credentials with other terminals. See the *Secure Card* section in [Integration Settings](https://docs.worldnettps.com/doku.php?id=developer:important_integration_settings) for more details about secure credentials sharing feature.  # noqa: E501

        :return: The terminal of this SearchCredentialTransactionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this SearchCredentialTransactionsRequest.

        The terminal number assigned by the gateway. This field indicates the terminal that owns the credentials, even though, it is possible to share credentials with other terminals. See the *Secure Card* section in [Integration Settings](https://docs.worldnettps.com/doku.php?id=developer:important_integration_settings) for more details about secure credentials sharing feature.  # noqa: E501

        :param terminal: The terminal of this SearchCredentialTransactionsRequest.  # noqa: E501
        :type: str
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def operator(self):
        """Gets the operator of this SearchCredentialTransactionsRequest.  # noqa: E501

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :return: The operator of this SearchCredentialTransactionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SearchCredentialTransactionsRequest.

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :param operator: The operator of this SearchCredentialTransactionsRequest.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def ip_address(self):
        """Gets the ip_address of this SearchCredentialTransactionsRequest.  # noqa: E501


        :return: The ip_address of this SearchCredentialTransactionsRequest.  # noqa: E501
        :rtype: IpAddress
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this SearchCredentialTransactionsRequest.


        :param ip_address: The ip_address of this SearchCredentialTransactionsRequest.  # noqa: E501
        :type: IpAddress
        """

        self._ip_address = ip_address

    @property
    def customer_account(self):
        """Gets the customer_account of this SearchCredentialTransactionsRequest.  # noqa: E501


        :return: The customer_account of this SearchCredentialTransactionsRequest.  # noqa: E501
        :rtype: Payload
        """
        return self._customer_account

    @customer_account.setter
    def customer_account(self, customer_account):
        """Sets the customer_account of this SearchCredentialTransactionsRequest.


        :param customer_account: The customer_account of this SearchCredentialTransactionsRequest.  # noqa: E501
        :type: Payload
        """
        if customer_account is None:
            raise ValueError("Invalid value for `customer_account`, must not be `None`")  # noqa: E501

        self._customer_account = customer_account
