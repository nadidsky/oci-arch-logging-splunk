# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Item(object):
    """
    The model for an item within an array of filter values.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Item object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Item.
        :type name: str

        :param code:
            The value to assign to the code property of this Item.
        :type code: str

        """
        self.swagger_types = {
            'name': 'str',
            'code': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'code': 'code'
        }

        self._name = None
        self._code = None

    @property
    def name(self):
        """
        Gets the name of this Item.
        The name of the item.


        :return: The name of this Item.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Item.
        The name of the item.


        :param name: The name of this Item.
        :type: str
        """
        self._name = name

    @property
    def code(self):
        """
        Gets the code of this Item.
        A code assigned to the item.


        :return: The code of this Item.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Item.
        A code assigned to the item.


        :param code: The code of this Item.
        :type: str
        """
        self._code = code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
