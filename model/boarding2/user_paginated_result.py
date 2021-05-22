# coding: utf-8

from model.serializable import SwaggerSerializable


class UserPaginatedResult(SwaggerSerializable):
    swagger_types = {
        'data': 'list[UserCompact]',
        'links': 'list[HypermediaLink]',
        'total_count': 'int'
    }

    attribute_map = {
        'data': 'data',
        'links': 'links',
        'total_count': 'totalCount'
    }

    def __init__(self, data=None, links=None, total_count=None):  # noqa: E501
        """UserPaginatedResult - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._links = None
        self._total_count = None
        self.discriminator = None
        self.data = data
        if links is not None:
            self.links = links
        self.total_count = total_count

    @property
    def data(self):
        """Gets the data of this UserPaginatedResult.  # noqa: E501

        List of elements.  # noqa: E501

        :return: The data of this UserPaginatedResult.  # noqa: E501
        :rtype: list[UserCompact]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UserPaginatedResult.

        List of elements.  # noqa: E501

        :param data: The data of this UserPaginatedResult.  # noqa: E501
        :type: list[UserCompact]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def links(self):
        """Gets the links of this UserPaginatedResult.  # noqa: E501

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :return: The links of this UserPaginatedResult.  # noqa: E501
        :rtype: list[HypermediaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserPaginatedResult.

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :param links: The links of this UserPaginatedResult.  # noqa: E501
        :type: list[HypermediaLink]
        """

        self._links = links

    @property
    def total_count(self):
        """Gets the total_count of this UserPaginatedResult.  # noqa: E501

        Total number of elements.  # noqa: E501

        :return: The total_count of this UserPaginatedResult.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this UserPaginatedResult.

        Total number of elements.  # noqa: E501

        :param total_count: The total_count of this UserPaginatedResult.  # noqa: E501
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

