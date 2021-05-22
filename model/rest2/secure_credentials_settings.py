# coding: utf-8

from model.serializable import SwaggerSerializable


class SecureCredentialsSettings(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'enable_secure_card_validation': 'bool',
        'force_secure_card_validation': 'bool'
    }

    attribute_map = {
        'enable': 'enable',
        'enable_secure_card_validation': 'enableSecureCardValidation',
        'force_secure_card_validation': 'forceSecureCardValidation'
    }

    def __init__(self, enable=None, enable_secure_card_validation=None, force_secure_card_validation=None):  # noqa: E501
        """SecureCredentialsSettings - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._enable_secure_card_validation = None
        self._force_secure_card_validation = None
        self.discriminator = None
        self.enable = enable
        self.enable_secure_card_validation = enable_secure_card_validation
        self.force_secure_card_validation = force_secure_card_validation

    @property
    def enable(self):
        """Gets the enable of this SecureCredentialsSettings.  # noqa: E501

        Indicates whether the terminal supports secure credentials which is our tokenization mechanism for cards and accounts.  # noqa: E501

        :return: The enable of this SecureCredentialsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this SecureCredentialsSettings.

        Indicates whether the terminal supports secure credentials which is our tokenization mechanism for cards and accounts.  # noqa: E501

        :param enable: The enable of this SecureCredentialsSettings.  # noqa: E501
        :type: bool
        """
        if enable is None:
            raise ValueError("Invalid value for `enable`, must not be `None`")  # noqa: E501

        self._enable = enable

    @property
    def enable_secure_card_validation(self):
        """Gets the enable_secure_card_validation of this SecureCredentialsSettings.  # noqa: E501

        Indicates that account verifications will be performed when the secure code (CVV) is provided during Secure Card registrations.  # noqa: E501

        :return: The enable_secure_card_validation of this SecureCredentialsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_secure_card_validation

    @enable_secure_card_validation.setter
    def enable_secure_card_validation(self, enable_secure_card_validation):
        """Sets the enable_secure_card_validation of this SecureCredentialsSettings.

        Indicates that account verifications will be performed when the secure code (CVV) is provided during Secure Card registrations.  # noqa: E501

        :param enable_secure_card_validation: The enable_secure_card_validation of this SecureCredentialsSettings.  # noqa: E501
        :type: bool
        """
        if enable_secure_card_validation is None:
            raise ValueError("Invalid value for `enable_secure_card_validation`, must not be `None`")  # noqa: E501

        self._enable_secure_card_validation = enable_secure_card_validation

    @property
    def force_secure_card_validation(self):
        """Gets the force_secure_card_validation of this SecureCredentialsSettings.  # noqa: E501

        Indicates that account verifications are mandatory for all Secure Card registrations.  # noqa: E501

        :return: The force_secure_card_validation of this SecureCredentialsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._force_secure_card_validation

    @force_secure_card_validation.setter
    def force_secure_card_validation(self, force_secure_card_validation):
        """Sets the force_secure_card_validation of this SecureCredentialsSettings.

        Indicates that account verifications are mandatory for all Secure Card registrations.  # noqa: E501

        :param force_secure_card_validation: The force_secure_card_validation of this SecureCredentialsSettings.  # noqa: E501
        :type: bool
        """
        if force_secure_card_validation is None:
            raise ValueError("Invalid value for `force_secure_card_validation`, must not be `None`")  # noqa: E501

        self._force_secure_card_validation = force_secure_card_validation
