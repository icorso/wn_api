# coding: utf-8
from model.serializable import SwaggerSerializable


class TerminalReceiptNotifications(SwaggerSerializable):
    swagger_types = {
        'show_email_field_on_virtual_terminal': 'bool',
        'merchant_support_email': 'str',
        'notification_emails': 'list[str]',
        'notification_language': 'str',
        'disable_receipts': 'bool',
        'enable_cardholder_email_receipt': 'bool',
        'email_receipt_response_codes': 'list[str]',
        'email_receipt_transaction_types': 'list[str]',
        'enable_cardholder_sms_receipt': 'bool',
        'sms_receipt_response_codes': 'list[str]',
        'sms_receipt_transaction_types': 'list[str]'
    }

    attribute_map = {
        'show_email_field_on_virtual_terminal': 'showEmailFieldOnVirtualTerminal',
        'merchant_support_email': 'merchantSupportEmail',
        'notification_emails': 'notificationEmails',
        'notification_language': 'notificationLanguage',
        'disable_receipts': 'disableReceipts',
        'enable_cardholder_email_receipt': 'enableCardholderEmailReceipt',
        'email_receipt_response_codes': 'emailReceiptResponseCodes',
        'email_receipt_transaction_types': 'emailReceiptTransactionTypes',
        'enable_cardholder_sms_receipt': 'enableCardholderSmsReceipt',
        'sms_receipt_response_codes': 'smsReceiptResponseCodes',
        'sms_receipt_transaction_types': 'smsReceiptTransactionTypes'
    }

    def __init__(self, show_email_field_on_virtual_terminal=False, merchant_support_email=None, notification_emails=None, notification_language=None, disable_receipts=False, enable_cardholder_email_receipt=False, email_receipt_response_codes=None, email_receipt_transaction_types=None, enable_cardholder_sms_receipt=False, sms_receipt_response_codes=None, sms_receipt_transaction_types=None):  # noqa: E501
        self._show_email_field_on_virtual_terminal = None
        self._merchant_support_email = None
        self._notification_emails = None
        self._notification_language = None
        self._disable_receipts = None
        self._enable_cardholder_email_receipt = None
        self._email_receipt_response_codes = None
        self._email_receipt_transaction_types = None
        self._enable_cardholder_sms_receipt = None
        self._sms_receipt_response_codes = None
        self._sms_receipt_transaction_types = None
        self.discriminator = None
        if show_email_field_on_virtual_terminal is not None:
            self.show_email_field_on_virtual_terminal = show_email_field_on_virtual_terminal
        if merchant_support_email is not None:
            self.merchant_support_email = merchant_support_email
        if notification_emails is not None:
            self.notification_emails = notification_emails
        if notification_language is not None:
            self.notification_language = notification_language
        if disable_receipts is not None:
            self.disable_receipts = disable_receipts
        if enable_cardholder_email_receipt is not None:
            self.enable_cardholder_email_receipt = enable_cardholder_email_receipt
        if email_receipt_response_codes is not None:
            self.email_receipt_response_codes = email_receipt_response_codes
        if email_receipt_transaction_types is not None:
            self.email_receipt_transaction_types = email_receipt_transaction_types
        if enable_cardholder_sms_receipt is not None:
            self.enable_cardholder_sms_receipt = enable_cardholder_sms_receipt
        if sms_receipt_response_codes is not None:
            self.sms_receipt_response_codes = sms_receipt_response_codes
        if sms_receipt_transaction_types is not None:
            self.sms_receipt_transaction_types = sms_receipt_transaction_types

    @property
    def show_email_field_on_virtual_terminal(self):
        return self._show_email_field_on_virtual_terminal

    @show_email_field_on_virtual_terminal.setter
    def show_email_field_on_virtual_terminal(self, show_email_field_on_virtual_terminal):
        self._show_email_field_on_virtual_terminal = show_email_field_on_virtual_terminal

    @property
    def merchant_support_email(self):
        return self._merchant_support_email

    @merchant_support_email.setter
    def merchant_support_email(self, merchant_support_email):
        self._merchant_support_email = merchant_support_email

    @property
    def notification_emails(self):
        return self._notification_emails

    @notification_emails.setter
    def notification_emails(self, notification_emails):
        self._notification_emails = notification_emails

    @property
    def notification_language(self):
        return self._notification_language

    @notification_language.setter
    def notification_language(self, notification_language):
        self._notification_language = notification_language

    @property
    def disable_receipts(self):
        return self._disable_receipts

    @disable_receipts.setter
    def disable_receipts(self, disable_receipts):
        self._disable_receipts = disable_receipts

    @property
    def enable_cardholder_email_receipt(self):
        return self._enable_cardholder_email_receipt

    @enable_cardholder_email_receipt.setter
    def enable_cardholder_email_receipt(self, enable_cardholder_email_receipt):
        self._enable_cardholder_email_receipt = enable_cardholder_email_receipt

    @property
    def email_receipt_response_codes(self):
        return self._email_receipt_response_codes

    @email_receipt_response_codes.setter
    def email_receipt_response_codes(self, email_receipt_response_codes):
        allowed_values = ["APPROVAL", "DECLINE", "REFERRAL", "OTHER"]  # noqa: E501
        if not set(email_receipt_response_codes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `email_receipt_response_codes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(email_receipt_response_codes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._email_receipt_response_codes = email_receipt_response_codes

    @property
    def email_receipt_transaction_types(self):
        return self._email_receipt_transaction_types

    @email_receipt_transaction_types.setter
    def email_receipt_transaction_types(self, email_receipt_transaction_types):
        allowed_values = ["SALE", "RETURN"]  # noqa: E501
        if not set(email_receipt_transaction_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `email_receipt_transaction_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(email_receipt_transaction_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._email_receipt_transaction_types = email_receipt_transaction_types

    @property
    def enable_cardholder_sms_receipt(self):
        return self._enable_cardholder_sms_receipt

    @enable_cardholder_sms_receipt.setter
    def enable_cardholder_sms_receipt(self, enable_cardholder_sms_receipt):
        self._enable_cardholder_sms_receipt = enable_cardholder_sms_receipt

    @property
    def sms_receipt_response_codes(self):
        return self._sms_receipt_response_codes

    @sms_receipt_response_codes.setter
    def sms_receipt_response_codes(self, sms_receipt_response_codes):
        allowed_values = ["APPROVAL", "DECLINE", "REFERRAL", "OTHER"]  # noqa: E501
        if not set(sms_receipt_response_codes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `sms_receipt_response_codes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(sms_receipt_response_codes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._sms_receipt_response_codes = sms_receipt_response_codes

    @property
    def sms_receipt_transaction_types(self):
        return self._sms_receipt_transaction_types

    @sms_receipt_transaction_types.setter
    def sms_receipt_transaction_types(self, sms_receipt_transaction_types):
        allowed_values = ["SALE", "RETURN"]  # noqa: E501
        if not set(sms_receipt_transaction_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `sms_receipt_transaction_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(sms_receipt_transaction_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._sms_receipt_transaction_types = sms_receipt_transaction_types

