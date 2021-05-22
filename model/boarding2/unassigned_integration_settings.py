# coding: utf-8

from model.serializable import SwaggerSerializable


class UnassignedIntegrationSettings(SwaggerSerializable):
    swagger_types = {
        'enable_background_validation': 'bool',
        'background_validation_url': 'str',
        'receipt_page_url': 'str',
        'enable_additional_field_xml_response_tag': 'bool',
        'enable_supports_apple_pay_xml_response_tag': 'bool',
        'enable_supports_google_pay_xml_response_tag': 'bool',
        'enable_enable3ds_xml_response_tag': 'bool',
        'enable_supported_cards_xml_response_tag': 'bool'
    }

    attribute_map = {
        'enable_background_validation': 'enableBackgroundValidation',
        'background_validation_url': 'backgroundValidationUrl',
        'receipt_page_url': 'receiptPageUrl',
        'enable_additional_field_xml_response_tag': 'enableAdditionalFieldXmlResponseTag',
        'enable_supports_apple_pay_xml_response_tag': 'enableSupportsApplePayXmlResponseTag',
        'enable_supports_google_pay_xml_response_tag': 'enableSupportsGooglePayXmlResponseTag',
        'enable_enable3ds_xml_response_tag': 'enableEnable3dsXmlResponseTag',
        'enable_supported_cards_xml_response_tag': 'enableSupportedCardsXmlResponseTag'
    }

    def __init__(self, enable_background_validation=False, background_validation_url=None, receipt_page_url=None, enable_additional_field_xml_response_tag=True, enable_supports_apple_pay_xml_response_tag=True, enable_supports_google_pay_xml_response_tag=True, enable_enable3ds_xml_response_tag=True, enable_supported_cards_xml_response_tag=True):  # noqa: E501
        """UnassignedIntegrationSettings - a model defined in Swagger"""  # noqa: E501
        self._enable_background_validation = None
        self._background_validation_url = None
        self._receipt_page_url = None
        self._enable_additional_field_xml_response_tag = None
        self._enable_supports_apple_pay_xml_response_tag = None
        self._enable_supports_google_pay_xml_response_tag = None
        self._enable_enable3ds_xml_response_tag = None
        self._enable_supported_cards_xml_response_tag = None
        self.discriminator = None
        if enable_background_validation is not None:
            self.enable_background_validation = enable_background_validation
        if background_validation_url is not None:
            self.background_validation_url = background_validation_url
        if receipt_page_url is not None:
            self.receipt_page_url = receipt_page_url
        if enable_additional_field_xml_response_tag is not None:
            self.enable_additional_field_xml_response_tag = enable_additional_field_xml_response_tag
        if enable_supports_apple_pay_xml_response_tag is not None:
            self.enable_supports_apple_pay_xml_response_tag = enable_supports_apple_pay_xml_response_tag
        if enable_supports_google_pay_xml_response_tag is not None:
            self.enable_supports_google_pay_xml_response_tag = enable_supports_google_pay_xml_response_tag
        if enable_enable3ds_xml_response_tag is not None:
            self.enable_enable3ds_xml_response_tag = enable_enable3ds_xml_response_tag
        if enable_supported_cards_xml_response_tag is not None:
            self.enable_supported_cards_xml_response_tag = enable_supported_cards_xml_response_tag

    @property
    def enable_background_validation(self):
        """Gets the enable_background_validation of this UnassignedIntegrationSettings.  # noqa: E501


        :return: The enable_background_validation of this UnassignedIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_background_validation

    @enable_background_validation.setter
    def enable_background_validation(self, enable_background_validation):
        """Sets the enable_background_validation of this UnassignedIntegrationSettings.


        :param enable_background_validation: The enable_background_validation of this UnassignedIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_background_validation = enable_background_validation

    @property
    def background_validation_url(self):
        """Gets the background_validation_url of this UnassignedIntegrationSettings.  # noqa: E501


        :return: The background_validation_url of this UnassignedIntegrationSettings.  # noqa: E501
        :rtype: str
        """
        return self._background_validation_url

    @background_validation_url.setter
    def background_validation_url(self, background_validation_url):
        """Sets the background_validation_url of this UnassignedIntegrationSettings.


        :param background_validation_url: The background_validation_url of this UnassignedIntegrationSettings.  # noqa: E501
        :type: str
        """

        self._background_validation_url = background_validation_url

    @property
    def receipt_page_url(self):
        """Gets the receipt_page_url of this UnassignedIntegrationSettings.  # noqa: E501


        :return: The receipt_page_url of this UnassignedIntegrationSettings.  # noqa: E501
        :rtype: str
        """
        return self._receipt_page_url

    @receipt_page_url.setter
    def receipt_page_url(self, receipt_page_url):
        """Sets the receipt_page_url of this UnassignedIntegrationSettings.


        :param receipt_page_url: The receipt_page_url of this UnassignedIntegrationSettings.  # noqa: E501
        :type: str
        """

        self._receipt_page_url = receipt_page_url

    @property
    def enable_additional_field_xml_response_tag(self):
        """Gets the enable_additional_field_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501


        :return: The enable_additional_field_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_additional_field_xml_response_tag

    @enable_additional_field_xml_response_tag.setter
    def enable_additional_field_xml_response_tag(self, enable_additional_field_xml_response_tag):
        """Sets the enable_additional_field_xml_response_tag of this UnassignedIntegrationSettings.


        :param enable_additional_field_xml_response_tag: The enable_additional_field_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_additional_field_xml_response_tag = enable_additional_field_xml_response_tag

    @property
    def enable_supports_apple_pay_xml_response_tag(self):
        """Gets the enable_supports_apple_pay_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501


        :return: The enable_supports_apple_pay_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_supports_apple_pay_xml_response_tag

    @enable_supports_apple_pay_xml_response_tag.setter
    def enable_supports_apple_pay_xml_response_tag(self, enable_supports_apple_pay_xml_response_tag):
        """Sets the enable_supports_apple_pay_xml_response_tag of this UnassignedIntegrationSettings.


        :param enable_supports_apple_pay_xml_response_tag: The enable_supports_apple_pay_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_supports_apple_pay_xml_response_tag = enable_supports_apple_pay_xml_response_tag

    @property
    def enable_supports_google_pay_xml_response_tag(self):
        """Gets the enable_supports_google_pay_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501


        :return: The enable_supports_google_pay_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_supports_google_pay_xml_response_tag

    @enable_supports_google_pay_xml_response_tag.setter
    def enable_supports_google_pay_xml_response_tag(self, enable_supports_google_pay_xml_response_tag):
        """Sets the enable_supports_google_pay_xml_response_tag of this UnassignedIntegrationSettings.


        :param enable_supports_google_pay_xml_response_tag: The enable_supports_google_pay_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_supports_google_pay_xml_response_tag = enable_supports_google_pay_xml_response_tag

    @property
    def enable_enable3ds_xml_response_tag(self):
        """Gets the enable_enable3ds_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501


        :return: The enable_enable3ds_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_enable3ds_xml_response_tag

    @enable_enable3ds_xml_response_tag.setter
    def enable_enable3ds_xml_response_tag(self, enable_enable3ds_xml_response_tag):
        """Sets the enable_enable3ds_xml_response_tag of this UnassignedIntegrationSettings.


        :param enable_enable3ds_xml_response_tag: The enable_enable3ds_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_enable3ds_xml_response_tag = enable_enable3ds_xml_response_tag

    @property
    def enable_supported_cards_xml_response_tag(self):
        """Gets the enable_supported_cards_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501


        :return: The enable_supported_cards_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_supported_cards_xml_response_tag

    @enable_supported_cards_xml_response_tag.setter
    def enable_supported_cards_xml_response_tag(self, enable_supported_cards_xml_response_tag):
        """Sets the enable_supported_cards_xml_response_tag of this UnassignedIntegrationSettings.


        :param enable_supported_cards_xml_response_tag: The enable_supported_cards_xml_response_tag of this UnassignedIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_supported_cards_xml_response_tag = enable_supported_cards_xml_response_tag

