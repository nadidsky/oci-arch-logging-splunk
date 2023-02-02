# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSourceDetails(object):
    """
    You can update the authorization details to access the source environment from which you want to migrate applications to
    Oracle Cloud Infrastructure. You can also update the description and tags of a source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateSourceDetails.
        :type description: str

        :param source_details:
            The value to assign to the source_details property of this UpdateSourceDetails.
        :type source_details: oci.application_migration.models.SourceDetails

        :param authorization_details:
            The value to assign to the authorization_details property of this UpdateSourceDetails.
        :type authorization_details: oci.application_migration.models.AuthorizationDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'source_details': 'SourceDetails',
            'authorization_details': 'AuthorizationDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'source_details': 'sourceDetails',
            'authorization_details': 'authorizationDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._source_details = None
        self._authorization_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateSourceDetails.
        Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.


        :return: The display_name of this UpdateSourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateSourceDetails.
        Name of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.


        :param display_name: The display_name of this UpdateSourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateSourceDetails.
        Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.


        :return: The description of this UpdateSourceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateSourceDetails.
        Description of the source. This helps you to identify the appropriate source environment when you have multiple sources defined.


        :param description: The description of this UpdateSourceDetails.
        :type: str
        """
        self._description = description

    @property
    def source_details(self):
        """
        Gets the source_details of this UpdateSourceDetails.

        :return: The source_details of this UpdateSourceDetails.
        :rtype: oci.application_migration.models.SourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this UpdateSourceDetails.

        :param source_details: The source_details of this UpdateSourceDetails.
        :type: oci.application_migration.models.SourceDetails
        """
        self._source_details = source_details

    @property
    def authorization_details(self):
        """
        Gets the authorization_details of this UpdateSourceDetails.

        :return: The authorization_details of this UpdateSourceDetails.
        :rtype: oci.application_migration.models.AuthorizationDetails
        """
        return self._authorization_details

    @authorization_details.setter
    def authorization_details(self, authorization_details):
        """
        Sets the authorization_details of this UpdateSourceDetails.

        :param authorization_details: The authorization_details of this UpdateSourceDetails.
        :type: oci.application_migration.models.AuthorizationDetails
        """
        self._authorization_details = authorization_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSourceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSourceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSourceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSourceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSourceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
