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

    def __init__(self, card=None, limits=None):
        self._card = None
        self._limits = None
        self.discriminator = None
        self.card = card
        if limits is not None:
            self.limits = limits

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, card):
        if card is None:
            raise ValueError("Invalid value for `card`, must not be `None`")

        self._card = card

    @property
    def limits(self):
        return self._limits

    @limits.setter
    def limits(self, limits):
        self._limits = limits
