# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbCredentialDetails(object):
    """
    CreateDbCredentialDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbCredentialDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password:
            The value to assign to the password property of this CreateDbCredentialDetails.
        :type password: str

        :param description:
            The value to assign to the description property of this CreateDbCredentialDetails.
        :type description: str

        """
        self.swagger_types = {
            'password': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'password': 'password',
            'description': 'description'
        }

        self._password = None
        self._description = None

    @property
    def password(self):
        """
        **[Required]** Gets the password of this CreateDbCredentialDetails.
        The password for the DB credentials during creation.


        :return: The password of this CreateDbCredentialDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateDbCredentialDetails.
        The password for the DB credentials during creation.


        :param password: The password of this CreateDbCredentialDetails.
        :type: str
        """
        self._password = password

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateDbCredentialDetails.
        The description you assign to the DB credentials during creation.

        (For tenancies that support identity domains) You can have an empty description.


        :return: The description of this CreateDbCredentialDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDbCredentialDetails.
        The description you assign to the DB credentials during creation.

        (For tenancies that support identity domains) You can have an empty description.


        :param description: The description of this CreateDbCredentialDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
