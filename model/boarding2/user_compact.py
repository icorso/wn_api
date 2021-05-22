# coding: utf-8

from model.serializable import SwaggerSerializable


class UserCompact(SwaggerSerializable):
    swagger_types = {
        'user_id': 'str',
        'user_name': 'str',
        'gete_mail': 'str',
        'active_status': 'str',
        'locked_status': 'str',
        'links': 'list[HypermediaLink]'
    }

    attribute_map = {
        'user_id': 'userId',
        'user_name': 'userName',
        'gete_mail': 'geteMail',
        'active_status': 'activeStatus',
        'locked_status': 'lockedStatus',
        'links': 'links'
    }

    def __init__(self, user_id=None, user_name=None, gete_mail=None, active_status=None, locked_status=None, links=None):  # noqa: E501
        """UserCompact - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._user_name = None
        self._gete_mail = None
        self._active_status = None
        self._locked_status = None
        self._links = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if gete_mail is not None:
            self.gete_mail = gete_mail
        if active_status is not None:
            self.active_status = active_status
        if locked_status is not None:
            self.locked_status = locked_status
        if links is not None:
            self.links = links

    @property
    def user_id(self):
        """Gets the user_id of this UserCompact.  # noqa: E501


        :return: The user_id of this UserCompact.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserCompact.


        :param user_id: The user_id of this UserCompact.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this UserCompact.  # noqa: E501


        :return: The user_name of this UserCompact.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserCompact.


        :param user_name: The user_name of this UserCompact.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def gete_mail(self):
        """Gets the gete_mail of this UserCompact.  # noqa: E501


        :return: The gete_mail of this UserCompact.  # noqa: E501
        :rtype: str
        """
        return self._gete_mail

    @gete_mail.setter
    def gete_mail(self, gete_mail):
        """Sets the gete_mail of this UserCompact.


        :param gete_mail: The gete_mail of this UserCompact.  # noqa: E501
        :type: str
        """

        self._gete_mail = gete_mail

    @property
    def active_status(self):
        """Gets the active_status of this UserCompact.  # noqa: E501


        :return: The active_status of this UserCompact.  # noqa: E501
        :rtype: str
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this UserCompact.


        :param active_status: The active_status of this UserCompact.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DESACTIVATED_BY_MERCHANT", "DESACTIVATED_BY_ADMIN", "MERCHANT_DESACTIVATED"]  # noqa: E501
        if active_status not in allowed_values:
            raise ValueError(
                "Invalid value for `active_status` ({0}), must be one of {1}"  # noqa: E501
                .format(active_status, allowed_values)
            )

        self._active_status = active_status

    @property
    def locked_status(self):
        """Gets the locked_status of this UserCompact.  # noqa: E501


        :return: The locked_status of this UserCompact.  # noqa: E501
        :rtype: str
        """
        return self._locked_status

    @locked_status.setter
    def locked_status(self, locked_status):
        """Sets the locked_status of this UserCompact.


        :param locked_status: The locked_status of this UserCompact.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "LOCKED_BY_TOO_MANY_ATTEMPTS", "LOCKED_BY_ADMIN", "LOCKED_BY_SELF"]  # noqa: E501
        if locked_status not in allowed_values:
            raise ValueError(
                "Invalid value for `locked_status` ({0}), must be one of {1}"  # noqa: E501
                .format(locked_status, allowed_values)
            )

        self._locked_status = locked_status

    @property
    def links(self):
        """Gets the links of this UserCompact.  # noqa: E501

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :return: The links of this UserCompact.  # noqa: E501
        :rtype: list[HypermediaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserCompact.

        List of hypermedia links containing the operations available for the resource.  # noqa: E501

        :param links: The links of this UserCompact.  # noqa: E501
        :type: list[HypermediaLink]
        """

        self._links = links

