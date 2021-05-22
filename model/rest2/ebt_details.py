# coding: utf-8

from model.serializable import SwaggerSerializable


class EbtDetails(SwaggerSerializable):
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
        'benefit_category': 'str',
        'withdrawal': 'bool',
        'voucher': 'Voucher'
    }

    attribute_map = {
        'benefit_category': 'benefitCategory',
        'withdrawal': 'withdrawal',
        'voucher': 'voucher'
    }

    def __init__(self, benefit_category=None, withdrawal=None, voucher=None):  # noqa: E501
        """EbtDetails - a model defined in Swagger"""  # noqa: E501
        self._benefit_category = None
        self._withdrawal = None
        self._voucher = None
        self.discriminator = None
        self.benefit_category = benefit_category
        if withdrawal is not None:
            self.withdrawal = withdrawal
        if voucher is not None:
            self.voucher = voucher

    @property
    def benefit_category(self):
        """Gets the benefit_category of this EbtDetails.  # noqa: E501


        :return: The benefit_category of this EbtDetails.  # noqa: E501
        :rtype: str
        """
        return self._benefit_category

    @benefit_category.setter
    def benefit_category(self, benefit_category):
        """Sets the benefit_category of this EbtDetails.


        :param benefit_category: The benefit_category of this EbtDetails.  # noqa: E501
        :type: str
        """
        if benefit_category is None:
            raise ValueError("Invalid value for `benefit_category`, must not be `None`")  # noqa: E501
        allowed_values = ["CASH", "FOOD_STAMP"]  # noqa: E501
        if benefit_category not in allowed_values:
            raise ValueError(
                "Invalid value for `benefit_category` ({0}), must be one of {1}"  # noqa: E501
                .format(benefit_category, allowed_values)
            )

        self._benefit_category = benefit_category

    @property
    def withdrawal(self):
        """Gets the withdrawal of this EbtDetails.  # noqa: E501

        Indicates a cash withdrawal request. This option is only available for EBT cash benefit accounts.  # noqa: E501

        :return: The withdrawal of this EbtDetails.  # noqa: E501
        :rtype: bool
        """
        return self._withdrawal

    @withdrawal.setter
    def withdrawal(self, withdrawal):
        """Sets the withdrawal of this EbtDetails.

        Indicates a cash withdrawal request. This option is only available for EBT cash benefit accounts.  # noqa: E501

        :param withdrawal: The withdrawal of this EbtDetails.  # noqa: E501
        :type: bool
        """

        self._withdrawal = withdrawal

    @property
    def voucher(self):
        """Gets the voucher of this EbtDetails.  # noqa: E501


        :return: The voucher of this EbtDetails.  # noqa: E501
        :rtype: Voucher
        """
        return self._voucher

    @voucher.setter
    def voucher(self, voucher):
        """Sets the voucher of this EbtDetails.


        :param voucher: The voucher of this EbtDetails.  # noqa: E501
        :type: Voucher
        """

        self._voucher = voucher
