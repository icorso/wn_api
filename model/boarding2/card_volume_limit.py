# coding: utf-8


import six

from model.serializable import SwaggerSerializable


class CardVolumeLimit(SwaggerSerializable):
    swagger_types = {
        'limit_threshold': 'int',
        'limit_scope': 'str',
        'current_value': 'float',
        'without_cvv_only': 'bool',
        'without_avs_only': 'bool'
    }

    attribute_map = {
        'limit_threshold': 'limitThreshold',
        'limit_scope': 'limitScope',
        'current_value': 'currentValue',
        'without_cvv_only': 'withoutCvvOnly',
        'without_avs_only': 'withoutAvsOnly'
    }

    def __init__(self, limit_threshold=None, limit_scope=None, current_value=None, without_cvv_only=None, without_avs_only=None):
        self._limit_threshold = None
        self._limit_scope = None
        self._current_value = None
        self._without_cvv_only = None
        self._without_avs_only = None
        self.discriminator = None
        self.limit_threshold = limit_threshold
        self.limit_scope = limit_scope
        if current_value is not None:
            self.current_value = current_value
        if without_cvv_only is not None:
            self.without_cvv_only = without_cvv_only
        if without_avs_only is not None:
            self.without_avs_only = without_avs_only

    @property
    def limit_threshold(self):
        return self._limit_threshold

    @limit_threshold.setter
    def limit_threshold(self, limit_threshold):
        if limit_threshold is None:
            raise ValueError("Invalid value for `limit_threshold`, must not be `None`")  # noqa: E501

        self._limit_threshold = limit_threshold

    @property
    def limit_scope(self):
        return self._limit_scope

    @limit_scope.setter
    def limit_scope(self, limit_scope):
        if limit_scope is None:
            raise ValueError("Invalid value for `limit_scope`, must not be `None`")
        allowed_values = ["DAILY", "MONTHLY", "SINGLE_TRANSACTION"]
        if limit_scope not in allowed_values:
            raise ValueError(
                "Invalid value for `limit_scope` ({0}), must be one of {1}"
                .format(limit_scope, allowed_values)
            )

        self._limit_scope = limit_scope

    @property
    def current_value(self):
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        self._current_value = current_value

    @property
    def without_cvv_only(self):
        return self._without_cvv_only

    @without_cvv_only.setter
    def without_cvv_only(self, without_cvv_only):
        self._without_cvv_only = without_cvv_only

    @property
    def without_avs_only(self):
        return self._without_avs_only

    @without_avs_only.setter
    def without_avs_only(self, without_avs_only):
        self._without_avs_only = without_avs_only

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CardVolumeLimit, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def __eq__(self, other):
        if not isinstance(other, CardVolumeLimit):
            return False

        return self.__dict__ == other.__dict__
