# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .artifact_import_details import ArtifactImportDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ArtifactImportDetailsObjectStorage(ArtifactImportDetails):
    """
    Artifact destination details for importing to destination bucket
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ArtifactImportDetailsObjectStorage object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.ArtifactImportDetailsObjectStorage.artifact_source_type` attribute
        of this class is ``ORACLE_OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param artifact_source_type:
            The value to assign to the artifact_source_type property of this ArtifactImportDetailsObjectStorage.
            Allowed values for this property are: "ORACLE_OBJECT_STORAGE"
        :type artifact_source_type: str

        :param namespace:
            The value to assign to the namespace property of this ArtifactImportDetailsObjectStorage.
        :type namespace: str

        :param destination_bucket:
            The value to assign to the destination_bucket property of this ArtifactImportDetailsObjectStorage.
        :type destination_bucket: str

        :param destination_object_name:
            The value to assign to the destination_object_name property of this ArtifactImportDetailsObjectStorage.
        :type destination_object_name: str

        :param destination_region:
            The value to assign to the destination_region property of this ArtifactImportDetailsObjectStorage.
        :type destination_region: str

        """
        self.swagger_types = {
            'artifact_source_type': 'str',
            'namespace': 'str',
            'destination_bucket': 'str',
            'destination_object_name': 'str',
            'destination_region': 'str'
        }

        self.attribute_map = {
            'artifact_source_type': 'artifactSourceType',
            'namespace': 'namespace',
            'destination_bucket': 'destinationBucket',
            'destination_object_name': 'destinationObjectName',
            'destination_region': 'destinationRegion'
        }

        self._artifact_source_type = None
        self._namespace = None
        self._destination_bucket = None
        self._destination_object_name = None
        self._destination_region = None
        self._artifact_source_type = 'ORACLE_OBJECT_STORAGE'

    @property
    def namespace(self):
        """
        Gets the namespace of this ArtifactImportDetailsObjectStorage.
        The Object Storage namespace used for the request.


        :return: The namespace of this ArtifactImportDetailsObjectStorage.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ArtifactImportDetailsObjectStorage.
        The Object Storage namespace used for the request.


        :param namespace: The namespace of this ArtifactImportDetailsObjectStorage.
        :type: str
        """
        self._namespace = namespace

    @property
    def destination_bucket(self):
        """
        Gets the destination_bucket of this ArtifactImportDetailsObjectStorage.
        The name of the bucket. Avoid entering confidential information.


        :return: The destination_bucket of this ArtifactImportDetailsObjectStorage.
        :rtype: str
        """
        return self._destination_bucket

    @destination_bucket.setter
    def destination_bucket(self, destination_bucket):
        """
        Sets the destination_bucket of this ArtifactImportDetailsObjectStorage.
        The name of the bucket. Avoid entering confidential information.


        :param destination_bucket: The destination_bucket of this ArtifactImportDetailsObjectStorage.
        :type: str
        """
        self._destination_bucket = destination_bucket

    @property
    def destination_object_name(self):
        """
        Gets the destination_object_name of this ArtifactImportDetailsObjectStorage.
        The name of the object resulting from the copy operation.


        :return: The destination_object_name of this ArtifactImportDetailsObjectStorage.
        :rtype: str
        """
        return self._destination_object_name

    @destination_object_name.setter
    def destination_object_name(self, destination_object_name):
        """
        Sets the destination_object_name of this ArtifactImportDetailsObjectStorage.
        The name of the object resulting from the copy operation.


        :param destination_object_name: The destination_object_name of this ArtifactImportDetailsObjectStorage.
        :type: str
        """
        self._destination_object_name = destination_object_name

    @property
    def destination_region(self):
        """
        Gets the destination_region of this ArtifactImportDetailsObjectStorage.
        Region in which OSS bucket is present


        :return: The destination_region of this ArtifactImportDetailsObjectStorage.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """
        Sets the destination_region of this ArtifactImportDetailsObjectStorage.
        Region in which OSS bucket is present


        :param destination_region: The destination_region of this ArtifactImportDetailsObjectStorage.
        :type: str
        """
        self._destination_region = destination_region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
