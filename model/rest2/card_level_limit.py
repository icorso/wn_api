# coding: utf-8
from model.serializable import SwaggerSerializable


class CardLevelLimit(SwaggerSerializable):
    swagger_types = {
        'card': 'str',
        'limits': 'list[CardVolumeLimit]'
    }

    attribute_map = {
        'card': 'card',
        'limits': 'limits'
    }

    def __init__(self, card=None, limits=None):  # noqa: E501
        """CardLevelLimit - a model defined in Swagger"""  # noqa: E501
        self._card = None
        self._limits = None
        self.discriminator = None
        self.card = card
        self.limits = limits

    @property
    def card(self):
        """Gets the card of this CardLevelLimit.  # noqa: E501

        The card brand to which the list of volume limits below will be applied.  # noqa: E501

        :return: The card of this CardLevelLimit.  # noqa: E501
        :rtype: str
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this CardLevelLimit.

        The card brand to which the list of volume limits below will be applied.  # noqa: E501

        :param card: The card of this CardLevelLimit.  # noqa: E501
        :type: str
        """
        if card is None:
            raise ValueError("Invalid value for `card`, must not be `None`")  # noqa: E501

        self._card = card

    @property
    def limits(self):
        """Gets the limits of this CardLevelLimit.  # noqa: E501

        List of limits to be applied to transactions using the brand specified in the property `card`.  # noqa: E501

        :return: The limits of this CardLevelLimit.  # noqa: E501
        :rtype: list[CardVolumeLimit]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this CardLevelLimit.

        List of limits to be applied to transactions using the brand specified in the property `card`.  # noqa: E501

        :param limits: The limits of this CardLevelLimit.  # noqa: E501
        :type: list[CardVolumeLimit]
        """
        if limits is None:
            raise ValueError("Invalid value for `limits`, must not be `None`")  # noqa: E501

        self._limits = limits

