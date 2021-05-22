# coding: utf-8
from model.serializable import SwaggerSerializable


class CardVolumeLimit(SwaggerSerializable):
    swagger_types = {
        'limit_scope': 'str',
        'limit_threshold': 'int',
        'without_cvv_only': 'bool',
        'without_avs_only': 'bool',
        'current_value': 'float'
    }

    attribute_map = {
        'limit_scope': 'limitScope',
        'limit_threshold': 'limitThreshold',
        'without_cvv_only': 'withoutCvvOnly',
        'without_avs_only': 'withoutAvsOnly',
        'current_value': 'currentValue'
    }

    def __init__(self, limit_scope=None, limit_threshold=None, without_cvv_only=None, without_avs_only=None, current_value=None):  # noqa: E501
        """CardVolumeLimit - a model defined in Swagger"""  # noqa: E501
        self._limit_scope = None
        self._limit_threshold = None
        self._without_cvv_only = None
        self._without_avs_only = None
        self._current_value = None
        self.discriminator = None
        self.limit_scope = limit_scope
        self.limit_threshold = limit_threshold
        if without_cvv_only is not None:
            self.without_cvv_only = without_cvv_only
        if without_avs_only is not None:
            self.without_avs_only = without_avs_only
        if current_value is not None:
            self.current_value = current_value

    @property
    def limit_scope(self):
        """Gets the limit_scope of this CardVolumeLimit.  # noqa: E501


        :return: The limit_scope of this CardVolumeLimit.  # noqa: E501
        :rtype: str
        """
        return self._limit_scope

    @limit_scope.setter
    def limit_scope(self, limit_scope):
        """Sets the limit_scope of this CardVolumeLimit.


        :param limit_scope: The limit_scope of this CardVolumeLimit.  # noqa: E501
        :type: str
        """
        if limit_scope is None:
            raise ValueError("Invalid value for `limit_scope`, must not be `None`")  # noqa: E501
        allowed_values = ["DAILY", "MONTHLY", "SINGLE_TRANSACTION"]  # noqa: E501
        if limit_scope not in allowed_values:
            raise ValueError(
                "Invalid value for `limit_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(limit_scope, allowed_values)
            )

        self._limit_scope = limit_scope

    @property
    def limit_threshold(self):
        """Gets the limit_threshold of this CardVolumeLimit.  # noqa: E501

        The maximum amount allowed within the period described in the `limitScope` attribute.  # noqa: E501

        :return: The limit_threshold of this CardVolumeLimit.  # noqa: E501
        :rtype: int
        """
        return self._limit_threshold

    @limit_threshold.setter
    def limit_threshold(self, limit_threshold):
        """Sets the limit_threshold of this CardVolumeLimit.

        The maximum amount allowed within the period described in the `limitScope` attribute.  # noqa: E501

        :param limit_threshold: The limit_threshold of this CardVolumeLimit.  # noqa: E501
        :type: int
        """
        if limit_threshold is None:
            raise ValueError("Invalid value for `limit_threshold`, must not be `None`")  # noqa: E501

        self._limit_threshold = limit_threshold

    @property
    def without_cvv_only(self):
        """Gets the without_cvv_only of this CardVolumeLimit.  # noqa: E501

        If enabled, the limit will only take transactions without CVV into account. This is specially useful for merchants who are looking for a way to add thresholds for transactions that may lead to chargebacks.<br />This filter only applies to limits within `SINGLE_TRANSACTION` scope.  # noqa: E501

        :return: The without_cvv_only of this CardVolumeLimit.  # noqa: E501
        :rtype: bool
        """
        return self._without_cvv_only

    @without_cvv_only.setter
    def without_cvv_only(self, without_cvv_only):
        """Sets the without_cvv_only of this CardVolumeLimit.

        If enabled, the limit will only take transactions without CVV into account. This is specially useful for merchants who are looking for a way to add thresholds for transactions that may lead to chargebacks.<br />This filter only applies to limits within `SINGLE_TRANSACTION` scope.  # noqa: E501

        :param without_cvv_only: The without_cvv_only of this CardVolumeLimit.  # noqa: E501
        :type: bool
        """

        self._without_cvv_only = without_cvv_only

    @property
    def without_avs_only(self):
        """Gets the without_avs_only of this CardVolumeLimit.  # noqa: E501

        If enabled, the limit will only take transactions without AVS into account. This is specially useful for merchants who are looking for a way to add thresholds for transactions that may lead to chargebacks.<br />This filter only applies to limits within `SINGLE_TRANSACTION` scope.  # noqa: E501

        :return: The without_avs_only of this CardVolumeLimit.  # noqa: E501
        :rtype: bool
        """
        return self._without_avs_only

    @without_avs_only.setter
    def without_avs_only(self, without_avs_only):
        """Sets the without_avs_only of this CardVolumeLimit.

        If enabled, the limit will only take transactions without AVS into account. This is specially useful for merchants who are looking for a way to add thresholds for transactions that may lead to chargebacks.<br />This filter only applies to limits within `SINGLE_TRANSACTION` scope.  # noqa: E501

        :param without_avs_only: The without_avs_only of this CardVolumeLimit.  # noqa: E501
        :type: bool
        """

        self._without_avs_only = without_avs_only

    @property
    def current_value(self):
        """Gets the current_value of this CardVolumeLimit.  # noqa: E501

        The sum of all transactions performed with the `card` within the period described in the `limitScope` attribute.<br />At the end of each period, this value is reset.  # noqa: E501

        :return: The current_value of this CardVolumeLimit.  # noqa: E501
        :rtype: float
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """Sets the current_value of this CardVolumeLimit.

        The sum of all transactions performed with the `card` within the period described in the `limitScope` attribute.<br />At the end of each period, this value is reset.  # noqa: E501

        :param current_value: The current_value of this CardVolumeLimit.  # noqa: E501
        :type: float
        """

        self._current_value = current_value
