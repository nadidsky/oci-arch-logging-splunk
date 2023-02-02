# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_tag_definition_validator import BaseTagDefinitionValidator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefaultTagDefinitionValidator(BaseTagDefinitionValidator):
    """
    Use this validator to clear any existing validator on the tag key definition with the UpdateTag
    operation. Using this `validatorType` is the same as not setting any value on the validator field.
    The resultant value for `validatorType` returned in the response body is `null`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DefaultTagDefinitionValidator object with values from keyword arguments. The default value of the :py:attr:`~oci.identity.models.DefaultTagDefinitionValidator.validator_type` attribute
        of this class is ``DEFAULT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param validator_type:
            The value to assign to the validator_type property of this DefaultTagDefinitionValidator.
            Allowed values for this property are: "ENUM", "DEFAULT"
        :type validator_type: str

        """
        self.swagger_types = {
            'validator_type': 'str'
        }

        self.attribute_map = {
            'validator_type': 'validatorType'
        }

        self._validator_type = None
        self._validator_type = 'DEFAULT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
