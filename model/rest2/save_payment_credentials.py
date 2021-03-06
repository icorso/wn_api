# coding: utf-8
from model.serializable import SwaggerSerializable


class SavePaymentCredentials(SwaggerSerializable):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'merchant_reference': 'str',
        'future_usage_agreement': 'str'
    }

    attribute_map = {
        'merchant_reference': 'merchantReference',
        'future_usage_agreement': 'futureUsageAgreement'
    }

    def __init__(self, merchant_reference=None, future_usage_agreement=None):  # noqa: E501
        """SavePaymentCredentials - a model defined in Swagger"""  # noqa: E501
        self._merchant_reference = None
        self._future_usage_agreement = None
        self.discriminator = None
        self.merchant_reference = merchant_reference
        if future_usage_agreement is not None:
            self.future_usage_agreement = future_usage_agreement

    @property
    def merchant_reference(self):
        """Gets the merchant_reference of this SavePaymentCredentials.  # noqa: E501

        Unique merchant reference that identifies the stored credentials on both platforms.  **Note:** Clients must be able to store this value in order to eventually retrieve, update and delete the stored credentials.  # noqa: E501

        :return: The merchant_reference of this SavePaymentCredentials.  # noqa: E501
        :rtype: str
        """
        return self._merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, merchant_reference):
        """Sets the merchant_reference of this SavePaymentCredentials.

        Unique merchant reference that identifies the stored credentials on both platforms.  **Note:** Clients must be able to store this value in order to eventually retrieve, update and delete the stored credentials.  # noqa: E501

        :param merchant_reference: The merchant_reference of this SavePaymentCredentials.  # noqa: E501
        :type: str
        """
        if merchant_reference is None:
            raise ValueError("Invalid value for `merchant_reference`, must not be `None`")  # noqa: E501

        self._merchant_reference = merchant_reference

    @property
    def future_usage_agreement(self):
        """Gets the future_usage_agreement of this SavePaymentCredentials.  # noqa: E501

        It has been a Card Scheme requirement since 14th October 2017 that you must establish an agreement with a new customer before storing their card details for future standing Merchant Initiated Transactions (MITs).  - **UNSCHEDULED**: Transactions that are for a fixed or variable amount that don???t occur on a scheduled or regularly occurring transaction date, but when a pre-defined event happens. - **RECURRING**: Transactions that are processed on a regular fixed interval for a pre agreed or advised amount, where applicable. Recurring transactions don???t have a fixed duration and will continue to be processed until the cardholder cancels the agreement. - **INSTALLMENT**: Transactions that are processed on a regular fixed interval for a pre agreed amount for a single purchase of good or services. Unlike recurring transactions, they do have a fixed duration and mustn???t continue to be processed after the end of the agreed instalment period   # noqa: E501

        :return: The future_usage_agreement of this SavePaymentCredentials.  # noqa: E501
        :rtype: str
        """
        return self._future_usage_agreement

    @future_usage_agreement.setter
    def future_usage_agreement(self, future_usage_agreement):
        """Sets the future_usage_agreement of this SavePaymentCredentials.

        It has been a Card Scheme requirement since 14th October 2017 that you must establish an agreement with a new customer before storing their card details for future standing Merchant Initiated Transactions (MITs).  - **UNSCHEDULED**: Transactions that are for a fixed or variable amount that don???t occur on a scheduled or regularly occurring transaction date, but when a pre-defined event happens. - **RECURRING**: Transactions that are processed on a regular fixed interval for a pre agreed or advised amount, where applicable. Recurring transactions don???t have a fixed duration and will continue to be processed until the cardholder cancels the agreement. - **INSTALLMENT**: Transactions that are processed on a regular fixed interval for a pre agreed amount for a single purchase of good or services. Unlike recurring transactions, they do have a fixed duration and mustn???t continue to be processed after the end of the agreed instalment period   # noqa: E501

        :param future_usage_agreement: The future_usage_agreement of this SavePaymentCredentials.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNSCHEDULED", "RECURRING", "INSTALLMENT"]  # noqa: E501
        if future_usage_agreement not in allowed_values:
            raise ValueError(
                "Invalid value for `future_usage_agreement` ({0}), must be one of {1}"  # noqa: E501
                .format(future_usage_agreement, allowed_values)
            )

        self._future_usage_agreement = future_usage_agreement
