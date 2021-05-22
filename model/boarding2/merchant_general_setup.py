# coding: utf-8

from model.serializable import SwaggerSerializable


class MerchantGeneralSetup(SwaggerSerializable):
    swagger_types = {
        'share_all_secure_cards': 'bool',
        'share_cards_from_deactivated_terminals': 'bool',
        'enable_merchant_level_limits': 'bool',
        'merchant_level_limits': 'list[MerchantLevelLimit]'
    }

    attribute_map = {
        'share_all_secure_cards': 'shareAllSecureCards',
        'share_cards_from_deactivated_terminals': 'shareCardsFromDeactivatedTerminals',
        'enable_merchant_level_limits': 'enableMerchantLevelLimits',
        'merchant_level_limits': 'merchantLevelLimits'
    }

    def __init__(self, share_all_secure_cards=None, share_cards_from_deactivated_terminals=None, enable_merchant_level_limits=None, merchant_level_limits=None):  # noqa: E501
        """MerchantGeneralSetup - a model defined in Swagger"""  # noqa: E501
        self._share_all_secure_cards = None
        self._share_cards_from_deactivated_terminals = None
        self._enable_merchant_level_limits = None
        self._merchant_level_limits = None
        self.discriminator = None
        if share_all_secure_cards is not None:
            self.share_all_secure_cards = share_all_secure_cards
        if share_cards_from_deactivated_terminals is not None:
            self.share_cards_from_deactivated_terminals = share_cards_from_deactivated_terminals
        if enable_merchant_level_limits is not None:
            self.enable_merchant_level_limits = enable_merchant_level_limits
        if merchant_level_limits is not None:
            self.merchant_level_limits = merchant_level_limits

    @property
    def share_all_secure_cards(self):
        """Gets the share_all_secure_cards of this MerchantGeneralSetup.  # noqa: E501


        :return: The share_all_secure_cards of this MerchantGeneralSetup.  # noqa: E501
        :rtype: bool
        """
        return self._share_all_secure_cards

    @share_all_secure_cards.setter
    def share_all_secure_cards(self, share_all_secure_cards):
        """Sets the share_all_secure_cards of this MerchantGeneralSetup.


        :param share_all_secure_cards: The share_all_secure_cards of this MerchantGeneralSetup.  # noqa: E501
        :type: bool
        """

        self._share_all_secure_cards = share_all_secure_cards

    @property
    def share_cards_from_deactivated_terminals(self):
        """Gets the share_cards_from_deactivated_terminals of this MerchantGeneralSetup.  # noqa: E501


        :return: The share_cards_from_deactivated_terminals of this MerchantGeneralSetup.  # noqa: E501
        :rtype: bool
        """
        return self._share_cards_from_deactivated_terminals

    @share_cards_from_deactivated_terminals.setter
    def share_cards_from_deactivated_terminals(self, share_cards_from_deactivated_terminals):
        """Sets the share_cards_from_deactivated_terminals of this MerchantGeneralSetup.


        :param share_cards_from_deactivated_terminals: The share_cards_from_deactivated_terminals of this MerchantGeneralSetup.  # noqa: E501
        :type: bool
        """

        self._share_cards_from_deactivated_terminals = share_cards_from_deactivated_terminals

    @property
    def enable_merchant_level_limits(self):
        """Gets the enable_merchant_level_limits of this MerchantGeneralSetup.  # noqa: E501


        :return: The enable_merchant_level_limits of this MerchantGeneralSetup.  # noqa: E501
        :rtype: bool
        """
        return self._enable_merchant_level_limits

    @enable_merchant_level_limits.setter
    def enable_merchant_level_limits(self, enable_merchant_level_limits):
        """Sets the enable_merchant_level_limits of this MerchantGeneralSetup.


        :param enable_merchant_level_limits: The enable_merchant_level_limits of this MerchantGeneralSetup.  # noqa: E501
        :type: bool
        """

        self._enable_merchant_level_limits = enable_merchant_level_limits

    @property
    def merchant_level_limits(self):
        """Gets the merchant_level_limits of this MerchantGeneralSetup.  # noqa: E501


        :return: The merchant_level_limits of this MerchantGeneralSetup.  # noqa: E501
        :rtype: list[MerchantLevelLimit]
        """
        return self._merchant_level_limits

    @merchant_level_limits.setter
    def merchant_level_limits(self, merchant_level_limits):
        """Sets the merchant_level_limits of this MerchantGeneralSetup.


        :param merchant_level_limits: The merchant_level_limits of this MerchantGeneralSetup.  # noqa: E501
        :type: list[MerchantLevelLimit]
        """

        self._merchant_level_limits = merchant_level_limits

