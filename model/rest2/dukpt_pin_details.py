# coding: utf-8

from model.serializable import SwaggerSerializable


class DukptPinDetails(SwaggerSerializable):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pin': 'str',
        'pin_ksn': 'str'
    }

    attribute_map = {
        'pin': 'pin',
        'pin_ksn': 'pinKsn'
    }

    def __init__(self, pin=None, pin_ksn=None):  # noqa: E501
        """DukptPinDetails - a model defined in Swagger"""  # noqa: E501
        self._pin = None
        self._pin_ksn = None
        self.discriminator = None
        self.pin = pin
        self.pin_ksn = pin_ksn

    @property
    def pin(self):
        """Gets the pin of this DukptPinDetails.  # noqa: E501

        The PIN encrypted using [DUKPT](https://en.wikipedia.org/wiki/Derived_unique_key_per_transaction) Scheme.  # noqa: E501

        :return: The pin of this DukptPinDetails.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this DukptPinDetails.

        The PIN encrypted using [DUKPT](https://en.wikipedia.org/wiki/Derived_unique_key_per_transaction) Scheme.  # noqa: E501

        :param pin: The pin of this DukptPinDetails.  # noqa: E501
        :type: str
        """
        if pin is None:
            raise ValueError("Invalid value for `pin`, must not be `None`")  # noqa: E501

        self._pin = pin

    @property
    def pin_ksn(self):
        """Gets the pin_ksn of this DukptPinDetails.  # noqa: E501

        The key serial number.  # noqa: E501

        :return: The pin_ksn of this DukptPinDetails.  # noqa: E501
        :rtype: str
        """
        return self._pin_ksn

    @pin_ksn.setter
    def pin_ksn(self, pin_ksn):
        """Sets the pin_ksn of this DukptPinDetails.

        The key serial number.  # noqa: E501

        :param pin_ksn: The pin_ksn of this DukptPinDetails.  # noqa: E501
        :type: str
        """
        if pin_ksn is None:
            raise ValueError("Invalid value for `pin_ksn`, must not be `None`")  # noqa: E501

        self._pin_ksn = pin_ksn
