# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrProtectionGroupMemberDetails(object):
    """
    Create properties for a member in a DR Protection Group.
    """

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "COMPUTE_INSTANCE"
    MEMBER_TYPE_COMPUTE_INSTANCE = "COMPUTE_INSTANCE"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "VOLUME_GROUP"
    MEMBER_TYPE_VOLUME_GROUP = "VOLUME_GROUP"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "DATABASE"
    MEMBER_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the member_type property of a CreateDrProtectionGroupMemberDetails.
    #: This constant has a value of "AUTONOMOUS_DATABASE"
    MEMBER_TYPE_AUTONOMOUS_DATABASE = "AUTONOMOUS_DATABASE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrProtectionGroupMemberDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberComputeInstanceDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberDatabaseDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberAutonomousDatabaseDetails`
        * :class:`~oci.disaster_recovery.models.CreateDrProtectionGroupMemberVolumeGroupDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this CreateDrProtectionGroupMemberDetails.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this CreateDrProtectionGroupMemberDetails.
            Allowed values for this property are: "COMPUTE_INSTANCE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE"
        :type member_type: str

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str'
        }

        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType'
        }

        self._member_id = None
        self._member_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['memberType']

        if type == 'COMPUTE_INSTANCE':
            return 'CreateDrProtectionGroupMemberComputeInstanceDetails'

        if type == 'DATABASE':
            return 'CreateDrProtectionGroupMemberDatabaseDetails'

        if type == 'AUTONOMOUS_DATABASE':
            return 'CreateDrProtectionGroupMemberAutonomousDatabaseDetails'

        if type == 'VOLUME_GROUP':
            return 'CreateDrProtectionGroupMemberVolumeGroupDetails'
        else:
            return 'CreateDrProtectionGroupMemberDetails'

    @property
    def member_id(self):
        """
        **[Required]** Gets the member_id of this CreateDrProtectionGroupMemberDetails.
        The OCID of the member.

        Example: `ocid1.instance.oc1.phx.exampleocid1`


        :return: The member_id of this CreateDrProtectionGroupMemberDetails.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this CreateDrProtectionGroupMemberDetails.
        The OCID of the member.

        Example: `ocid1.instance.oc1.phx.exampleocid1`


        :param member_id: The member_id of this CreateDrProtectionGroupMemberDetails.
        :type: str
        """
        self._member_id = member_id

    @property
    def member_type(self):
        """
        **[Required]** Gets the member_type of this CreateDrProtectionGroupMemberDetails.
        The type of the member.

        Allowed values for this property are: "COMPUTE_INSTANCE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE"


        :return: The member_type of this CreateDrProtectionGroupMemberDetails.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """
        Sets the member_type of this CreateDrProtectionGroupMemberDetails.
        The type of the member.


        :param member_type: The member_type of this CreateDrProtectionGroupMemberDetails.
        :type: str
        """
        allowed_values = ["COMPUTE_INSTANCE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE"]
        if not value_allowed_none_or_none_sentinel(member_type, allowed_values):
            raise ValueError(
                "Invalid value for `member_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._member_type = member_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
