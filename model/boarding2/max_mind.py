# coding: utf-8
from model.serializable import SwaggerSerializable


class MaxMind(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'reject_on_error': 'bool',
        'risk_score_threshold': 'float'
    }

    attribute_map = {
        'enable': 'enable',
        'reject_on_error': 'rejectOnError',
        'risk_score_threshold': 'riskScoreThreshold'
    }

    def __init__(self, enable=False, reject_on_error=False, risk_score_threshold=50):  # noqa: E501
        """MaxMind - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._reject_on_error = None
        self._risk_score_threshold = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if risk_score_threshold is not None:
            self.risk_score_threshold = risk_score_threshold

    @property
    def enable(self):
        """Gets the enable of this MaxMind.  # noqa: E501


        :return: The enable of this MaxMind.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this MaxMind.


        :param enable: The enable of this MaxMind.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this MaxMind.  # noqa: E501


        :return: The reject_on_error of this MaxMind.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this MaxMind.


        :param reject_on_error: The reject_on_error of this MaxMind.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def risk_score_threshold(self):
        """Gets the risk_score_threshold of this MaxMind.  # noqa: E501


        :return: The risk_score_threshold of this MaxMind.  # noqa: E501
        :rtype: float
        """
        return self._risk_score_threshold

    @risk_score_threshold.setter
    def risk_score_threshold(self, risk_score_threshold):
        """Sets the risk_score_threshold of this MaxMind.


        :param risk_score_threshold: The risk_score_threshold of this MaxMind.  # noqa: E501
        :type: float
        """

        self._risk_score_threshold = risk_score_threshold
