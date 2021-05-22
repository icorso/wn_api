# coding: utf-8
from model.serializable import SwaggerSerializable


class FdrcFraudDetection(SwaggerSerializable):
    swagger_types = {
        'allow_cardholder_signature_bypass': 'bool',
        'allow_unreferenced_refunds': 'bool',
        'unreferenced_refund_amount_limit': 'int',
        'refund_percentage_limit': 'float',
        'address_verification': 'AddressVerificationSystem',
        'cvv_verification': 'CardSecurityCodeVerification',
        'max_mind': 'MaxMind',
        'sentinel_defend': 'SentinelDefend',
        'three_d_secure': 'ThreeDSecure'
    }

    attribute_map = {
        'allow_cardholder_signature_bypass': 'allowCardholderSignatureBypass',
        'allow_unreferenced_refunds': 'allowUnreferencedRefunds',
        'unreferenced_refund_amount_limit': 'unreferencedRefundAmountLimit',
        'refund_percentage_limit': 'refundPercentageLimit',
        'address_verification': 'addressVerification',
        'cvv_verification': 'cvvVerification',
        'max_mind': 'maxMind',
        'sentinel_defend': 'sentinelDefend',
        'three_d_secure': 'threeDSecure'
    }

    def __init__(self, allow_cardholder_signature_bypass=False, allow_unreferenced_refunds=False, unreferenced_refund_amount_limit=None, refund_percentage_limit=100, address_verification=None, cvv_verification=None, max_mind=None, sentinel_defend=None, three_d_secure=None):  # noqa: E501
        self._allow_cardholder_signature_bypass = None
        self._allow_unreferenced_refunds = None
        self._unreferenced_refund_amount_limit = None
        self._refund_percentage_limit = None
        self._address_verification = None
        self._cvv_verification = None
        self._max_mind = None
        self._sentinel_defend = None
        self._three_d_secure = None
        self.discriminator = None
        if allow_cardholder_signature_bypass is not None:
            self.allow_cardholder_signature_bypass = allow_cardholder_signature_bypass
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
        if max_mind is not None:
            self.max_mind = max_mind
        if sentinel_defend is not None:
            self.sentinel_defend = sentinel_defend
        if three_d_secure is not None:
            self.three_d_secure = three_d_secure

    @property
    def allow_cardholder_signature_bypass(self):
        """Gets the allow_cardholder_signature_bypass of this FdrcFraudDetection.  # noqa: E501


        :return: The allow_cardholder_signature_bypass of this FdrcFraudDetection.  # noqa: E501
        :rtype: bool
        """
        return self._allow_cardholder_signature_bypass

    @allow_cardholder_signature_bypass.setter
    def allow_cardholder_signature_bypass(self, allow_cardholder_signature_bypass):
        """Sets the allow_cardholder_signature_bypass of this FdrcFraudDetection.


        :param allow_cardholder_signature_bypass: The allow_cardholder_signature_bypass of this FdrcFraudDetection.  # noqa: E501
        :type: bool
        """

        self._allow_cardholder_signature_bypass = allow_cardholder_signature_bypass

    @property
    def allow_unreferenced_refunds(self):
        """Gets the allow_unreferenced_refunds of this FdrcFraudDetection.  # noqa: E501


        :return: The allow_unreferenced_refunds of this FdrcFraudDetection.  # noqa: E501
        :rtype: bool
        """
        return self._allow_unreferenced_refunds

    @allow_unreferenced_refunds.setter
    def allow_unreferenced_refunds(self, allow_unreferenced_refunds):
        """Sets the allow_unreferenced_refunds of this FdrcFraudDetection.


        :param allow_unreferenced_refunds: The allow_unreferenced_refunds of this FdrcFraudDetection.  # noqa: E501
        :type: bool
        """

        self._allow_unreferenced_refunds = allow_unreferenced_refunds

    @property
    def unreferenced_refund_amount_limit(self):
        """Gets the unreferenced_refund_amount_limit of this FdrcFraudDetection.  # noqa: E501


        :return: The unreferenced_refund_amount_limit of this FdrcFraudDetection.  # noqa: E501
        :rtype: int
        """
        return self._unreferenced_refund_amount_limit

    @unreferenced_refund_amount_limit.setter
    def unreferenced_refund_amount_limit(self, unreferenced_refund_amount_limit):
        """Sets the unreferenced_refund_amount_limit of this FdrcFraudDetection.


        :param unreferenced_refund_amount_limit: The unreferenced_refund_amount_limit of this FdrcFraudDetection.  # noqa: E501
        :type: int
        """

        self._unreferenced_refund_amount_limit = unreferenced_refund_amount_limit

    @property
    def refund_percentage_limit(self):
        """Gets the refund_percentage_limit of this FdrcFraudDetection.  # noqa: E501


        :return: The refund_percentage_limit of this FdrcFraudDetection.  # noqa: E501
        :rtype: float
        """
        return self._refund_percentage_limit

    @refund_percentage_limit.setter
    def refund_percentage_limit(self, refund_percentage_limit):
        """Sets the refund_percentage_limit of this FdrcFraudDetection.


        :param refund_percentage_limit: The refund_percentage_limit of this FdrcFraudDetection.  # noqa: E501
        :type: float
        """

        self._refund_percentage_limit = refund_percentage_limit

    @property
    def address_verification(self):
        """Gets the address_verification of this FdrcFraudDetection.  # noqa: E501


        :return: The address_verification of this FdrcFraudDetection.  # noqa: E501
        :rtype: AddressVerificationSystem
        """
        return self._address_verification

    @address_verification.setter
    def address_verification(self, address_verification):
        """Sets the address_verification of this FdrcFraudDetection.


        :param address_verification: The address_verification of this FdrcFraudDetection.  # noqa: E501
        :type: AddressVerificationSystem
        """

        self._address_verification = address_verification

    @property
    def cvv_verification(self):
        """Gets the cvv_verification of this FdrcFraudDetection.  # noqa: E501


        :return: The cvv_verification of this FdrcFraudDetection.  # noqa: E501
        :rtype: CardSecurityCodeVerification
        """
        return self._cvv_verification

    @cvv_verification.setter
    def cvv_verification(self, cvv_verification):
        """Sets the cvv_verification of this FdrcFraudDetection.


        :param cvv_verification: The cvv_verification of this FdrcFraudDetection.  # noqa: E501
        :type: CardSecurityCodeVerification
        """

        self._cvv_verification = cvv_verification

    @property
    def max_mind(self):
        """Gets the max_mind of this FdrcFraudDetection.  # noqa: E501


        :return: The max_mind of this FdrcFraudDetection.  # noqa: E501
        :rtype: MaxMind
        """
        return self._max_mind

    @max_mind.setter
    def max_mind(self, max_mind):
        """Sets the max_mind of this FdrcFraudDetection.


        :param max_mind: The max_mind of this FdrcFraudDetection.  # noqa: E501
        :type: MaxMind
        """

        self._max_mind = max_mind

    @property
    def sentinel_defend(self):
        """Gets the sentinel_defend of this FdrcFraudDetection.  # noqa: E501


        :return: The sentinel_defend of this FdrcFraudDetection.  # noqa: E501
        :rtype: SentinelDefend
        """
        return self._sentinel_defend

    @sentinel_defend.setter
    def sentinel_defend(self, sentinel_defend):
        """Sets the sentinel_defend of this FdrcFraudDetection.


        :param sentinel_defend: The sentinel_defend of this FdrcFraudDetection.  # noqa: E501
        :type: SentinelDefend
        """

        self._sentinel_defend = sentinel_defend

    @property
    def three_d_secure(self):
        """Gets the three_d_secure of this FdrcFraudDetection.  # noqa: E501


        :return: The three_d_secure of this FdrcFraudDetection.  # noqa: E501
        :rtype: ThreeDSecure
        """
        return self._three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, three_d_secure):
        """Sets the three_d_secure of this FdrcFraudDetection.


        :param three_d_secure: The three_d_secure of this FdrcFraudDetection.  # noqa: E501
        :type: ThreeDSecure
        """

        self._three_d_secure = three_d_secure

