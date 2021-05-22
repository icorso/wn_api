# coding: utf-8
from model.serializable import SwaggerSerializable


class AddressVerificationSystem(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'compulsory': 'bool',
        'auto_decline_on_failure': 'bool',
        'preferred_address_mode': 'str',
        'approval_codes': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'compulsory': 'compulsory',
        'auto_decline_on_failure': 'autoDeclineOnFailure',
        'preferred_address_mode': 'preferredAddressMode',
        'approval_codes': 'approvalCodes'
    }

    def __init__(self, enable=None, compulsory=None, auto_decline_on_failure=None, preferred_address_mode=None, approval_codes=None):  # noqa: E501
        """AddressVerificationSystem - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._compulsory = None
        self._auto_decline_on_failure = None
        self._preferred_address_mode = None
        self._approval_codes = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if compulsory is not None:
            self.compulsory = compulsory
        if auto_decline_on_failure is not None:
            self.auto_decline_on_failure = auto_decline_on_failure
        if preferred_address_mode is not None:
            self.preferred_address_mode = preferred_address_mode
        if approval_codes is not None:
            self.approval_codes = approval_codes

    @property
    def enable(self):
        """Gets the enable of this AddressVerificationSystem.  # noqa: E501

        Indicates whether AVS check is available for the terminal and merchants may send cardholder’s billing address for verification.  # noqa: E501

        :return: The enable of this AddressVerificationSystem.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AddressVerificationSystem.

        Indicates whether AVS check is available for the terminal and merchants may send cardholder’s billing address for verification.  # noqa: E501

        :param enable: The enable of this AddressVerificationSystem.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def compulsory(self):
        """Gets the compulsory of this AddressVerificationSystem.  # noqa: E501

        If enabled, it ensures that a transaction will never be processed without billing address information.  # noqa: E501

        :return: The compulsory of this AddressVerificationSystem.  # noqa: E501
        :rtype: bool
        """
        return self._compulsory

    @compulsory.setter
    def compulsory(self, compulsory):
        """Sets the compulsory of this AddressVerificationSystem.

        If enabled, it ensures that a transaction will never be processed without billing address information.  # noqa: E501

        :param compulsory: The compulsory of this AddressVerificationSystem.  # noqa: E501
        :type: bool
        """

        self._compulsory = compulsory

    @property
    def auto_decline_on_failure(self):
        """Gets the auto_decline_on_failure of this AddressVerificationSystem.  # noqa: E501

        Indicates that all AVS non-match will lead to a transaction decline. This is sometimes desirable as not all card issuers will decline a transaction that has failed an AVS check.  # noqa: E501

        :return: The auto_decline_on_failure of this AddressVerificationSystem.  # noqa: E501
        :rtype: bool
        """
        return self._auto_decline_on_failure

    @auto_decline_on_failure.setter
    def auto_decline_on_failure(self, auto_decline_on_failure):
        """Sets the auto_decline_on_failure of this AddressVerificationSystem.

        Indicates that all AVS non-match will lead to a transaction decline. This is sometimes desirable as not all card issuers will decline a transaction that has failed an AVS check.  # noqa: E501

        :param auto_decline_on_failure: The auto_decline_on_failure of this AddressVerificationSystem.  # noqa: E501
        :type: bool
        """

        self._auto_decline_on_failure = auto_decline_on_failure

    @property
    def preferred_address_mode(self):
        """Gets the preferred_address_mode of this AddressVerificationSystem.  # noqa: E501

        This field defines a configuration for the execution and validation of AVS transactions.  - Exact: At least the first line of the address as well as city and postal code are mandatory. - Postal: Only postal code is mandatory when filling up customer's billing address.  # noqa: E501

        :return: The preferred_address_mode of this AddressVerificationSystem.  # noqa: E501
        :rtype: str
        """
        return self._preferred_address_mode

    @preferred_address_mode.setter
    def preferred_address_mode(self, preferred_address_mode):
        """Sets the preferred_address_mode of this AddressVerificationSystem.

        This field defines a configuration for the execution and validation of AVS transactions.  - Exact: At least the first line of the address as well as city and postal code are mandatory. - Postal: Only postal code is mandatory when filling up customer's billing address.  # noqa: E501

        :param preferred_address_mode: The preferred_address_mode of this AddressVerificationSystem.  # noqa: E501
        :type: str
        """
        allowed_values = ["EXACT", "POSTAL"]  # noqa: E501
        if preferred_address_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `preferred_address_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(preferred_address_mode, allowed_values)
            )

        self._preferred_address_mode = preferred_address_mode

    @property
    def approval_codes(self):
        """Gets the approval_codes of this AddressVerificationSystem.  # noqa: E501

        List of AVS result codes that are considered to be a match. The codes left out of this list will lead to a transaction decline when `autoDeclineTransactionsOnAvsFailures` is enabled.  # noqa: E501

        :return: The approval_codes of this AddressVerificationSystem.  # noqa: E501
        :rtype: list[str]
        """
        return self._approval_codes

    @approval_codes.setter
    def approval_codes(self, approval_codes):
        """Sets the approval_codes of this AddressVerificationSystem.

        List of AVS result codes that are considered to be a match. The codes left out of this list will lead to a transaction decline when `autoDeclineTransactionsOnAvsFailures` is enabled.  # noqa: E501

        :param approval_codes: The approval_codes of this AddressVerificationSystem.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Y", "A", "Z", "N", "U", "R", "G", "S", "F", "W", "X"]  # noqa: E501
        if not set(approval_codes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `approval_codes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(approval_codes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._approval_codes = approval_codes
