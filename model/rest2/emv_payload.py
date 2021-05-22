# coding: utf-8

from model.rest2.payload import Payload
from model.serializable import SwaggerSerializable


class EmvPayload(SwaggerSerializable):
    swagger_types = {
        'payload_type': 'str',
        'account_type': 'str',
        'downgrade_to': 'str',
        'device': 'EncryptionCapableDevice',
        'tlv': 'str',
        'tags': 'list[EmvTag]',
        'first_digit_of_pan': 'str',
        'cardholder_signature': 'str',
        'save_payment_credentials': 'SavePaymentCredentials'
    }
    if hasattr(Payload, "swagger_types"):
        swagger_types.update(Payload.swagger_types)

    attribute_map = {
        'payload_type': 'payloadType',
        'account_type': 'accountType',
        'downgrade_to': 'downgradeTo',
        'device': 'device',
        'tlv': 'tlv',
        'tags': 'tags',
        'first_digit_of_pan': 'firstDigitOfPan',
        'cardholder_signature': 'cardholderSignature',
        'save_payment_credentials': 'savePaymentCredentials'
    }
    if hasattr(Payload, "attribute_map"):
        attribute_map.update(Payload.attribute_map)

    def __init__(self, payload_type=None, account_type='CHECKING', downgrade_to=None, device=None, tlv=None, tags=None, first_digit_of_pan=None, cardholder_signature=None, save_payment_credentials=None, *args, **kwargs):  # noqa: E501
        """EmvPayload - a model defined in Swagger"""  # noqa: E501
        self._payload_type = None
        self._account_type = None
        self._downgrade_to = None
        self._device = None
        self._tlv = None
        self._tags = None
        self._first_digit_of_pan = None
        self._cardholder_signature = None
        self._save_payment_credentials = None
        self.discriminator = None
        self.payload_type = payload_type
        if account_type is not None:
            self.account_type = account_type
        if downgrade_to is not None:
            self.downgrade_to = downgrade_to
        self.device = device
        if tlv is not None:
            self.tlv = tlv
        if tags is not None:
            self.tags = tags
        if first_digit_of_pan is not None:
            self.first_digit_of_pan = first_digit_of_pan
        if cardholder_signature is not None:
            self.cardholder_signature = cardholder_signature
        if save_payment_credentials is not None:
            self.save_payment_credentials = save_payment_credentials

    @property
    def payload_type(self):
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type):
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
    def downgrade_to(self):
        return self._downgrade_to

    @downgrade_to.setter
    def downgrade_to(self, downgrade_to):
        allowed_values = ["MAG_STRIPE", "KEYED"]  # noqa: E501
        if downgrade_to not in allowed_values:
            raise ValueError(
                "Invalid value for `downgrade_to` ({0}), must be one of {1}"  # noqa: E501
                .format(downgrade_to, allowed_values)
            )

        self._downgrade_to = downgrade_to

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, device):
        self._device = device

    @property
    def tlv(self):
        return self._tlv

    @tlv.setter
    def tlv(self, tlv):
        self._tlv = tlv

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags

    @property
    def first_digit_of_pan(self):
        return self._first_digit_of_pan

    @first_digit_of_pan.setter
    def first_digit_of_pan(self, first_digit_of_pan):
        self._first_digit_of_pan = first_digit_of_pan

    @property
    def cardholder_signature(self):
        return self._cardholder_signature

    @cardholder_signature.setter
    def cardholder_signature(self, cardholder_signature):
        self._cardholder_signature = cardholder_signature

    @property
    def save_payment_credentials(self):
        return self._save_payment_credentials

    @save_payment_credentials.setter
    def save_payment_credentials(self, save_payment_credentials):
        self._save_payment_credentials = save_payment_credentials
