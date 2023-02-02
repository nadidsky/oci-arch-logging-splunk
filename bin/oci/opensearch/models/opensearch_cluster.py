# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpensearchCluster(object):
    """
    An OpenSearch cluster resource. An OpenSearch cluster is set of instances that provide OpenSearch functionality in OCI Search Service with OpenSearch.
    For more information, see `About Search Service with OpenSearch`__.

    __ https://docs.cloud.oracle.com/iaas/Content/search-opensearch/Concepts/ociopensearch.htm
    """

    #: A constant which can be used with the lifecycle_state property of a OpensearchCluster.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OpensearchCluster.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OpensearchCluster.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OpensearchCluster.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OpensearchCluster.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OpensearchCluster.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the master_node_host_type property of a OpensearchCluster.
    #: This constant has a value of "FLEX"
    MASTER_NODE_HOST_TYPE_FLEX = "FLEX"

    #: A constant which can be used with the master_node_host_type property of a OpensearchCluster.
    #: This constant has a value of "BM"
    MASTER_NODE_HOST_TYPE_BM = "BM"

    #: A constant which can be used with the data_node_host_type property of a OpensearchCluster.
    #: This constant has a value of "FLEX"
    DATA_NODE_HOST_TYPE_FLEX = "FLEX"

    #: A constant which can be used with the data_node_host_type property of a OpensearchCluster.
    #: This constant has a value of "BM"
    DATA_NODE_HOST_TYPE_BM = "BM"

    def __init__(self, **kwargs):
        """
        Initializes a new OpensearchCluster object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OpensearchCluster.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OpensearchCluster.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OpensearchCluster.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OpensearchCluster.
            Allowed values for this property are: "ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this OpensearchCluster.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OpensearchCluster.
        :type time_updated: datetime

        :param time_deleted:
            The value to assign to the time_deleted property of this OpensearchCluster.
        :type time_deleted: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OpensearchCluster.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OpensearchCluster.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OpensearchCluster.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OpensearchCluster.
        :type system_tags: dict(str, dict(str, object))

        :param software_version:
            The value to assign to the software_version property of this OpensearchCluster.
        :type software_version: str

        :param total_storage_gb:
            The value to assign to the total_storage_gb property of this OpensearchCluster.
        :type total_storage_gb: int

        :param opensearch_fqdn:
            The value to assign to the opensearch_fqdn property of this OpensearchCluster.
        :type opensearch_fqdn: str

        :param opensearch_private_ip:
            The value to assign to the opensearch_private_ip property of this OpensearchCluster.
        :type opensearch_private_ip: str

        :param opendashboard_fqdn:
            The value to assign to the opendashboard_fqdn property of this OpensearchCluster.
        :type opendashboard_fqdn: str

        :param opendashboard_private_ip:
            The value to assign to the opendashboard_private_ip property of this OpensearchCluster.
        :type opendashboard_private_ip: str

        :param master_node_count:
            The value to assign to the master_node_count property of this OpensearchCluster.
        :type master_node_count: int

        :param master_node_host_type:
            The value to assign to the master_node_host_type property of this OpensearchCluster.
            Allowed values for this property are: "FLEX", "BM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type master_node_host_type: str

        :param master_node_host_bare_metal_shape:
            The value to assign to the master_node_host_bare_metal_shape property of this OpensearchCluster.
        :type master_node_host_bare_metal_shape: str

        :param master_node_host_ocpu_count:
            The value to assign to the master_node_host_ocpu_count property of this OpensearchCluster.
        :type master_node_host_ocpu_count: int

        :param master_node_host_memory_gb:
            The value to assign to the master_node_host_memory_gb property of this OpensearchCluster.
        :type master_node_host_memory_gb: int

        :param data_node_count:
            The value to assign to the data_node_count property of this OpensearchCluster.
        :type data_node_count: int

        :param data_node_host_type:
            The value to assign to the data_node_host_type property of this OpensearchCluster.
            Allowed values for this property are: "FLEX", "BM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_node_host_type: str

        :param data_node_host_bare_metal_shape:
            The value to assign to the data_node_host_bare_metal_shape property of this OpensearchCluster.
        :type data_node_host_bare_metal_shape: str

        :param data_node_host_ocpu_count:
            The value to assign to the data_node_host_ocpu_count property of this OpensearchCluster.
        :type data_node_host_ocpu_count: int

        :param data_node_host_memory_gb:
            The value to assign to the data_node_host_memory_gb property of this OpensearchCluster.
        :type data_node_host_memory_gb: int

        :param data_node_storage_gb:
            The value to assign to the data_node_storage_gb property of this OpensearchCluster.
        :type data_node_storage_gb: int

        :param opendashboard_node_count:
            The value to assign to the opendashboard_node_count property of this OpensearchCluster.
        :type opendashboard_node_count: int

        :param opendashboard_node_host_ocpu_count:
            The value to assign to the opendashboard_node_host_ocpu_count property of this OpensearchCluster.
        :type opendashboard_node_host_ocpu_count: int

        :param opendashboard_node_host_memory_gb:
            The value to assign to the opendashboard_node_host_memory_gb property of this OpensearchCluster.
        :type opendashboard_node_host_memory_gb: int

        :param vcn_id:
            The value to assign to the vcn_id property of this OpensearchCluster.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this OpensearchCluster.
        :type subnet_id: str

        :param vcn_compartment_id:
            The value to assign to the vcn_compartment_id property of this OpensearchCluster.
        :type vcn_compartment_id: str

        :param subnet_compartment_id:
            The value to assign to the subnet_compartment_id property of this OpensearchCluster.
        :type subnet_compartment_id: str

        :param fqdn:
            The value to assign to the fqdn property of this OpensearchCluster.
        :type fqdn: str

        :param availability_domains:
            The value to assign to the availability_domains property of this OpensearchCluster.
        :type availability_domains: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_deleted': 'datetime',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'software_version': 'str',
            'total_storage_gb': 'int',
            'opensearch_fqdn': 'str',
            'opensearch_private_ip': 'str',
            'opendashboard_fqdn': 'str',
            'opendashboard_private_ip': 'str',
            'master_node_count': 'int',
            'master_node_host_type': 'str',
            'master_node_host_bare_metal_shape': 'str',
            'master_node_host_ocpu_count': 'int',
            'master_node_host_memory_gb': 'int',
            'data_node_count': 'int',
            'data_node_host_type': 'str',
            'data_node_host_bare_metal_shape': 'str',
            'data_node_host_ocpu_count': 'int',
            'data_node_host_memory_gb': 'int',
            'data_node_storage_gb': 'int',
            'opendashboard_node_count': 'int',
            'opendashboard_node_host_ocpu_count': 'int',
            'opendashboard_node_host_memory_gb': 'int',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'vcn_compartment_id': 'str',
            'subnet_compartment_id': 'str',
            'fqdn': 'str',
            'availability_domains': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_deleted': 'timeDeleted',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'software_version': 'softwareVersion',
            'total_storage_gb': 'totalStorageGB',
            'opensearch_fqdn': 'opensearchFqdn',
            'opensearch_private_ip': 'opensearchPrivateIp',
            'opendashboard_fqdn': 'opendashboardFqdn',
            'opendashboard_private_ip': 'opendashboardPrivateIp',
            'master_node_count': 'masterNodeCount',
            'master_node_host_type': 'masterNodeHostType',
            'master_node_host_bare_metal_shape': 'masterNodeHostBareMetalShape',
            'master_node_host_ocpu_count': 'masterNodeHostOcpuCount',
            'master_node_host_memory_gb': 'masterNodeHostMemoryGB',
            'data_node_count': 'dataNodeCount',
            'data_node_host_type': 'dataNodeHostType',
            'data_node_host_bare_metal_shape': 'dataNodeHostBareMetalShape',
            'data_node_host_ocpu_count': 'dataNodeHostOcpuCount',
            'data_node_host_memory_gb': 'dataNodeHostMemoryGB',
            'data_node_storage_gb': 'dataNodeStorageGB',
            'opendashboard_node_count': 'opendashboardNodeCount',
            'opendashboard_node_host_ocpu_count': 'opendashboardNodeHostOcpuCount',
            'opendashboard_node_host_memory_gb': 'opendashboardNodeHostMemoryGB',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'vcn_compartment_id': 'vcnCompartmentId',
            'subnet_compartment_id': 'subnetCompartmentId',
            'fqdn': 'fqdn',
            'availability_domains': 'availabilityDomains'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._time_deleted = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._software_version = None
        self._total_storage_gb = None
        self._opensearch_fqdn = None
        self._opensearch_private_ip = None
        self._opendashboard_fqdn = None
        self._opendashboard_private_ip = None
        self._master_node_count = None
        self._master_node_host_type = None
        self._master_node_host_bare_metal_shape = None
        self._master_node_host_ocpu_count = None
        self._master_node_host_memory_gb = None
        self._data_node_count = None
        self._data_node_host_type = None
        self._data_node_host_bare_metal_shape = None
        self._data_node_host_ocpu_count = None
        self._data_node_host_memory_gb = None
        self._data_node_storage_gb = None
        self._opendashboard_node_count = None
        self._opendashboard_node_host_ocpu_count = None
        self._opendashboard_node_host_memory_gb = None
        self._vcn_id = None
        self._subnet_id = None
        self._vcn_compartment_id = None
        self._subnet_compartment_id = None
        self._fqdn = None
        self._availability_domains = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OpensearchCluster.
        The OCID of the cluster.


        :return: The id of this OpensearchCluster.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OpensearchCluster.
        The OCID of the cluster.


        :param id: The id of this OpensearchCluster.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OpensearchCluster.
        The name of the cluster. Avoid entering confidential information.


        :return: The display_name of this OpensearchCluster.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OpensearchCluster.
        The name of the cluster. Avoid entering confidential information.


        :param display_name: The display_name of this OpensearchCluster.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OpensearchCluster.
        The OCID of the compartment where the cluster is located.


        :return: The compartment_id of this OpensearchCluster.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OpensearchCluster.
        The OCID of the compartment where the cluster is located.


        :param compartment_id: The compartment_id of this OpensearchCluster.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OpensearchCluster.
        The current state of the cluster.

        Allowed values for this property are: "ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OpensearchCluster.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OpensearchCluster.
        The current state of the cluster.


        :param lifecycle_state: The lifecycle_state of this OpensearchCluster.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OpensearchCluster.
        The amount of time in milliseconds since the cluster was created.


        :return: The time_created of this OpensearchCluster.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OpensearchCluster.
        The amount of time in milliseconds since the cluster was created.


        :param time_created: The time_created of this OpensearchCluster.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OpensearchCluster.
        The amount of time in milliseconds since the cluster was updated.


        :return: The time_updated of this OpensearchCluster.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OpensearchCluster.
        The amount of time in milliseconds since the cluster was updated.


        :param time_updated: The time_updated of this OpensearchCluster.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_deleted(self):
        """
        Gets the time_deleted of this OpensearchCluster.
        The amount of time in milliseconds since the cluster was updated.


        :return: The time_deleted of this OpensearchCluster.
        :rtype: datetime
        """
        return self._time_deleted

    @time_deleted.setter
    def time_deleted(self, time_deleted):
        """
        Sets the time_deleted of this OpensearchCluster.
        The amount of time in milliseconds since the cluster was updated.


        :param time_deleted: The time_deleted of this OpensearchCluster.
        :type: datetime
        """
        self._time_deleted = time_deleted

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OpensearchCluster.
        Additional information about the current lifecycle state of the cluster.


        :return: The lifecycle_details of this OpensearchCluster.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OpensearchCluster.
        Additional information about the current lifecycle state of the cluster.


        :param lifecycle_details: The lifecycle_details of this OpensearchCluster.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OpensearchCluster.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OpensearchCluster.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OpensearchCluster.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OpensearchCluster.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OpensearchCluster.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OpensearchCluster.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OpensearchCluster.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OpensearchCluster.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OpensearchCluster.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OpensearchCluster.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OpensearchCluster.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OpensearchCluster.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def software_version(self):
        """
        **[Required]** Gets the software_version of this OpensearchCluster.
        The software version the cluster is running.


        :return: The software_version of this OpensearchCluster.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """
        Sets the software_version of this OpensearchCluster.
        The software version the cluster is running.


        :param software_version: The software_version of this OpensearchCluster.
        :type: str
        """
        self._software_version = software_version

    @property
    def total_storage_gb(self):
        """
        **[Required]** Gets the total_storage_gb of this OpensearchCluster.
        The size in GB of the cluster's total storage.


        :return: The total_storage_gb of this OpensearchCluster.
        :rtype: int
        """
        return self._total_storage_gb

    @total_storage_gb.setter
    def total_storage_gb(self, total_storage_gb):
        """
        Sets the total_storage_gb of this OpensearchCluster.
        The size in GB of the cluster's total storage.


        :param total_storage_gb: The total_storage_gb of this OpensearchCluster.
        :type: int
        """
        self._total_storage_gb = total_storage_gb

    @property
    def opensearch_fqdn(self):
        """
        **[Required]** Gets the opensearch_fqdn of this OpensearchCluster.
        The fully qualified domain name (FQDN) for the cluster's API endpoint.


        :return: The opensearch_fqdn of this OpensearchCluster.
        :rtype: str
        """
        return self._opensearch_fqdn

    @opensearch_fqdn.setter
    def opensearch_fqdn(self, opensearch_fqdn):
        """
        Sets the opensearch_fqdn of this OpensearchCluster.
        The fully qualified domain name (FQDN) for the cluster's API endpoint.


        :param opensearch_fqdn: The opensearch_fqdn of this OpensearchCluster.
        :type: str
        """
        self._opensearch_fqdn = opensearch_fqdn

    @property
    def opensearch_private_ip(self):
        """
        **[Required]** Gets the opensearch_private_ip of this OpensearchCluster.
        The cluster's private IP address.


        :return: The opensearch_private_ip of this OpensearchCluster.
        :rtype: str
        """
        return self._opensearch_private_ip

    @opensearch_private_ip.setter
    def opensearch_private_ip(self, opensearch_private_ip):
        """
        Sets the opensearch_private_ip of this OpensearchCluster.
        The cluster's private IP address.


        :param opensearch_private_ip: The opensearch_private_ip of this OpensearchCluster.
        :type: str
        """
        self._opensearch_private_ip = opensearch_private_ip

    @property
    def opendashboard_fqdn(self):
        """
        **[Required]** Gets the opendashboard_fqdn of this OpensearchCluster.
        The fully qualified domain name (FQDN) for the cluster's OpenSearch Dashboard API endpoint.


        :return: The opendashboard_fqdn of this OpensearchCluster.
        :rtype: str
        """
        return self._opendashboard_fqdn

    @opendashboard_fqdn.setter
    def opendashboard_fqdn(self, opendashboard_fqdn):
        """
        Sets the opendashboard_fqdn of this OpensearchCluster.
        The fully qualified domain name (FQDN) for the cluster's OpenSearch Dashboard API endpoint.


        :param opendashboard_fqdn: The opendashboard_fqdn of this OpensearchCluster.
        :type: str
        """
        self._opendashboard_fqdn = opendashboard_fqdn

    @property
    def opendashboard_private_ip(self):
        """
        **[Required]** Gets the opendashboard_private_ip of this OpensearchCluster.
        The private IP address for the cluster's OpenSearch Dashboard.


        :return: The opendashboard_private_ip of this OpensearchCluster.
        :rtype: str
        """
        return self._opendashboard_private_ip

    @opendashboard_private_ip.setter
    def opendashboard_private_ip(self, opendashboard_private_ip):
        """
        Sets the opendashboard_private_ip of this OpensearchCluster.
        The private IP address for the cluster's OpenSearch Dashboard.


        :param opendashboard_private_ip: The opendashboard_private_ip of this OpensearchCluster.
        :type: str
        """
        self._opendashboard_private_ip = opendashboard_private_ip

    @property
    def master_node_count(self):
        """
        **[Required]** Gets the master_node_count of this OpensearchCluster.
        The number of master nodes configured for the cluster.


        :return: The master_node_count of this OpensearchCluster.
        :rtype: int
        """
        return self._master_node_count

    @master_node_count.setter
    def master_node_count(self, master_node_count):
        """
        Sets the master_node_count of this OpensearchCluster.
        The number of master nodes configured for the cluster.


        :param master_node_count: The master_node_count of this OpensearchCluster.
        :type: int
        """
        self._master_node_count = master_node_count

    @property
    def master_node_host_type(self):
        """
        **[Required]** Gets the master_node_host_type of this OpensearchCluster.
        The instance type for the cluster's master nodes.

        Allowed values for this property are: "FLEX", "BM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The master_node_host_type of this OpensearchCluster.
        :rtype: str
        """
        return self._master_node_host_type

    @master_node_host_type.setter
    def master_node_host_type(self, master_node_host_type):
        """
        Sets the master_node_host_type of this OpensearchCluster.
        The instance type for the cluster's master nodes.


        :param master_node_host_type: The master_node_host_type of this OpensearchCluster.
        :type: str
        """
        allowed_values = ["FLEX", "BM"]
        if not value_allowed_none_or_none_sentinel(master_node_host_type, allowed_values):
            master_node_host_type = 'UNKNOWN_ENUM_VALUE'
        self._master_node_host_type = master_node_host_type

    @property
    def master_node_host_bare_metal_shape(self):
        """
        Gets the master_node_host_bare_metal_shape of this OpensearchCluster.
        The bare metal shape for the cluster's master nodes.


        :return: The master_node_host_bare_metal_shape of this OpensearchCluster.
        :rtype: str
        """
        return self._master_node_host_bare_metal_shape

    @master_node_host_bare_metal_shape.setter
    def master_node_host_bare_metal_shape(self, master_node_host_bare_metal_shape):
        """
        Sets the master_node_host_bare_metal_shape of this OpensearchCluster.
        The bare metal shape for the cluster's master nodes.


        :param master_node_host_bare_metal_shape: The master_node_host_bare_metal_shape of this OpensearchCluster.
        :type: str
        """
        self._master_node_host_bare_metal_shape = master_node_host_bare_metal_shape

    @property
    def master_node_host_ocpu_count(self):
        """
        **[Required]** Gets the master_node_host_ocpu_count of this OpensearchCluster.
        The number of OCPUs configured for cluster's master nodes.


        :return: The master_node_host_ocpu_count of this OpensearchCluster.
        :rtype: int
        """
        return self._master_node_host_ocpu_count

    @master_node_host_ocpu_count.setter
    def master_node_host_ocpu_count(self, master_node_host_ocpu_count):
        """
        Sets the master_node_host_ocpu_count of this OpensearchCluster.
        The number of OCPUs configured for cluster's master nodes.


        :param master_node_host_ocpu_count: The master_node_host_ocpu_count of this OpensearchCluster.
        :type: int
        """
        self._master_node_host_ocpu_count = master_node_host_ocpu_count

    @property
    def master_node_host_memory_gb(self):
        """
        **[Required]** Gets the master_node_host_memory_gb of this OpensearchCluster.
        The amount of memory in GB, for the cluster's master nodes.


        :return: The master_node_host_memory_gb of this OpensearchCluster.
        :rtype: int
        """
        return self._master_node_host_memory_gb

    @master_node_host_memory_gb.setter
    def master_node_host_memory_gb(self, master_node_host_memory_gb):
        """
        Sets the master_node_host_memory_gb of this OpensearchCluster.
        The amount of memory in GB, for the cluster's master nodes.


        :param master_node_host_memory_gb: The master_node_host_memory_gb of this OpensearchCluster.
        :type: int
        """
        self._master_node_host_memory_gb = master_node_host_memory_gb

    @property
    def data_node_count(self):
        """
        **[Required]** Gets the data_node_count of this OpensearchCluster.
        The number of data nodes configured for the cluster.


        :return: The data_node_count of this OpensearchCluster.
        :rtype: int
        """
        return self._data_node_count

    @data_node_count.setter
    def data_node_count(self, data_node_count):
        """
        Sets the data_node_count of this OpensearchCluster.
        The number of data nodes configured for the cluster.


        :param data_node_count: The data_node_count of this OpensearchCluster.
        :type: int
        """
        self._data_node_count = data_node_count

    @property
    def data_node_host_type(self):
        """
        **[Required]** Gets the data_node_host_type of this OpensearchCluster.
        The instance type for the cluster's data nodes.

        Allowed values for this property are: "FLEX", "BM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_node_host_type of this OpensearchCluster.
        :rtype: str
        """
        return self._data_node_host_type

    @data_node_host_type.setter
    def data_node_host_type(self, data_node_host_type):
        """
        Sets the data_node_host_type of this OpensearchCluster.
        The instance type for the cluster's data nodes.


        :param data_node_host_type: The data_node_host_type of this OpensearchCluster.
        :type: str
        """
        allowed_values = ["FLEX", "BM"]
        if not value_allowed_none_or_none_sentinel(data_node_host_type, allowed_values):
            data_node_host_type = 'UNKNOWN_ENUM_VALUE'
        self._data_node_host_type = data_node_host_type

    @property
    def data_node_host_bare_metal_shape(self):
        """
        Gets the data_node_host_bare_metal_shape of this OpensearchCluster.
        The bare metal shape for the cluster's data nodes.


        :return: The data_node_host_bare_metal_shape of this OpensearchCluster.
        :rtype: str
        """
        return self._data_node_host_bare_metal_shape

    @data_node_host_bare_metal_shape.setter
    def data_node_host_bare_metal_shape(self, data_node_host_bare_metal_shape):
        """
        Sets the data_node_host_bare_metal_shape of this OpensearchCluster.
        The bare metal shape for the cluster's data nodes.


        :param data_node_host_bare_metal_shape: The data_node_host_bare_metal_shape of this OpensearchCluster.
        :type: str
        """
        self._data_node_host_bare_metal_shape = data_node_host_bare_metal_shape

    @property
    def data_node_host_ocpu_count(self):
        """
        **[Required]** Gets the data_node_host_ocpu_count of this OpensearchCluster.
        The number of OCPUs configured for the cluster's data nodes.


        :return: The data_node_host_ocpu_count of this OpensearchCluster.
        :rtype: int
        """
        return self._data_node_host_ocpu_count

    @data_node_host_ocpu_count.setter
    def data_node_host_ocpu_count(self, data_node_host_ocpu_count):
        """
        Sets the data_node_host_ocpu_count of this OpensearchCluster.
        The number of OCPUs configured for the cluster's data nodes.


        :param data_node_host_ocpu_count: The data_node_host_ocpu_count of this OpensearchCluster.
        :type: int
        """
        self._data_node_host_ocpu_count = data_node_host_ocpu_count

    @property
    def data_node_host_memory_gb(self):
        """
        **[Required]** Gets the data_node_host_memory_gb of this OpensearchCluster.
        The amount of memory in GB, for the cluster's data nodes.


        :return: The data_node_host_memory_gb of this OpensearchCluster.
        :rtype: int
        """
        return self._data_node_host_memory_gb

    @data_node_host_memory_gb.setter
    def data_node_host_memory_gb(self, data_node_host_memory_gb):
        """
        Sets the data_node_host_memory_gb of this OpensearchCluster.
        The amount of memory in GB, for the cluster's data nodes.


        :param data_node_host_memory_gb: The data_node_host_memory_gb of this OpensearchCluster.
        :type: int
        """
        self._data_node_host_memory_gb = data_node_host_memory_gb

    @property
    def data_node_storage_gb(self):
        """
        **[Required]** Gets the data_node_storage_gb of this OpensearchCluster.
        The amount of storage in GB, to configure per node for the cluster's data nodes.


        :return: The data_node_storage_gb of this OpensearchCluster.
        :rtype: int
        """
        return self._data_node_storage_gb

    @data_node_storage_gb.setter
    def data_node_storage_gb(self, data_node_storage_gb):
        """
        Sets the data_node_storage_gb of this OpensearchCluster.
        The amount of storage in GB, to configure per node for the cluster's data nodes.


        :param data_node_storage_gb: The data_node_storage_gb of this OpensearchCluster.
        :type: int
        """
        self._data_node_storage_gb = data_node_storage_gb

    @property
    def opendashboard_node_count(self):
        """
        **[Required]** Gets the opendashboard_node_count of this OpensearchCluster.
        The number of OpenSearch Dashboard nodes configured for the cluster.


        :return: The opendashboard_node_count of this OpensearchCluster.
        :rtype: int
        """
        return self._opendashboard_node_count

    @opendashboard_node_count.setter
    def opendashboard_node_count(self, opendashboard_node_count):
        """
        Sets the opendashboard_node_count of this OpensearchCluster.
        The number of OpenSearch Dashboard nodes configured for the cluster.


        :param opendashboard_node_count: The opendashboard_node_count of this OpensearchCluster.
        :type: int
        """
        self._opendashboard_node_count = opendashboard_node_count

    @property
    def opendashboard_node_host_ocpu_count(self):
        """
        **[Required]** Gets the opendashboard_node_host_ocpu_count of this OpensearchCluster.
        The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.


        :return: The opendashboard_node_host_ocpu_count of this OpensearchCluster.
        :rtype: int
        """
        return self._opendashboard_node_host_ocpu_count

    @opendashboard_node_host_ocpu_count.setter
    def opendashboard_node_host_ocpu_count(self, opendashboard_node_host_ocpu_count):
        """
        Sets the opendashboard_node_host_ocpu_count of this OpensearchCluster.
        The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.


        :param opendashboard_node_host_ocpu_count: The opendashboard_node_host_ocpu_count of this OpensearchCluster.
        :type: int
        """
        self._opendashboard_node_host_ocpu_count = opendashboard_node_host_ocpu_count

    @property
    def opendashboard_node_host_memory_gb(self):
        """
        **[Required]** Gets the opendashboard_node_host_memory_gb of this OpensearchCluster.
        The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.


        :return: The opendashboard_node_host_memory_gb of this OpensearchCluster.
        :rtype: int
        """
        return self._opendashboard_node_host_memory_gb

    @opendashboard_node_host_memory_gb.setter
    def opendashboard_node_host_memory_gb(self, opendashboard_node_host_memory_gb):
        """
        Sets the opendashboard_node_host_memory_gb of this OpensearchCluster.
        The amount of memory in GB, for the cluster's OpenSearch Dashboard nodes.


        :param opendashboard_node_host_memory_gb: The opendashboard_node_host_memory_gb of this OpensearchCluster.
        :type: int
        """
        self._opendashboard_node_host_memory_gb = opendashboard_node_host_memory_gb

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this OpensearchCluster.
        The OCID of the cluster's VCN.


        :return: The vcn_id of this OpensearchCluster.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this OpensearchCluster.
        The OCID of the cluster's VCN.


        :param vcn_id: The vcn_id of this OpensearchCluster.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this OpensearchCluster.
        The OCID of the cluster's subnet.


        :return: The subnet_id of this OpensearchCluster.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this OpensearchCluster.
        The OCID of the cluster's subnet.


        :param subnet_id: The subnet_id of this OpensearchCluster.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def vcn_compartment_id(self):
        """
        **[Required]** Gets the vcn_compartment_id of this OpensearchCluster.
        The OCID for the compartment where the cluster's VCN is located.


        :return: The vcn_compartment_id of this OpensearchCluster.
        :rtype: str
        """
        return self._vcn_compartment_id

    @vcn_compartment_id.setter
    def vcn_compartment_id(self, vcn_compartment_id):
        """
        Sets the vcn_compartment_id of this OpensearchCluster.
        The OCID for the compartment where the cluster's VCN is located.


        :param vcn_compartment_id: The vcn_compartment_id of this OpensearchCluster.
        :type: str
        """
        self._vcn_compartment_id = vcn_compartment_id

    @property
    def subnet_compartment_id(self):
        """
        **[Required]** Gets the subnet_compartment_id of this OpensearchCluster.
        The OCID for the compartment where the cluster's subnet is located.


        :return: The subnet_compartment_id of this OpensearchCluster.
        :rtype: str
        """
        return self._subnet_compartment_id

    @subnet_compartment_id.setter
    def subnet_compartment_id(self, subnet_compartment_id):
        """
        Sets the subnet_compartment_id of this OpensearchCluster.
        The OCID for the compartment where the cluster's subnet is located.


        :param subnet_compartment_id: The subnet_compartment_id of this OpensearchCluster.
        :type: str
        """
        self._subnet_compartment_id = subnet_compartment_id

    @property
    def fqdn(self):
        """
        Gets the fqdn of this OpensearchCluster.
        The fully qualified domain name (FQDN) for the cluster's API endpoint.


        :return: The fqdn of this OpensearchCluster.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this OpensearchCluster.
        The fully qualified domain name (FQDN) for the cluster's API endpoint.


        :param fqdn: The fqdn of this OpensearchCluster.
        :type: str
        """
        self._fqdn = fqdn

    @property
    def availability_domains(self):
        """
        **[Required]** Gets the availability_domains of this OpensearchCluster.
        The availability domains to distribute the cluser nodes across.


        :return: The availability_domains of this OpensearchCluster.
        :rtype: list[str]
        """
        return self._availability_domains

    @availability_domains.setter
    def availability_domains(self, availability_domains):
        """
        Sets the availability_domains of this OpensearchCluster.
        The availability domains to distribute the cluser nodes across.


        :param availability_domains: The availability_domains of this OpensearchCluster.
        :type: list[str]
        """
        self._availability_domains = availability_domains

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
