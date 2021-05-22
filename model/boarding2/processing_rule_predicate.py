# coding: utf-8
from model.serializable import SwaggerSerializable


class ProcessingRulePredicate(SwaggerSerializable):
    swagger_types = {
        'when': 'str'
    }

    attribute_map = {
        'when': 'when'
    }

    def __init__(self, when=None):  # noqa: E501
        """ProcessingRulePredicate - a model defined in Swagger"""  # noqa: E501
        self._when = None
        self.discriminator = None
        self.when = when

    @property
    def when(self):
        """Gets the when of this ProcessingRulePredicate.  # noqa: E501


        :return: The when of this ProcessingRulePredicate.  # noqa: E501
        :rtype: str
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this ProcessingRulePredicate.


        :param when: The when of this ProcessingRulePredicate.  # noqa: E501
        :type: str
        """
        if when is None:
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501

        self._when = when
