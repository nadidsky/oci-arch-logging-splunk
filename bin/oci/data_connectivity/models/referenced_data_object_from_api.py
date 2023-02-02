# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .referenced_data_object import ReferencedDataObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReferencedDataObjectFromAPI(ReferencedDataObject):
    """
    The input procedure object
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReferencedDataObjectFromAPI object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.ReferencedDataObjectFromAPI.model_type` attribute
        of this class is ``API`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ReferencedDataObjectFromAPI.
            Allowed values for this property are: "PROCEDURE", "API"
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this ReferencedDataObjectFromAPI.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ReferencedDataObjectFromAPI.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this ReferencedDataObjectFromAPI.
        :type name: str

        :param object_version:
            The value to assign to the object_version property of this ReferencedDataObjectFromAPI.
        :type object_version: int

        :param resource_name:
            The value to assign to the resource_name property of this ReferencedDataObjectFromAPI.
        :type resource_name: str

        :param object_status:
            The value to assign to the object_status property of this ReferencedDataObjectFromAPI.
        :type object_status: int

        :param external_key:
            The value to assign to the external_key property of this ReferencedDataObjectFromAPI.
        :type external_key: str

        :param key:
            The value to assign to the key property of this ReferencedDataObjectFromAPI.
        :type key: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_version': 'int',
            'resource_name': 'str',
            'object_status': 'int',
            'external_key': 'str',
            'key': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_version': 'objectVersion',
            'resource_name': 'resourceName',
            'object_status': 'objectStatus',
            'external_key': 'externalKey',
            'key': 'key'
        }

        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_version = None
        self._resource_name = None
        self._object_status = None
        self._external_key = None
        self._key = None
        self._model_type = 'API'

    @property
    def key(self):
        """
        Gets the key of this ReferencedDataObjectFromAPI.
        The object key.


        :return: The key of this ReferencedDataObjectFromAPI.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ReferencedDataObjectFromAPI.
        The object key.


        :param key: The key of this ReferencedDataObjectFromAPI.
        :type: str
        """
        self._key = key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
