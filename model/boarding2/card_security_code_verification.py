# coding: utf-8

import six

from model.serializable import SwaggerSerializable


class CardSecurityCodeVerification(SwaggerSerializable):
    swagger_types = {
        'enable': 'bool',
        'auto_decline_on_failure': 'bool',
        'decline_codes': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'auto_decline_on_failure': 'autoDeclineOnFailure',
        'decline_codes': 'declineCodes'
    }

    def __init__(self, enable=False, auto_decline_on_failure=False, decline_codes=None):  # noqa: E501
        """CardSecurityCodeVerification - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._auto_decline_on_failure = None
        self._decline_codes = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if auto_decline_on_failure is not None:
            self.auto_decline_on_failure = auto_decline_on_failure
        if decline_codes is not None:
            self.decline_codes = decline_codes

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, enable):
        self._enable = enable

    @property
    def auto_decline_on_failure(self):
        return self._auto_decline_on_failure

    @auto_decline_on_failure.setter
    def auto_decline_on_failure(self, auto_decline_on_failure):
        self._auto_decline_on_failure = auto_decline_on_failure

    @property
    def decline_codes(self):
        return self._decline_codes

    @decline_codes.setter
    def decline_codes(self, decline_codes):
        allowed_values = ["M", "N", "P", "U"]
        if not set(decline_codes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `decline_codes` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(decline_codes) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._decline_codes = decline_codes

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CardSecurityCodeVerification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def __eq__(self, other):
        if not isinstance(other, CardSecurityCodeVerification):
            return False

        return self.__dict__ == other.__dict__
