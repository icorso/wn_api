# coding: utf-8
from model.serializable import SwaggerSerializable


class TerminalPaginatedResult(SwaggerSerializable):
    swagger_types = {
        'data': 'list[TerminalCompact]',
        'links': 'list[HypermediaLink]',
        'total_count': 'int'
    }

    attribute_map = {
        'data': 'data',
        'links': 'links',
        'total_count': 'totalCount'
    }

    def __init__(self, data=None, links=None, total_count=None):
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
        return self._data

    @data.setter
    def data(self, data):
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

