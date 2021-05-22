# coding: utf-8
from model.serializable import SwaggerSerializable


class SentinelDefend(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'organization_id': 'str',
        'api_key': 'str',
        'policy_name': 'str',
        'reject_on_error': 'bool',
        'risk_score_threshold': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'organization_id': 'organizationId',
        'api_key': 'apiKey',
        'policy_name': 'policyName',
        'reject_on_error': 'rejectOnError',
        'risk_score_threshold': 'riskScoreThreshold'
    }

    def __init__(self, enable=False, organization_id=None, api_key=None, policy_name=None, reject_on_error=False, risk_score_threshold=0):  # noqa: E501
        self._enable = None
        self._organization_id = None
        self._api_key = None
        self._policy_name = None
        self._reject_on_error = None
        self._risk_score_threshold = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if organization_id is not None:
            self.organization_id = organization_id
        if api_key is not None:
            self.api_key = api_key
        if policy_name is not None:
            self.policy_name = policy_name
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if risk_score_threshold is not None:
            self.risk_score_threshold = risk_score_threshold

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def organization_id(self):
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        self._organization_id = organization_id

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key

    @property
    def policy_name(self):
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        self._policy_name = policy_name

    @property
    def reject_on_error(self):
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        self._reject_on_error = reject_on_error

    @property
    def risk_score_threshold(self):
        return self._risk_score_threshold

    @risk_score_threshold.setter
    def risk_score_threshold(self, risk_score_threshold):
        self._risk_score_threshold = risk_score_threshold

