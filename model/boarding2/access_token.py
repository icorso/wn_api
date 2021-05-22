# coding: utf-8
from model.serializable import SwaggerSerializable


class AccessToken(SwaggerSerializable):
    swagger_types = {
        'audience': 'str',
        'bound_to': 'str',
        'enable_hypermedia': 'bool',
        'token_type': 'str',
        'token': 'str',
        'issued_at': 'datetime',
        'expires_in': 'int',
        'roles': 'list[str]'
    }

    attribute_map = {
        'audience': 'audience',
        'bound_to': 'boundTo',
        'enable_hypermedia': 'enableHypermedia',
        'token_type': 'tokenType',
        'token': 'token',
        'issued_at': 'issuedAt',
        'expires_in': 'expiresIn',
        'roles': 'roles'
    }

    def __init__(self, audience=None, bound_to=None, enable_hypermedia=None, token_type=None, token=None, issued_at=None, expires_in=None, roles=None):  # noqa: E501
        """AccessToken - a model defined in Swagger"""  # noqa: E501
        self._audience = None
        self._bound_to = None
        self._enable_hypermedia = None
        self._token_type = None
        self._token = None
        self._issued_at = None
        self._expires_in = None
        self._roles = None
        self.discriminator = None
        self.audience = audience
        self.bound_to = bound_to
        self.enable_hypermedia = enable_hypermedia
        self.token_type = token_type
        self.token = token
        self.issued_at = issued_at
        self.expires_in = expires_in
        if roles is not None:
            self.roles = roles

    @property
    def audience(self):
        """Gets the audience of this AccessToken.  # noqa: E501


        :return: The audience of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this AccessToken.


        :param audience: The audience of this AccessToken.  # noqa: E501
        :type: str
        """
        if audience is None:
            raise ValueError("Invalid value for `audience`, must not be `None`")  # noqa: E501

        self._audience = audience

    @property
    def bound_to(self):
        """Gets the bound_to of this AccessToken.  # noqa: E501


        :return: The bound_to of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._bound_to

    @bound_to.setter
    def bound_to(self, bound_to):
        """Sets the bound_to of this AccessToken.


        :param bound_to: The bound_to of this AccessToken.  # noqa: E501
        :type: str
        """
        if bound_to is None:
            raise ValueError("Invalid value for `bound_to`, must not be `None`")  # noqa: E501

        self._bound_to = bound_to

    @property
    def enable_hypermedia(self):
        """Gets the enable_hypermedia of this AccessToken.  # noqa: E501


        :return: The enable_hypermedia of this AccessToken.  # noqa: E501
        :rtype: bool
        """
        return self._enable_hypermedia

    @enable_hypermedia.setter
    def enable_hypermedia(self, enable_hypermedia):
        """Sets the enable_hypermedia of this AccessToken.


        :param enable_hypermedia: The enable_hypermedia of this AccessToken.  # noqa: E501
        :type: bool
        """
        if enable_hypermedia is None:
            raise ValueError("Invalid value for `enable_hypermedia`, must not be `None`")  # noqa: E501

        self._enable_hypermedia = enable_hypermedia

    @property
    def token_type(self):
        """Gets the token_type of this AccessToken.  # noqa: E501


        :return: The token_type of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this AccessToken.


        :param token_type: The token_type of this AccessToken.  # noqa: E501
        :type: str
        """
        if token_type is None:
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501

        self._token_type = token_type

    @property
    def token(self):
        """Gets the token of this AccessToken.  # noqa: E501


        :return: The token of this AccessToken.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AccessToken.


        :param token: The token of this AccessToken.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def issued_at(self):
        """Gets the issued_at of this AccessToken.  # noqa: E501

        Exact date and time that the token was issued represented as per [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.  **Note:** This field has been deprecated. You should rely exclusively on the `expiresIn` field when implementing your authentication logic.  # noqa: E501

        :return: The issued_at of this AccessToken.  # noqa: E501
        :rtype: datetime
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        """Sets the issued_at of this AccessToken.

        Exact date and time that the token was issued represented as per [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.  **Note:** This field has been deprecated. You should rely exclusively on the `expiresIn` field when implementing your authentication logic.  # noqa: E501

        :param issued_at: The issued_at of this AccessToken.  # noqa: E501
        :type: datetime
        """
        if issued_at is None:
            raise ValueError("Invalid value for `issued_at`, must not be `None`")  # noqa: E501

        self._issued_at = issued_at

    @property
    def expires_in(self):
        """Gets the expires_in of this AccessToken.  # noqa: E501


        :return: The expires_in of this AccessToken.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this AccessToken.


        :param expires_in: The expires_in of this AccessToken.  # noqa: E501
        :type: int
        """
        if expires_in is None:
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

    @property
    def roles(self):
        """Gets the roles of this AccessToken.  # noqa: E501


        :return: The roles of this AccessToken.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AccessToken.


        :param roles: The roles of this AccessToken.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles
