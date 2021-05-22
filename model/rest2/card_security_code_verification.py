# coding: utf-8
from model.serializable import SwaggerSerializable


class CardSecurityCodeVerification(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'auto_decline_on_failure': 'bool',
        'decline_codes': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'auto_decline_on_failure': 'autoDeclineOnFailure',
        'decline_codes': 'declineCodes'
    }

    def __init__(self, enable=None, auto_decline_on_failure=None, decline_codes=None):  # noqa: E501
        """CardSecurityCodeVerification - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._auto_decline_on_failure = None
        self._decline_codes = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if auto_decline_on_failure is not None:
            self.auto_decline_on_failure = auto_decline_on_failure
        if decline_codes is not None:
            self.decline_codes = decline_codes

    @property
    def enable(self):
        """Gets the enable of this CardSecurityCodeVerification.  # noqa: E501

        Indicates whether CVV check is available for the terminal.  # noqa: E501

        :return: The enable of this CardSecurityCodeVerification.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CardSecurityCodeVerification.

        Indicates whether CVV check is available for the terminal.  # noqa: E501

        :param enable: The enable of this CardSecurityCodeVerification.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def auto_decline_on_failure(self):
        """Gets the auto_decline_on_failure of this CardSecurityCodeVerification.  # noqa: E501

        Indicates that all CVV codes listed in `cvvDeclineCodes` property will lead to a transaction decline.This is sometimes desirable as not all card issuers will decline a transaction that has failed a CVV check.  # noqa: E501

        :return: The auto_decline_on_failure of this CardSecurityCodeVerification.  # noqa: E501
        :rtype: bool
        """
        return self._auto_decline_on_failure

    @auto_decline_on_failure.setter
    def auto_decline_on_failure(self, auto_decline_on_failure):
        """Sets the auto_decline_on_failure of this CardSecurityCodeVerification.

        Indicates that all CVV codes listed in `cvvDeclineCodes` property will lead to a transaction decline.This is sometimes desirable as not all card issuers will decline a transaction that has failed a CVV check.  # noqa: E501

        :param auto_decline_on_failure: The auto_decline_on_failure of this CardSecurityCodeVerification.  # noqa: E501
        :type: bool
        """

        self._auto_decline_on_failure = auto_decline_on_failure

    @property
    def decline_codes(self):
        """Gets the decline_codes of this CardSecurityCodeVerification.  # noqa: E501

        List of CVV result codes that will lead to a transaction decline when `autoDeclineTransactionsOnCvvFailures` is enabled.  # noqa: E501

        :return: The decline_codes of this CardSecurityCodeVerification.  # noqa: E501
        :rtype: list[str]
        """
        return self._decline_codes

    @decline_codes.setter
    def decline_codes(self, decline_codes):
        """Sets the decline_codes of this CardSecurityCodeVerification.

        List of CVV result codes that will lead to a transaction decline when `autoDeclineTransactionsOnCvvFailures` is enabled.  # noqa: E501

        :param decline_codes: The decline_codes of this CardSecurityCodeVerification.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["M", "N", "P", "U"]  # noqa: E501
        if not set(decline_codes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `decline_codes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(decline_codes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._decline_codes = decline_codes
