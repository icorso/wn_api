# coding: utf-8

from model.serializable import SwaggerSerializable


class AccessToken(SwaggerSerializable):
    swagger_types = {
        'audience': 'str',
        'bound_to': 'str',
        'token_type': 'str',
        'token': 'str',
        'expires_in': 'int',
        'enable_receipts': 'bool',
        'enable_hypermedia': 'bool',
        'roles': 'list[str]',
        'allowed_terminals': 'list[str]'
    }

    attribute_map = {
        'audience': 'audience',
        'bound_to': 'boundTo',
        'token_type': 'tokenType',
        'token': 'token',
        'expires_in': 'expiresIn',
        'enable_receipts': 'enableReceipts',
        'enable_hypermedia': 'enableHypermedia',
        'roles': 'roles',
        'allowed_terminals': 'allowedTerminals'
    }

    def __init__(self, audience=None, bound_to=None, token_type=None, token=None, expires_in=None, enable_receipts=None, enable_hypermedia=None, roles=None, allowed_terminals=None):  # noqa: E501
        self._audience = None
        self._bound_to = None
        self._token_type = None
        self._token = None
        self._expires_in = None
        self._enable_receipts = None
        self._enable_hypermedia = None
        self._roles = None
        self._allowed_terminals = None
        self.discriminator = None
        self.audience = audience
        self.bound_to = bound_to
        self.token_type = token_type
        self.token = token
        self.expires_in = expires_in
        self.enable_receipts = enable_receipts
        self.enable_hypermedia = enable_hypermedia
        if roles is not None:
            self.roles = roles
        if allowed_terminals is not None:
            self.allowed_terminals = allowed_terminals

    @property
    def audience(self):
        return self._audience

    @audience.setter
    def audience(self, audience):
        self._audience = audience

    @property
    def bound_to(self):
        return self._bound_to

    @bound_to.setter
    def bound_to(self, bound_to):
        self._bound_to = bound_to

    @property
    def token_type(self):
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        self._token_type = token_type

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def expires_in(self):
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        self._expires_in = expires_in

    @property
    def enable_receipts(self):
        return self._enable_receipts

    @enable_receipts.setter
    def enable_receipts(self, enable_receipts):
        self._enable_receipts = enable_receipts

    @property
    def enable_hypermedia(self):
        return self._enable_hypermedia

    @enable_hypermedia.setter
    def enable_hypermedia(self, enable_hypermedia):
        self._enable_hypermedia = enable_hypermedia

    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, roles):
        self._roles = roles

    @property
    def allowed_terminals(self):
        return self._allowed_terminals

    @allowed_terminals.setter
    def allowed_terminals(self, allowed_terminals):
        self._allowed_terminals = allowed_terminals
