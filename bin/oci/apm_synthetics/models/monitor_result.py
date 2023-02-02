# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitorResult(object):
    """
    The monitor result for a specific execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitorResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param result_type:
            The value to assign to the result_type property of this MonitorResult.
        :type result_type: str

        :param result_content_type:
            The value to assign to the result_content_type property of this MonitorResult.
        :type result_content_type: str

        :param result_data_set:
            The value to assign to the result_data_set property of this MonitorResult.
        :type result_data_set: list[oci.apm_synthetics.models.MonitorResultData]

        :param monitor_id:
            The value to assign to the monitor_id property of this MonitorResult.
        :type monitor_id: str

        :param vantage_point:
            The value to assign to the vantage_point property of this MonitorResult.
        :type vantage_point: str

        :param execution_time:
            The value to assign to the execution_time property of this MonitorResult.
        :type execution_time: str

        """
        self.swagger_types = {
            'result_type': 'str',
            'result_content_type': 'str',
            'result_data_set': 'list[MonitorResultData]',
            'monitor_id': 'str',
            'vantage_point': 'str',
            'execution_time': 'str'
        }

        self.attribute_map = {
            'result_type': 'resultType',
            'result_content_type': 'resultContentType',
            'result_data_set': 'resultDataSet',
            'monitor_id': 'monitorId',
            'vantage_point': 'vantagePoint',
            'execution_time': 'executionTime'
        }

        self._result_type = None
        self._result_content_type = None
        self._result_data_set = None
        self._monitor_id = None
        self._vantage_point = None
        self._execution_time = None

    @property
    def result_type(self):
        """
        Gets the result_type of this MonitorResult.
        Type of result.
        Example: HAR, Screenshot, Log or Network.


        :return: The result_type of this MonitorResult.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """
        Sets the result_type of this MonitorResult.
        Type of result.
        Example: HAR, Screenshot, Log or Network.


        :param result_type: The result_type of this MonitorResult.
        :type: str
        """
        self._result_type = result_type

    @property
    def result_content_type(self):
        """
        **[Required]** Gets the result_content_type of this MonitorResult.
        Type of result content.
        Example: Zip or Raw file.


        :return: The result_content_type of this MonitorResult.
        :rtype: str
        """
        return self._result_content_type

    @result_content_type.setter
    def result_content_type(self, result_content_type):
        """
        Sets the result_content_type of this MonitorResult.
        Type of result content.
        Example: Zip or Raw file.


        :param result_content_type: The result_content_type of this MonitorResult.
        :type: str
        """
        self._result_content_type = result_content_type

    @property
    def result_data_set(self):
        """
        Gets the result_data_set of this MonitorResult.
        Monitor result data set.


        :return: The result_data_set of this MonitorResult.
        :rtype: list[oci.apm_synthetics.models.MonitorResultData]
        """
        return self._result_data_set

    @result_data_set.setter
    def result_data_set(self, result_data_set):
        """
        Sets the result_data_set of this MonitorResult.
        Monitor result data set.


        :param result_data_set: The result_data_set of this MonitorResult.
        :type: list[oci.apm_synthetics.models.MonitorResultData]
        """
        self._result_data_set = result_data_set

    @property
    def monitor_id(self):
        """
        Gets the monitor_id of this MonitorResult.
        The `OCID`__ of the monitor.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The monitor_id of this MonitorResult.
        :rtype: str
        """
        return self._monitor_id

    @monitor_id.setter
    def monitor_id(self, monitor_id):
        """
        Sets the monitor_id of this MonitorResult.
        The `OCID`__ of the monitor.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param monitor_id: The monitor_id of this MonitorResult.
        :type: str
        """
        self._monitor_id = monitor_id

    @property
    def vantage_point(self):
        """
        Gets the vantage_point of this MonitorResult.
        The name of the public or dedicated vantage point.


        :return: The vantage_point of this MonitorResult.
        :rtype: str
        """
        return self._vantage_point

    @vantage_point.setter
    def vantage_point(self, vantage_point):
        """
        Sets the vantage_point of this MonitorResult.
        The name of the public or dedicated vantage point.


        :param vantage_point: The vantage_point of this MonitorResult.
        :type: str
        """
        self._vantage_point = vantage_point

    @property
    def execution_time(self):
        """
        Gets the execution_time of this MonitorResult.
        The specific point of time when the result of an execution is collected.


        :return: The execution_time of this MonitorResult.
        :rtype: str
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """
        Sets the execution_time of this MonitorResult.
        The specific point of time when the result of an execution is collected.


        :param execution_time: The execution_time of this MonitorResult.
        :type: str
        """
        self._execution_time = execution_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
