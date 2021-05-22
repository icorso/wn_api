# coding: utf-8

from model.serializable import SwaggerSerializable


class SecureCredentialsPayload(SwaggerSerializable):
    swagger_types = {
        'payload_type': 'str',
        'account_type': 'str',
        'credentials_number': 'str'
    }

    attribute_map = {
        'payload_type': 'payloadType',
        'account_type': 'accountType',
        'credentials_number': 'credentialsNumber'
    }

    def __init__(self, payload_type=None, account_type='CHECKING', credentials_number=None, *args, **kwargs):  # noqa: E501
        """SecureCredentialsPayload - a model defined in Swagger"""  # noqa: E501
        self._payload_type = None
        self._account_type = None
        self._credentials_number = None
        self.discriminator = None
        self.payload_type = payload_type
        if account_type is not None:
            self.account_type = account_type
        self.credentials_number = credentials_number

    @property
    def payload_type(self):
        """Gets the payload_type of this SecureCredentialsPayload.  # noqa: E501


        :return: The payload_type of this SecureCredentialsPayload.  # noqa: E501
        :rtype: str
        """
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type):
        """Sets the payload_type of this SecureCredentialsPayload.


        :param payload_type: The payload_type of this SecureCredentialsPayload.  # noqa: E501
        :type: str
        """
        if payload_type is None:
            raise ValueError("Invalid value for `payload_type`, must not be `None`")  # noqa: E501

        self._payload_type = payload_type

    @property
    def account_type(self):
        """Gets the account_type of this SecureCredentialsPayload.  # noqa: E501


        :return: The account_type of this SecureCredentialsPayload.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this SecureCredentialsPayload.


        :param account_type: The account_type of this SecureCredentialsPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["CHECKING", "SAVINGS"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def credentials_number(self):
        """Gets the credentials_number of this SecureCredentialsPayload.  # noqa: E501

        The unique number assigned by the gateway that should be used to reference the payment credentials when performing transactions.  # noqa: E501

        :return: The credentials_number of this SecureCredentialsPayload.  # noqa: E501
        :rtype: str
        """
        return self._credentials_number

    @credentials_number.setter
    def credentials_number(self, credentials_number):
        """Sets the credentials_number of this SecureCredentialsPayload.

        The unique number assigned by the gateway that should be used to reference the payment credentials when performing transactions.  # noqa: E501

        :param credentials_number: The credentials_number of this SecureCredentialsPayload.  # noqa: E501
        :type: str
        """
        if credentials_number is None:
            raise ValueError("Invalid value for `credentials_number`, must not be `None`")  # noqa: E501

        self._credentials_number = credentials_number
