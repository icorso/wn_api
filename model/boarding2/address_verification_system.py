# coding: utf-8
from model.serializable import SwaggerSerializable


class AddressVerificationSystem(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'action': 'str',
        'compulsory': 'bool',
        'preferred_address_mode': 'str',
        'auto_decline_on_failure': 'bool',
        'approval_codes': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'action': 'action',
        'compulsory': 'compulsory',
        'preferred_address_mode': 'preferredAddressMode',
        'auto_decline_on_failure': 'autoDeclineOnFailure',
        'approval_codes': 'approvalCodes'
    }

    def __init__(self, enable=False, action=None, compulsory=False, preferred_address_mode=None, auto_decline_on_failure=False, approval_codes=None):  # noqa: E501
        self._enable = None
        self._action = None
        self._compulsory = None
        self._preferred_address_mode = None
        self._auto_decline_on_failure = None
        self._approval_codes = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if action is not None:
            self.action = action
        if compulsory is not None:
            self.compulsory = compulsory
        if preferred_address_mode is not None:
            self.preferred_address_mode = preferred_address_mode
        if auto_decline_on_failure is not None:
            self.auto_decline_on_failure = auto_decline_on_failure
        if approval_codes is not None:
            self.approval_codes = approval_codes

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        allowed_values = ["HIDE", "DISPLAY", "EDITABLE"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def compulsory(self):
        return self._compulsory

    @compulsory.setter
    def compulsory(self, compulsory):
        self._compulsory = compulsory

    @property
    def preferred_address_mode(self):
        return self._preferred_address_mode

    @preferred_address_mode.setter
    def preferred_address_mode(self, preferred_address_mode):
        allowed_values = ["EXACT", "POSTAL"]  # noqa: E501
        if preferred_address_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `preferred_address_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(preferred_address_mode, allowed_values)
            )

        self._preferred_address_mode = preferred_address_mode

    @property
    def auto_decline_on_failure(self):
        return self._auto_decline_on_failure

    @auto_decline_on_failure.setter
    def auto_decline_on_failure(self, auto_decline_on_failure):
        self._auto_decline_on_failure = auto_decline_on_failure

    @property
    def approval_codes(self):
        return self._approval_codes

    @approval_codes.setter
    def approval_codes(self, approval_codes):
        allowed_values = ["Y", "A", "Z", "N", "U", "R", "G", "S", "F", "W", "X"]
        if not set(approval_codes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `approval_codes` [{0}], must be a subset of [{1}]".format(", ".join(map(str,
                    set(approval_codes) - set(allowed_values))), ", ".join(map(str, allowed_values)))
            )

        self._approval_codes = approval_codes
