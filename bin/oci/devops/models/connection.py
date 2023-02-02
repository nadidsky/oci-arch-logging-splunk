# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Connection(object):
    """
    The properties that define a connection to external repositories.
    """

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "GITHUB_ACCESS_TOKEN"
    CONNECTION_TYPE_GITHUB_ACCESS_TOKEN = "GITHUB_ACCESS_TOKEN"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "GITLAB_ACCESS_TOKEN"
    CONNECTION_TYPE_GITLAB_ACCESS_TOKEN = "GITLAB_ACCESS_TOKEN"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "GITLAB_SERVER_ACCESS_TOKEN"
    CONNECTION_TYPE_GITLAB_SERVER_ACCESS_TOKEN = "GITLAB_SERVER_ACCESS_TOKEN"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "BITBUCKET_SERVER_ACCESS_TOKEN"
    CONNECTION_TYPE_BITBUCKET_SERVER_ACCESS_TOKEN = "BITBUCKET_SERVER_ACCESS_TOKEN"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "BITBUCKET_CLOUD_APP_PASSWORD"
    CONNECTION_TYPE_BITBUCKET_CLOUD_APP_PASSWORD = "BITBUCKET_CLOUD_APP_PASSWORD"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "VBS_ACCESS_TOKEN"
    CONNECTION_TYPE_VBS_ACCESS_TOKEN = "VBS_ACCESS_TOKEN"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new Connection object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.BitbucketServerAccessTokenConnection`
        * :class:`~oci.devops.models.GitlabAccessTokenConnection`
        * :class:`~oci.devops.models.GithubAccessTokenConnection`
        * :class:`~oci.devops.models.BitbucketCloudAppPasswordConnection`
        * :class:`~oci.devops.models.GitlabServerAccessTokenConnection`
        * :class:`~oci.devops.models.VbsAccessTokenConnection`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Connection.
        :type id: str

        :param description:
            The value to assign to the description property of this Connection.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this Connection.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Connection.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this Connection.
        :type project_id: str

        :param connection_type:
            The value to assign to the connection_type property of this Connection.
            Allowed values for this property are: "GITHUB_ACCESS_TOKEN", "GITLAB_ACCESS_TOKEN", "GITLAB_SERVER_ACCESS_TOKEN", "BITBUCKET_SERVER_ACCESS_TOKEN", "BITBUCKET_CLOUD_APP_PASSWORD", "VBS_ACCESS_TOKEN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param time_created:
            The value to assign to the time_created property of this Connection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Connection.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Connection.
            Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Connection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Connection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Connection.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'project_id': 'str',
            'connection_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'connection_type': 'connectionType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._compartment_id = None
        self._project_id = None
        self._connection_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectionType']

        if type == 'BITBUCKET_SERVER_ACCESS_TOKEN':
            return 'BitbucketServerAccessTokenConnection'

        if type == 'GITLAB_ACCESS_TOKEN':
            return 'GitlabAccessTokenConnection'

        if type == 'GITHUB_ACCESS_TOKEN':
            return 'GithubAccessTokenConnection'

        if type == 'BITBUCKET_CLOUD_APP_PASSWORD':
            return 'BitbucketCloudAppPasswordConnection'

        if type == 'GITLAB_SERVER_ACCESS_TOKEN':
            return 'GitlabServerAccessTokenConnection'

        if type == 'VBS_ACCESS_TOKEN':
            return 'VbsAccessTokenConnection'
        else:
            return 'Connection'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Connection.
        Unique identifier that is immutable on creation.


        :return: The id of this Connection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Connection.
        Unique identifier that is immutable on creation.


        :param id: The id of this Connection.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this Connection.
        Optional description about the connection.


        :return: The description of this Connection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Connection.
        Optional description about the connection.


        :param description: The description of this Connection.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this Connection.
        Connection display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this Connection.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Connection.
        Connection display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this Connection.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Connection.
        The OCID of the compartment containing the connection.


        :return: The compartment_id of this Connection.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Connection.
        The OCID of the compartment containing the connection.


        :param compartment_id: The compartment_id of this Connection.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this Connection.
        The OCID of the DevOps project.


        :return: The project_id of this Connection.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this Connection.
        The OCID of the DevOps project.


        :param project_id: The project_id of this Connection.
        :type: str
        """
        self._project_id = project_id

    @property
    def connection_type(self):
        """
        **[Required]** Gets the connection_type of this Connection.
        The type of connection.

        Allowed values for this property are: "GITHUB_ACCESS_TOKEN", "GITLAB_ACCESS_TOKEN", "GITLAB_SERVER_ACCESS_TOKEN", "BITBUCKET_SERVER_ACCESS_TOKEN", "BITBUCKET_CLOUD_APP_PASSWORD", "VBS_ACCESS_TOKEN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connection_type of this Connection.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this Connection.
        The type of connection.


        :param connection_type: The connection_type of this Connection.
        :type: str
        """
        allowed_values = ["GITHUB_ACCESS_TOKEN", "GITLAB_ACCESS_TOKEN", "GITLAB_SERVER_ACCESS_TOKEN", "BITBUCKET_SERVER_ACCESS_TOKEN", "BITBUCKET_CLOUD_APP_PASSWORD", "VBS_ACCESS_TOKEN"]
        if not value_allowed_none_or_none_sentinel(connection_type, allowed_values):
            connection_type = 'UNKNOWN_ENUM_VALUE'
        self._connection_type = connection_type

    @property
    def time_created(self):
        """
        Gets the time_created of this Connection.
        The time the connection was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this Connection.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Connection.
        The time the connection was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this Connection.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Connection.
        The time the connection was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this Connection.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Connection.
        The time the connection was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this Connection.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Connection.
        The current state of the connection.

        Allowed values for this property are: "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Connection.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Connection.
        The current state of the connection.


        :param lifecycle_state: The lifecycle_state of this Connection.
        :type: str
        """
        allowed_values = ["ACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Connection.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Connection.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Connection.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Connection.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Connection.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Connection.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Connection.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Connection.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Connection.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this Connection.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Connection.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this Connection.
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