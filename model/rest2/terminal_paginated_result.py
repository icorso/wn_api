# coding: utf-8

from model.serializable import SwaggerSerializable


class TerminalPaginatedResult(SwaggerSerializable):
    swagger_types = {
        'data': 'list[TerminalCompact]',
        'next': 'str',
        'links': 'list[HypermediaLink]'
    }

    attribute_map = {
        'data': 'data',
        'next': 'next',
        'links': 'links'
    }

    def __init__(self, data=None, next=None, links=None):  # noqa: E501
        """TerminalPaginatedResult - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._next = None
        self._links = None
        self.discriminator = None
        self.data = data
        if next is not None:
            self.next = next
        if links is not None:
            self.links = links

    @property
    def data(self):
        """Gets the data of this TerminalPaginatedResult.  # noqa: E501

        List of elements.  # noqa: E501

        :return: The data of this TerminalPaginatedResult.  # noqa: E501
        :rtype: list[TerminalCompact]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TerminalPaginatedResult.

        List of elements.  # noqa: E501

        :param data: The data of this TerminalPaginatedResult.  # noqa: E501
        :type: list[TerminalCompact]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def next(self):
        """Gets the next of this TerminalPaginatedResult.  # noqa: E501

        The cursor pointing to the next set of elements.  # noqa: E501

        :return: The next of this TerminalPaginatedResult.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this TerminalPaginatedResult.

        The cursor pointing to the next set of elements.  # noqa: E501

        :param next: The next of this TerminalPaginatedResult.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def links(self):
        """Gets the links of this TerminalPaginatedResult.  # noqa: E501

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :return: The links of this TerminalPaginatedResult.  # noqa: E501
        :rtype: list[HypermediaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TerminalPaginatedResult.

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :param links: The links of this TerminalPaginatedResult.  # noqa: E501
        :type: list[HypermediaLink]
        """

        self._links = links
