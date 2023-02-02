# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateRowDetails(object):
    """
    Specifications for the putting of a table row.
    """

    #: A constant which can be used with the option property of a UpdateRowDetails.
    #: This constant has a value of "IF_ABSENT"
    OPTION_IF_ABSENT = "IF_ABSENT"

    #: A constant which can be used with the option property of a UpdateRowDetails.
    #: This constant has a value of "IF_PRESENT"
    OPTION_IF_PRESENT = "IF_PRESENT"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateRowDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateRowDetails.
        :type compartment_id: str

        :param value:
            The value to assign to the value property of this UpdateRowDetails.
        :type value: dict(str, object)

        :param option:
            The value to assign to the option property of this UpdateRowDetails.
            Allowed values for this property are: "IF_ABSENT", "IF_PRESENT"
        :type option: str

        :param is_get_return_row:
            The value to assign to the is_get_return_row property of this UpdateRowDetails.
        :type is_get_return_row: bool

        :param timeout_in_ms:
            The value to assign to the timeout_in_ms property of this UpdateRowDetails.
        :type timeout_in_ms: int

        :param ttl:
            The value to assign to the ttl property of this UpdateRowDetails.
        :type ttl: int

        :param is_ttl_use_table_default:
            The value to assign to the is_ttl_use_table_default property of this UpdateRowDetails.
        :type is_ttl_use_table_default: bool

        :param identity_cache_size:
            The value to assign to the identity_cache_size property of this UpdateRowDetails.
        :type identity_cache_size: int

        :param is_exact_match:
            The value to assign to the is_exact_match property of this UpdateRowDetails.
        :type is_exact_match: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'value': 'dict(str, object)',
            'option': 'str',
            'is_get_return_row': 'bool',
            'timeout_in_ms': 'int',
            'ttl': 'int',
            'is_ttl_use_table_default': 'bool',
            'identity_cache_size': 'int',
            'is_exact_match': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'value': 'value',
            'option': 'option',
            'is_get_return_row': 'isGetReturnRow',
            'timeout_in_ms': 'timeoutInMs',
            'ttl': 'ttl',
            'is_ttl_use_table_default': 'isTtlUseTableDefault',
            'identity_cache_size': 'identityCacheSize',
            'is_exact_match': 'isExactMatch'
        }

        self._compartment_id = None
        self._value = None
        self._option = None
        self._is_get_return_row = None
        self._timeout_in_ms = None
        self._ttl = None
        self._is_ttl_use_table_default = None
        self._identity_cache_size = None
        self._is_exact_match = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UpdateRowDetails.
        The OCID of the table's compartment.  Required
        if the tableNameOrId path parameter is a table name.
        Optional if tableNameOrId is an OCID.  If tableNameOrId
        is an OCID, and compartmentId is supplied, the latter
        must match the identified table's compartmentId.


        :return: The compartment_id of this UpdateRowDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UpdateRowDetails.
        The OCID of the table's compartment.  Required
        if the tableNameOrId path parameter is a table name.
        Optional if tableNameOrId is an OCID.  If tableNameOrId
        is an OCID, and compartmentId is supplied, the latter
        must match the identified table's compartmentId.


        :param compartment_id: The compartment_id of this UpdateRowDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UpdateRowDetails.
        The map of values from a row.


        :return: The value of this UpdateRowDetails.
        :rtype: dict(str, object)
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UpdateRowDetails.
        The map of values from a row.


        :param value: The value of this UpdateRowDetails.
        :type: dict(str, object)
        """
        self._value = value

    @property
    def option(self):
        """
        Gets the option of this UpdateRowDetails.
        Specifies a condition for the put operation.

        Allowed values for this property are: "IF_ABSENT", "IF_PRESENT"


        :return: The option of this UpdateRowDetails.
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """
        Sets the option of this UpdateRowDetails.
        Specifies a condition for the put operation.


        :param option: The option of this UpdateRowDetails.
        :type: str
        """
        allowed_values = ["IF_ABSENT", "IF_PRESENT"]
        if not value_allowed_none_or_none_sentinel(option, allowed_values):
            raise ValueError(
                "Invalid value for `option`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._option = option

    @property
    def is_get_return_row(self):
        """
        Gets the is_get_return_row of this UpdateRowDetails.
        If true, and the put fails due to an option setting, then
        the existing row will be returned.


        :return: The is_get_return_row of this UpdateRowDetails.
        :rtype: bool
        """
        return self._is_get_return_row

    @is_get_return_row.setter
    def is_get_return_row(self, is_get_return_row):
        """
        Sets the is_get_return_row of this UpdateRowDetails.
        If true, and the put fails due to an option setting, then
        the existing row will be returned.


        :param is_get_return_row: The is_get_return_row of this UpdateRowDetails.
        :type: bool
        """
        self._is_get_return_row = is_get_return_row

    @property
    def timeout_in_ms(self):
        """
        Gets the timeout_in_ms of this UpdateRowDetails.
        Timeout setting for the put.


        :return: The timeout_in_ms of this UpdateRowDetails.
        :rtype: int
        """
        return self._timeout_in_ms

    @timeout_in_ms.setter
    def timeout_in_ms(self, timeout_in_ms):
        """
        Sets the timeout_in_ms of this UpdateRowDetails.
        Timeout setting for the put.


        :param timeout_in_ms: The timeout_in_ms of this UpdateRowDetails.
        :type: int
        """
        self._timeout_in_ms = timeout_in_ms

    @property
    def ttl(self):
        """
        Gets the ttl of this UpdateRowDetails.
        Time-to-live for the row, in days.


        :return: The ttl of this UpdateRowDetails.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this UpdateRowDetails.
        Time-to-live for the row, in days.


        :param ttl: The ttl of this UpdateRowDetails.
        :type: int
        """
        self._ttl = ttl

    @property
    def is_ttl_use_table_default(self):
        """
        Gets the is_ttl_use_table_default of this UpdateRowDetails.
        If true, set time-to-live for this row to the table's default.


        :return: The is_ttl_use_table_default of this UpdateRowDetails.
        :rtype: bool
        """
        return self._is_ttl_use_table_default

    @is_ttl_use_table_default.setter
    def is_ttl_use_table_default(self, is_ttl_use_table_default):
        """
        Sets the is_ttl_use_table_default of this UpdateRowDetails.
        If true, set time-to-live for this row to the table's default.


        :param is_ttl_use_table_default: The is_ttl_use_table_default of this UpdateRowDetails.
        :type: bool
        """
        self._is_ttl_use_table_default = is_ttl_use_table_default

    @property
    def identity_cache_size(self):
        """
        Gets the identity_cache_size of this UpdateRowDetails.
        Sets the number of generated identity values that are
        requested from the server during a put. If present and greater than 0,
        this value takes precedence over a default value for the table.


        :return: The identity_cache_size of this UpdateRowDetails.
        :rtype: int
        """
        return self._identity_cache_size

    @identity_cache_size.setter
    def identity_cache_size(self, identity_cache_size):
        """
        Sets the identity_cache_size of this UpdateRowDetails.
        Sets the number of generated identity values that are
        requested from the server during a put. If present and greater than 0,
        this value takes precedence over a default value for the table.


        :param identity_cache_size: The identity_cache_size of this UpdateRowDetails.
        :type: int
        """
        self._identity_cache_size = identity_cache_size

    @property
    def is_exact_match(self):
        """
        Gets the is_exact_match of this UpdateRowDetails.
        If present and true, the presented row value must exactly
        match the table's schema.  Otherwise, rows with missing
        non-key fields or extra fields can be written successfully.


        :return: The is_exact_match of this UpdateRowDetails.
        :rtype: bool
        """
        return self._is_exact_match

    @is_exact_match.setter
    def is_exact_match(self, is_exact_match):
        """
        Sets the is_exact_match of this UpdateRowDetails.
        If present and true, the presented row value must exactly
        match the table's schema.  Otherwise, rows with missing
        non-key fields or extra fields can be written successfully.


        :param is_exact_match: The is_exact_match of this UpdateRowDetails.
        :type: bool
        """
        self._is_exact_match = is_exact_match

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other