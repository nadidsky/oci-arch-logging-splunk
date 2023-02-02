# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SetAutoUpgradableConfigDetails(object):
    """
    Details for configuring tenancy-level agent AutoUpgradable configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SetAutoUpgradableConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this SetAutoUpgradableConfigDetails.
        :type compartment_id: str

        :param is_agent_auto_upgradable:
            The value to assign to the is_agent_auto_upgradable property of this SetAutoUpgradableConfigDetails.
        :type is_agent_auto_upgradable: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'is_agent_auto_upgradable': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'is_agent_auto_upgradable': 'isAgentAutoUpgradable'
        }

        self._compartment_id = None
        self._is_agent_auto_upgradable = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SetAutoUpgradableConfigDetails.
        Tenancy identifier i.e, Root compartment identifier


        :return: The compartment_id of this SetAutoUpgradableConfigDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SetAutoUpgradableConfigDetails.
        Tenancy identifier i.e, Root compartment identifier


        :param compartment_id: The compartment_id of this SetAutoUpgradableConfigDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_agent_auto_upgradable(self):
        """
        **[Required]** Gets the is_agent_auto_upgradable of this SetAutoUpgradableConfigDetails.
        true if the agents can be upgraded automatically; false if they must be upgraded manually.


        :return: The is_agent_auto_upgradable of this SetAutoUpgradableConfigDetails.
        :rtype: bool
        """
        return self._is_agent_auto_upgradable

    @is_agent_auto_upgradable.setter
    def is_agent_auto_upgradable(self, is_agent_auto_upgradable):
        """
        Sets the is_agent_auto_upgradable of this SetAutoUpgradableConfigDetails.
        true if the agents can be upgraded automatically; false if they must be upgraded manually.


        :param is_agent_auto_upgradable: The is_agent_auto_upgradable of this SetAutoUpgradableConfigDetails.
        :type: bool
        """
        self._is_agent_auto_upgradable = is_agent_auto_upgradable

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
