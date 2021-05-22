# coding: utf-8

from model.serializable import SwaggerSerializable


class CredoraxDynamicDescriptor(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'prefix': 'str',
        'suffix': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'prefix': 'prefix',
        'suffix': 'suffix'
    }

    def __init__(self, enable=False, prefix=None, suffix=None):  # noqa: E501
        """CredoraxDynamicDescriptor - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._prefix = None
        self._suffix = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if prefix is not None:
            self.prefix = prefix
        if suffix is not None:
            self.suffix = suffix

    @property
    def enable(self):
        """Gets the enable of this CredoraxDynamicDescriptor.  # noqa: E501


        :return: The enable of this CredoraxDynamicDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CredoraxDynamicDescriptor.


        :param enable: The enable of this CredoraxDynamicDescriptor.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def prefix(self):
        """Gets the prefix of this CredoraxDynamicDescriptor.  # noqa: E501


        :return: The prefix of this CredoraxDynamicDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this CredoraxDynamicDescriptor.


        :param prefix: The prefix of this CredoraxDynamicDescriptor.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def suffix(self):
        """Gets the suffix of this CredoraxDynamicDescriptor.  # noqa: E501


        :return: The suffix of this CredoraxDynamicDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this CredoraxDynamicDescriptor.


        :param suffix: The suffix of this CredoraxDynamicDescriptor.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

