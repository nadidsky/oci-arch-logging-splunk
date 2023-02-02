# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .endpoint import Endpoint
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubnetEndpoint(Endpoint):
    """
    Defines the details required for a SUBNET-type `Endpoint`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubnetEndpoint object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.SubnetEndpoint.type` attribute
        of this class is ``SUBNET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SubnetEndpoint.
            Allowed values for this property are: "IP_ADDRESS", "SUBNET", "COMPUTE_INSTANCE", "VNIC", "LOAD_BALANCER", "LOAD_BALANCER_LISTENER", "NETWORK_LOAD_BALANCER", "NETWORK_LOAD_BALANCER_LISTENER", "VLAN"
        :type type: str

        :param address:
            The value to assign to the address property of this SubnetEndpoint.
        :type address: str

        :param subnet_id:
            The value to assign to the subnet_id property of this SubnetEndpoint.
        :type subnet_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'address': 'str',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'address': 'address',
            'subnet_id': 'subnetId'
        }

        self._type = None
        self._address = None
        self._subnet_id = None
        self._type = 'SUBNET'

    @property
    def address(self):
        """
        **[Required]** Gets the address of this SubnetEndpoint.
        The IPv4 address of the `Endpoint`.


        :return: The address of this SubnetEndpoint.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this SubnetEndpoint.
        The IPv4 address of the `Endpoint`.


        :param address: The address of this SubnetEndpoint.
        :type: str
        """
        self._address = address

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this SubnetEndpoint.
        The `OCID`__ of the subnet containing the IP address.
        This can be used to disambiguate which subnet is intended, in case the IP address
        is used in more than one subnet (when there are subnets with overlapping IP ranges).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this SubnetEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this SubnetEndpoint.
        The `OCID`__ of the subnet containing the IP address.
        This can be used to disambiguate which subnet is intended, in case the IP address
        is used in more than one subnet (when there are subnets with overlapping IP ranges).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this SubnetEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
