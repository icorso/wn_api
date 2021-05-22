# coding: utf-8

from model.rest2.payload import Payload
from model.serializable import SwaggerSerializable


class KeyedPayload(SwaggerSerializable):
    swagger_types = {
        'payload_type': 'str',
        'account_type': 'str',
        'cardholder_name': 'str',
        'card_details': 'KeyedDataFormat',
        'pin_details': 'DukptPinDetails',
        'ebt_details': 'EbtDetails',
        'save_payment_credentials': 'SavePaymentCredentials'
    }
    if hasattr(Payload, "swagger_types"):
        swagger_types.update(Payload.swagger_types)

    attribute_map = {
        'payload_type': 'payloadType',
        'account_type': 'accountType',
        'cardholder_name': 'cardholderName',
        'card_details': 'cardDetails',
        'pin_details': 'pinDetails',
        'ebt_details': 'ebtDetails',
        'save_payment_credentials': 'savePaymentCredentials'
    }
    if hasattr(Payload, "attribute_map"):
        attribute_map.update(Payload.attribute_map)

    def __init__(self, payload_type=None, account_type='CHECKING', cardholder_name=None, card_details=None, pin_details=None, ebt_details=None, save_payment_credentials=None, *args, **kwargs):  # noqa: E501
        """KeyedPayload - a model defined in Swagger"""  # noqa: E501
        self._payload_type = None
        self._account_type = None
        self._cardholder_name = None
        self._card_details = None
        self._pin_details = None
        self._ebt_details = None
        self._save_payment_credentials = None
        self.discriminator = None
        self.payload_type = payload_type
        if account_type is not None:
            self.account_type = account_type
        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        self.card_details = card_details
        if pin_details is not None:
            self.pin_details = pin_details
        if ebt_details is not None:
            self.ebt_details = ebt_details
        if save_payment_credentials is not None:
            self.save_payment_credentials = save_payment_credentials

    @property
    def payload_type(self):
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type):
        if payload_type is None:
            raise ValueError("Invalid value for `payload_type`, must not be `None`")  # noqa: E501

        self._payload_type = payload_type

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        allowed_values = ["CHECKING", "SAVINGS"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def cardholder_name(self):
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        self._cardholder_name = cardholder_name

    @property
    def card_details(self):
        return self._card_details

    @card_details.setter
    def card_details(self, card_details):
        if card_details is None:
            raise ValueError("Invalid value for `card_details`, must not be `None`")  # noqa: E501

        self._card_details = card_details

    @property
    def pin_details(self):
        return self._pin_details

    @pin_details.setter
    def pin_details(self, pin_details):
        self._pin_details = pin_details

    @property
    def ebt_details(self):
        return self._ebt_details

    @ebt_details.setter
    def ebt_details(self, ebt_details):
        self._ebt_details = ebt_details

    @property
    def save_payment_credentials(self):
        return self._save_payment_credentials

    @save_payment_credentials.setter
    def save_payment_credentials(self, save_payment_credentials):
        self._save_payment_credentials = save_payment_credentials
