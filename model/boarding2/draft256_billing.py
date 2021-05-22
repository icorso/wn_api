# coding: utf-8

from model.serializable import SwaggerSerializable


class Draft256Billing(SwaggerSerializable):
    swagger_types = {
        'bank_merchant_id': 'str',
        'terminal_id_number': 'str',
        'acq_institution_id_code': 'str',
        'store_number': 'str',
        'card_acceptor_name': 'str',
        'local_phone_number': 'str',
        'state': 'str',
        'city': 'str',
        'postal_code': 'str',
        'street_address': 'str'
    }

    attribute_map = {
        'bank_merchant_id': 'bankMerchantId',
        'terminal_id_number': 'terminalIdNumber',
        'acq_institution_id_code': 'acqInstitutionIdCode',
        'store_number': 'storeNumber',
        'card_acceptor_name': 'cardAcceptorName',
        'local_phone_number': 'localPhoneNumber',
        'state': 'state',
        'city': 'city',
        'postal_code': 'postalCode',
        'street_address': 'streetAddress'
    }

    def __init__(self, bank_merchant_id=None, terminal_id_number=None, acq_institution_id_code=None, store_number=None, card_acceptor_name=None, local_phone_number=None, state=None, city=None, postal_code=None, street_address=None):  # noqa: E501
        """Draft256Billing - a model defined in Swagger"""  # noqa: E501
        self._bank_merchant_id = None
        self._terminal_id_number = None
        self._acq_institution_id_code = None
        self._store_number = None
        self._card_acceptor_name = None
        self._local_phone_number = None
        self._state = None
        self._city = None
        self._postal_code = None
        self._street_address = None
        self.discriminator = None
        self.bank_merchant_id = bank_merchant_id
        self.terminal_id_number = terminal_id_number
        if acq_institution_id_code is not None:
            self.acq_institution_id_code = acq_institution_id_code
        self.store_number = store_number
        self.card_acceptor_name = card_acceptor_name
        self.local_phone_number = local_phone_number
        if state is not None:
            self.state = state
        self.city = city
        self.postal_code = postal_code
        if street_address is not None:
            self.street_address = street_address

    @property
    def bank_merchant_id(self):
        """Gets the bank_merchant_id of this Draft256Billing.  # noqa: E501


        :return: The bank_merchant_id of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._bank_merchant_id

    @bank_merchant_id.setter
    def bank_merchant_id(self, bank_merchant_id):
        """Sets the bank_merchant_id of this Draft256Billing.


        :param bank_merchant_id: The bank_merchant_id of this Draft256Billing.  # noqa: E501
        :type: str
        """
        self._bank_merchant_id = bank_merchant_id

    @property
    def terminal_id_number(self):
        """Gets the terminal_id_number of this Draft256Billing.  # noqa: E501


        :return: The terminal_id_number of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._terminal_id_number

    @terminal_id_number.setter
    def terminal_id_number(self, terminal_id_number):
        """Sets the terminal_id_number of this Draft256Billing.


        :param terminal_id_number: The terminal_id_number of this Draft256Billing.  # noqa: E501
        :type: str
        """
        if terminal_id_number is None:
            raise ValueError("Invalid value for `terminal_id_number`, must not be `None`")  # noqa: E501

        self._terminal_id_number = terminal_id_number

    @property
    def acq_institution_id_code(self):
        """Gets the acq_institution_id_code of this Draft256Billing.  # noqa: E501


        :return: The acq_institution_id_code of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._acq_institution_id_code

    @acq_institution_id_code.setter
    def acq_institution_id_code(self, acq_institution_id_code):
        """Sets the acq_institution_id_code of this Draft256Billing.


        :param acq_institution_id_code: The acq_institution_id_code of this Draft256Billing.  # noqa: E501
        :type: str
        """

        self._acq_institution_id_code = acq_institution_id_code

    @property
    def store_number(self):
        """Gets the store_number of this Draft256Billing.  # noqa: E501


        :return: The store_number of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._store_number

    @store_number.setter
    def store_number(self, store_number):
        """Sets the store_number of this Draft256Billing.


        :param store_number: The store_number of this Draft256Billing.  # noqa: E501
        :type: str
        """
        if store_number is None:
            raise ValueError("Invalid value for `store_number`, must not be `None`")  # noqa: E501

        self._store_number = store_number

    @property
    def card_acceptor_name(self):
        """Gets the card_acceptor_name of this Draft256Billing.  # noqa: E501


        :return: The card_acceptor_name of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._card_acceptor_name

    @card_acceptor_name.setter
    def card_acceptor_name(self, card_acceptor_name):
        """Sets the card_acceptor_name of this Draft256Billing.


        :param card_acceptor_name: The card_acceptor_name of this Draft256Billing.  # noqa: E501
        :type: str
        """
        if card_acceptor_name is None:
            raise ValueError("Invalid value for `card_acceptor_name`, must not be `None`")  # noqa: E501

        self._card_acceptor_name = card_acceptor_name

    @property
    def local_phone_number(self):
        """Gets the local_phone_number of this Draft256Billing.  # noqa: E501


        :return: The local_phone_number of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._local_phone_number

    @local_phone_number.setter
    def local_phone_number(self, local_phone_number):
        """Sets the local_phone_number of this Draft256Billing.


        :param local_phone_number: The local_phone_number of this Draft256Billing.  # noqa: E501
        :type: str
        """
        if local_phone_number is None:
            raise ValueError("Invalid value for `local_phone_number`, must not be `None`")  # noqa: E501

        self._local_phone_number = local_phone_number

    @property
    def state(self):
        """Gets the state of this Draft256Billing.  # noqa: E501

        The state code defined by [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) standard. This field only applies for American and Canadian terminals.  # noqa: E501

        :return: The state of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Draft256Billing.

        The state code defined by [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) standard. This field only applies for American and Canadian terminals.  # noqa: E501

        :param state: The state of this Draft256Billing.  # noqa: E501
        :type: str
        """
        allowed_values = ["CA-AB", "CA-BC", "CA-MB", "CA-NB", "CA-NL", "CA-NS", "CA-ON", "CA-PE", "CA-QC", "CA-SK", "CA-NT", "CA-NU", "CA-YT", "US-AL", "US-AK", "US-AZ", "US-AR", "US-CA", "US-CO", "US-CT", "US-DE", "US-FL", "US-GA", "US-HI", "US-ID", "US-IL", "US-IN", "US-IA", "US-KS", "US-KY", "US-LA", "US-ME", "US-MD", "US-MA", "US-MI", "US-MN", "US-MS", "US-MO", "US-MT", "US-NE", "US-NV", "US-NH", "US-NJ", "US-NM", "US-NY", "US-NC", "US-ND", "US-OH", "US-OK", "US-OR", "US-PA", "US-RI", "US-SC", "US-SD", "US-TN", "US-TX", "US-UT", "US-VT", "US-VA", "US-WA", "US-WV", "US-WI", "US-WY", "US-DC", "US-AS", "US-GU", "US-MP", "US-PR", "US-UM", "US-VI"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def city(self):
        """Gets the city of this Draft256Billing.  # noqa: E501


        :return: The city of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Draft256Billing.


        :param city: The city of this Draft256Billing.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this Draft256Billing.  # noqa: E501


        :return: The postal_code of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Draft256Billing.


        :param postal_code: The postal_code of this Draft256Billing.  # noqa: E501
        :type: str
        """
        if postal_code is None:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def street_address(self):
        """Gets the street_address of this Draft256Billing.  # noqa: E501


        :return: The street_address of this Draft256Billing.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this Draft256Billing.


        :param street_address: The street_address of this Draft256Billing.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

