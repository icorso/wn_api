# coding: utf-8
from model.serializable import SwaggerSerializable


class Customer(SwaggerSerializable):
    swagger_types = {
        'name': 'str',
        'phone': 'str',
        'email': 'str',
        'notification_language': 'str',
        'billing_address': 'Address',
        'shipping_address': 'Address'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'email': 'email',
        'notification_language': 'notificationLanguage',
        'billing_address': 'billingAddress',
        'shipping_address': 'shippingAddress'
    }

    def __init__(self, name=None, phone=None, email=None, notification_language=None, billing_address=None, shipping_address=None):  # noqa: E501
        """Customer - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._phone = None
        self._email = None
        self._notification_language = None
        self._billing_address = None
        self._shipping_address = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if notification_language is not None:
            self.notification_language = notification_language
        if billing_address is not None:
            self.billing_address = billing_address
        if shipping_address is not None:
            self.shipping_address = shipping_address

    @property
    def name(self):
        """Gets the name of this Customer.  # noqa: E501

        The customer's name.  # noqa: E501

        :return: The name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Customer.

        The customer's name.  # noqa: E501

        :param name: The name of this Customer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this Customer.  # noqa: E501

        The customer's contact phone number.<br />If **SMS Cardholder Receipts** feature is enabled in the terminal, We will use this number to automatically send the receipts of eventual transactions.  # noqa: E501

        :return: The phone of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Customer.

        The customer's contact phone number.<br />If **SMS Cardholder Receipts** feature is enabled in the terminal, We will use this number to automatically send the receipts of eventual transactions.  # noqa: E501

        :param phone: The phone of this Customer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this Customer.  # noqa: E501

        The customer's contact email address.<br />If **Email Cardholder Receipt** feature is enabled in the terminal, We will use this address to automatically send the receipts of eventual transactions.  # noqa: E501

        :return: The email of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Customer.

        The customer's contact email address.<br />If **Email Cardholder Receipt** feature is enabled in the terminal, We will use this address to automatically send the receipts of eventual transactions.  # noqa: E501

        :param email: The email of this Customer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def notification_language(self):
        """Gets the notification_language of this Customer.  # noqa: E501

        The customer's preferred notification language.<br />The two-letter language code defined by the [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard.  # noqa: E501

        :return: The notification_language of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._notification_language

    @notification_language.setter
    def notification_language(self, notification_language):
        """Sets the notification_language of this Customer.

        The customer's preferred notification language.<br />The two-letter language code defined by the [ISO 639-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard.  # noqa: E501

        :param notification_language: The notification_language of this Customer.  # noqa: E501
        :type: str
        """
        allowed_values = ["en", "fr"]  # noqa: E501
        if notification_language not in allowed_values:
            raise ValueError(
                "Invalid value for `notification_language` ({0}), must be one of {1}"  # noqa: E501
                .format(notification_language, allowed_values)
            )

        self._notification_language = notification_language

    @property
    def billing_address(self):
        """Gets the billing_address of this Customer.  # noqa: E501


        :return: The billing_address of this Customer.  # noqa: E501
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this Customer.


        :param billing_address: The billing_address of this Customer.  # noqa: E501
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this Customer.  # noqa: E501


        :return: The shipping_address of this Customer.  # noqa: E501
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Customer.


        :param shipping_address: The shipping_address of this Customer.  # noqa: E501
        :type: Address
        """

        self._shipping_address = shipping_address
