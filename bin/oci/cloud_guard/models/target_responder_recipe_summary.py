# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetResponderRecipeSummary(object):
    """
    Summary of ResponderRecipe
    """

    #: A constant which can be used with the owner property of a TargetResponderRecipeSummary.
    #: This constant has a value of "CUSTOMER"
    OWNER_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the owner property of a TargetResponderRecipeSummary.
    #: This constant has a value of "ORACLE"
    OWNER_ORACLE = "ORACLE"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetResponderRecipeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TargetResponderRecipeSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TargetResponderRecipeSummary.
        :type compartment_id: str

        :param responder_recipe_id:
            The value to assign to the responder_recipe_id property of this TargetResponderRecipeSummary.
        :type responder_recipe_id: str

        :param display_name:
            The value to assign to the display_name property of this TargetResponderRecipeSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TargetResponderRecipeSummary.
        :type description: str

        :param owner:
            The value to assign to the owner property of this TargetResponderRecipeSummary.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type owner: str

        :param time_created:
            The value to assign to the time_created property of this TargetResponderRecipeSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TargetResponderRecipeSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TargetResponderRecipeSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TargetResponderRecipeSummary.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'responder_recipe_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'owner': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'responder_recipe_id': 'responderRecipeId',
            'display_name': 'displayName',
            'description': 'description',
            'owner': 'owner',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._compartment_id = None
        self._responder_recipe_id = None
        self._display_name = None
        self._description = None
        self._owner = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TargetResponderRecipeSummary.
        Unique identifier that is immutable on creation


        :return: The id of this TargetResponderRecipeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TargetResponderRecipeSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this TargetResponderRecipeSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TargetResponderRecipeSummary.
        Compartment Identifier


        :return: The compartment_id of this TargetResponderRecipeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TargetResponderRecipeSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this TargetResponderRecipeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def responder_recipe_id(self):
        """
        **[Required]** Gets the responder_recipe_id of this TargetResponderRecipeSummary.
        Unique identifier for Responder Recipe of which this is an extension


        :return: The responder_recipe_id of this TargetResponderRecipeSummary.
        :rtype: str
        """
        return self._responder_recipe_id

    @responder_recipe_id.setter
    def responder_recipe_id(self, responder_recipe_id):
        """
        Sets the responder_recipe_id of this TargetResponderRecipeSummary.
        Unique identifier for Responder Recipe of which this is an extension


        :param responder_recipe_id: The responder_recipe_id of this TargetResponderRecipeSummary.
        :type: str
        """
        self._responder_recipe_id = responder_recipe_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TargetResponderRecipeSummary.
        ResponderRecipe Identifier Name


        :return: The display_name of this TargetResponderRecipeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TargetResponderRecipeSummary.
        ResponderRecipe Identifier Name


        :param display_name: The display_name of this TargetResponderRecipeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this TargetResponderRecipeSummary.
        ResponderRecipe Description


        :return: The description of this TargetResponderRecipeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TargetResponderRecipeSummary.
        ResponderRecipe Description


        :param description: The description of this TargetResponderRecipeSummary.
        :type: str
        """
        self._description = description

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this TargetResponderRecipeSummary.
        Owner of ResponderRecipe

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The owner of this TargetResponderRecipeSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this TargetResponderRecipeSummary.
        Owner of ResponderRecipe


        :param owner: The owner of this TargetResponderRecipeSummary.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(owner, allowed_values):
            owner = 'UNKNOWN_ENUM_VALUE'
        self._owner = owner

    @property
    def time_created(self):
        """
        Gets the time_created of this TargetResponderRecipeSummary.
        The date and time the target responder recipe was created. Format defined by RFC3339.


        :return: The time_created of this TargetResponderRecipeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TargetResponderRecipeSummary.
        The date and time the target responder recipe was created. Format defined by RFC3339.


        :param time_created: The time_created of this TargetResponderRecipeSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TargetResponderRecipeSummary.
        The date and time the target responder recipe was updated. Format defined by RFC3339.


        :return: The time_updated of this TargetResponderRecipeSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TargetResponderRecipeSummary.
        The date and time the target responder recipe was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this TargetResponderRecipeSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TargetResponderRecipeSummary.
        The current state of the Example.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TargetResponderRecipeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TargetResponderRecipeSummary.
        The current state of the Example.


        :param lifecycle_state: The lifecycle_state of this TargetResponderRecipeSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TargetResponderRecipeSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TargetResponderRecipeSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TargetResponderRecipeSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TargetResponderRecipeSummary.
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
