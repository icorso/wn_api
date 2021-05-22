# coding: utf-8
from model.rest2 import ProcessingRulePredicate
from model.serializable import SwaggerSerializable


class TenderTypePredicate(SwaggerSerializable):
    swagger_types = {
        'when': 'str',
        '_is': 'str',
        'value': 'str'
    }
    if hasattr(ProcessingRulePredicate, "swagger_types"):
        swagger_types.update(ProcessingRulePredicate.swagger_types)

    attribute_map = {
        'when': 'when',
        '_is': 'is',
        'value': 'value'
    }
    if hasattr(ProcessingRulePredicate, "attribute_map"):
        attribute_map.update(ProcessingRulePredicate.attribute_map)

    def __init__(self, when=None, _is=None, value=None, *args, **kwargs):  # noqa: E501
        """TenderTypePredicate - a model defined in Swagger"""  # noqa: E501
        self._when = None
        self.__is = None
        self._value = None
        self.discriminator = None
        self.when = when
        self._is = _is
        self.value = value
        ProcessingRulePredicate.__init__(self, *args, **kwargs)

    @property
    def when(self):
        """Gets the when of this TenderTypePredicate.  # noqa: E501


        :return: The when of this TenderTypePredicate.  # noqa: E501
        :rtype: str
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this TenderTypePredicate.


        :param when: The when of this TenderTypePredicate.  # noqa: E501
        :type: str
        """
        if when is None:
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501

        self._when = when

    @property
    def _is(self):
        """Gets the _is of this TenderTypePredicate.  # noqa: E501

        The comparison operator.  # noqa: E501

        :return: The _is of this TenderTypePredicate.  # noqa: E501
        :rtype: str
        """
        return self.__is

    @_is.setter
    def _is(self, _is):
        """Sets the _is of this TenderTypePredicate.

        The comparison operator.  # noqa: E501

        :param _is: The _is of this TenderTypePredicate.  # noqa: E501
        :type: str
        """
        if _is is None:
            raise ValueError("Invalid value for `_is`, must not be `None`")  # noqa: E501
        allowed_values = ["EQUALS"]  # noqa: E501
        if _is not in allowed_values:
            raise ValueError(
                "Invalid value for `_is` ({0}), must be one of {1}"  # noqa: E501
                .format(_is, allowed_values)
            )

        self.__is = _is

    @property
    def value(self):
        """Gets the value of this TenderTypePredicate.  # noqa: E501

        The required value for the condition to be met.  # noqa: E501

        :return: The value of this TenderTypePredicate.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TenderTypePredicate.

        The required value for the condition to be met.  # noqa: E501

        :param value: The value of this TenderTypePredicate.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        allowed_values = ["CREDIT_DEBIT", "EBT"]  # noqa: E501
        if value not in allowed_values:
            raise ValueError(
                "Invalid value for `value` ({0}), must be one of {1}"  # noqa: E501
                .format(value, allowed_values)
            )

        self._value = value
