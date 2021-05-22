# coding: utf-8
from model.serializable import SwaggerSerializable


class TerminalVolumeLimits(SwaggerSerializable):
    swagger_types = {
        'enable_terminal_level_limits': 'bool',
        'terminal_level_limits': 'list[TerminalLevelLimit]',
        'enable_card_level_limits': 'bool',
        'card_level_limits': 'list[CardLevelLimit]'
    }

    attribute_map = {
        'enable_terminal_level_limits': 'enableTerminalLevelLimits',
        'terminal_level_limits': 'terminalLevelLimits',
        'enable_card_level_limits': 'enableCardLevelLimits',
        'card_level_limits': 'cardLevelLimits'
    }

    def __init__(self, enable_terminal_level_limits=False, terminal_level_limits=None, enable_card_level_limits=False, card_level_limits=None):  # noqa: E501
        self._enable_terminal_level_limits = None
        self._terminal_level_limits = None
        self._enable_card_level_limits = None
        self._card_level_limits = None
        self.discriminator = None
        if enable_terminal_level_limits is not None:
            self.enable_terminal_level_limits = enable_terminal_level_limits
        if terminal_level_limits is not None:
            self.terminal_level_limits = terminal_level_limits
        if enable_card_level_limits is not None:
            self.enable_card_level_limits = enable_card_level_limits
        if card_level_limits is not None:
            self.card_level_limits = card_level_limits

    @property
    def enable_terminal_level_limits(self):
        return self._enable_terminal_level_limits

    @enable_terminal_level_limits.setter
    def enable_terminal_level_limits(self, enable_terminal_level_limits):
        self._enable_terminal_level_limits = enable_terminal_level_limits

    @property
    def terminal_level_limits(self):
        return self._terminal_level_limits

    @terminal_level_limits.setter
    def terminal_level_limits(self, terminal_level_limits):
        self._terminal_level_limits = terminal_level_limits

    @property
    def enable_card_level_limits(self):
        return self._enable_card_level_limits

    @enable_card_level_limits.setter
    def enable_card_level_limits(self, enable_card_level_limits):
        self._enable_card_level_limits = enable_card_level_limits

    @property
    def card_level_limits(self):
        return self._card_level_limits

    @card_level_limits.setter
    def card_level_limits(self, card_level_limits):
        self._card_level_limits = card_level_limits

