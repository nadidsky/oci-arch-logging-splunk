# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .topology_entity_relationship import TopologyEntityRelationship
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopologyRoutesToEntityRelationship(TopologyEntityRelationship):
    """
    Defines the `routesTo` relationship between virtual network topology entities. A `RoutesTo` relationship
    is defined when a routing table and a routing rule  are used to govern how to route traffic
    from one entity to another. For example, a DRG might have a routing rule to send certain traffic to an LPG.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TopologyRoutesToEntityRelationship object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.TopologyRoutesToEntityRelationship.type` attribute
        of this class is ``ROUTES_TO`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id1:
            The value to assign to the id1 property of this TopologyRoutesToEntityRelationship.
        :type id1: str

        :param id2:
            The value to assign to the id2 property of this TopologyRoutesToEntityRelationship.
        :type id2: str

        :param type:
            The value to assign to the type property of this TopologyRoutesToEntityRelationship.
            Allowed values for this property are: "CONTAINS", "ASSOCIATED_WITH", "ROUTES_TO"
        :type type: str

        :param route_rule_details:
            The value to assign to the route_rule_details property of this TopologyRoutesToEntityRelationship.
        :type route_rule_details: oci.core.models.TopologyRoutesToRelationshipDetails

        """
        self.swagger_types = {
            'id1': 'str',
            'id2': 'str',
            'type': 'str',
            'route_rule_details': 'TopologyRoutesToRelationshipDetails'
        }

        self.attribute_map = {
            'id1': 'id1',
            'id2': 'id2',
            'type': 'type',
            'route_rule_details': 'routeRuleDetails'
        }

        self._id1 = None
        self._id2 = None
        self._type = None
        self._route_rule_details = None
        self._type = 'ROUTES_TO'

    @property
    def route_rule_details(self):
        """
        **[Required]** Gets the route_rule_details of this TopologyRoutesToEntityRelationship.

        :return: The route_rule_details of this TopologyRoutesToEntityRelationship.
        :rtype: oci.core.models.TopologyRoutesToRelationshipDetails
        """
        return self._route_rule_details

    @route_rule_details.setter
    def route_rule_details(self, route_rule_details):
        """
        Sets the route_rule_details of this TopologyRoutesToEntityRelationship.

        :param route_rule_details: The route_rule_details of this TopologyRoutesToEntityRelationship.
        :type: oci.core.models.TopologyRoutesToRelationshipDetails
        """
        self._route_rule_details = route_rule_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
