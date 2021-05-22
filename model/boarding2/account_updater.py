# coding: utf-8
from model.serializable import SwaggerSerializable


class AccountUpdater(SwaggerSerializable):
    swagger_types = {
        'enable_vau': 'bool',
        'vau_type': 'str',
        'vau_merchant_id': 'str',
        'enable_abu': 'bool',
        'abu_type': 'str',
        'abu_merchant_id': 'str',
        'enable_background_notifications': 'bool',
        'enable_background_notifications_for_failures': 'bool',
        'background_notifications_url': 'str'
    }

    attribute_map = {
        'enable_vau': 'enableVau',
        'vau_type': 'vauType',
        'vau_merchant_id': 'vauMerchantId',
        'enable_abu': 'enableAbu',
        'abu_type': 'abuType',
        'abu_merchant_id': 'abuMerchantId',
        'enable_background_notifications': 'enableBackgroundNotifications',
        'enable_background_notifications_for_failures': 'enableBackgroundNotificationsForFailures',
        'background_notifications_url': 'backgroundNotificationsUrl'
    }

    def __init__(self, enable_vau=False, vau_type=None, vau_merchant_id=None, enable_abu=False, abu_type=None, abu_merchant_id=None, enable_background_notifications=False, enable_background_notifications_for_failures=False, background_notifications_url=None):  # noqa: E501
        """AccountUpdater - a model defined in Swagger"""  # noqa: E501
        self._enable_vau = None
        self._vau_type = None
        self._vau_merchant_id = None
        self._enable_abu = None
        self._abu_type = None
        self._abu_merchant_id = None
        self._enable_background_notifications = None
        self._enable_background_notifications_for_failures = None
        self._background_notifications_url = None
        self.discriminator = None
        if enable_vau is not None:
            self.enable_vau = enable_vau
        if vau_type is not None:
            self.vau_type = vau_type
        if vau_merchant_id is not None:
            self.vau_merchant_id = vau_merchant_id
        if enable_abu is not None:
            self.enable_abu = enable_abu
        if abu_type is not None:
            self.abu_type = abu_type
        if abu_merchant_id is not None:
            self.abu_merchant_id = abu_merchant_id
        if enable_background_notifications is not None:
            self.enable_background_notifications = enable_background_notifications
        if enable_background_notifications_for_failures is not None:
            self.enable_background_notifications_for_failures = enable_background_notifications_for_failures
        if background_notifications_url is not None:
            self.background_notifications_url = background_notifications_url

    @property
    def enable_vau(self):
        return self._enable_vau

    @enable_vau.setter
    def enable_vau(self, enable_vau):
        self._enable_vau = enable_vau

    @property
    def vau_type(self):
        return self._vau_type

    @vau_type.setter
    def vau_type(self, vau_type):
        allowed_values = ["GLOBAL_VAU", "ELAVONPOS_VAU"]  # noqa: E501
        if vau_type not in allowed_values:
            raise ValueError(
                "Invalid value for `vau_type` ({0}), must be one of {1}"  # noqa: E501
                .format(vau_type, allowed_values)
            )

        self._vau_type = vau_type

    @property
    def vau_merchant_id(self):
        return self._vau_merchant_id

    @vau_merchant_id.setter
    def vau_merchant_id(self, vau_merchant_id):
        self._vau_merchant_id = vau_merchant_id

    @property
    def enable_abu(self):
        return self._enable_abu

    @enable_abu.setter
    def enable_abu(self, enable_abu):
        self._enable_abu = enable_abu

    @property
    def abu_type(self):
        return self._abu_type

    @abu_type.setter
    def abu_type(self, abu_type):
        allowed_values = ["GLOBAL_ABU", "ELAVONPOS_ABU"]
        if abu_type not in allowed_values:
            raise ValueError(
                "Invalid value for `abu_type` ({0}), must be one of {1}"
                .format(abu_type, allowed_values)
            )

        self._abu_type = abu_type

    @property
    def abu_merchant_id(self):
        return self._abu_merchant_id

    @abu_merchant_id.setter
    def abu_merchant_id(self, abu_merchant_id):
        self._abu_merchant_id = abu_merchant_id

    @property
    def enable_background_notifications(self):
        return self._enable_background_notifications

    @enable_background_notifications.setter
    def enable_background_notifications(self, enable_background_notifications):
        self._enable_background_notifications = enable_background_notifications

    @property
    def enable_background_notifications_for_failures(self):
        return self._enable_background_notifications_for_failures

    @enable_background_notifications_for_failures.setter
    def enable_background_notifications_for_failures(self, enable_background_notifications_for_failures):
        self._enable_background_notifications_for_failures = enable_background_notifications_for_failures

    @property
    def background_notifications_url(self):
        return self._background_notifications_url

    @background_notifications_url.setter
    def background_notifications_url(self, background_notifications_url):
        self._background_notifications_url = background_notifications_url
