# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaintenancePolicy(object):
    """
    The policy that specifies the maintenance and upgrade preferences for an environment. For more information about the options, see `Understanding Environment Maintenance`__.

    __ https://docs.cloud.oracle.com/iaas/Content/fusion-applications/plan-environment-family.htm#about-env-maintenance
    """

    #: A constant which can be used with the monthly_patching_override property of a MaintenancePolicy.
    #: This constant has a value of "ENABLED"
    MONTHLY_PATCHING_OVERRIDE_ENABLED = "ENABLED"

    #: A constant which can be used with the monthly_patching_override property of a MaintenancePolicy.
    #: This constant has a value of "DISABLED"
    MONTHLY_PATCHING_OVERRIDE_DISABLED = "DISABLED"

    #: A constant which can be used with the monthly_patching_override property of a MaintenancePolicy.
    #: This constant has a value of "NONE"
    MONTHLY_PATCHING_OVERRIDE_NONE = "NONE"

    #: A constant which can be used with the environment_maintenance_override property of a MaintenancePolicy.
    #: This constant has a value of "PROD"
    ENVIRONMENT_MAINTENANCE_OVERRIDE_PROD = "PROD"

    #: A constant which can be used with the environment_maintenance_override property of a MaintenancePolicy.
    #: This constant has a value of "NON_PROD"
    ENVIRONMENT_MAINTENANCE_OVERRIDE_NON_PROD = "NON_PROD"

    #: A constant which can be used with the environment_maintenance_override property of a MaintenancePolicy.
    #: This constant has a value of "NONE"
    ENVIRONMENT_MAINTENANCE_OVERRIDE_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new MaintenancePolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param monthly_patching_override:
            The value to assign to the monthly_patching_override property of this MaintenancePolicy.
            Allowed values for this property are: "ENABLED", "DISABLED", "NONE"
        :type monthly_patching_override: str

        :param environment_maintenance_override:
            The value to assign to the environment_maintenance_override property of this MaintenancePolicy.
            Allowed values for this property are: "PROD", "NON_PROD", "NONE"
        :type environment_maintenance_override: str

        """
        self.swagger_types = {
            'monthly_patching_override': 'str',
            'environment_maintenance_override': 'str'
        }

        self.attribute_map = {
            'monthly_patching_override': 'monthlyPatchingOverride',
            'environment_maintenance_override': 'environmentMaintenanceOverride'
        }

        self._monthly_patching_override = None
        self._environment_maintenance_override = None

    @property
    def monthly_patching_override(self):
        """
        Gets the monthly_patching_override of this MaintenancePolicy.
        When \"ENABLED\", the Fusion environment is patched monthly. When \"DISABLED\", the Fusion environment is not patched monthly. This setting overrides the environment family setting. When not set, the environment follows the environment family policy.

        Allowed values for this property are: "ENABLED", "DISABLED", "NONE"


        :return: The monthly_patching_override of this MaintenancePolicy.
        :rtype: str
        """
        return self._monthly_patching_override

    @monthly_patching_override.setter
    def monthly_patching_override(self, monthly_patching_override):
        """
        Sets the monthly_patching_override of this MaintenancePolicy.
        When \"ENABLED\", the Fusion environment is patched monthly. When \"DISABLED\", the Fusion environment is not patched monthly. This setting overrides the environment family setting. When not set, the environment follows the environment family policy.


        :param monthly_patching_override: The monthly_patching_override of this MaintenancePolicy.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "NONE"]
        if not value_allowed_none_or_none_sentinel(monthly_patching_override, allowed_values):
            raise ValueError(
                "Invalid value for `monthly_patching_override`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._monthly_patching_override = monthly_patching_override

    @property
    def environment_maintenance_override(self):
        """
        Gets the environment_maintenance_override of this MaintenancePolicy.
        User choice to upgrade both test and prod pods at the same time. Overrides fusion environment families'.

        Allowed values for this property are: "PROD", "NON_PROD", "NONE"


        :return: The environment_maintenance_override of this MaintenancePolicy.
        :rtype: str
        """
        return self._environment_maintenance_override

    @environment_maintenance_override.setter
    def environment_maintenance_override(self, environment_maintenance_override):
        """
        Sets the environment_maintenance_override of this MaintenancePolicy.
        User choice to upgrade both test and prod pods at the same time. Overrides fusion environment families'.


        :param environment_maintenance_override: The environment_maintenance_override of this MaintenancePolicy.
        :type: str
        """
        allowed_values = ["PROD", "NON_PROD", "NONE"]
        if not value_allowed_none_or_none_sentinel(environment_maintenance_override, allowed_values):
            raise ValueError(
                "Invalid value for `environment_maintenance_override`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._environment_maintenance_override = environment_maintenance_override

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
