# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalingPolicy(object):
    """
    Autoscaling policies define the criteria that trigger autoscaling actions and the actions to take.

    An autoscaling policy is part of an autoscaling configuration. For more information, see
    `Autoscaling`__.

    You can create the following types of autoscaling policies:

    - **Schedule-based:** Autoscaling events take place at the specific times that you schedule.
    - **Threshold-based:** An autoscaling action is triggered when a performance metric meets or exceeds a threshold.

    __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalingPolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.autoscaling.models.ScheduledPolicy`
        * :class:`~oci.autoscaling.models.ThresholdPolicy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity:
            The value to assign to the capacity property of this AutoScalingPolicy.
        :type capacity: oci.autoscaling.models.Capacity

        :param id:
            The value to assign to the id property of this AutoScalingPolicy.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AutoScalingPolicy.
        :type display_name: str

        :param policy_type:
            The value to assign to the policy_type property of this AutoScalingPolicy.
        :type policy_type: str

        :param time_created:
            The value to assign to the time_created property of this AutoScalingPolicy.
        :type time_created: datetime

        :param is_enabled:
            The value to assign to the is_enabled property of this AutoScalingPolicy.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'capacity': 'Capacity',
            'id': 'str',
            'display_name': 'str',
            'policy_type': 'str',
            'time_created': 'datetime',
            'is_enabled': 'bool'
        }

        self.attribute_map = {
            'capacity': 'capacity',
            'id': 'id',
            'display_name': 'displayName',
            'policy_type': 'policyType',
            'time_created': 'timeCreated',
            'is_enabled': 'isEnabled'
        }

        self._capacity = None
        self._id = None
        self._display_name = None
        self._policy_type = None
        self._time_created = None
        self._is_enabled = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['policyType']

        if type == 'scheduled':
            return 'ScheduledPolicy'

        if type == 'threshold':
            return 'ThresholdPolicy'
        else:
            return 'AutoScalingPolicy'

    @property
    def capacity(self):
        """
        Gets the capacity of this AutoScalingPolicy.
        The capacity requirements of the autoscaling policy.


        :return: The capacity of this AutoScalingPolicy.
        :rtype: oci.autoscaling.models.Capacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this AutoScalingPolicy.
        The capacity requirements of the autoscaling policy.


        :param capacity: The capacity of this AutoScalingPolicy.
        :type: oci.autoscaling.models.Capacity
        """
        self._capacity = capacity

    @property
    def id(self):
        """
        Gets the id of this AutoScalingPolicy.
        The ID of the autoscaling policy that is assigned after creation.


        :return: The id of this AutoScalingPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutoScalingPolicy.
        The ID of the autoscaling policy that is assigned after creation.


        :param id: The id of this AutoScalingPolicy.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this AutoScalingPolicy.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this AutoScalingPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutoScalingPolicy.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this AutoScalingPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this AutoScalingPolicy.
        The type of autoscaling policy.


        :return: The policy_type of this AutoScalingPolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this AutoScalingPolicy.
        The type of autoscaling policy.


        :param policy_type: The policy_type of this AutoScalingPolicy.
        :type: str
        """
        self._policy_type = policy_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AutoScalingPolicy.
        The date and time the autoscaling configuration was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this AutoScalingPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutoScalingPolicy.
        The date and time the autoscaling configuration was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this AutoScalingPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this AutoScalingPolicy.
        Whether the autoscaling policy is enabled.


        :return: The is_enabled of this AutoScalingPolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AutoScalingPolicy.
        Whether the autoscaling policy is enabled.


        :param is_enabled: The is_enabled of this AutoScalingPolicy.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
