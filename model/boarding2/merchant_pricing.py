# coding: utf-8

from model.serializable import SwaggerSerializable


class MerchantPricing(SwaggerSerializable):
    swagger_types = {
        'monthly_fee': 'float',
        'monthly_fee_type': 'str',
        'monthly_included_standard_transactions': 'int',
        'per_standard_txn_fee': 'float',
        'per_threed_txn_fee': 'float',
        'per_edcc_txn_fee': 'float',
        'per_secure_card_txn_fee': 'float',
        'per_sms_fee': 'float',
        'max_mind_request_fee': 'float',
        'max_mind_rejection_fee': 'float',
        'standard_transaction_classification': 'str'
    }

    attribute_map = {
        'monthly_fee': 'monthlyFee',
        'monthly_fee_type': 'monthlyFeeType',
        'monthly_included_standard_transactions': 'monthlyIncludedStandardTransactions',
        'per_standard_txn_fee': 'perStandardTxnFee',
        'per_threed_txn_fee': 'perThreedTxnFee',
        'per_edcc_txn_fee': 'perEdccTxnFee',
        'per_secure_card_txn_fee': 'perSecureCardTxnFee',
        'per_sms_fee': 'perSmsFee',
        'max_mind_request_fee': 'maxMindRequestFee',
        'max_mind_rejection_fee': 'maxMindRejectionFee',
        'standard_transaction_classification': 'standardTransactionClassification'
    }

    def __init__(self, monthly_fee=None, monthly_fee_type=None, monthly_included_standard_transactions=None, per_standard_txn_fee=None, per_threed_txn_fee=None, per_edcc_txn_fee=None, per_secure_card_txn_fee=None, per_sms_fee=None, max_mind_request_fee=None, max_mind_rejection_fee=None, standard_transaction_classification=None):  # noqa: E501
        """MerchantPricing - a model defined in Swagger"""  # noqa: E501
        self._monthly_fee = None
        self._monthly_fee_type = None
        self._monthly_included_standard_transactions = None
        self._per_standard_txn_fee = None
        self._per_threed_txn_fee = None
        self._per_edcc_txn_fee = None
        self._per_secure_card_txn_fee = None
        self._per_sms_fee = None
        self._max_mind_request_fee = None
        self._max_mind_rejection_fee = None
        self._standard_transaction_classification = None
        self.discriminator = None
        if monthly_fee is not None:
            self.monthly_fee = monthly_fee
        self.monthly_fee_type = monthly_fee_type
        if monthly_included_standard_transactions is not None:
            self.monthly_included_standard_transactions = monthly_included_standard_transactions
        if per_standard_txn_fee is not None:
            self.per_standard_txn_fee = per_standard_txn_fee
        if per_threed_txn_fee is not None:
            self.per_threed_txn_fee = per_threed_txn_fee
        if per_edcc_txn_fee is not None:
            self.per_edcc_txn_fee = per_edcc_txn_fee
        if per_secure_card_txn_fee is not None:
            self.per_secure_card_txn_fee = per_secure_card_txn_fee
        if per_sms_fee is not None:
            self.per_sms_fee = per_sms_fee
        if max_mind_request_fee is not None:
            self.max_mind_request_fee = max_mind_request_fee
        if max_mind_rejection_fee is not None:
            self.max_mind_rejection_fee = max_mind_rejection_fee
        if standard_transaction_classification is not None:
            self.standard_transaction_classification = standard_transaction_classification

    @property
    def monthly_fee(self):
        """Gets the monthly_fee of this MerchantPricing.  # noqa: E501


        :return: The monthly_fee of this MerchantPricing.  # noqa: E501
        :rtype: float
        """
        return self._monthly_fee

    @monthly_fee.setter
    def monthly_fee(self, monthly_fee):
        """Sets the monthly_fee of this MerchantPricing.


        :param monthly_fee: The monthly_fee of this MerchantPricing.  # noqa: E501
        :type: float
        """

        self._monthly_fee = monthly_fee

    @property
    def monthly_fee_type(self):
        """Gets the monthly_fee_type of this MerchantPricing.  # noqa: E501


        :return: The monthly_fee_type of this MerchantPricing.  # noqa: E501
        :rtype: str
        """
        return self._monthly_fee_type

    @monthly_fee_type.setter
    def monthly_fee_type(self, monthly_fee_type):
        """Sets the monthly_fee_type of this MerchantPricing.


        :param monthly_fee_type: The monthly_fee_type of this MerchantPricing.  # noqa: E501
        :type: str
        """
        if monthly_fee_type is None:
            raise ValueError("Invalid value for `monthly_fee_type`, must not be `None`")  # noqa: E501
        allowed_values = ["INCLUDED_TRANS", "MINIMUM"]  # noqa: E501
        if monthly_fee_type not in allowed_values:
            raise ValueError(
                "Invalid value for `monthly_fee_type` ({0}), must be one of {1}"  # noqa: E501
                .format(monthly_fee_type, allowed_values)
            )

        self._monthly_fee_type = monthly_fee_type

    @property
    def monthly_included_standard_transactions(self):
        """Gets the monthly_included_standard_transactions of this MerchantPricing.  # noqa: E501


        :return: The monthly_included_standard_transactions of this MerchantPricing.  # noqa: E501
        :rtype: int
        """
        return self._monthly_included_standard_transactions

    @monthly_included_standard_transactions.setter
    def monthly_included_standard_transactions(self, monthly_included_standard_transactions):
        """Sets the monthly_included_standard_transactions of this MerchantPricing.


        :param monthly_included_standard_transactions: The monthly_included_standard_transactions of this MerchantPricing.  # noqa: E501
        :type: int
        """

        self._monthly_included_standard_transactions = monthly_included_standard_transactions

    @property
    def per_standard_txn_fee(self):
        """Gets the per_standard_txn_fee of this MerchantPricing.  # noqa: E501


        :return: The per_standard_txn_fee of this MerchantPricing.  # noqa: E501
        :rtype: float
        """
        return self._per_standard_txn_fee

    @per_standard_txn_fee.setter
    def per_standard_txn_fee(self, per_standard_txn_fee):
        """Sets the per_standard_txn_fee of this MerchantPricing.


        :param per_standard_txn_fee: The per_standard_txn_fee of this MerchantPricing.  # noqa: E501
        :type: float
        """

        self._per_standard_txn_fee = per_standard_txn_fee

    @property
    def per_threed_txn_fee(self):
        """Gets the per_threed_txn_fee of this MerchantPricing.  # noqa: E501


        :return: The per_threed_txn_fee of this MerchantPricing.  # noqa: E501
        :rtype: float
        """
        return self._per_threed_txn_fee

    @per_threed_txn_fee.setter
    def per_threed_txn_fee(self, per_threed_txn_fee):
        """Sets the per_threed_txn_fee of this MerchantPricing.


        :param per_threed_txn_fee: The per_threed_txn_fee of this MerchantPricing.  # noqa: E501
        :type: float
        """

        self._per_threed_txn_fee = per_threed_txn_fee

    @property
    def per_edcc_txn_fee(self):
        """Gets the per_edcc_txn_fee of this MerchantPricing.  # noqa: E501


        :return: The per_edcc_txn_fee of this MerchantPricing.  # noqa: E501
        :rtype: float
        """
        return self._per_edcc_txn_fee

    @per_edcc_txn_fee.setter
    def per_edcc_txn_fee(self, per_edcc_txn_fee):
        """Sets the per_edcc_txn_fee of this MerchantPricing.


        :param per_edcc_txn_fee: The per_edcc_txn_fee of this MerchantPricing.  # noqa: E501
        :type: float
        """

        self._per_edcc_txn_fee = per_edcc_txn_fee

    @property
    def per_secure_card_txn_fee(self):
        """Gets the per_secure_card_txn_fee of this MerchantPricing.  # noqa: E501


        :return: The per_secure_card_txn_fee of this MerchantPricing.  # noqa: E501
        :rtype: float
        """
        return self._per_secure_card_txn_fee

    @per_secure_card_txn_fee.setter
    def per_secure_card_txn_fee(self, per_secure_card_txn_fee):
        """Sets the per_secure_card_txn_fee of this MerchantPricing.


        :param per_secure_card_txn_fee: The per_secure_card_txn_fee of this MerchantPricing.  # noqa: E501
        :type: float
        """

        self._per_secure_card_txn_fee = per_secure_card_txn_fee

    @property
    def per_sms_fee(self):
        """Gets the per_sms_fee of this MerchantPricing.  # noqa: E501


        :return: The per_sms_fee of this MerchantPricing.  # noqa: E501
        :rtype: float
        """
        return self._per_sms_fee

    @per_sms_fee.setter
    def per_sms_fee(self, per_sms_fee):
        """Sets the per_sms_fee of this MerchantPricing.


        :param per_sms_fee: The per_sms_fee of this MerchantPricing.  # noqa: E501
        :type: float
        """

        self._per_sms_fee = per_sms_fee

    @property
    def max_mind_request_fee(self):
        """Gets the max_mind_request_fee of this MerchantPricing.  # noqa: E501


        :return: The max_mind_request_fee of this MerchantPricing.  # noqa: E501
        :rtype: float
        """
        return self._max_mind_request_fee

    @max_mind_request_fee.setter
    def max_mind_request_fee(self, max_mind_request_fee):
        """Sets the max_mind_request_fee of this MerchantPricing.


        :param max_mind_request_fee: The max_mind_request_fee of this MerchantPricing.  # noqa: E501
        :type: float
        """

        self._max_mind_request_fee = max_mind_request_fee

    @property
    def max_mind_rejection_fee(self):
        """Gets the max_mind_rejection_fee of this MerchantPricing.  # noqa: E501


        :return: The max_mind_rejection_fee of this MerchantPricing.  # noqa: E501
        :rtype: float
        """
        return self._max_mind_rejection_fee

    @max_mind_rejection_fee.setter
    def max_mind_rejection_fee(self, max_mind_rejection_fee):
        """Sets the max_mind_rejection_fee of this MerchantPricing.


        :param max_mind_rejection_fee: The max_mind_rejection_fee of this MerchantPricing.  # noqa: E501
        :type: float
        """

        self._max_mind_rejection_fee = max_mind_rejection_fee

    @property
    def standard_transaction_classification(self):
        """Gets the standard_transaction_classification of this MerchantPricing.  # noqa: E501


        :return: The standard_transaction_classification of this MerchantPricing.  # noqa: E501
        :rtype: str
        """
        return self._standard_transaction_classification

    @standard_transaction_classification.setter
    def standard_transaction_classification(self, standard_transaction_classification):
        """Sets the standard_transaction_classification of this MerchantPricing.


        :param standard_transaction_classification: The standard_transaction_classification of this MerchantPricing.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALL", "COMPLETED"]  # noqa: E501
        if standard_transaction_classification not in allowed_values:
            raise ValueError(
                "Invalid value for `standard_transaction_classification` ({0}), must be one of {1}"  # noqa: E501
                .format(standard_transaction_classification, allowed_values)
            )

        self._standard_transaction_classification = standard_transaction_classification

