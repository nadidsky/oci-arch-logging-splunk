# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DynamicSelectionKey(object):
    """
    Information around the values for selector of an authentication/ routing branch.
    """

    #: A constant which can be used with the type property of a DynamicSelectionKey.
    #: This constant has a value of "ANY_OF"
    TYPE_ANY_OF = "ANY_OF"

    #: A constant which can be used with the type property of a DynamicSelectionKey.
    #: This constant has a value of "WILDCARD"
    TYPE_WILDCARD = "WILDCARD"

    def __init__(self, **kwargs):
        """
        Initializes a new DynamicSelectionKey object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apigateway.models.WildcardSelectionKey`
        * :class:`~oci.apigateway.models.AnyOfSelectionKey`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DynamicSelectionKey.
            Allowed values for this property are: "ANY_OF", "WILDCARD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param is_default:
            The value to assign to the is_default property of this DynamicSelectionKey.
        :type is_default: bool

        :param name:
            The value to assign to the name property of this DynamicSelectionKey.
        :type name: str

        """
        self.swagger_types = {
            'type': 'str',
            'is_default': 'bool',
            'name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'is_default': 'isDefault',
            'name': 'name'
        }

        self._type = None
        self._is_default = None
        self._name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'WILDCARD':
            return 'WildcardSelectionKey'

        if type == 'ANY_OF':
            return 'AnyOfSelectionKey'
        else:
            return 'DynamicSelectionKey'

    @property
    def type(self):
        """
        Gets the type of this DynamicSelectionKey.
        Information regarding type of the selection key.

        Allowed values for this property are: "ANY_OF", "WILDCARD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DynamicSelectionKey.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DynamicSelectionKey.
        Information regarding type of the selection key.


        :param type: The type of this DynamicSelectionKey.
        :type: str
        """
        allowed_values = ["ANY_OF", "WILDCARD"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def is_default(self):
        """
        Gets the is_default of this DynamicSelectionKey.
        Information regarding whether this is the default branch.


        :return: The is_default of this DynamicSelectionKey.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this DynamicSelectionKey.
        Information regarding whether this is the default branch.


        :param is_default: The is_default of this DynamicSelectionKey.
        :type: bool
        """
        self._is_default = is_default

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DynamicSelectionKey.
        Name assigned to the branch.


        :return: The name of this DynamicSelectionKey.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DynamicSelectionKey.
        Name assigned to the branch.


        :param name: The name of this DynamicSelectionKey.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other