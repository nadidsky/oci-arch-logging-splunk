# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .ingest_time_rule_condition import IngestTimeRuleCondition
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngestTimeRuleFieldCondition(IngestTimeRuleCondition):
    """
    The field condition(s) to evaluate for an ingest time rule.
    """

    #: A constant which can be used with the field_operator property of a IngestTimeRuleFieldCondition.
    #: This constant has a value of "EQUAL"
    FIELD_OPERATOR_EQUAL = "EQUAL"

    def __init__(self, **kwargs):
        """
        Initializes a new IngestTimeRuleFieldCondition object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.IngestTimeRuleFieldCondition.kind` attribute
        of this class is ``FIELD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this IngestTimeRuleFieldCondition.
            Allowed values for this property are: "FIELD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param field_name:
            The value to assign to the field_name property of this IngestTimeRuleFieldCondition.
        :type field_name: str

        :param field_operator:
            The value to assign to the field_operator property of this IngestTimeRuleFieldCondition.
            Allowed values for this property are: "EQUAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type field_operator: str

        :param field_value:
            The value to assign to the field_value property of this IngestTimeRuleFieldCondition.
        :type field_value: str

        :param additional_conditions:
            The value to assign to the additional_conditions property of this IngestTimeRuleFieldCondition.
        :type additional_conditions: list[oci.log_analytics.models.IngestTimeRuleAdditionalFieldCondition]

        """
        self.swagger_types = {
            'kind': 'str',
            'field_name': 'str',
            'field_operator': 'str',
            'field_value': 'str',
            'additional_conditions': 'list[IngestTimeRuleAdditionalFieldCondition]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'field_name': 'fieldName',
            'field_operator': 'fieldOperator',
            'field_value': 'fieldValue',
            'additional_conditions': 'additionalConditions'
        }

        self._kind = None
        self._field_name = None
        self._field_operator = None
        self._field_value = None
        self._additional_conditions = None
        self._kind = 'FIELD'

    @property
    def field_name(self):
        """
        **[Required]** Gets the field_name of this IngestTimeRuleFieldCondition.
        The field name to be evaluated.


        :return: The field_name of this IngestTimeRuleFieldCondition.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this IngestTimeRuleFieldCondition.
        The field name to be evaluated.


        :param field_name: The field_name of this IngestTimeRuleFieldCondition.
        :type: str
        """
        self._field_name = field_name

    @property
    def field_operator(self):
        """
        **[Required]** Gets the field_operator of this IngestTimeRuleFieldCondition.
        The operator to be used for evaluating the field.

        Allowed values for this property are: "EQUAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The field_operator of this IngestTimeRuleFieldCondition.
        :rtype: str
        """
        return self._field_operator

    @field_operator.setter
    def field_operator(self, field_operator):
        """
        Sets the field_operator of this IngestTimeRuleFieldCondition.
        The operator to be used for evaluating the field.


        :param field_operator: The field_operator of this IngestTimeRuleFieldCondition.
        :type: str
        """
        allowed_values = ["EQUAL"]
        if not value_allowed_none_or_none_sentinel(field_operator, allowed_values):
            field_operator = 'UNKNOWN_ENUM_VALUE'
        self._field_operator = field_operator

    @property
    def field_value(self):
        """
        **[Required]** Gets the field_value of this IngestTimeRuleFieldCondition.
        The field value to be evaluated.


        :return: The field_value of this IngestTimeRuleFieldCondition.
        :rtype: str
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        """
        Sets the field_value of this IngestTimeRuleFieldCondition.
        The field value to be evaluated.


        :param field_value: The field_value of this IngestTimeRuleFieldCondition.
        :type: str
        """
        self._field_value = field_value

    @property
    def additional_conditions(self):
        """
        Gets the additional_conditions of this IngestTimeRuleFieldCondition.
        Optional additional condition(s) to be evaluated.


        :return: The additional_conditions of this IngestTimeRuleFieldCondition.
        :rtype: list[oci.log_analytics.models.IngestTimeRuleAdditionalFieldCondition]
        """
        return self._additional_conditions

    @additional_conditions.setter
    def additional_conditions(self, additional_conditions):
        """
        Sets the additional_conditions of this IngestTimeRuleFieldCondition.
        Optional additional condition(s) to be evaluated.


        :param additional_conditions: The additional_conditions of this IngestTimeRuleFieldCondition.
        :type: list[oci.log_analytics.models.IngestTimeRuleAdditionalFieldCondition]
        """
        self._additional_conditions = additional_conditions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
