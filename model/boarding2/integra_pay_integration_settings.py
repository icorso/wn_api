# coding: utf-8

from model.serializable import SwaggerSerializable


class IntegraPayIntegrationSettings(SwaggerSerializable):
    swagger_types = {
        'use_unique_ref': 'bool',
        'enable_auto_ready': 'bool',
        'auto_ready_amount_limit': 'int',
        'hosted_page_version': 'str',
        'enable_background_validation': 'bool',
        'background_validation_url': 'str',
        'receipt_page_url': 'str',
        'mpi_receipt_url': 'str',
        'enable_additional_field_xml_response_tag': 'bool',
        'enable_original_response_xml_response_tag': 'bool',
        'enable_masked_card_xml_response_tag': 'bool',
        'enable_supports_apple_pay_xml_response_tag': 'bool',
        'enable_supports_google_pay_xml_response_tag': 'bool',
        'enable_enable3ds_xml_response_tag': 'bool',
        'enable_supported_cards_xml_response_tag': 'bool'
    }

    attribute_map = {
        'use_unique_ref': 'useUniqueRef',
        'enable_auto_ready': 'enableAutoReady',
        'auto_ready_amount_limit': 'autoReadyAmountLimit',
        'hosted_page_version': 'hostedPageVersion',
        'enable_background_validation': 'enableBackgroundValidation',
        'background_validation_url': 'backgroundValidationUrl',
        'receipt_page_url': 'receiptPageUrl',
        'mpi_receipt_url': 'mpiReceiptUrl',
        'enable_additional_field_xml_response_tag': 'enableAdditionalFieldXmlResponseTag',
        'enable_original_response_xml_response_tag': 'enableOriginalResponseXmlResponseTag',
        'enable_masked_card_xml_response_tag': 'enableMaskedCardXmlResponseTag',
        'enable_supports_apple_pay_xml_response_tag': 'enableSupportsApplePayXmlResponseTag',
        'enable_supports_google_pay_xml_response_tag': 'enableSupportsGooglePayXmlResponseTag',
        'enable_enable3ds_xml_response_tag': 'enableEnable3dsXmlResponseTag',
        'enable_supported_cards_xml_response_tag': 'enableSupportedCardsXmlResponseTag'
    }

    def __init__(self, use_unique_ref=True, enable_auto_ready=True, auto_ready_amount_limit=0, hosted_page_version='VERSION_2', enable_background_validation=False, background_validation_url=None, receipt_page_url=None, mpi_receipt_url=None, enable_additional_field_xml_response_tag=True, enable_original_response_xml_response_tag=False, enable_masked_card_xml_response_tag=False, enable_supports_apple_pay_xml_response_tag=True, enable_supports_google_pay_xml_response_tag=True, enable_enable3ds_xml_response_tag=True, enable_supported_cards_xml_response_tag=True):  # noqa: E501
        """IntegraPayIntegrationSettings - a model defined in Swagger"""  # noqa: E501
        self._use_unique_ref = None
        self._enable_auto_ready = None
        self._auto_ready_amount_limit = None
        self._hosted_page_version = None
        self._enable_background_validation = None
        self._background_validation_url = None
        self._receipt_page_url = None
        self._mpi_receipt_url = None
        self._enable_additional_field_xml_response_tag = None
        self._enable_original_response_xml_response_tag = None
        self._enable_masked_card_xml_response_tag = None
        self._enable_supports_apple_pay_xml_response_tag = None
        self._enable_supports_google_pay_xml_response_tag = None
        self._enable_enable3ds_xml_response_tag = None
        self._enable_supported_cards_xml_response_tag = None
        self.discriminator = None
        if use_unique_ref is not None:
            self.use_unique_ref = use_unique_ref
        if enable_auto_ready is not None:
            self.enable_auto_ready = enable_auto_ready
        if auto_ready_amount_limit is not None:
            self.auto_ready_amount_limit = auto_ready_amount_limit
        if hosted_page_version is not None:
            self.hosted_page_version = hosted_page_version
        if enable_background_validation is not None:
            self.enable_background_validation = enable_background_validation
        if background_validation_url is not None:
            self.background_validation_url = background_validation_url
        if receipt_page_url is not None:
            self.receipt_page_url = receipt_page_url
        if mpi_receipt_url is not None:
            self.mpi_receipt_url = mpi_receipt_url
        if enable_additional_field_xml_response_tag is not None:
            self.enable_additional_field_xml_response_tag = enable_additional_field_xml_response_tag
        if enable_original_response_xml_response_tag is not None:
            self.enable_original_response_xml_response_tag = enable_original_response_xml_response_tag
        if enable_masked_card_xml_response_tag is not None:
            self.enable_masked_card_xml_response_tag = enable_masked_card_xml_response_tag
        if enable_supports_apple_pay_xml_response_tag is not None:
            self.enable_supports_apple_pay_xml_response_tag = enable_supports_apple_pay_xml_response_tag
        if enable_supports_google_pay_xml_response_tag is not None:
            self.enable_supports_google_pay_xml_response_tag = enable_supports_google_pay_xml_response_tag
        if enable_enable3ds_xml_response_tag is not None:
            self.enable_enable3ds_xml_response_tag = enable_enable3ds_xml_response_tag
        if enable_supported_cards_xml_response_tag is not None:
            self.enable_supported_cards_xml_response_tag = enable_supported_cards_xml_response_tag

    @property
    def use_unique_ref(self):
        """Gets the use_unique_ref of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The use_unique_ref of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_unique_ref

    @use_unique_ref.setter
    def use_unique_ref(self, use_unique_ref):
        """Sets the use_unique_ref of this IntegraPayIntegrationSettings.


        :param use_unique_ref: The use_unique_ref of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._use_unique_ref = use_unique_ref

    @property
    def enable_auto_ready(self):
        """Gets the enable_auto_ready of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The enable_auto_ready of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_auto_ready

    @enable_auto_ready.setter
    def enable_auto_ready(self, enable_auto_ready):
        """Sets the enable_auto_ready of this IntegraPayIntegrationSettings.


        :param enable_auto_ready: The enable_auto_ready of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_auto_ready = enable_auto_ready

    @property
    def auto_ready_amount_limit(self):
        """Gets the auto_ready_amount_limit of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The auto_ready_amount_limit of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: int
        """
        return self._auto_ready_amount_limit

    @auto_ready_amount_limit.setter
    def auto_ready_amount_limit(self, auto_ready_amount_limit):
        """Sets the auto_ready_amount_limit of this IntegraPayIntegrationSettings.


        :param auto_ready_amount_limit: The auto_ready_amount_limit of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: int
        """

        self._auto_ready_amount_limit = auto_ready_amount_limit

    @property
    def hosted_page_version(self):
        """Gets the hosted_page_version of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The hosted_page_version of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: str
        """
        return self._hosted_page_version

    @hosted_page_version.setter
    def hosted_page_version(self, hosted_page_version):
        """Sets the hosted_page_version of this IntegraPayIntegrationSettings.


        :param hosted_page_version: The hosted_page_version of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["VERSION_1", "VERSION_2"]  # noqa: E501
        if hosted_page_version not in allowed_values:
            raise ValueError(
                "Invalid value for `hosted_page_version` ({0}), must be one of {1}"  # noqa: E501
                .format(hosted_page_version, allowed_values)
            )

        self._hosted_page_version = hosted_page_version

    @property
    def enable_background_validation(self):
        """Gets the enable_background_validation of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The enable_background_validation of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_background_validation

    @enable_background_validation.setter
    def enable_background_validation(self, enable_background_validation):
        """Sets the enable_background_validation of this IntegraPayIntegrationSettings.


        :param enable_background_validation: The enable_background_validation of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_background_validation = enable_background_validation

    @property
    def background_validation_url(self):
        """Gets the background_validation_url of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The background_validation_url of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: str
        """
        return self._background_validation_url

    @background_validation_url.setter
    def background_validation_url(self, background_validation_url):
        """Sets the background_validation_url of this IntegraPayIntegrationSettings.


        :param background_validation_url: The background_validation_url of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: str
        """

        self._background_validation_url = background_validation_url

    @property
    def receipt_page_url(self):
        """Gets the receipt_page_url of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The receipt_page_url of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: str
        """
        return self._receipt_page_url

    @receipt_page_url.setter
    def receipt_page_url(self, receipt_page_url):
        """Sets the receipt_page_url of this IntegraPayIntegrationSettings.


        :param receipt_page_url: The receipt_page_url of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: str
        """

        self._receipt_page_url = receipt_page_url

    @property
    def mpi_receipt_url(self):
        """Gets the mpi_receipt_url of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The mpi_receipt_url of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: str
        """
        return self._mpi_receipt_url

    @mpi_receipt_url.setter
    def mpi_receipt_url(self, mpi_receipt_url):
        """Sets the mpi_receipt_url of this IntegraPayIntegrationSettings.


        :param mpi_receipt_url: The mpi_receipt_url of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: str
        """

        self._mpi_receipt_url = mpi_receipt_url

    @property
    def enable_additional_field_xml_response_tag(self):
        """Gets the enable_additional_field_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The enable_additional_field_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_additional_field_xml_response_tag

    @enable_additional_field_xml_response_tag.setter
    def enable_additional_field_xml_response_tag(self, enable_additional_field_xml_response_tag):
        """Sets the enable_additional_field_xml_response_tag of this IntegraPayIntegrationSettings.


        :param enable_additional_field_xml_response_tag: The enable_additional_field_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_additional_field_xml_response_tag = enable_additional_field_xml_response_tag

    @property
    def enable_original_response_xml_response_tag(self):
        """Gets the enable_original_response_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The enable_original_response_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_original_response_xml_response_tag

    @enable_original_response_xml_response_tag.setter
    def enable_original_response_xml_response_tag(self, enable_original_response_xml_response_tag):
        """Sets the enable_original_response_xml_response_tag of this IntegraPayIntegrationSettings.


        :param enable_original_response_xml_response_tag: The enable_original_response_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_original_response_xml_response_tag = enable_original_response_xml_response_tag

    @property
    def enable_masked_card_xml_response_tag(self):
        """Gets the enable_masked_card_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The enable_masked_card_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_masked_card_xml_response_tag

    @enable_masked_card_xml_response_tag.setter
    def enable_masked_card_xml_response_tag(self, enable_masked_card_xml_response_tag):
        """Sets the enable_masked_card_xml_response_tag of this IntegraPayIntegrationSettings.


        :param enable_masked_card_xml_response_tag: The enable_masked_card_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_masked_card_xml_response_tag = enable_masked_card_xml_response_tag

    @property
    def enable_supports_apple_pay_xml_response_tag(self):
        """Gets the enable_supports_apple_pay_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The enable_supports_apple_pay_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_supports_apple_pay_xml_response_tag

    @enable_supports_apple_pay_xml_response_tag.setter
    def enable_supports_apple_pay_xml_response_tag(self, enable_supports_apple_pay_xml_response_tag):
        """Sets the enable_supports_apple_pay_xml_response_tag of this IntegraPayIntegrationSettings.


        :param enable_supports_apple_pay_xml_response_tag: The enable_supports_apple_pay_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_supports_apple_pay_xml_response_tag = enable_supports_apple_pay_xml_response_tag

    @property
    def enable_supports_google_pay_xml_response_tag(self):
        """Gets the enable_supports_google_pay_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The enable_supports_google_pay_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_supports_google_pay_xml_response_tag

    @enable_supports_google_pay_xml_response_tag.setter
    def enable_supports_google_pay_xml_response_tag(self, enable_supports_google_pay_xml_response_tag):
        """Sets the enable_supports_google_pay_xml_response_tag of this IntegraPayIntegrationSettings.


        :param enable_supports_google_pay_xml_response_tag: The enable_supports_google_pay_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_supports_google_pay_xml_response_tag = enable_supports_google_pay_xml_response_tag

    @property
    def enable_enable3ds_xml_response_tag(self):
        """Gets the enable_enable3ds_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The enable_enable3ds_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_enable3ds_xml_response_tag

    @enable_enable3ds_xml_response_tag.setter
    def enable_enable3ds_xml_response_tag(self, enable_enable3ds_xml_response_tag):
        """Sets the enable_enable3ds_xml_response_tag of this IntegraPayIntegrationSettings.


        :param enable_enable3ds_xml_response_tag: The enable_enable3ds_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_enable3ds_xml_response_tag = enable_enable3ds_xml_response_tag

    @property
    def enable_supported_cards_xml_response_tag(self):
        """Gets the enable_supported_cards_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501


        :return: The enable_supported_cards_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_supported_cards_xml_response_tag

    @enable_supported_cards_xml_response_tag.setter
    def enable_supported_cards_xml_response_tag(self, enable_supported_cards_xml_response_tag):
        """Sets the enable_supported_cards_xml_response_tag of this IntegraPayIntegrationSettings.


        :param enable_supported_cards_xml_response_tag: The enable_supported_cards_xml_response_tag of this IntegraPayIntegrationSettings.  # noqa: E501
        :type: bool
        """

        self._enable_supported_cards_xml_response_tag = enable_supported_cards_xml_response_tag

