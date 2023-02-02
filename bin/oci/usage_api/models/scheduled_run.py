# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledRun(object):
    """
    The saved schedule run.
    """

    #: A constant which can be used with the lifecycle_state property of a ScheduledRun.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ScheduledRun.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledRun object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScheduledRun.
        :type id: str

        :param schedule_id:
            The value to assign to the schedule_id property of this ScheduledRun.
        :type schedule_id: str

        :param time_created:
            The value to assign to the time_created property of this ScheduledRun.
        :type time_created: datetime

        :param time_finished:
            The value to assign to the time_finished property of this ScheduledRun.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduledRun.
            Allowed values for this property are: "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ScheduledRun.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'schedule_id': 'str',
            'time_created': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'schedule_id': 'scheduleId',
            'time_created': 'timeCreated',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._schedule_id = None
        self._time_created = None
        self._time_finished = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduledRun.
        The ocid representing unique shedule run


        :return: The id of this ScheduledRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledRun.
        The ocid representing unique shedule run


        :param id: The id of this ScheduledRun.
        :type: str
        """
        self._id = id

    @property
    def schedule_id(self):
        """
        **[Required]** Gets the schedule_id of this ScheduledRun.
        The ocid representing unique shedule


        :return: The schedule_id of this ScheduledRun.
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """
        Sets the schedule_id of this ScheduledRun.
        The ocid representing unique shedule


        :param schedule_id: The schedule_id of this ScheduledRun.
        :type: str
        """
        self._schedule_id = schedule_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ScheduledRun.
        The time when schedule started executing


        :return: The time_created of this ScheduledRun.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ScheduledRun.
        The time when schedule started executing


        :param time_created: The time_created of this ScheduledRun.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_finished(self):
        """
        **[Required]** Gets the time_finished of this ScheduledRun.
        The time when schedule finished executing


        :return: The time_finished of this ScheduledRun.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this ScheduledRun.
        The time when schedule finished executing


        :param time_finished: The time_finished of this ScheduledRun.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ScheduledRun.
        Specifies if the schedule job was run successfully or not.

        Allowed values for this property are: "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ScheduledRun.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduledRun.
        Specifies if the schedule job was run successfully or not.


        :param lifecycle_state: The lifecycle_state of this ScheduledRun.
        :type: str
        """
        allowed_values = ["FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this ScheduledRun.
        Additional details about scheduled run failure


        :return: The lifecycle_details of this ScheduledRun.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ScheduledRun.
        Additional details about scheduled run failure


        :param lifecycle_details: The lifecycle_details of this ScheduledRun.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
