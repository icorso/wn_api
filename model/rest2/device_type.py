# coding: utf-8

from model.serializable import SwaggerSerializable


class DeviceType(SwaggerSerializable):
    swagger_types = {
        'type': 'str',
        'manufacturer': 'str',
        'supports_mag_stripe': 'bool',
        'supports_icc': 'bool',
        'supports_keyed': 'bool',
        'supports_contactless': 'bool',
        'supports_pin_entry': 'bool',
        'supports_output_printing': 'bool',
        'supports_output_displaying': 'bool',
        'applications': 'list[EmvApplication]',
        'certificates': 'list[EmvCertificate]',
        'revoked_certificates': 'list[EmvCertificate]',
        'default_emv_tags': 'list[EmvTag]'
    }

    attribute_map = {
        'type': 'type',
        'manufacturer': 'manufacturer',
        'supports_mag_stripe': 'supportsMagStripe',
        'supports_icc': 'supportsIcc',
        'supports_keyed': 'supportsKeyed',
        'supports_contactless': 'supportsContactless',
        'supports_pin_entry': 'supportsPinEntry',
        'supports_output_printing': 'supportsOutputPrinting',
        'supports_output_displaying': 'supportsOutputDisplaying',
        'applications': 'applications',
        'certificates': 'certificates',
        'revoked_certificates': 'revokedCertificates',
        'default_emv_tags': 'defaultEmvTags'
    }

    def __init__(self, type=None, manufacturer=None, supports_mag_stripe=None, supports_icc=None, supports_keyed=None, supports_contactless=None, supports_pin_entry=None, supports_output_printing=None, supports_output_displaying=None, applications=None, certificates=None, revoked_certificates=None, default_emv_tags=None):  # noqa: E501
        """DeviceType - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._manufacturer = None
        self._supports_mag_stripe = None
        self._supports_icc = None
        self._supports_keyed = None
        self._supports_contactless = None
        self._supports_pin_entry = None
        self._supports_output_printing = None
        self._supports_output_displaying = None
        self._applications = None
        self._certificates = None
        self._revoked_certificates = None
        self._default_emv_tags = None
        self.discriminator = None
        self.type = type
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if supports_mag_stripe is not None:
            self.supports_mag_stripe = supports_mag_stripe
        if supports_icc is not None:
            self.supports_icc = supports_icc
        if supports_keyed is not None:
            self.supports_keyed = supports_keyed
        if supports_contactless is not None:
            self.supports_contactless = supports_contactless
        if supports_pin_entry is not None:
            self.supports_pin_entry = supports_pin_entry
        if supports_output_printing is not None:
            self.supports_output_printing = supports_output_printing
        if supports_output_displaying is not None:
            self.supports_output_displaying = supports_output_displaying
        if applications is not None:
            self.applications = applications
        if certificates is not None:
            self.certificates = certificates
        if revoked_certificates is not None:
            self.revoked_certificates = revoked_certificates
        if default_emv_tags is not None:
            self.default_emv_tags = default_emv_tags

    @property
    def type(self):
        """Gets the type of this DeviceType.  # noqa: E501

        Type of device.  # noqa: E501

        :return: The type of this DeviceType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceType.

        Type of device.  # noqa: E501

        :param type: The type of this DeviceType.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def manufacturer(self):
        """Gets the manufacturer of this DeviceType.  # noqa: E501

        Company responsible for manufacturing the devices of this type.  # noqa: E501

        :return: The manufacturer of this DeviceType.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this DeviceType.

        Company responsible for manufacturing the devices of this type.  # noqa: E501

        :param manufacturer: The manufacturer of this DeviceType.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def supports_mag_stripe(self):
        """Gets the supports_mag_stripe of this DeviceType.  # noqa: E501

        Indicates whether this type of device is capable of performing card swipes.  # noqa: E501

        :return: The supports_mag_stripe of this DeviceType.  # noqa: E501
        :rtype: bool
        """
        return self._supports_mag_stripe

    @supports_mag_stripe.setter
    def supports_mag_stripe(self, supports_mag_stripe):
        """Sets the supports_mag_stripe of this DeviceType.

        Indicates whether this type of device is capable of performing card swipes.  # noqa: E501

        :param supports_mag_stripe: The supports_mag_stripe of this DeviceType.  # noqa: E501
        :type: bool
        """

        self._supports_mag_stripe = supports_mag_stripe

    @property
    def supports_icc(self):
        """Gets the supports_icc of this DeviceType.  # noqa: E501

        Indicates whether this type of device is capable of reading card chips.  # noqa: E501

        :return: The supports_icc of this DeviceType.  # noqa: E501
        :rtype: bool
        """
        return self._supports_icc

    @supports_icc.setter
    def supports_icc(self, supports_icc):
        """Sets the supports_icc of this DeviceType.

        Indicates whether this type of device is capable of reading card chips.  # noqa: E501

        :param supports_icc: The supports_icc of this DeviceType.  # noqa: E501
        :type: bool
        """

        self._supports_icc = supports_icc

    @property
    def supports_keyed(self):
        """Gets the supports_keyed of this DeviceType.  # noqa: E501

        Indicates whether this type of device is capable of accepting keyed inputs.  # noqa: E501

        :return: The supports_keyed of this DeviceType.  # noqa: E501
        :rtype: bool
        """
        return self._supports_keyed

    @supports_keyed.setter
    def supports_keyed(self, supports_keyed):
        """Sets the supports_keyed of this DeviceType.

        Indicates whether this type of device is capable of accepting keyed inputs.  # noqa: E501

        :param supports_keyed: The supports_keyed of this DeviceType.  # noqa: E501
        :type: bool
        """

        self._supports_keyed = supports_keyed

    @property
    def supports_contactless(self):
        """Gets the supports_contactless of this DeviceType.  # noqa: E501

        Indicates whether this type of device is capable of performing contactless transactions.  # noqa: E501

        :return: The supports_contactless of this DeviceType.  # noqa: E501
        :rtype: bool
        """
        return self._supports_contactless

    @supports_contactless.setter
    def supports_contactless(self, supports_contactless):
        """Sets the supports_contactless of this DeviceType.

        Indicates whether this type of device is capable of performing contactless transactions.  # noqa: E501

        :param supports_contactless: The supports_contactless of this DeviceType.  # noqa: E501
        :type: bool
        """

        self._supports_contactless = supports_contactless

    @property
    def supports_pin_entry(self):
        """Gets the supports_pin_entry of this DeviceType.  # noqa: E501

        Indicates whether this type of device is capable of accepting PIN entry.  # noqa: E501

        :return: The supports_pin_entry of this DeviceType.  # noqa: E501
        :rtype: bool
        """
        return self._supports_pin_entry

    @supports_pin_entry.setter
    def supports_pin_entry(self, supports_pin_entry):
        """Sets the supports_pin_entry of this DeviceType.

        Indicates whether this type of device is capable of accepting PIN entry.  # noqa: E501

        :param supports_pin_entry: The supports_pin_entry of this DeviceType.  # noqa: E501
        :type: bool
        """

        self._supports_pin_entry = supports_pin_entry

    @property
    def supports_output_printing(self):
        """Gets the supports_output_printing of this DeviceType.  # noqa: E501

        Indicates whether this type of device is capable of printing.  # noqa: E501

        :return: The supports_output_printing of this DeviceType.  # noqa: E501
        :rtype: bool
        """
        return self._supports_output_printing

    @supports_output_printing.setter
    def supports_output_printing(self, supports_output_printing):
        """Sets the supports_output_printing of this DeviceType.

        Indicates whether this type of device is capable of printing.  # noqa: E501

        :param supports_output_printing: The supports_output_printing of this DeviceType.  # noqa: E501
        :type: bool
        """

        self._supports_output_printing = supports_output_printing

    @property
    def supports_output_displaying(self):
        """Gets the supports_output_displaying of this DeviceType.  # noqa: E501

        Indicates whether this type of device is capable of displaying information.  # noqa: E501

        :return: The supports_output_displaying of this DeviceType.  # noqa: E501
        :rtype: bool
        """
        return self._supports_output_displaying

    @supports_output_displaying.setter
    def supports_output_displaying(self, supports_output_displaying):
        """Sets the supports_output_displaying of this DeviceType.

        Indicates whether this type of device is capable of displaying information.  # noqa: E501

        :param supports_output_displaying: The supports_output_displaying of this DeviceType.  # noqa: E501
        :type: bool
        """

        self._supports_output_displaying = supports_output_displaying

    @property
    def applications(self):
        """Gets the applications of this DeviceType.  # noqa: E501


        :return: The applications of this DeviceType.  # noqa: E501
        :rtype: list[EmvApplication]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this DeviceType.


        :param applications: The applications of this DeviceType.  # noqa: E501
        :type: list[EmvApplication]
        """

        self._applications = applications

    @property
    def certificates(self):
        """Gets the certificates of this DeviceType.  # noqa: E501


        :return: The certificates of this DeviceType.  # noqa: E501
        :rtype: list[EmvCertificate]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this DeviceType.


        :param certificates: The certificates of this DeviceType.  # noqa: E501
        :type: list[EmvCertificate]
        """

        self._certificates = certificates

    @property
    def revoked_certificates(self):
        """Gets the revoked_certificates of this DeviceType.  # noqa: E501


        :return: The revoked_certificates of this DeviceType.  # noqa: E501
        :rtype: list[EmvCertificate]
        """
        return self._revoked_certificates

    @revoked_certificates.setter
    def revoked_certificates(self, revoked_certificates):
        """Sets the revoked_certificates of this DeviceType.


        :param revoked_certificates: The revoked_certificates of this DeviceType.  # noqa: E501
        :type: list[EmvCertificate]
        """

        self._revoked_certificates = revoked_certificates

    @property
    def default_emv_tags(self):
        """Gets the default_emv_tags of this DeviceType.  # noqa: E501


        :return: The default_emv_tags of this DeviceType.  # noqa: E501
        :rtype: list[EmvTag]
        """
        return self._default_emv_tags

    @default_emv_tags.setter
    def default_emv_tags(self, default_emv_tags):
        """Sets the default_emv_tags of this DeviceType.


        :param default_emv_tags: The default_emv_tags of this DeviceType.  # noqa: E501
        :type: list[EmvTag]
        """

        self._default_emv_tags = default_emv_tags
