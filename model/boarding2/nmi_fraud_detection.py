# coding: utf-8

from model.serializable import SwaggerSerializable


class NmiFraudDetection(SwaggerSerializable):
    swagger_types = {
        'refund_percentage_limit': 'float',
        'address_verification': 'AddressVerificationSystem',
        'cvv_verification': 'CardSecurityCodeVerification',
        'max_mind': 'MaxMind',
        'sentinel_defend': 'SentinelDefend'
    }

    attribute_map = {
        'refund_percentage_limit': 'refundPercentageLimit',
        'address_verification': 'addressVerification',
        'cvv_verification': 'cvvVerification',
        'max_mind': 'maxMind',
        'sentinel_defend': 'sentinelDefend'
    }

    def __init__(self, refund_percentage_limit=100, address_verification=None, cvv_verification=None, max_mind=None, sentinel_defend=None):  # noqa: E501
        """NmiFraudDetection - a model defined in Swagger"""  # noqa: E501
        self._refund_percentage_limit = None
        self._address_verification = None
        self._cvv_verification = None
        self._max_mind = None
        self._sentinel_defend = None
        self.discriminator = None
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

    @property
    def refund_percentage_limit(self):
        """Gets the refund_percentage_limit of this NmiFraudDetection.  # noqa: E501


        :return: The refund_percentage_limit of this NmiFraudDetection.  # noqa: E501
        :rtype: float
        """
        return self._refund_percentage_limit

    @refund_percentage_limit.setter
    def refund_percentage_limit(self, refund_percentage_limit):
        """Sets the refund_percentage_limit of this NmiFraudDetection.


        :param refund_percentage_limit: The refund_percentage_limit of this NmiFraudDetection.  # noqa: E501
        :type: float
        """

        self._refund_percentage_limit = refund_percentage_limit

    @property
    def address_verification(self):
        """Gets the address_verification of this NmiFraudDetection.  # noqa: E501


        :return: The address_verification of this NmiFraudDetection.  # noqa: E501
        :rtype: AddressVerificationSystem
        """
        return self._address_verification

    @address_verification.setter
    def address_verification(self, address_verification):
        """Sets the address_verification of this NmiFraudDetection.


        :param address_verification: The address_verification of this NmiFraudDetection.  # noqa: E501
        :type: AddressVerificationSystem
        """

        self._address_verification = address_verification

    @property
    def cvv_verification(self):
        """Gets the cvv_verification of this NmiFraudDetection.  # noqa: E501


        :return: The cvv_verification of this NmiFraudDetection.  # noqa: E501
        :rtype: CardSecurityCodeVerification
        """
        return self._cvv_verification

    @cvv_verification.setter
    def cvv_verification(self, cvv_verification):
        """Sets the cvv_verification of this NmiFraudDetection.


        :param cvv_verification: The cvv_verification of this NmiFraudDetection.  # noqa: E501
        :type: CardSecurityCodeVerification
        """

        self._cvv_verification = cvv_verification

    @property
    def max_mind(self):
        """Gets the max_mind of this NmiFraudDetection.  # noqa: E501


        :return: The max_mind of this NmiFraudDetection.  # noqa: E501
        :rtype: MaxMind
        """
        return self._max_mind

    @max_mind.setter
    def max_mind(self, max_mind):
        """Sets the max_mind of this NmiFraudDetection.


        :param max_mind: The max_mind of this NmiFraudDetection.  # noqa: E501
        :type: MaxMind
        """

        self._max_mind = max_mind

    @property
    def sentinel_defend(self):
        """Gets the sentinel_defend of this NmiFraudDetection.  # noqa: E501


        :return: The sentinel_defend of this NmiFraudDetection.  # noqa: E501
        :rtype: SentinelDefend
        """
        return self._sentinel_defend

    @sentinel_defend.setter
    def sentinel_defend(self, sentinel_defend):
        """Sets the sentinel_defend of this NmiFraudDetection.


        :param sentinel_defend: The sentinel_defend of this NmiFraudDetection.  # noqa: E501
        :type: SentinelDefend
        """

        self._sentinel_defend = sentinel_defend

