# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessRequestSummary(object):
    """
    Summary of access request.
    """

    #: A constant which can be used with the resource_type property of a AccessRequestSummary.
    #: This constant has a value of "EXACC"
    RESOURCE_TYPE_EXACC = "EXACC"

    #: A constant which can be used with the resource_type property of a AccessRequestSummary.
    #: This constant has a value of "EXADATAINFRASTRUCTURE"
    RESOURCE_TYPE_EXADATAINFRASTRUCTURE = "EXADATAINFRASTRUCTURE"

    #: A constant which can be used with the resource_type property of a AccessRequestSummary.
    #: This constant has a value of "AUTONOMOUSVMCLUSTER"
    RESOURCE_TYPE_AUTONOMOUSVMCLUSTER = "AUTONOMOUSVMCLUSTER"

    #: A constant which can be used with the resource_type property of a AccessRequestSummary.
    #: This constant has a value of "CLOUDAUTONOMOUSVMCLUSTER"
    RESOURCE_TYPE_CLOUDAUTONOMOUSVMCLUSTER = "CLOUDAUTONOMOUSVMCLUSTER"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "CREATED"
    LIFECYCLE_STATE_CREATED = "CREATED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "APPROVALWAITING"
    LIFECYCLE_STATE_APPROVALWAITING = "APPROVALWAITING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "PREAPPROVED"
    LIFECYCLE_STATE_PREAPPROVED = "PREAPPROVED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "APPROVED"
    LIFECYCLE_STATE_APPROVED = "APPROVED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "MOREINFO"
    LIFECYCLE_STATE_MOREINFO = "MOREINFO"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "REJECTED"
    LIFECYCLE_STATE_REJECTED = "REJECTED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "DEPLOYED"
    LIFECYCLE_STATE_DEPLOYED = "DEPLOYED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "DEPLOYFAILED"
    LIFECYCLE_STATE_DEPLOYFAILED = "DEPLOYFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "UNDEPLOYED"
    LIFECYCLE_STATE_UNDEPLOYED = "UNDEPLOYED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "UNDEPLOYFAILED"
    LIFECYCLE_STATE_UNDEPLOYFAILED = "UNDEPLOYFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "CLOSEFAILED"
    LIFECYCLE_STATE_CLOSEFAILED = "CLOSEFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "REVOKEFAILED"
    LIFECYCLE_STATE_REVOKEFAILED = "REVOKEFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "EXPIRYFAILED"
    LIFECYCLE_STATE_EXPIRYFAILED = "EXPIRYFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "REVOKING"
    LIFECYCLE_STATE_REVOKING = "REVOKING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "REVOKED"
    LIFECYCLE_STATE_REVOKED = "REVOKED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "EXTENDING"
    LIFECYCLE_STATE_EXTENDING = "EXTENDING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "EXTENDED"
    LIFECYCLE_STATE_EXTENDED = "EXTENDED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "EXTENSIONREJECTED"
    LIFECYCLE_STATE_EXTENSIONREJECTED = "EXTENSIONREJECTED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "COMPLETING"
    LIFECYCLE_STATE_COMPLETING = "COMPLETING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "COMPLETED"
    LIFECYCLE_STATE_COMPLETED = "COMPLETED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "EXPIRED"
    LIFECYCLE_STATE_EXPIRED = "EXPIRED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "APPROVEDFORFUTURE"
    LIFECYCLE_STATE_APPROVEDFORFUTURE = "APPROVEDFORFUTURE"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestSummary.
    #: This constant has a value of "INREVIEW"
    LIFECYCLE_STATE_INREVIEW = "INREVIEW"

    #: A constant which can be used with the severity property of a AccessRequestSummary.
    #: This constant has a value of "S1"
    SEVERITY_S1 = "S1"

    #: A constant which can be used with the severity property of a AccessRequestSummary.
    #: This constant has a value of "S2"
    SEVERITY_S2 = "S2"

    #: A constant which can be used with the severity property of a AccessRequestSummary.
    #: This constant has a value of "S3"
    SEVERITY_S3 = "S3"

    #: A constant which can be used with the severity property of a AccessRequestSummary.
    #: This constant has a value of "S4"
    SEVERITY_S4 = "S4"

    def __init__(self, **kwargs):
        """
        Initializes a new AccessRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AccessRequestSummary.
        :type id: str

        :param request_id:
            The value to assign to the request_id property of this AccessRequestSummary.
        :type request_id: str

        :param access_reason_summary:
            The value to assign to the access_reason_summary property of this AccessRequestSummary.
        :type access_reason_summary: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AccessRequestSummary.
        :type compartment_id: str

        :param resource_id:
            The value to assign to the resource_id property of this AccessRequestSummary.
        :type resource_id: str

        :param resource_name:
            The value to assign to the resource_name property of this AccessRequestSummary.
        :type resource_name: str

        :param resource_type:
            The value to assign to the resource_type property of this AccessRequestSummary.
            Allowed values for this property are: "EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER", "CLOUDAUTONOMOUSVMCLUSTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AccessRequestSummary.
            Allowed values for this property are: "CREATED", "APPROVALWAITING", "PREAPPROVED", "APPROVED", "MOREINFO", "REJECTED", "DEPLOYED", "DEPLOYFAILED", "UNDEPLOYED", "UNDEPLOYFAILED", "CLOSEFAILED", "REVOKEFAILED", "EXPIRYFAILED", "REVOKING", "REVOKED", "EXTENDING", "EXTENDED", "EXTENSIONREJECTED", "COMPLETING", "COMPLETED", "EXPIRED", "APPROVEDFORFUTURE", "INREVIEW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AccessRequestSummary.
        :type lifecycle_details: str

        :param time_of_creation:
            The value to assign to the time_of_creation property of this AccessRequestSummary.
        :type time_of_creation: datetime

        :param time_of_modification:
            The value to assign to the time_of_modification property of this AccessRequestSummary.
        :type time_of_modification: datetime

        :param time_of_user_creation:
            The value to assign to the time_of_user_creation property of this AccessRequestSummary.
        :type time_of_user_creation: datetime

        :param duration:
            The value to assign to the duration property of this AccessRequestSummary.
        :type duration: int

        :param extend_duration:
            The value to assign to the extend_duration property of this AccessRequestSummary.
        :type extend_duration: int

        :param severity:
            The value to assign to the severity property of this AccessRequestSummary.
            Allowed values for this property are: "S1", "S2", "S3", "S4", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param is_auto_approved:
            The value to assign to the is_auto_approved property of this AccessRequestSummary.
        :type is_auto_approved: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AccessRequestSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AccessRequestSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'request_id': 'str',
            'access_reason_summary': 'str',
            'compartment_id': 'str',
            'resource_id': 'str',
            'resource_name': 'str',
            'resource_type': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_of_creation': 'datetime',
            'time_of_modification': 'datetime',
            'time_of_user_creation': 'datetime',
            'duration': 'int',
            'extend_duration': 'int',
            'severity': 'str',
            'is_auto_approved': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'request_id': 'requestId',
            'access_reason_summary': 'accessReasonSummary',
            'compartment_id': 'compartmentId',
            'resource_id': 'resourceId',
            'resource_name': 'resourceName',
            'resource_type': 'resourceType',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_of_creation': 'timeOfCreation',
            'time_of_modification': 'timeOfModification',
            'time_of_user_creation': 'timeOfUserCreation',
            'duration': 'duration',
            'extend_duration': 'extendDuration',
            'severity': 'severity',
            'is_auto_approved': 'isAutoApproved',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._request_id = None
        self._access_reason_summary = None
        self._compartment_id = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_of_creation = None
        self._time_of_modification = None
        self._time_of_user_creation = None
        self._duration = None
        self._extend_duration = None
        self._severity = None
        self._is_auto_approved = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AccessRequestSummary.
        The OCID of the access request.


        :return: The id of this AccessRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccessRequestSummary.
        The OCID of the access request.


        :param id: The id of this AccessRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def request_id(self):
        """
        Gets the request_id of this AccessRequestSummary.
        This is a system-generated identifier.


        :return: The request_id of this AccessRequestSummary.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this AccessRequestSummary.
        This is a system-generated identifier.


        :param request_id: The request_id of this AccessRequestSummary.
        :type: str
        """
        self._request_id = request_id

    @property
    def access_reason_summary(self):
        """
        **[Required]** Gets the access_reason_summary of this AccessRequestSummary.
        Comment associated with the access request.


        :return: The access_reason_summary of this AccessRequestSummary.
        :rtype: str
        """
        return self._access_reason_summary

    @access_reason_summary.setter
    def access_reason_summary(self, access_reason_summary):
        """
        Sets the access_reason_summary of this AccessRequestSummary.
        Comment associated with the access request.


        :param access_reason_summary: The access_reason_summary of this AccessRequestSummary.
        :type: str
        """
        self._access_reason_summary = access_reason_summary

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this AccessRequestSummary.
        The OCID of the compartment that contains the access request.


        :return: The compartment_id of this AccessRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AccessRequestSummary.
        The OCID of the compartment that contains the access request.


        :param compartment_id: The compartment_id of this AccessRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this AccessRequestSummary.
        The OCID of the target resource associated with the access request. The operator raises an access request to get approval to
        access the target resource.


        :return: The resource_id of this AccessRequestSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this AccessRequestSummary.
        The OCID of the target resource associated with the access request. The operator raises an access request to get approval to
        access the target resource.


        :param resource_id: The resource_id of this AccessRequestSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """
        Gets the resource_name of this AccessRequestSummary.
        The name of the target resource.


        :return: The resource_name of this AccessRequestSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this AccessRequestSummary.
        The name of the target resource.


        :param resource_name: The resource_name of this AccessRequestSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this AccessRequestSummary.
        resourceType for which the AccessRequest is applicable

        Allowed values for this property are: "EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER", "CLOUDAUTONOMOUSVMCLUSTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this AccessRequestSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this AccessRequestSummary.
        resourceType for which the AccessRequest is applicable


        :param resource_type: The resource_type of this AccessRequestSummary.
        :type: str
        """
        allowed_values = ["EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER", "CLOUDAUTONOMOUSVMCLUSTER"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AccessRequestSummary.
        The current state of the AccessRequest.

        Allowed values for this property are: "CREATED", "APPROVALWAITING", "PREAPPROVED", "APPROVED", "MOREINFO", "REJECTED", "DEPLOYED", "DEPLOYFAILED", "UNDEPLOYED", "UNDEPLOYFAILED", "CLOSEFAILED", "REVOKEFAILED", "EXPIRYFAILED", "REVOKING", "REVOKED", "EXTENDING", "EXTENDED", "EXTENSIONREJECTED", "COMPLETING", "COMPLETED", "EXPIRED", "APPROVEDFORFUTURE", "INREVIEW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AccessRequestSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AccessRequestSummary.
        The current state of the AccessRequest.


        :param lifecycle_state: The lifecycle_state of this AccessRequestSummary.
        :type: str
        """
        allowed_values = ["CREATED", "APPROVALWAITING", "PREAPPROVED", "APPROVED", "MOREINFO", "REJECTED", "DEPLOYED", "DEPLOYFAILED", "UNDEPLOYED", "UNDEPLOYFAILED", "CLOSEFAILED", "REVOKEFAILED", "EXPIRYFAILED", "REVOKING", "REVOKED", "EXTENDING", "EXTENDED", "EXTENSIONREJECTED", "COMPLETING", "COMPLETED", "EXPIRED", "APPROVEDFORFUTURE", "INREVIEW"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AccessRequestSummary.
        More in detail about the lifeCycleState.


        :return: The lifecycle_details of this AccessRequestSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AccessRequestSummary.
        More in detail about the lifeCycleState.


        :param lifecycle_details: The lifecycle_details of this AccessRequestSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_of_creation(self):
        """
        Gets the time_of_creation of this AccessRequestSummary.
        Time when the access request was created by the operator user in `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_creation of this AccessRequestSummary.
        :rtype: datetime
        """
        return self._time_of_creation

    @time_of_creation.setter
    def time_of_creation(self, time_of_creation):
        """
        Sets the time_of_creation of this AccessRequestSummary.
        Time when the access request was created by the operator user in `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_creation: The time_of_creation of this AccessRequestSummary.
        :type: datetime
        """
        self._time_of_creation = time_of_creation

    @property
    def time_of_modification(self):
        """
        Gets the time_of_modification of this AccessRequestSummary.
        Time when the access request was last modified in `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_modification of this AccessRequestSummary.
        :rtype: datetime
        """
        return self._time_of_modification

    @time_of_modification.setter
    def time_of_modification(self, time_of_modification):
        """
        Sets the time_of_modification of this AccessRequestSummary.
        Time when the access request was last modified in `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_modification: The time_of_modification of this AccessRequestSummary.
        :type: datetime
        """
        self._time_of_modification = time_of_modification

    @property
    def time_of_user_creation(self):
        """
        Gets the time_of_user_creation of this AccessRequestSummary.
        The time when access request is scheduled to be approved in `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_user_creation of this AccessRequestSummary.
        :rtype: datetime
        """
        return self._time_of_user_creation

    @time_of_user_creation.setter
    def time_of_user_creation(self, time_of_user_creation):
        """
        Sets the time_of_user_creation of this AccessRequestSummary.
        The time when access request is scheduled to be approved in `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_user_creation: The time_of_user_creation of this AccessRequestSummary.
        :type: datetime
        """
        self._time_of_user_creation = time_of_user_creation

    @property
    def duration(self):
        """
        Gets the duration of this AccessRequestSummary.
        Duration in hours for which access is sought on the target resource.


        :return: The duration of this AccessRequestSummary.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this AccessRequestSummary.
        Duration in hours for which access is sought on the target resource.


        :param duration: The duration of this AccessRequestSummary.
        :type: int
        """
        self._duration = duration

    @property
    def extend_duration(self):
        """
        Gets the extend_duration of this AccessRequestSummary.
        Duration in hours for which extension access is sought on the target resource.


        :return: The extend_duration of this AccessRequestSummary.
        :rtype: int
        """
        return self._extend_duration

    @extend_duration.setter
    def extend_duration(self, extend_duration):
        """
        Sets the extend_duration of this AccessRequestSummary.
        Duration in hours for which extension access is sought on the target resource.


        :param extend_duration: The extend_duration of this AccessRequestSummary.
        :type: int
        """
        self._extend_duration = extend_duration

    @property
    def severity(self):
        """
        Gets the severity of this AccessRequestSummary.
        Priority assigned to the access request by the operator

        Allowed values for this property are: "S1", "S2", "S3", "S4", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this AccessRequestSummary.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this AccessRequestSummary.
        Priority assigned to the access request by the operator


        :param severity: The severity of this AccessRequestSummary.
        :type: str
        """
        allowed_values = ["S1", "S2", "S3", "S4"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def is_auto_approved(self):
        """
        Gets the is_auto_approved of this AccessRequestSummary.
        Whether the access request was automatically approved.


        :return: The is_auto_approved of this AccessRequestSummary.
        :rtype: bool
        """
        return self._is_auto_approved

    @is_auto_approved.setter
    def is_auto_approved(self, is_auto_approved):
        """
        Sets the is_auto_approved of this AccessRequestSummary.
        Whether the access request was automatically approved.


        :param is_auto_approved: The is_auto_approved of this AccessRequestSummary.
        :type: bool
        """
        self._is_auto_approved = is_auto_approved

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AccessRequestSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :return: The freeform_tags of this AccessRequestSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AccessRequestSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :param freeform_tags: The freeform_tags of this AccessRequestSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AccessRequestSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :return: The defined_tags of this AccessRequestSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AccessRequestSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :param defined_tags: The defined_tags of this AccessRequestSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
