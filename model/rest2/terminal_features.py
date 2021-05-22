# coding: utf-8

from model.serializable import SwaggerSerializable


class TerminalFeatures(SwaggerSerializable):
    swagger_types = {
        'allow_offline_sales': 'bool',
        'allow_partial_refund': 'bool',
        'allow_tax': 'bool',
        'allow_tip': 'bool',
        'allow_google_pay': 'bool',
        'allow_apple_pay': 'bool',
        'allow_emv': 'bool',
        'allow_keyed': 'bool',
        'allow_mag_stripe': 'bool',
        'allow_mag_stripe_fallback': 'bool',
        'secure_credentials': 'SecureCredentialsSettings',
        'surcharge': 'SurchargeSettings'
    }

    attribute_map = {
        'allow_offline_sales': 'allowOfflineSales',
        'allow_partial_refund': 'allowPartialRefund',
        'allow_tax': 'allowTax',
        'allow_tip': 'allowTip',
        'allow_google_pay': 'allowGooglePay',
        'allow_apple_pay': 'allowApplePay',
        'allow_emv': 'allowEmv',
        'allow_keyed': 'allowKeyed',
        'allow_mag_stripe': 'allowMagStripe',
        'allow_mag_stripe_fallback': 'allowMagStripeFallback',
        'secure_credentials': 'secureCredentials',
        'surcharge': 'surcharge'
    }

    def __init__(self, allow_offline_sales=None, allow_partial_refund=None, allow_tax=None, allow_tip=None, allow_google_pay=None, allow_apple_pay=None, allow_emv=None, allow_keyed=None, allow_mag_stripe=None, allow_mag_stripe_fallback=None, secure_credentials=None, surcharge=None):  # noqa: E501
        """TerminalFeatures - a model defined in Swagger"""  # noqa: E501
        self._allow_offline_sales = None
        self._allow_partial_refund = None
        self._allow_tax = None
        self._allow_tip = None
        self._allow_google_pay = None
        self._allow_apple_pay = None
        self._allow_emv = None
        self._allow_keyed = None
        self._allow_mag_stripe = None
        self._allow_mag_stripe_fallback = None
        self._secure_credentials = None
        self._surcharge = None
        self.discriminator = None
        self.allow_offline_sales = allow_offline_sales
        self.allow_partial_refund = allow_partial_refund
        self.allow_tax = allow_tax
        self.allow_tip = allow_tip
        self.allow_google_pay = allow_google_pay
        self.allow_apple_pay = allow_apple_pay
        self.allow_emv = allow_emv
        self.allow_keyed = allow_keyed
        self.allow_mag_stripe = allow_mag_stripe
        self.allow_mag_stripe_fallback = allow_mag_stripe_fallback
        if secure_credentials is not None:
            self.secure_credentials = secure_credentials
        if surcharge is not None:
            self.surcharge = surcharge

    @property
    def allow_offline_sales(self):
        """Gets the allow_offline_sales of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal allows offline sales.  # noqa: E501

        :return: The allow_offline_sales of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_offline_sales

    @allow_offline_sales.setter
    def allow_offline_sales(self, allow_offline_sales):
        """Sets the allow_offline_sales of this TerminalFeatures.

        Indicates whether the terminal allows offline sales.  # noqa: E501

        :param allow_offline_sales: The allow_offline_sales of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_offline_sales is None:
            raise ValueError("Invalid value for `allow_offline_sales`, must not be `None`")  # noqa: E501

        self._allow_offline_sales = allow_offline_sales

    @property
    def allow_partial_refund(self):
        """Gets the allow_partial_refund of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal allows partial refunds.  # noqa: E501

        :return: The allow_partial_refund of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_partial_refund

    @allow_partial_refund.setter
    def allow_partial_refund(self, allow_partial_refund):
        """Sets the allow_partial_refund of this TerminalFeatures.

        Indicates whether the terminal allows partial refunds.  # noqa: E501

        :param allow_partial_refund: The allow_partial_refund of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_partial_refund is None:
            raise ValueError("Invalid value for `allow_partial_refund`, must not be `None`")  # noqa: E501

        self._allow_partial_refund = allow_partial_refund

    @property
    def allow_tax(self):
        """Gets the allow_tax of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal is able to process taxes.  # noqa: E501

        :return: The allow_tax of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_tax

    @allow_tax.setter
    def allow_tax(self, allow_tax):
        """Sets the allow_tax of this TerminalFeatures.

        Indicates whether the terminal is able to process taxes.  # noqa: E501

        :param allow_tax: The allow_tax of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_tax is None:
            raise ValueError("Invalid value for `allow_tax`, must not be `None`")  # noqa: E501

        self._allow_tax = allow_tax

    @property
    def allow_tip(self):
        """Gets the allow_tip of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal is able to process tips.  # noqa: E501

        :return: The allow_tip of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_tip

    @allow_tip.setter
    def allow_tip(self, allow_tip):
        """Sets the allow_tip of this TerminalFeatures.

        Indicates whether the terminal is able to process tips.  # noqa: E501

        :param allow_tip: The allow_tip of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_tip is None:
            raise ValueError("Invalid value for `allow_tip`, must not be `None`")  # noqa: E501

        self._allow_tip = allow_tip

    @property
    def allow_google_pay(self):
        """Gets the allow_google_pay of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal is able to handle digital wallet payloads from Google Pay.  # noqa: E501

        :return: The allow_google_pay of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_google_pay

    @allow_google_pay.setter
    def allow_google_pay(self, allow_google_pay):
        """Sets the allow_google_pay of this TerminalFeatures.

        Indicates whether the terminal is able to handle digital wallet payloads from Google Pay.  # noqa: E501

        :param allow_google_pay: The allow_google_pay of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_google_pay is None:
            raise ValueError("Invalid value for `allow_google_pay`, must not be `None`")  # noqa: E501

        self._allow_google_pay = allow_google_pay

    @property
    def allow_apple_pay(self):
        """Gets the allow_apple_pay of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal is able to handle digital wallet payloads from Apple Pay.  # noqa: E501

        :return: The allow_apple_pay of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_apple_pay

    @allow_apple_pay.setter
    def allow_apple_pay(self, allow_apple_pay):
        """Sets the allow_apple_pay of this TerminalFeatures.

        Indicates whether the terminal is able to handle digital wallet payloads from Apple Pay.  # noqa: E501

        :param allow_apple_pay: The allow_apple_pay of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_apple_pay is None:
            raise ValueError("Invalid value for `allow_apple_pay`, must not be `None`")  # noqa: E501

        self._allow_apple_pay = allow_apple_pay

    @property
    def allow_emv(self):
        """Gets the allow_emv of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal is able to handle card payloads from EMV devices.  # noqa: E501

        :return: The allow_emv of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_emv

    @allow_emv.setter
    def allow_emv(self, allow_emv):
        """Sets the allow_emv of this TerminalFeatures.

        Indicates whether the terminal is able to handle card payloads from EMV devices.  # noqa: E501

        :param allow_emv: The allow_emv of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_emv is None:
            raise ValueError("Invalid value for `allow_emv`, must not be `None`")  # noqa: E501

        self._allow_emv = allow_emv

    @property
    def allow_keyed(self):
        """Gets the allow_keyed of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal is able to handle manually keyed card details.  # noqa: E501

        :return: The allow_keyed of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_keyed

    @allow_keyed.setter
    def allow_keyed(self, allow_keyed):
        """Sets the allow_keyed of this TerminalFeatures.

        Indicates whether the terminal is able to handle manually keyed card details.  # noqa: E501

        :param allow_keyed: The allow_keyed of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_keyed is None:
            raise ValueError("Invalid value for `allow_keyed`, must not be `None`")  # noqa: E501

        self._allow_keyed = allow_keyed

    @property
    def allow_mag_stripe(self):
        """Gets the allow_mag_stripe of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal is able to handle card payloads from MSR devices.  # noqa: E501

        :return: The allow_mag_stripe of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_mag_stripe

    @allow_mag_stripe.setter
    def allow_mag_stripe(self, allow_mag_stripe):
        """Sets the allow_mag_stripe of this TerminalFeatures.

        Indicates whether the terminal is able to handle card payloads from MSR devices.  # noqa: E501

        :param allow_mag_stripe: The allow_mag_stripe of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_mag_stripe is None:
            raise ValueError("Invalid value for `allow_mag_stripe`, must not be `None`")  # noqa: E501

        self._allow_mag_stripe = allow_mag_stripe

    @property
    def allow_mag_stripe_fallback(self):
        """Gets the allow_mag_stripe_fallback of this TerminalFeatures.  # noqa: E501

        Indicates whether the terminal allows transactions to fallback to swipe method due to chip card reader failures.  # noqa: E501

        :return: The allow_mag_stripe_fallback of this TerminalFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allow_mag_stripe_fallback

    @allow_mag_stripe_fallback.setter
    def allow_mag_stripe_fallback(self, allow_mag_stripe_fallback):
        """Sets the allow_mag_stripe_fallback of this TerminalFeatures.

        Indicates whether the terminal allows transactions to fallback to swipe method due to chip card reader failures.  # noqa: E501

        :param allow_mag_stripe_fallback: The allow_mag_stripe_fallback of this TerminalFeatures.  # noqa: E501
        :type: bool
        """
        if allow_mag_stripe_fallback is None:
            raise ValueError("Invalid value for `allow_mag_stripe_fallback`, must not be `None`")  # noqa: E501

        self._allow_mag_stripe_fallback = allow_mag_stripe_fallback

    @property
    def secure_credentials(self):
        """Gets the secure_credentials of this TerminalFeatures.  # noqa: E501


        :return: The secure_credentials of this TerminalFeatures.  # noqa: E501
        :rtype: SecureCredentialsSettings
        """
        return self._secure_credentials

    @secure_credentials.setter
    def secure_credentials(self, secure_credentials):
        """Sets the secure_credentials of this TerminalFeatures.


        :param secure_credentials: The secure_credentials of this TerminalFeatures.  # noqa: E501
        :type: SecureCredentialsSettings
        """

        self._secure_credentials = secure_credentials

    @property
    def surcharge(self):
        """Gets the surcharge of this TerminalFeatures.  # noqa: E501


        :return: The surcharge of this TerminalFeatures.  # noqa: E501
        :rtype: SurchargeSettings
        """
        return self._surcharge

    @surcharge.setter
    def surcharge(self, surcharge):
        """Sets the surcharge of this TerminalFeatures.


        :param surcharge: The surcharge of this TerminalFeatures.  # noqa: E501
        :type: SurchargeSettings
        """

        self._surcharge = surcharge
