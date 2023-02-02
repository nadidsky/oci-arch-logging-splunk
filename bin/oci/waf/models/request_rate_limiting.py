# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestRateLimiting(object):
    """
    Module that allows inspection of HTTP connection properties and to limit requests frequency for a given key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestRateLimiting object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rules:
            The value to assign to the rules property of this RequestRateLimiting.
        :type rules: list[oci.waf.models.RequestRateLimitingRule]

        """
        self.swagger_types = {
            'rules': 'list[RequestRateLimitingRule]'
        }

        self.attribute_map = {
            'rules': 'rules'
        }

        self._rules = None

    @property
    def rules(self):
        """
        Gets the rules of this RequestRateLimiting.
        Ordered list of RequestRateLimitingRules. Rules are executed in order of appearance in this array.


        :return: The rules of this RequestRateLimiting.
        :rtype: list[oci.waf.models.RequestRateLimitingRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this RequestRateLimiting.
        Ordered list of RequestRateLimitingRules. Rules are executed in order of appearance in this array.


        :param rules: The rules of this RequestRateLimiting.
        :type: list[oci.waf.models.RequestRateLimitingRule]
        """
        self._rules = rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
