# coding: utf-8
from model.serializable import SwaggerSerializable


class KeyedDataFormat(SwaggerSerializable):
    swagger_types = {
        'data_format': 'str'
    }

    attribute_map = {
        'data_format': 'dataFormat'
    }

    def __init__(self, data_format='PLAIN_TEXT'):  # noqa: E501
        """KeyedDataFormat - a model defined in Swagger"""  # noqa: E501
        self._data_format = None
        self.discriminator = None
        if data_format is not None:
            self.data_format = data_format

    @property
    def data_format(self):
        """Gets the data_format of this KeyedDataFormat.  # noqa: E501


        :return: The data_format of this KeyedDataFormat.  # noqa: E501
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this KeyedDataFormat.


        :param data_format: The data_format of this KeyedDataFormat.  # noqa: E501
        :type: str
        """

        self._data_format = data_format
