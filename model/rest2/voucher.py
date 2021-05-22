# coding: utf-8

from model.serializable import SwaggerSerializable


class Voucher(SwaggerSerializable):
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
        'approval_code': 'str',
        'serial_number': 'str'
    }

    attribute_map = {
        'approval_code': 'approvalCode',
        'serial_number': 'serialNumber'
    }

    def __init__(self, approval_code=None, serial_number=None):  # noqa: E501
        """Voucher - a model defined in Swagger"""  # noqa: E501
        self._approval_code = None
        self._serial_number = None
        self.discriminator = None
        self.approval_code = approval_code
        self.serial_number = serial_number

    @property
    def approval_code(self):
        """Gets the approval_code of this Voucher.  # noqa: E501

        The authorization code issued by a customer service representative. This code is usually acquired via a phone call during which it is ensured that there are enough funds in the cardholder’s EBT account for the transaction.  # noqa: E501

        :return: The approval_code of this Voucher.  # noqa: E501
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """Sets the approval_code of this Voucher.

        The authorization code issued by a customer service representative. This code is usually acquired via a phone call during which it is ensured that there are enough funds in the cardholder’s EBT account for the transaction.  # noqa: E501

        :param approval_code: The approval_code of this Voucher.  # noqa: E501
        :type: str
        """
        if approval_code is None:
            raise ValueError("Invalid value for `approval_code`, must not be `None`")  # noqa: E501

        self._approval_code = approval_code

    @property
    def serial_number(self):
        """Gets the serial_number of this Voucher.  # noqa: E501

        The voucher serial number.  # noqa: E501

        :return: The serial_number of this Voucher.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this Voucher.

        The voucher serial number.  # noqa: E501

        :param serial_number: The serial_number of this Voucher.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number