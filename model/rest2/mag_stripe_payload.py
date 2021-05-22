# coding: utf-8

from model.rest2.payload import Payload
from model.serializable import SwaggerSerializable


class MagStripePayload(SwaggerSerializable):
    swagger_types = {
        'payload_type': 'str',
        'account_type': 'str',
        'downgrade_to': 'str',
        'cardholder_name': 'str',
        'cardholder_signature': 'str',
        'card_details': 'MagStripeDataFormat',
        'pin_details': 'DukptPinDetails',
        'ebt_details': 'EbtDetails'
    }
    if hasattr(Payload, "swagger_types"):
        swagger_types.update(Payload.swagger_types)

    attribute_map = {
        'payload_type': 'payloadType',
        'account_type': 'accountType',
        'downgrade_to': 'downgradeTo',
        'cardholder_name': 'cardholderName',
        'cardholder_signature': 'cardholderSignature',
        'card_details': 'cardDetails',
        'pin_details': 'pinDetails',
        'ebt_details': 'ebtDetails'
    }
    if hasattr(Payload, "attribute_map"):
        attribute_map.update(Payload.attribute_map)

    def __init__(self, payload_type=None, account_type='CHECKING', downgrade_to=None, cardholder_name=None, cardholder_signature=None, card_details=None, pin_details=None, ebt_details=None, *args, **kwargs):  # noqa: E501
        """MagStripePayload - a model defined in Swagger"""  # noqa: E501
        self._payload_type = None
        self._account_type = None
        self._downgrade_to = None
        self._cardholder_name = None
        self._cardholder_signature = None
        self._card_details = None
        self._pin_details = None
        self._ebt_details = None
        self.discriminator = None
        self.payload_type = payload_type
        if account_type is not None:
            self.account_type = account_type
        if downgrade_to is not None:
            self.downgrade_to = downgrade_to
        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if cardholder_signature is not None:
            self.cardholder_signature = cardholder_signature
        self.card_details = card_details
        if pin_details is not None:
            self.pin_details = pin_details
        if ebt_details is not None:
            self.ebt_details = ebt_details

    @property
    def payload_type(self):
        """Gets the payload_type of this MagStripePayload.  # noqa: E501


        :return: The payload_type of this MagStripePayload.  # noqa: E501
        :rtype: str
        """
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type):
        """Sets the payload_type of this MagStripePayload.


        :param payload_type: The payload_type of this MagStripePayload.  # noqa: E501
        :type: str
        """
        if payload_type is None:
            raise ValueError("Invalid value for `payload_type`, must not be `None`")  # noqa: E501

        self._payload_type = payload_type

    @property
    def account_type(self):
        """Gets the account_type of this MagStripePayload.  # noqa: E501


        :return: The account_type of this MagStripePayload.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this MagStripePayload.


        :param account_type: The account_type of this MagStripePayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["CHECKING", "SAVINGS"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def downgrade_to(self):
        """Gets the downgrade_to of this MagStripePayload.  # noqa: E501

        This field gives clients the ability to reprocess offline transactions that were not approved initially in a different entry mode.<br />For instance, `MAG_STRIPE` transactions are allowed to be downgraded to `KEYED`.  # noqa: E501

        :return: The downgrade_to of this MagStripePayload.  # noqa: E501
        :rtype: str
        """
        return self._downgrade_to

    @downgrade_to.setter
    def downgrade_to(self, downgrade_to):
        """Sets the downgrade_to of this MagStripePayload.

        This field gives clients the ability to reprocess offline transactions that were not approved initially in a different entry mode.<br />For instance, `MAG_STRIPE` transactions are allowed to be downgraded to `KEYED`.  # noqa: E501

        :param downgrade_to: The downgrade_to of this MagStripePayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["MAG_STRIPE", "KEYED"]  # noqa: E501
        if downgrade_to not in allowed_values:
            raise ValueError(
                "Invalid value for `downgrade_to` ({0}), must be one of {1}"  # noqa: E501
                .format(downgrade_to, allowed_values)
            )

        self._downgrade_to = downgrade_to

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this MagStripePayload.  # noqa: E501

        The cardholder's name as it appears on the card.  # noqa: E501

        :return: The cardholder_name of this MagStripePayload.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this MagStripePayload.

        The cardholder's name as it appears on the card.  # noqa: E501

        :param cardholder_name: The cardholder_name of this MagStripePayload.  # noqa: E501
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def cardholder_signature(self):
        """Gets the cardholder_signature of this MagStripePayload.  # noqa: E501

        Cardholder's signature in the format described in the [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters#the_signature_field_format) section.  # noqa: E501

        :return: The cardholder_signature of this MagStripePayload.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_signature

    @cardholder_signature.setter
    def cardholder_signature(self, cardholder_signature):
        """Sets the cardholder_signature of this MagStripePayload.

        Cardholder's signature in the format described in the [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters#the_signature_field_format) section.  # noqa: E501

        :param cardholder_signature: The cardholder_signature of this MagStripePayload.  # noqa: E501
        :type: str
        """

        self._cardholder_signature = cardholder_signature

    @property
    def card_details(self):
        """Gets the card_details of this MagStripePayload.  # noqa: E501


        :return: The card_details of this MagStripePayload.  # noqa: E501
        :rtype: MagStripeDataFormat
        """
        return self._card_details

    @card_details.setter
    def card_details(self, card_details):
        """Sets the card_details of this MagStripePayload.


        :param card_details: The card_details of this MagStripePayload.  # noqa: E501
        :type: MagStripeDataFormat
        """
        if card_details is None:
            raise ValueError("Invalid value for `card_details`, must not be `None`")  # noqa: E501

        self._card_details = card_details

    @property
    def pin_details(self):
        """Gets the pin_details of this MagStripePayload.  # noqa: E501


        :return: The pin_details of this MagStripePayload.  # noqa: E501
        :rtype: DukptPinDetails
        """
        return self._pin_details

    @pin_details.setter
    def pin_details(self, pin_details):
        """Sets the pin_details of this MagStripePayload.


        :param pin_details: The pin_details of this MagStripePayload.  # noqa: E501
        :type: DukptPinDetails
        """

        self._pin_details = pin_details

    @property
    def ebt_details(self):
        """Gets the ebt_details of this MagStripePayload.  # noqa: E501


        :return: The ebt_details of this MagStripePayload.  # noqa: E501
        :rtype: EbtDetails
        """
        return self._ebt_details

    @ebt_details.setter
    def ebt_details(self, ebt_details):
        """Sets the ebt_details of this MagStripePayload.


        :param ebt_details: The ebt_details of this MagStripePayload.  # noqa: E501
        :type: EbtDetails
        """

        self._ebt_details = ebt_details
