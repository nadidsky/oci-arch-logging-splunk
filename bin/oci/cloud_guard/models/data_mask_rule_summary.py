# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataMaskRuleSummary(object):
    """
    Summary of DataMaskRule.
    """

    #: A constant which can be used with the data_mask_categories property of a DataMaskRuleSummary.
    #: This constant has a value of "ACTOR"
    DATA_MASK_CATEGORIES_ACTOR = "ACTOR"

    #: A constant which can be used with the data_mask_categories property of a DataMaskRuleSummary.
    #: This constant has a value of "PII"
    DATA_MASK_CATEGORIES_PII = "PII"

    #: A constant which can be used with the data_mask_categories property of a DataMaskRuleSummary.
    #: This constant has a value of "PHI"
    DATA_MASK_CATEGORIES_PHI = "PHI"

    #: A constant which can be used with the data_mask_categories property of a DataMaskRuleSummary.
    #: This constant has a value of "FINANCIAL"
    DATA_MASK_CATEGORIES_FINANCIAL = "FINANCIAL"

    #: A constant which can be used with the data_mask_categories property of a DataMaskRuleSummary.
    #: This constant has a value of "LOCATION"
    DATA_MASK_CATEGORIES_LOCATION = "LOCATION"

    #: A constant which can be used with the data_mask_categories property of a DataMaskRuleSummary.
    #: This constant has a value of "CUSTOM"
    DATA_MASK_CATEGORIES_CUSTOM = "CUSTOM"

    #: A constant which can be used with the data_mask_rule_status property of a DataMaskRuleSummary.
    #: This constant has a value of "ENABLED"
    DATA_MASK_RULE_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the data_mask_rule_status property of a DataMaskRuleSummary.
    #: This constant has a value of "DISABLED"
    DATA_MASK_RULE_STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a DataMaskRuleSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DataMaskRuleSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DataMaskRuleSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DataMaskRuleSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DataMaskRuleSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DataMaskRuleSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DataMaskRuleSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DataMaskRuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DataMaskRuleSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DataMaskRuleSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DataMaskRuleSummary.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this DataMaskRuleSummary.
        :type description: str

        :param iam_group_id:
            The value to assign to the iam_group_id property of this DataMaskRuleSummary.
        :type iam_group_id: str

        :param target_selected:
            The value to assign to the target_selected property of this DataMaskRuleSummary.
        :type target_selected: oci.cloud_guard.models.TargetSelected

        :param data_mask_categories:
            The value to assign to the data_mask_categories property of this DataMaskRuleSummary.
            Allowed values for items in this list are: "ACTOR", "PII", "PHI", "FINANCIAL", "LOCATION", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_mask_categories: list[str]

        :param time_created:
            The value to assign to the time_created property of this DataMaskRuleSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DataMaskRuleSummary.
        :type time_updated: datetime

        :param data_mask_rule_status:
            The value to assign to the data_mask_rule_status property of this DataMaskRuleSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_mask_rule_status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataMaskRuleSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecyle_details:
            The value to assign to the lifecyle_details property of this DataMaskRuleSummary.
        :type lifecyle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DataMaskRuleSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DataMaskRuleSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DataMaskRuleSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'iam_group_id': 'str',
            'target_selected': 'TargetSelected',
            'data_mask_categories': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'data_mask_rule_status': 'str',
            'lifecycle_state': 'str',
            'lifecyle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'iam_group_id': 'iamGroupId',
            'target_selected': 'targetSelected',
            'data_mask_categories': 'dataMaskCategories',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'data_mask_rule_status': 'dataMaskRuleStatus',
            'lifecycle_state': 'lifecycleState',
            'lifecyle_details': 'lifecyleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._iam_group_id = None
        self._target_selected = None
        self._data_mask_categories = None
        self._time_created = None
        self._time_updated = None
        self._data_mask_rule_status = None
        self._lifecycle_state = None
        self._lifecyle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DataMaskRuleSummary.
        Unique identifier that is immutable on creation


        :return: The id of this DataMaskRuleSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataMaskRuleSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this DataMaskRuleSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this DataMaskRuleSummary.
        Data Mask Rule Name.


        :return: The display_name of this DataMaskRuleSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DataMaskRuleSummary.
        Data Mask Rule Name.


        :param display_name: The display_name of this DataMaskRuleSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DataMaskRuleSummary.
        Compartment Identifier where the resource is created


        :return: The compartment_id of this DataMaskRuleSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DataMaskRuleSummary.
        Compartment Identifier where the resource is created


        :param compartment_id: The compartment_id of this DataMaskRuleSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this DataMaskRuleSummary.
        The data mask rule description.


        :return: The description of this DataMaskRuleSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataMaskRuleSummary.
        The data mask rule description.


        :param description: The description of this DataMaskRuleSummary.
        :type: str
        """
        self._description = description

    @property
    def iam_group_id(self):
        """
        **[Required]** Gets the iam_group_id of this DataMaskRuleSummary.
        IAM Group id associated with the data mask rule


        :return: The iam_group_id of this DataMaskRuleSummary.
        :rtype: str
        """
        return self._iam_group_id

    @iam_group_id.setter
    def iam_group_id(self, iam_group_id):
        """
        Sets the iam_group_id of this DataMaskRuleSummary.
        IAM Group id associated with the data mask rule


        :param iam_group_id: The iam_group_id of this DataMaskRuleSummary.
        :type: str
        """
        self._iam_group_id = iam_group_id

    @property
    def target_selected(self):
        """
        **[Required]** Gets the target_selected of this DataMaskRuleSummary.

        :return: The target_selected of this DataMaskRuleSummary.
        :rtype: oci.cloud_guard.models.TargetSelected
        """
        return self._target_selected

    @target_selected.setter
    def target_selected(self, target_selected):
        """
        Sets the target_selected of this DataMaskRuleSummary.

        :param target_selected: The target_selected of this DataMaskRuleSummary.
        :type: oci.cloud_guard.models.TargetSelected
        """
        self._target_selected = target_selected

    @property
    def data_mask_categories(self):
        """
        Gets the data_mask_categories of this DataMaskRuleSummary.
        Data Mask Categories

        Allowed values for items in this list are: "ACTOR", "PII", "PHI", "FINANCIAL", "LOCATION", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_mask_categories of this DataMaskRuleSummary.
        :rtype: list[str]
        """
        return self._data_mask_categories

    @data_mask_categories.setter
    def data_mask_categories(self, data_mask_categories):
        """
        Sets the data_mask_categories of this DataMaskRuleSummary.
        Data Mask Categories


        :param data_mask_categories: The data_mask_categories of this DataMaskRuleSummary.
        :type: list[str]
        """
        allowed_values = ["ACTOR", "PII", "PHI", "FINANCIAL", "LOCATION", "CUSTOM"]
        if data_mask_categories:
            data_mask_categories[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in data_mask_categories]
        self._data_mask_categories = data_mask_categories

    @property
    def time_created(self):
        """
        Gets the time_created of this DataMaskRuleSummary.
        The date and time the target was created. Format defined by RFC3339.


        :return: The time_created of this DataMaskRuleSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataMaskRuleSummary.
        The date and time the target was created. Format defined by RFC3339.


        :param time_created: The time_created of this DataMaskRuleSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DataMaskRuleSummary.
        The date and time the target was updated. Format defined by RFC3339.


        :return: The time_updated of this DataMaskRuleSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DataMaskRuleSummary.
        The date and time the target was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this DataMaskRuleSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def data_mask_rule_status(self):
        """
        Gets the data_mask_rule_status of this DataMaskRuleSummary.
        The status of the dataMaskRule.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_mask_rule_status of this DataMaskRuleSummary.
        :rtype: str
        """
        return self._data_mask_rule_status

    @data_mask_rule_status.setter
    def data_mask_rule_status(self, data_mask_rule_status):
        """
        Sets the data_mask_rule_status of this DataMaskRuleSummary.
        The status of the dataMaskRule.


        :param data_mask_rule_status: The data_mask_rule_status of this DataMaskRuleSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(data_mask_rule_status, allowed_values):
            data_mask_rule_status = 'UNKNOWN_ENUM_VALUE'
        self._data_mask_rule_status = data_mask_rule_status

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DataMaskRuleSummary.
        The current state of the DataMaskRule.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DataMaskRuleSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataMaskRuleSummary.
        The current state of the DataMaskRule.


        :param lifecycle_state: The lifecycle_state of this DataMaskRuleSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecyle_details(self):
        """
        Gets the lifecyle_details of this DataMaskRuleSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecyle_details of this DataMaskRuleSummary.
        :rtype: str
        """
        return self._lifecyle_details

    @lifecyle_details.setter
    def lifecyle_details(self, lifecyle_details):
        """
        Sets the lifecyle_details of this DataMaskRuleSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecyle_details: The lifecyle_details of this DataMaskRuleSummary.
        :type: str
        """
        self._lifecyle_details = lifecyle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DataMaskRuleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this DataMaskRuleSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DataMaskRuleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this DataMaskRuleSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DataMaskRuleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DataMaskRuleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DataMaskRuleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DataMaskRuleSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DataMaskRuleSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DataMaskRuleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DataMaskRuleSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DataMaskRuleSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
