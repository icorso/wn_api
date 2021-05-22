# coding: utf-8

from model.serializable import SwaggerSerializable


class MerchantLevelLimit(SwaggerSerializable):
    swagger_types = {
        'limit_threshold': 'int',
        'without_cvv_only': 'bool',
        'without_avs_only': 'bool',
        'limit_scope': 'str'
    }

    attribute_map = {
        'limit_threshold': 'limitThreshold',
        'without_cvv_only': 'withoutCvvOnly',
        'without_avs_only': 'withoutAvsOnly',
        'limit_scope': 'limitScope'
    }

    def __init__(self, limit_threshold=None, without_cvv_only=None, without_avs_only=None, limit_scope=None):  # noqa: E501
        """MerchantLevelLimit - a model defined in Swagger"""  # noqa: E501
        self._limit_threshold = None
        self._without_cvv_only = None
        self._without_avs_only = None
        self._limit_scope = None
        self.discriminator = None
        if limit_threshold is not None:
            self.limit_threshold = limit_threshold
        if without_cvv_only is not None:
            self.without_cvv_only = without_cvv_only
        if without_avs_only is not None:
            self.without_avs_only = without_avs_only
        self.limit_scope = limit_scope

    @property
    def limit_threshold(self):
        """Gets the limit_threshold of this MerchantLevelLimit.  # noqa: E501


        :return: The limit_threshold of this MerchantLevelLimit.  # noqa: E501
        :rtype: int
        """
        return self._limit_threshold

    @limit_threshold.setter
    def limit_threshold(self, limit_threshold):
        """Sets the limit_threshold of this MerchantLevelLimit.


        :param limit_threshold: The limit_threshold of this MerchantLevelLimit.  # noqa: E501
        :type: int
        """

        self._limit_threshold = limit_threshold

    @property
    def without_cvv_only(self):
        """Gets the without_cvv_only of this MerchantLevelLimit.  # noqa: E501


        :return: The without_cvv_only of this MerchantLevelLimit.  # noqa: E501
        :rtype: bool
        """
        return self._without_cvv_only

    @without_cvv_only.setter
    def without_cvv_only(self, without_cvv_only):
        """Sets the without_cvv_only of this MerchantLevelLimit.


        :param without_cvv_only: The without_cvv_only of this MerchantLevelLimit.  # noqa: E501
        :type: bool
        """

        self._without_cvv_only = without_cvv_only

    @property
    def without_avs_only(self):
        """Gets the without_avs_only of this MerchantLevelLimit.  # noqa: E501


        :return: The without_avs_only of this MerchantLevelLimit.  # noqa: E501
        :rtype: bool
        """
        return self._without_avs_only

    @without_avs_only.setter
    def without_avs_only(self, without_avs_only):
        """Sets the without_avs_only of this MerchantLevelLimit.


        :param without_avs_only: The without_avs_only of this MerchantLevelLimit.  # noqa: E501
        :type: bool
        """

        self._without_avs_only = without_avs_only

    @property
    def limit_scope(self):
        """Gets the limit_scope of this MerchantLevelLimit.  # noqa: E501


        :return: The limit_scope of this MerchantLevelLimit.  # noqa: E501
        :rtype: str
        """
        return self._limit_scope

    @limit_scope.setter
    def limit_scope(self, limit_scope):
        """Sets the limit_scope of this MerchantLevelLimit.


        :param limit_scope: The limit_scope of this MerchantLevelLimit.  # noqa: E501
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

