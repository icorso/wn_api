# coding: utf-8
from model.serializable import SwaggerSerializable


class ProcessingRuleInstruction(SwaggerSerializable):
    swagger_types = {
        'action': 'str',
        'terminal_number': 'str'
    }

    attribute_map = {
        'action': 'action',
        'terminal_number': 'terminalNumber'
    }

    def __init__(self, action=None, terminal_number=None):  # noqa: E501
        """ProcessingRuleInstruction - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._terminal_number = None
        self.discriminator = None
        self.action = action
        if terminal_number is not None:
            self.terminal_number = terminal_number

    @property
    def action(self):
        """Gets the action of this ProcessingRuleInstruction.  # noqa: E501

        The action to be performed when the conditions are met.  # noqa: E501

        :return: The action of this ProcessingRuleInstruction.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ProcessingRuleInstruction.

        The action to be performed when the conditions are met.  # noqa: E501

        :param action: The action of this ProcessingRuleInstruction.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["ROUTE_TO_TERMINAL"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def terminal_number(self):
        """Gets the terminal_number of this ProcessingRuleInstruction.  # noqa: E501

        The number of the terminal which is the target of the action.  # noqa: E501

        :return: The terminal_number of this ProcessingRuleInstruction.  # noqa: E501
        :rtype: str
        """
        return self._terminal_number

    @terminal_number.setter
    def terminal_number(self, terminal_number):
        """Sets the terminal_number of this ProcessingRuleInstruction.

        The number of the terminal which is the target of the action.  # noqa: E501

        :param terminal_number: The terminal_number of this ProcessingRuleInstruction.  # noqa: E501
        :type: str
        """

        self._terminal_number = terminal_number
