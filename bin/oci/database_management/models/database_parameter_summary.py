# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseParameterSummary(object):
    """
    A summary of the database parameter.
    """

    #: A constant which can be used with the type property of a DatabaseParameterSummary.
    #: This constant has a value of "BOOLEAN"
    TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the type property of a DatabaseParameterSummary.
    #: This constant has a value of "STRING"
    TYPE_STRING = "STRING"

    #: A constant which can be used with the type property of a DatabaseParameterSummary.
    #: This constant has a value of "INTEGER"
    TYPE_INTEGER = "INTEGER"

    #: A constant which can be used with the type property of a DatabaseParameterSummary.
    #: This constant has a value of "FILENAME"
    TYPE_FILENAME = "FILENAME"

    #: A constant which can be used with the type property of a DatabaseParameterSummary.
    #: This constant has a value of "BIG_INTEGER"
    TYPE_BIG_INTEGER = "BIG_INTEGER"

    #: A constant which can be used with the type property of a DatabaseParameterSummary.
    #: This constant has a value of "RESERVED"
    TYPE_RESERVED = "RESERVED"

    #: A constant which can be used with the is_system_modifiable property of a DatabaseParameterSummary.
    #: This constant has a value of "IMMEDIATE"
    IS_SYSTEM_MODIFIABLE_IMMEDIATE = "IMMEDIATE"

    #: A constant which can be used with the is_system_modifiable property of a DatabaseParameterSummary.
    #: This constant has a value of "DEFERRED"
    IS_SYSTEM_MODIFIABLE_DEFERRED = "DEFERRED"

    #: A constant which can be used with the is_system_modifiable property of a DatabaseParameterSummary.
    #: This constant has a value of "FALSE"
    IS_SYSTEM_MODIFIABLE_FALSE = "FALSE"

    #: A constant which can be used with the is_modified property of a DatabaseParameterSummary.
    #: This constant has a value of "MODIFIED"
    IS_MODIFIED_MODIFIED = "MODIFIED"

    #: A constant which can be used with the is_modified property of a DatabaseParameterSummary.
    #: This constant has a value of "FALSE"
    IS_MODIFIED_FALSE = "FALSE"

    #: A constant which can be used with the constraint property of a DatabaseParameterSummary.
    #: This constant has a value of "UNIQUE"
    CONSTRAINT_UNIQUE = "UNIQUE"

    #: A constant which can be used with the constraint property of a DatabaseParameterSummary.
    #: This constant has a value of "IDENTICAL"
    CONSTRAINT_IDENTICAL = "IDENTICAL"

    #: A constant which can be used with the constraint property of a DatabaseParameterSummary.
    #: This constant has a value of "NONE"
    CONSTRAINT_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseParameterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DatabaseParameterSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this DatabaseParameterSummary.
            Allowed values for this property are: "BOOLEAN", "STRING", "INTEGER", "FILENAME", "BIG_INTEGER", "RESERVED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param value:
            The value to assign to the value property of this DatabaseParameterSummary.
        :type value: str

        :param display_value:
            The value to assign to the display_value property of this DatabaseParameterSummary.
        :type display_value: str

        :param number:
            The value to assign to the number property of this DatabaseParameterSummary.
        :type number: float

        :param is_default:
            The value to assign to the is_default property of this DatabaseParameterSummary.
        :type is_default: bool

        :param is_session_modifiable:
            The value to assign to the is_session_modifiable property of this DatabaseParameterSummary.
        :type is_session_modifiable: bool

        :param is_system_modifiable:
            The value to assign to the is_system_modifiable property of this DatabaseParameterSummary.
            Allowed values for this property are: "IMMEDIATE", "DEFERRED", "FALSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type is_system_modifiable: str

        :param is_pdb_modifiable:
            The value to assign to the is_pdb_modifiable property of this DatabaseParameterSummary.
        :type is_pdb_modifiable: bool

        :param is_instance_modifiable:
            The value to assign to the is_instance_modifiable property of this DatabaseParameterSummary.
        :type is_instance_modifiable: bool

        :param is_modified:
            The value to assign to the is_modified property of this DatabaseParameterSummary.
            Allowed values for this property are: "MODIFIED", "FALSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type is_modified: str

        :param is_adjusted:
            The value to assign to the is_adjusted property of this DatabaseParameterSummary.
        :type is_adjusted: bool

        :param is_deprecated:
            The value to assign to the is_deprecated property of this DatabaseParameterSummary.
        :type is_deprecated: bool

        :param is_basic:
            The value to assign to the is_basic property of this DatabaseParameterSummary.
        :type is_basic: bool

        :param description:
            The value to assign to the description property of this DatabaseParameterSummary.
        :type description: str

        :param ordinal:
            The value to assign to the ordinal property of this DatabaseParameterSummary.
        :type ordinal: float

        :param update_comment:
            The value to assign to the update_comment property of this DatabaseParameterSummary.
        :type update_comment: str

        :param container_id:
            The value to assign to the container_id property of this DatabaseParameterSummary.
        :type container_id: float

        :param category:
            The value to assign to the category property of this DatabaseParameterSummary.
        :type category: str

        :param constraint:
            The value to assign to the constraint property of this DatabaseParameterSummary.
            Allowed values for this property are: "UNIQUE", "IDENTICAL", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type constraint: str

        :param sid:
            The value to assign to the sid property of this DatabaseParameterSummary.
        :type sid: str

        :param is_specified:
            The value to assign to the is_specified property of this DatabaseParameterSummary.
        :type is_specified: bool

        :param allowed_values:
            The value to assign to the allowed_values property of this DatabaseParameterSummary.
        :type allowed_values: list[oci.database_management.models.AllowedParameterValue]

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'value': 'str',
            'display_value': 'str',
            'number': 'float',
            'is_default': 'bool',
            'is_session_modifiable': 'bool',
            'is_system_modifiable': 'str',
            'is_pdb_modifiable': 'bool',
            'is_instance_modifiable': 'bool',
            'is_modified': 'str',
            'is_adjusted': 'bool',
            'is_deprecated': 'bool',
            'is_basic': 'bool',
            'description': 'str',
            'ordinal': 'float',
            'update_comment': 'str',
            'container_id': 'float',
            'category': 'str',
            'constraint': 'str',
            'sid': 'str',
            'is_specified': 'bool',
            'allowed_values': 'list[AllowedParameterValue]'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'value': 'value',
            'display_value': 'displayValue',
            'number': 'number',
            'is_default': 'isDefault',
            'is_session_modifiable': 'isSessionModifiable',
            'is_system_modifiable': 'isSystemModifiable',
            'is_pdb_modifiable': 'isPdbModifiable',
            'is_instance_modifiable': 'isInstanceModifiable',
            'is_modified': 'isModified',
            'is_adjusted': 'isAdjusted',
            'is_deprecated': 'isDeprecated',
            'is_basic': 'isBasic',
            'description': 'description',
            'ordinal': 'ordinal',
            'update_comment': 'updateComment',
            'container_id': 'containerId',
            'category': 'category',
            'constraint': 'constraint',
            'sid': 'sid',
            'is_specified': 'isSpecified',
            'allowed_values': 'allowedValues'
        }

        self._name = None
        self._type = None
        self._value = None
        self._display_value = None
        self._number = None
        self._is_default = None
        self._is_session_modifiable = None
        self._is_system_modifiable = None
        self._is_pdb_modifiable = None
        self._is_instance_modifiable = None
        self._is_modified = None
        self._is_adjusted = None
        self._is_deprecated = None
        self._is_basic = None
        self._description = None
        self._ordinal = None
        self._update_comment = None
        self._container_id = None
        self._category = None
        self._constraint = None
        self._sid = None
        self._is_specified = None
        self._allowed_values = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DatabaseParameterSummary.
        The parameter name.


        :return: The name of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DatabaseParameterSummary.
        The parameter name.


        :param name: The name of this DatabaseParameterSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DatabaseParameterSummary.
        The parameter type.

        Allowed values for this property are: "BOOLEAN", "STRING", "INTEGER", "FILENAME", "BIG_INTEGER", "RESERVED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DatabaseParameterSummary.
        The parameter type.


        :param type: The type of this DatabaseParameterSummary.
        :type: str
        """
        allowed_values = ["BOOLEAN", "STRING", "INTEGER", "FILENAME", "BIG_INTEGER", "RESERVED"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this DatabaseParameterSummary.
        The parameter value.


        :return: The value of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DatabaseParameterSummary.
        The parameter value.


        :param value: The value of this DatabaseParameterSummary.
        :type: str
        """
        self._value = value

    @property
    def display_value(self):
        """
        **[Required]** Gets the display_value of this DatabaseParameterSummary.
        The parameter value in a user-friendly format. For example, if the `value` property shows the value 262144 for a big integer parameter, then the `displayValue` property will show the value 256K.


        :return: The display_value of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        """
        Sets the display_value of this DatabaseParameterSummary.
        The parameter value in a user-friendly format. For example, if the `value` property shows the value 262144 for a big integer parameter, then the `displayValue` property will show the value 256K.


        :param display_value: The display_value of this DatabaseParameterSummary.
        :type: str
        """
        self._display_value = display_value

    @property
    def number(self):
        """
        Gets the number of this DatabaseParameterSummary.
        The parameter number.


        :return: The number of this DatabaseParameterSummary.
        :rtype: float
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this DatabaseParameterSummary.
        The parameter number.


        :param number: The number of this DatabaseParameterSummary.
        :type: float
        """
        self._number = number

    @property
    def is_default(self):
        """
        Gets the is_default of this DatabaseParameterSummary.
        Indicates whether the parameter is set to the default value (`TRUE`) or the parameter value was specified in the parameter file (`FALSE`).


        :return: The is_default of this DatabaseParameterSummary.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this DatabaseParameterSummary.
        Indicates whether the parameter is set to the default value (`TRUE`) or the parameter value was specified in the parameter file (`FALSE`).


        :param is_default: The is_default of this DatabaseParameterSummary.
        :type: bool
        """
        self._is_default = is_default

    @property
    def is_session_modifiable(self):
        """
        Gets the is_session_modifiable of this DatabaseParameterSummary.
        Indicates whether the parameter can be changed with `ALTER SESSION` (`TRUE`) or not (`FALSE`)


        :return: The is_session_modifiable of this DatabaseParameterSummary.
        :rtype: bool
        """
        return self._is_session_modifiable

    @is_session_modifiable.setter
    def is_session_modifiable(self, is_session_modifiable):
        """
        Sets the is_session_modifiable of this DatabaseParameterSummary.
        Indicates whether the parameter can be changed with `ALTER SESSION` (`TRUE`) or not (`FALSE`)


        :param is_session_modifiable: The is_session_modifiable of this DatabaseParameterSummary.
        :type: bool
        """
        self._is_session_modifiable = is_session_modifiable

    @property
    def is_system_modifiable(self):
        """
        Gets the is_system_modifiable of this DatabaseParameterSummary.
        Indicates whether the parameter can be changed with `ALTER SYSTEM` and when the change takes effect:
        - IMMEDIATE: Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect immediately.
        - DEFERRED: Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect in subsequent sessions.
        - FALSE: Parameter cannot be changed with `ALTER SYSTEM` unless a server parameter file was used to start the instance. The change takes effect in subsequent instances.

        Allowed values for this property are: "IMMEDIATE", "DEFERRED", "FALSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The is_system_modifiable of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._is_system_modifiable

    @is_system_modifiable.setter
    def is_system_modifiable(self, is_system_modifiable):
        """
        Sets the is_system_modifiable of this DatabaseParameterSummary.
        Indicates whether the parameter can be changed with `ALTER SYSTEM` and when the change takes effect:
        - IMMEDIATE: Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect immediately.
        - DEFERRED: Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect in subsequent sessions.
        - FALSE: Parameter cannot be changed with `ALTER SYSTEM` unless a server parameter file was used to start the instance. The change takes effect in subsequent instances.


        :param is_system_modifiable: The is_system_modifiable of this DatabaseParameterSummary.
        :type: str
        """
        allowed_values = ["IMMEDIATE", "DEFERRED", "FALSE"]
        if not value_allowed_none_or_none_sentinel(is_system_modifiable, allowed_values):
            is_system_modifiable = 'UNKNOWN_ENUM_VALUE'
        self._is_system_modifiable = is_system_modifiable

    @property
    def is_pdb_modifiable(self):
        """
        Gets the is_pdb_modifiable of this DatabaseParameterSummary.
        Indicates whether the parameter can be modified on a per-PDB basis (`TRUE`) or not (`FALSE`). In a non-CDB, the value of this property is `null`.


        :return: The is_pdb_modifiable of this DatabaseParameterSummary.
        :rtype: bool
        """
        return self._is_pdb_modifiable

    @is_pdb_modifiable.setter
    def is_pdb_modifiable(self, is_pdb_modifiable):
        """
        Sets the is_pdb_modifiable of this DatabaseParameterSummary.
        Indicates whether the parameter can be modified on a per-PDB basis (`TRUE`) or not (`FALSE`). In a non-CDB, the value of this property is `null`.


        :param is_pdb_modifiable: The is_pdb_modifiable of this DatabaseParameterSummary.
        :type: bool
        """
        self._is_pdb_modifiable = is_pdb_modifiable

    @property
    def is_instance_modifiable(self):
        """
        Gets the is_instance_modifiable of this DatabaseParameterSummary.
        For parameters that can be changed with `ALTER SYSTEM`, indicates whether the value of the parameter can be different for every instance (`TRUE`) or whether the parameter must have the same value for all Real Application Clusters instances (`FALSE`). For other parameters, this is always `FALSE`.


        :return: The is_instance_modifiable of this DatabaseParameterSummary.
        :rtype: bool
        """
        return self._is_instance_modifiable

    @is_instance_modifiable.setter
    def is_instance_modifiable(self, is_instance_modifiable):
        """
        Sets the is_instance_modifiable of this DatabaseParameterSummary.
        For parameters that can be changed with `ALTER SYSTEM`, indicates whether the value of the parameter can be different for every instance (`TRUE`) or whether the parameter must have the same value for all Real Application Clusters instances (`FALSE`). For other parameters, this is always `FALSE`.


        :param is_instance_modifiable: The is_instance_modifiable of this DatabaseParameterSummary.
        :type: bool
        """
        self._is_instance_modifiable = is_instance_modifiable

    @property
    def is_modified(self):
        """
        Gets the is_modified of this DatabaseParameterSummary.
        Indicates how the parameter was modified. If an `ALTER SYSTEM` was performed, the value will be `MODIFIED`.

        Allowed values for this property are: "MODIFIED", "FALSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The is_modified of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._is_modified

    @is_modified.setter
    def is_modified(self, is_modified):
        """
        Sets the is_modified of this DatabaseParameterSummary.
        Indicates how the parameter was modified. If an `ALTER SYSTEM` was performed, the value will be `MODIFIED`.


        :param is_modified: The is_modified of this DatabaseParameterSummary.
        :type: str
        """
        allowed_values = ["MODIFIED", "FALSE"]
        if not value_allowed_none_or_none_sentinel(is_modified, allowed_values):
            is_modified = 'UNKNOWN_ENUM_VALUE'
        self._is_modified = is_modified

    @property
    def is_adjusted(self):
        """
        Gets the is_adjusted of this DatabaseParameterSummary.
        Indicates whether Oracle adjusted the input value to a more suitable value.


        :return: The is_adjusted of this DatabaseParameterSummary.
        :rtype: bool
        """
        return self._is_adjusted

    @is_adjusted.setter
    def is_adjusted(self, is_adjusted):
        """
        Sets the is_adjusted of this DatabaseParameterSummary.
        Indicates whether Oracle adjusted the input value to a more suitable value.


        :param is_adjusted: The is_adjusted of this DatabaseParameterSummary.
        :type: bool
        """
        self._is_adjusted = is_adjusted

    @property
    def is_deprecated(self):
        """
        Gets the is_deprecated of this DatabaseParameterSummary.
        Indicates whether the parameter has been deprecated (`TRUE`) or not (`FALSE`).


        :return: The is_deprecated of this DatabaseParameterSummary.
        :rtype: bool
        """
        return self._is_deprecated

    @is_deprecated.setter
    def is_deprecated(self, is_deprecated):
        """
        Sets the is_deprecated of this DatabaseParameterSummary.
        Indicates whether the parameter has been deprecated (`TRUE`) or not (`FALSE`).


        :param is_deprecated: The is_deprecated of this DatabaseParameterSummary.
        :type: bool
        """
        self._is_deprecated = is_deprecated

    @property
    def is_basic(self):
        """
        Gets the is_basic of this DatabaseParameterSummary.
        Indicates whether the parameter is a basic parameter (`TRUE`) or not (`FALSE`).


        :return: The is_basic of this DatabaseParameterSummary.
        :rtype: bool
        """
        return self._is_basic

    @is_basic.setter
    def is_basic(self, is_basic):
        """
        Sets the is_basic of this DatabaseParameterSummary.
        Indicates whether the parameter is a basic parameter (`TRUE`) or not (`FALSE`).


        :param is_basic: The is_basic of this DatabaseParameterSummary.
        :type: bool
        """
        self._is_basic = is_basic

    @property
    def description(self):
        """
        Gets the description of this DatabaseParameterSummary.
        The description of the parameter.


        :return: The description of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DatabaseParameterSummary.
        The description of the parameter.


        :param description: The description of this DatabaseParameterSummary.
        :type: str
        """
        self._description = description

    @property
    def ordinal(self):
        """
        Gets the ordinal of this DatabaseParameterSummary.
        The position (ordinal number) of the parameter value. Useful only for parameters whose values are lists of strings.


        :return: The ordinal of this DatabaseParameterSummary.
        :rtype: float
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """
        Sets the ordinal of this DatabaseParameterSummary.
        The position (ordinal number) of the parameter value. Useful only for parameters whose values are lists of strings.


        :param ordinal: The ordinal of this DatabaseParameterSummary.
        :type: float
        """
        self._ordinal = ordinal

    @property
    def update_comment(self):
        """
        Gets the update_comment of this DatabaseParameterSummary.
        The comments associated with the most recent update.


        :return: The update_comment of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._update_comment

    @update_comment.setter
    def update_comment(self, update_comment):
        """
        Sets the update_comment of this DatabaseParameterSummary.
        The comments associated with the most recent update.


        :param update_comment: The update_comment of this DatabaseParameterSummary.
        :type: str
        """
        self._update_comment = update_comment

    @property
    def container_id(self):
        """
        Gets the container_id of this DatabaseParameterSummary.
        The ID of the database container to which the data pertains.
        Possible values include:
        - `0`: This value is used for data that pertain to the entire CDB. This value is also used for data in non-CDBs.
        - `1`: This value is used for data that pertain to only the root container.
        - `n`: Where n is the applicable container ID for the data.


        :return: The container_id of this DatabaseParameterSummary.
        :rtype: float
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this DatabaseParameterSummary.
        The ID of the database container to which the data pertains.
        Possible values include:
        - `0`: This value is used for data that pertain to the entire CDB. This value is also used for data in non-CDBs.
        - `1`: This value is used for data that pertain to only the root container.
        - `n`: Where n is the applicable container ID for the data.


        :param container_id: The container_id of this DatabaseParameterSummary.
        :type: float
        """
        self._container_id = container_id

    @property
    def category(self):
        """
        Gets the category of this DatabaseParameterSummary.
        The parameter category.


        :return: The category of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this DatabaseParameterSummary.
        The parameter category.


        :param category: The category of this DatabaseParameterSummary.
        :type: str
        """
        self._category = category

    @property
    def constraint(self):
        """
        Gets the constraint of this DatabaseParameterSummary.
        Applicable in case of Oracle Real Application Clusters (Oracle RAC) databases.
        A `UNIQUE` parameter is one which is unique to each Oracle Real Application
        Clusters (Oracle RAC) instance. For example, the parameter `INSTANCE_NUMBER`
        must have different values in each instance. An `IDENTICAL` parameter must
        have the same value for every instance. For example, the parameter
        `DB_BLOCK_SIZE` must have the same value in all instances.

        Allowed values for this property are: "UNIQUE", "IDENTICAL", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The constraint of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        """
        Sets the constraint of this DatabaseParameterSummary.
        Applicable in case of Oracle Real Application Clusters (Oracle RAC) databases.
        A `UNIQUE` parameter is one which is unique to each Oracle Real Application
        Clusters (Oracle RAC) instance. For example, the parameter `INSTANCE_NUMBER`
        must have different values in each instance. An `IDENTICAL` parameter must
        have the same value for every instance. For example, the parameter
        `DB_BLOCK_SIZE` must have the same value in all instances.


        :param constraint: The constraint of this DatabaseParameterSummary.
        :type: str
        """
        allowed_values = ["UNIQUE", "IDENTICAL", "NONE"]
        if not value_allowed_none_or_none_sentinel(constraint, allowed_values):
            constraint = 'UNKNOWN_ENUM_VALUE'
        self._constraint = constraint

    @property
    def sid(self):
        """
        Gets the sid of this DatabaseParameterSummary.
        The database instance SID for which the parameter is defined.


        :return: The sid of this DatabaseParameterSummary.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this DatabaseParameterSummary.
        The database instance SID for which the parameter is defined.


        :param sid: The sid of this DatabaseParameterSummary.
        :type: str
        """
        self._sid = sid

    @property
    def is_specified(self):
        """
        Gets the is_specified of this DatabaseParameterSummary.
        Indicates whether the parameter was specified in the server parameter file (`TRUE`) or not (`FALSE`). Applicable only when the parameter source is `SPFILE`.


        :return: The is_specified of this DatabaseParameterSummary.
        :rtype: bool
        """
        return self._is_specified

    @is_specified.setter
    def is_specified(self, is_specified):
        """
        Sets the is_specified of this DatabaseParameterSummary.
        Indicates whether the parameter was specified in the server parameter file (`TRUE`) or not (`FALSE`). Applicable only when the parameter source is `SPFILE`.


        :param is_specified: The is_specified of this DatabaseParameterSummary.
        :type: bool
        """
        self._is_specified = is_specified

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this DatabaseParameterSummary.
        A list of allowed values for this parameter.


        :return: The allowed_values of this DatabaseParameterSummary.
        :rtype: list[oci.database_management.models.AllowedParameterValue]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this DatabaseParameterSummary.
        A list of allowed values for this parameter.


        :param allowed_values: The allowed_values of this DatabaseParameterSummary.
        :type: list[oci.database_management.models.AllowedParameterValue]
        """
        self._allowed_values = allowed_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
