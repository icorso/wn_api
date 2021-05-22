# coding: utf-8

from model.serializable import SwaggerSerializable


class PayLink(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'logo_url': 'str',
        'footer_notes': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'logo_url': 'logoUrl',
        'footer_notes': 'footerNotes'
    }

    def __init__(self, enable=False, logo_url=None, footer_notes=None):  # noqa: E501
        """PayLink - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._logo_url = None
        self._footer_notes = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if logo_url is not None:
            self.logo_url = logo_url
        if footer_notes is not None:
            self.footer_notes = footer_notes

    @property
    def enable(self):
        """Gets the enable of this PayLink.  # noqa: E501


        :return: The enable of this PayLink.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PayLink.


        :param enable: The enable of this PayLink.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def logo_url(self):
        """Gets the logo_url of this PayLink.  # noqa: E501


        :return: The logo_url of this PayLink.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this PayLink.


        :param logo_url: The logo_url of this PayLink.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def footer_notes(self):
        """Gets the footer_notes of this PayLink.  # noqa: E501


        :return: The footer_notes of this PayLink.  # noqa: E501
        :rtype: str
        """
        return self._footer_notes

    @footer_notes.setter
    def footer_notes(self, footer_notes):
        """Sets the footer_notes of this PayLink.


        :param footer_notes: The footer_notes of this PayLink.  # noqa: E501
        :type: str
        """

        self._footer_notes = footer_notes

