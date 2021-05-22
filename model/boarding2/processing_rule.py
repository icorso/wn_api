# coding: utf-8
from model.serializable import SwaggerSerializable


class ProcessingRule(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'conditions': 'list[ProcessingRulePredicate]',
        'then': 'ProcessingRuleInstruction'
    }

    attribute_map = {
        'enable': 'enable',
        'conditions': 'conditions',
        'then': 'then'
    }

    def __init__(self, enable=False, conditions=None, then=None):
        self._enable = None
        self._conditions = None
        self._then = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if conditions is not None:
            self.conditions = conditions
        if then is not None:
            self.then = then

    @property
    def enable(self):
        """Gets the enable of this ProcessingRule.  # noqa: E501

        Indicates whether the rule should be evaluated.  # noqa: E501

        :return: The enable of this ProcessingRule.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this ProcessingRule.

        Indicates whether the rule should be evaluated.  # noqa: E501

        :param enable: The enable of this ProcessingRule.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def conditions(self):
        """Gets the conditions of this ProcessingRule.  # noqa: E501

        The conditions that trigger the action, if met.  # noqa: E501

        :return: The conditions of this ProcessingRule.  # noqa: E501
        :rtype: list[ProcessingRulePredicate]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ProcessingRule.

        The conditions that trigger the action, if met.  # noqa: E501

        :param conditions: The conditions of this ProcessingRule.  # noqa: E501
        :type: list[ProcessingRulePredicate]
        """

        self._conditions = conditions

    @property
    def then(self):
        """Gets the then of this ProcessingRule.  # noqa: E501


        :return: The then of this ProcessingRule.  # noqa: E501
        :rtype: ProcessingRuleInstruction
        """
        return self._then

    @then.setter
    def then(self, then):
        """Sets the then of this ProcessingRule.


        :param then: The then of this ProcessingRule.  # noqa: E501
        :type: ProcessingRuleInstruction
        """

        self._then = then
