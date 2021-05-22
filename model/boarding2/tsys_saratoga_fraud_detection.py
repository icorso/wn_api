# coding: utf-8
from model.serializable import SwaggerSerializable


class TsysSaratogaFraudDetection(SwaggerSerializable):
    swagger_types = {
        'allow_cardholder_signature_bypass': 'bool',
        'allow_cvv_compliance_rule_bypass': 'bool',
        'allow_unreferenced_refunds': 'bool',
        'unreferenced_refund_amount_limit': 'int',
        'refund_percentage_limit': 'float',
        'address_verification': 'AddressVerificationSystem',
        'cvv_verification': 'CardSecurityCodeVerification',
        'three_d_secure': 'ThreeDSecure',
        'max_mind': 'MaxMind',
        'sentinel_defend': 'SentinelDefend'
    }

    attribute_map = {
        'allow_cardholder_signature_bypass': 'allowCardholderSignatureBypass',
        'allow_cvv_compliance_rule_bypass': 'allowCvvComplianceRuleBypass',
        'allow_unreferenced_refunds': 'allowUnreferencedRefunds',
        'unreferenced_refund_amount_limit': 'unreferencedRefundAmountLimit',
        'refund_percentage_limit': 'refundPercentageLimit',
        'address_verification': 'addressVerification',
        'cvv_verification': 'cvvVerification',
        'three_d_secure': 'threeDSecure',
        'max_mind': 'maxMind',
        'sentinel_defend': 'sentinelDefend'
    }

    def __init__(self, allow_cardholder_signature_bypass=False, allow_cvv_compliance_rule_bypass=False, allow_unreferenced_refunds=False, unreferenced_refund_amount_limit=None, refund_percentage_limit=100, address_verification=None, cvv_verification=None, three_d_secure=None, max_mind=None, sentinel_defend=None):  # noqa: E501
        self._allow_cardholder_signature_bypass = None
        self._allow_cvv_compliance_rule_bypass = None
        self._allow_unreferenced_refunds = None
        self._unreferenced_refund_amount_limit = None
        self._refund_percentage_limit = None
        self._address_verification = None
        self._cvv_verification = None
        self._three_d_secure = None
        self._max_mind = None
        self._sentinel_defend = None
        self.discriminator = None
        if allow_cardholder_signature_bypass is not None:
            self.allow_cardholder_signature_bypass = allow_cardholder_signature_bypass
        if allow_cvv_compliance_rule_bypass is not None:
            self.allow_cvv_compliance_rule_bypass = allow_cvv_compliance_rule_bypass
        if allow_unreferenced_refunds is not None:
            self.allow_unreferenced_refunds = allow_unreferenced_refunds
        if unreferenced_refund_amount_limit is not None:
            self.unreferenced_refund_amount_limit = unreferenced_refund_amount_limit
        if refund_percentage_limit is not None:
            self.refund_percentage_limit = refund_percentage_limit
        if address_verification is not None:
            self.address_verification = address_verification
        if cvv_verification is not None:
            self.cvv_verification = cvv_verification
        if three_d_secure is not None:
            self.three_d_secure = three_d_secure
        if max_mind is not None:
            self.max_mind = max_mind
        if sentinel_defend is not None:
            self.sentinel_defend = sentinel_defend

    @property
    def allow_cardholder_signature_bypass(self):
        return self._allow_cardholder_signature_bypass

    @allow_cardholder_signature_bypass.setter
    def allow_cardholder_signature_bypass(self, allow_cardholder_signature_bypass):
        self._allow_cardholder_signature_bypass = allow_cardholder_signature_bypass

    @property
    def allow_cvv_compliance_rule_bypass(self):
        return self._allow_cvv_compliance_rule_bypass

    @allow_cvv_compliance_rule_bypass.setter
    def allow_cvv_compliance_rule_bypass(self, allow_cvv_compliance_rule_bypass):
        self._allow_cvv_compliance_rule_bypass = allow_cvv_compliance_rule_bypass

    @property
    def allow_unreferenced_refunds(self):
        return self._allow_unreferenced_refunds

    @allow_unreferenced_refunds.setter
    def allow_unreferenced_refunds(self, allow_unreferenced_refunds):
        self._allow_unreferenced_refunds = allow_unreferenced_refunds

    @property
    def unreferenced_refund_amount_limit(self):
        return self._unreferenced_refund_amount_limit

    @unreferenced_refund_amount_limit.setter
    def unreferenced_refund_amount_limit(self, unreferenced_refund_amount_limit):
        self._unreferenced_refund_amount_limit = unreferenced_refund_amount_limit

    @property
    def refund_percentage_limit(self):
        return self._refund_percentage_limit

    @refund_percentage_limit.setter
    def refund_percentage_limit(self, refund_percentage_limit):
        self._refund_percentage_limit = refund_percentage_limit

    @property
    def address_verification(self):
        return self._address_verification

    @address_verification.setter
    def address_verification(self, address_verification):
        self._address_verification = address_verification

    @property
    def cvv_verification(self):
        return self._cvv_verification

    @cvv_verification.setter
    def cvv_verification(self, cvv_verification):
        self._cvv_verification = cvv_verification

    @property
    def three_d_secure(self):
        return self._three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, three_d_secure):
        self._three_d_secure = three_d_secure

    @property
    def max_mind(self):
        return self._max_mind

    @max_mind.setter
    def max_mind(self, max_mind):
        self._max_mind = max_mind

    @property
    def sentinel_defend(self):
        return self._sentinel_defend

    @sentinel_defend.setter
    def sentinel_defend(self, sentinel_defend):
        self._sentinel_defend = sentinel_defend

