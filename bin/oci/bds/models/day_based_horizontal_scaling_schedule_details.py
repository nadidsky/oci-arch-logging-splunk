# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .horizontal_scaling_schedule_details import HorizontalScalingScheduleDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DayBasedHorizontalScalingScheduleDetails(HorizontalScalingScheduleDetails):
    """
    Details of day based horizontal scaling schedule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DayBasedHorizontalScalingScheduleDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.DayBasedHorizontalScalingScheduleDetails.schedule_type` attribute
        of this class is ``DAY_BASED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schedule_type:
            The value to assign to the schedule_type property of this DayBasedHorizontalScalingScheduleDetails.
        :type schedule_type: str

        :param time_and_horizontal_scaling_config:
            The value to assign to the time_and_horizontal_scaling_config property of this DayBasedHorizontalScalingScheduleDetails.
        :type time_and_horizontal_scaling_config: list[oci.bds.models.TimeAndHorizontalScalingConfig]

        """
        self.swagger_types = {
            'schedule_type': 'str',
            'time_and_horizontal_scaling_config': 'list[TimeAndHorizontalScalingConfig]'
        }

        self.attribute_map = {
            'schedule_type': 'scheduleType',
            'time_and_horizontal_scaling_config': 'timeAndHorizontalScalingConfig'
        }

        self._schedule_type = None
        self._time_and_horizontal_scaling_config = None
        self._schedule_type = 'DAY_BASED'

    @property
    def time_and_horizontal_scaling_config(self):
        """
        Gets the time_and_horizontal_scaling_config of this DayBasedHorizontalScalingScheduleDetails.

        :return: The time_and_horizontal_scaling_config of this DayBasedHorizontalScalingScheduleDetails.
        :rtype: list[oci.bds.models.TimeAndHorizontalScalingConfig]
        """
        return self._time_and_horizontal_scaling_config

    @time_and_horizontal_scaling_config.setter
    def time_and_horizontal_scaling_config(self, time_and_horizontal_scaling_config):
        """
        Sets the time_and_horizontal_scaling_config of this DayBasedHorizontalScalingScheduleDetails.

        :param time_and_horizontal_scaling_config: The time_and_horizontal_scaling_config of this DayBasedHorizontalScalingScheduleDetails.
        :type: list[oci.bds.models.TimeAndHorizontalScalingConfig]
        """
        self._time_and_horizontal_scaling_config = time_and_horizontal_scaling_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
