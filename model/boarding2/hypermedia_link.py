# coding: utf-8

from model.serializable import SwaggerSerializable


class HypermediaLink(SwaggerSerializable):
    swagger_types = {
        'rel': 'str',
        'method': 'str',
        'href': 'str'
    }

    attribute_map = {
        'rel': 'rel',
        'method': 'method',
        'href': 'href'
    }

    def __init__(self, rel=None, method=None, href=None):  # noqa: E501
        """HypermediaLink - a model defined in Swagger"""  # noqa: E501
        self._rel = None
        self._method = None
        self._href = None
        self.discriminator = None
        if rel is not None:
            self.rel = rel
        if method is not None:
            self.method = method
        if href is not None:
            self.href = href

    @property
    def rel(self):
        """Gets the rel of this HypermediaLink.  # noqa: E501

        Keyword that represents the action that the link is supposed to perform.  # noqa: E501

        :return: The rel of this HypermediaLink.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this HypermediaLink.

        Keyword that represents the action that the link is supposed to perform.  # noqa: E501

        :param rel: The rel of this HypermediaLink.  # noqa: E501
        :type: str
        """

        self._rel = rel

    @property
    def method(self):
        """Gets the method of this HypermediaLink.  # noqa: E501

        The HTTP method or verb.  # noqa: E501

        :return: The method of this HypermediaLink.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this HypermediaLink.

        The HTTP method or verb.  # noqa: E501

        :param method: The method of this HypermediaLink.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def href(self):
        """Gets the href of this HypermediaLink.  # noqa: E501

        The actual request URL.  # noqa: E501

        :return: The href of this HypermediaLink.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this HypermediaLink.

        The actual request URL.  # noqa: E501

        :param href: The href of this HypermediaLink.  # noqa: E501
        :type: str
        """

        self._href = href

