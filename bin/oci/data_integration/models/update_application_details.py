# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateApplicationDetails(object):
    """
    Properties used in application create operations.
    """

    #: A constant which can be used with the lifecycle_state property of a UpdateApplicationDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a UpdateApplicationDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a UpdateApplicationDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a UpdateApplicationDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a UpdateApplicationDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a UpdateApplicationDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateApplicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this UpdateApplicationDetails.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this UpdateApplicationDetails.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this UpdateApplicationDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this UpdateApplicationDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateApplicationDetails.
        :type description: str

        :param application_version:
            The value to assign to the application_version property of this UpdateApplicationDetails.
        :type application_version: int

        :param object_status:
            The value to assign to the object_status property of this UpdateApplicationDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this UpdateApplicationDetails.
        :type identifier: str

        :param parent_ref:
            The value to assign to the parent_ref property of this UpdateApplicationDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param object_version:
            The value to assign to the object_version property of this UpdateApplicationDetails.
        :type object_version: int

        :param metadata:
            The value to assign to the metadata property of this UpdateApplicationDetails.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param display_name:
            The value to assign to the display_name property of this UpdateApplicationDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateApplicationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateApplicationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UpdateApplicationDetails.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'application_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'parent_ref': 'ParentReference',
            'object_version': 'int',
            'metadata': 'ObjectMetadata',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'application_version': 'applicationVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parent_ref': 'parentRef',
            'object_version': 'objectVersion',
            'metadata': 'metadata',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_state': 'lifecycleState'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._name = None
        self._description = None
        self._application_version = None
        self._object_status = None
        self._identifier = None
        self._parent_ref = None
        self._object_version = None
        self._metadata = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_state = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this UpdateApplicationDetails.
        Generated key that can be used in API calls to identify application.


        :return: The key of this UpdateApplicationDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this UpdateApplicationDetails.
        Generated key that can be used in API calls to identify application.


        :param key: The key of this UpdateApplicationDetails.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this UpdateApplicationDetails.
        The object type.


        :return: The model_type of this UpdateApplicationDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this UpdateApplicationDetails.
        The object type.


        :param model_type: The model_type of this UpdateApplicationDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this UpdateApplicationDetails.
        The object's model version.


        :return: The model_version of this UpdateApplicationDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this UpdateApplicationDetails.
        The object's model version.


        :param model_version: The model_version of this UpdateApplicationDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this UpdateApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this UpdateApplicationDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this UpdateApplicationDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateApplicationDetails.
        Detailed description for the object.


        :return: The description of this UpdateApplicationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateApplicationDetails.
        Detailed description for the object.


        :param description: The description of this UpdateApplicationDetails.
        :type: str
        """
        self._description = description

    @property
    def application_version(self):
        """
        Gets the application_version of this UpdateApplicationDetails.
        version


        :return: The application_version of this UpdateApplicationDetails.
        :rtype: int
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """
        Sets the application_version of this UpdateApplicationDetails.
        version


        :param application_version: The application_version of this UpdateApplicationDetails.
        :type: int
        """
        self._application_version = application_version

    @property
    def object_status(self):
        """
        Gets the object_status of this UpdateApplicationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this UpdateApplicationDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this UpdateApplicationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this UpdateApplicationDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this UpdateApplicationDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this UpdateApplicationDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this UpdateApplicationDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this UpdateApplicationDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this UpdateApplicationDetails.

        :return: The parent_ref of this UpdateApplicationDetails.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this UpdateApplicationDetails.

        :param parent_ref: The parent_ref of this UpdateApplicationDetails.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def object_version(self):
        """
        **[Required]** Gets the object_version of this UpdateApplicationDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this UpdateApplicationDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this UpdateApplicationDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this UpdateApplicationDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def metadata(self):
        """
        Gets the metadata of this UpdateApplicationDetails.

        :return: The metadata of this UpdateApplicationDetails.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UpdateApplicationDetails.

        :param metadata: The metadata of this UpdateApplicationDetails.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The display_name of this UpdateApplicationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param display_name: The display_name of this UpdateApplicationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateApplicationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateApplicationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateApplicationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateApplicationDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateApplicationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateApplicationDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateApplicationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this UpdateApplicationDetails.
        The current state of the workspace.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this UpdateApplicationDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UpdateApplicationDetails.
        The current state of the workspace.


        :param lifecycle_state: The lifecycle_state of this UpdateApplicationDetails.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other