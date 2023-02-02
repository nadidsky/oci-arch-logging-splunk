# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .absolute_time_start_policy import AbsoluteTimeStartPolicy
from .activity_problem_aggregation import ActivityProblemAggregation
from .activity_problem_aggregation_collection import ActivityProblemAggregationCollection
from .add_compartment_details import AddCompartmentDetails
from .all_targets_selected import AllTargetsSelected
from .attach_target_detector_recipe_details import AttachTargetDetectorRecipeDetails
from .attach_target_responder_recipe_details import AttachTargetResponderRecipeDetails
from .candidate_responder_rule import CandidateResponderRule
from .change_data_source_compartment_details import ChangeDataSourceCompartmentDetails
from .change_detector_recipe_compartment_details import ChangeDetectorRecipeCompartmentDetails
from .change_managed_list_compartment_details import ChangeManagedListCompartmentDetails
from .change_responder_recipe_compartment_details import ChangeResponderRecipeCompartmentDetails
from .change_security_policy_compartment_details import ChangeSecurityPolicyCompartmentDetails
from .change_security_recipe_compartment_details import ChangeSecurityRecipeCompartmentDetails
from .change_security_zone_compartment_details import ChangeSecurityZoneCompartmentDetails
from .composite_condition import CompositeCondition
from .condition import Condition
from .condition_group import ConditionGroup
from .condition_metadata_type import ConditionMetadataType
from .condition_metadata_type_collection import ConditionMetadataTypeCollection
from .condition_metadata_type_summary import ConditionMetadataTypeSummary
from .condition_operator import ConditionOperator
from .config_value import ConfigValue
from .configuration import Configuration
from .continuous_query_start_policy import ContinuousQueryStartPolicy
from .create_data_mask_rule_details import CreateDataMaskRuleDetails
from .create_data_source_details import CreateDataSourceDetails
from .create_detector_recipe_details import CreateDetectorRecipeDetails
from .create_detector_recipe_detector_rule_details import CreateDetectorRecipeDetectorRuleDetails
from .create_detector_rule_details import CreateDetectorRuleDetails
from .create_managed_list_details import CreateManagedListDetails
from .create_responder_recipe_details import CreateResponderRecipeDetails
from .create_security_policy_details import CreateSecurityPolicyDetails
from .create_security_recipe_details import CreateSecurityRecipeDetails
from .create_security_zone_details import CreateSecurityZoneDetails
from .create_target_details import CreateTargetDetails
from .create_target_detector_recipe_details import CreateTargetDetectorRecipeDetails
from .create_target_responder_recipe_details import CreateTargetResponderRecipeDetails
from .data_mask_rule import DataMaskRule
from .data_mask_rule_collection import DataMaskRuleCollection
from .data_mask_rule_summary import DataMaskRuleSummary
from .data_source import DataSource
from .data_source_collection import DataSourceCollection
from .data_source_details import DataSourceDetails
from .data_source_event_collection import DataSourceEventCollection
from .data_source_event_info import DataSourceEventInfo
from .data_source_event_summary import DataSourceEventSummary
from .data_source_mapping_info import DataSourceMappingInfo
from .data_source_summary import DataSourceSummary
from .data_source_summary_details import DataSourceSummaryDetails
from .detector import Detector
from .detector_collection import DetectorCollection
from .detector_configuration import DetectorConfiguration
from .detector_details import DetectorDetails
from .detector_recipe import DetectorRecipe
from .detector_recipe_collection import DetectorRecipeCollection
from .detector_recipe_detector_rule import DetectorRecipeDetectorRule
from .detector_recipe_detector_rule_collection import DetectorRecipeDetectorRuleCollection
from .detector_recipe_detector_rule_summary import DetectorRecipeDetectorRuleSummary
from .detector_recipe_summary import DetectorRecipeSummary
from .detector_rule import DetectorRule
from .detector_rule_collection import DetectorRuleCollection
from .detector_rule_summary import DetectorRuleSummary
from .detector_summary import DetectorSummary
from .entities_mapping import EntitiesMapping
from .entity_details import EntityDetails
from .execute_responder_execution_details import ExecuteResponderExecutionDetails
from .geographical_location import GeographicalLocation
from .impacted_resource_collection import ImpactedResourceCollection
from .impacted_resource_summary import ImpactedResourceSummary
from .insight_type_logging_query_details import InsightTypeLoggingQueryDetails
from .logging_event_info import LoggingEventInfo
from .logging_query_data_source_details import LoggingQueryDataSourceDetails
from .logging_query_data_source_summary_details import LoggingQueryDataSourceSummaryDetails
from .logging_query_details import LoggingQueryDetails
from .managed_list import ManagedList
from .managed_list_collection import ManagedListCollection
from .managed_list_summary import ManagedListSummary
from .managed_list_type_collection import ManagedListTypeCollection
from .managed_list_type_summary import ManagedListTypeSummary
from .no_delay_start_policy import NoDelayStartPolicy
from .operator_summary import OperatorSummary
from .policy_collection import PolicyCollection
from .policy_summary import PolicySummary
from .political_location import PoliticalLocation
from .problem import Problem
from .problem_aggregation import ProblemAggregation
from .problem_aggregation_collection import ProblemAggregationCollection
from .problem_collection import ProblemCollection
from .problem_endpoint_collection import ProblemEndpointCollection
from .problem_endpoint_summary import ProblemEndpointSummary
from .problem_entity_collection import ProblemEntityCollection
from .problem_entity_summary import ProblemEntitySummary
from .problem_history_collection import ProblemHistoryCollection
from .problem_history_summary import ProblemHistorySummary
from .problem_summary import ProblemSummary
from .problem_trend_aggregation import ProblemTrendAggregation
from .problem_trend_aggregation_collection import ProblemTrendAggregationCollection
from .recommendation_summary import RecommendationSummary
from .recommendation_summary_collection import RecommendationSummaryCollection
from .region_status_detail import RegionStatusDetail
from .remove_compartment_details import RemoveCompartmentDetails
from .request_summarized_trend_resource_risk_scores_details import RequestSummarizedTrendResourceRiskScoresDetails
from .resource_profile import ResourceProfile
from .resource_profile_collection import ResourceProfileCollection
from .resource_profile_endpoint_collection import ResourceProfileEndpointCollection
from .resource_profile_endpoint_summary import ResourceProfileEndpointSummary
from .resource_profile_impacted_resource_collection import ResourceProfileImpactedResourceCollection
from .resource_profile_impacted_resource_summary import ResourceProfileImpactedResourceSummary
from .resource_profile_risk_score_aggregation_summary import ResourceProfileRiskScoreAggregationSummary
from .resource_profile_risk_score_aggregation_summary_collection import ResourceProfileRiskScoreAggregationSummaryCollection
from .resource_profile_summary import ResourceProfileSummary
from .resource_risk_score_aggregation import ResourceRiskScoreAggregation
from .resource_risk_score_aggregation_collection import ResourceRiskScoreAggregationCollection
from .resource_type_collection import ResourceTypeCollection
from .resource_type_summary import ResourceTypeSummary
from .responder_activity_collection import ResponderActivityCollection
from .responder_activity_summary import ResponderActivitySummary
from .responder_configuration import ResponderConfiguration
from .responder_execution import ResponderExecution
from .responder_execution_aggregation import ResponderExecutionAggregation
from .responder_execution_aggregation_collection import ResponderExecutionAggregationCollection
from .responder_execution_collection import ResponderExecutionCollection
from .responder_execution_summary import ResponderExecutionSummary
from .responder_execution_trend_aggregation import ResponderExecutionTrendAggregation
from .responder_execution_trend_aggregation_collection import ResponderExecutionTrendAggregationCollection
from .responder_recipe import ResponderRecipe
from .responder_recipe_collection import ResponderRecipeCollection
from .responder_recipe_responder_rule import ResponderRecipeResponderRule
from .responder_recipe_responder_rule_collection import ResponderRecipeResponderRuleCollection
from .responder_recipe_responder_rule_summary import ResponderRecipeResponderRuleSummary
from .responder_recipe_summary import ResponderRecipeSummary
from .responder_rule import ResponderRule
from .responder_rule_collection import ResponderRuleCollection
from .responder_rule_details import ResponderRuleDetails
from .responder_rule_execution_details import ResponderRuleExecutionDetails
from .responder_rule_summary import ResponderRuleSummary
from .risk_score_aggregation import RiskScoreAggregation
from .risk_score_aggregation_collection import RiskScoreAggregationCollection
from .rule_summary import RuleSummary
from .security_policy import SecurityPolicy
from .security_policy_collection import SecurityPolicyCollection
from .security_policy_summary import SecurityPolicySummary
from .security_recipe import SecurityRecipe
from .security_recipe_collection import SecurityRecipeCollection
from .security_recipe_summary import SecurityRecipeSummary
from .security_score_aggregation import SecurityScoreAggregation
from .security_score_aggregation_collection import SecurityScoreAggregationCollection
from .security_score_trend_aggregation import SecurityScoreTrendAggregation
from .security_score_trend_aggregation_collection import SecurityScoreTrendAggregationCollection
from .security_zone import SecurityZone
from .security_zone_collection import SecurityZoneCollection
from .security_zone_summary import SecurityZoneSummary
from .security_zone_target_details import SecurityZoneTargetDetails
from .service_type_summary import ServiceTypeSummary
from .sighting import Sighting
from .sighting_collection import SightingCollection
from .sighting_endpoint_collection import SightingEndpointCollection
from .sighting_endpoint_summary import SightingEndpointSummary
from .sighting_impacted_resource_collection import SightingImpactedResourceCollection
from .sighting_impacted_resource_summary import SightingImpactedResourceSummary
from .sighting_summary import SightingSummary
from .sighting_type import SightingType
from .simple_condition import SimpleCondition
from .skip_bulk_responder_execution_details import SkipBulkResponderExecutionDetails
from .tactic_collection import TacticCollection
from .tactic_summary import TacticSummary
from .target import Target
from .target_collection import TargetCollection
from .target_details import TargetDetails
from .target_detector_details import TargetDetectorDetails
from .target_detector_recipe import TargetDetectorRecipe
from .target_detector_recipe_collection import TargetDetectorRecipeCollection
from .target_detector_recipe_detector_rule import TargetDetectorRecipeDetectorRule
from .target_detector_recipe_detector_rule_collection import TargetDetectorRecipeDetectorRuleCollection
from .target_detector_recipe_detector_rule_summary import TargetDetectorRecipeDetectorRuleSummary
from .target_detector_recipe_summary import TargetDetectorRecipeSummary
from .target_ids_selected import TargetIdsSelected
from .target_resource_types_selected import TargetResourceTypesSelected
from .target_responder_recipe import TargetResponderRecipe
from .target_responder_recipe_collection import TargetResponderRecipeCollection
from .target_responder_recipe_responder_rule import TargetResponderRecipeResponderRule
from .target_responder_recipe_responder_rule_collection import TargetResponderRecipeResponderRuleCollection
from .target_responder_recipe_responder_rule_summary import TargetResponderRecipeResponderRuleSummary
from .target_responder_recipe_summary import TargetResponderRecipeSummary
from .target_selected import TargetSelected
from .target_summary import TargetSummary
from .technique_collection import TechniqueCollection
from .technique_summary import TechniqueSummary
from .trigger_responder_details import TriggerResponderDetails
from .update_bulk_problem_status_details import UpdateBulkProblemStatusDetails
from .update_configuration_details import UpdateConfigurationDetails
from .update_data_mask_rule_details import UpdateDataMaskRuleDetails
from .update_data_source_details import UpdateDataSourceDetails
from .update_detector_recipe_details import UpdateDetectorRecipeDetails
from .update_detector_recipe_detector_rule import UpdateDetectorRecipeDetectorRule
from .update_detector_recipe_detector_rule_details import UpdateDetectorRecipeDetectorRuleDetails
from .update_detector_rule_details import UpdateDetectorRuleDetails
from .update_managed_list_details import UpdateManagedListDetails
from .update_problem_status_details import UpdateProblemStatusDetails
from .update_responder_recipe_details import UpdateResponderRecipeDetails
from .update_responder_recipe_responder_rule import UpdateResponderRecipeResponderRule
from .update_responder_recipe_responder_rule_details import UpdateResponderRecipeResponderRuleDetails
from .update_responder_rule_details import UpdateResponderRuleDetails
from .update_security_policy_details import UpdateSecurityPolicyDetails
from .update_security_recipe_details import UpdateSecurityRecipeDetails
from .update_security_zone_details import UpdateSecurityZoneDetails
from .update_target_details import UpdateTargetDetails
from .update_target_detector_recipe import UpdateTargetDetectorRecipe
from .update_target_detector_recipe_details import UpdateTargetDetectorRecipeDetails
from .update_target_detector_recipe_detector_rule_details import UpdateTargetDetectorRecipeDetectorRuleDetails
from .update_target_detector_rule_details import UpdateTargetDetectorRuleDetails
from .update_target_recipe_detector_rule_details import UpdateTargetRecipeDetectorRuleDetails
from .update_target_recipe_responder_rule_details import UpdateTargetRecipeResponderRuleDetails
from .update_target_responder_recipe import UpdateTargetResponderRecipe
from .update_target_responder_recipe_details import UpdateTargetResponderRecipeDetails
from .update_target_responder_recipe_responder_rule_details import UpdateTargetResponderRecipeResponderRuleDetails
from .update_target_responder_rule_details import UpdateTargetResponderRuleDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for cloud_guard services.
cloud_guard_type_mapping = {
    "AbsoluteTimeStartPolicy": AbsoluteTimeStartPolicy,
    "ActivityProblemAggregation": ActivityProblemAggregation,
    "ActivityProblemAggregationCollection": ActivityProblemAggregationCollection,
    "AddCompartmentDetails": AddCompartmentDetails,
    "AllTargetsSelected": AllTargetsSelected,
    "AttachTargetDetectorRecipeDetails": AttachTargetDetectorRecipeDetails,
    "AttachTargetResponderRecipeDetails": AttachTargetResponderRecipeDetails,
    "CandidateResponderRule": CandidateResponderRule,
    "ChangeDataSourceCompartmentDetails": ChangeDataSourceCompartmentDetails,
    "ChangeDetectorRecipeCompartmentDetails": ChangeDetectorRecipeCompartmentDetails,
    "ChangeManagedListCompartmentDetails": ChangeManagedListCompartmentDetails,
    "ChangeResponderRecipeCompartmentDetails": ChangeResponderRecipeCompartmentDetails,
    "ChangeSecurityPolicyCompartmentDetails": ChangeSecurityPolicyCompartmentDetails,
    "ChangeSecurityRecipeCompartmentDetails": ChangeSecurityRecipeCompartmentDetails,
    "ChangeSecurityZoneCompartmentDetails": ChangeSecurityZoneCompartmentDetails,
    "CompositeCondition": CompositeCondition,
    "Condition": Condition,
    "ConditionGroup": ConditionGroup,
    "ConditionMetadataType": ConditionMetadataType,
    "ConditionMetadataTypeCollection": ConditionMetadataTypeCollection,
    "ConditionMetadataTypeSummary": ConditionMetadataTypeSummary,
    "ConditionOperator": ConditionOperator,
    "ConfigValue": ConfigValue,
    "Configuration": Configuration,
    "ContinuousQueryStartPolicy": ContinuousQueryStartPolicy,
    "CreateDataMaskRuleDetails": CreateDataMaskRuleDetails,
    "CreateDataSourceDetails": CreateDataSourceDetails,
    "CreateDetectorRecipeDetails": CreateDetectorRecipeDetails,
    "CreateDetectorRecipeDetectorRuleDetails": CreateDetectorRecipeDetectorRuleDetails,
    "CreateDetectorRuleDetails": CreateDetectorRuleDetails,
    "CreateManagedListDetails": CreateManagedListDetails,
    "CreateResponderRecipeDetails": CreateResponderRecipeDetails,
    "CreateSecurityPolicyDetails": CreateSecurityPolicyDetails,
    "CreateSecurityRecipeDetails": CreateSecurityRecipeDetails,
    "CreateSecurityZoneDetails": CreateSecurityZoneDetails,
    "CreateTargetDetails": CreateTargetDetails,
    "CreateTargetDetectorRecipeDetails": CreateTargetDetectorRecipeDetails,
    "CreateTargetResponderRecipeDetails": CreateTargetResponderRecipeDetails,
    "DataMaskRule": DataMaskRule,
    "DataMaskRuleCollection": DataMaskRuleCollection,
    "DataMaskRuleSummary": DataMaskRuleSummary,
    "DataSource": DataSource,
    "DataSourceCollection": DataSourceCollection,
    "DataSourceDetails": DataSourceDetails,
    "DataSourceEventCollection": DataSourceEventCollection,
    "DataSourceEventInfo": DataSourceEventInfo,
    "DataSourceEventSummary": DataSourceEventSummary,
    "DataSourceMappingInfo": DataSourceMappingInfo,
    "DataSourceSummary": DataSourceSummary,
    "DataSourceSummaryDetails": DataSourceSummaryDetails,
    "Detector": Detector,
    "DetectorCollection": DetectorCollection,
    "DetectorConfiguration": DetectorConfiguration,
    "DetectorDetails": DetectorDetails,
    "DetectorRecipe": DetectorRecipe,
    "DetectorRecipeCollection": DetectorRecipeCollection,
    "DetectorRecipeDetectorRule": DetectorRecipeDetectorRule,
    "DetectorRecipeDetectorRuleCollection": DetectorRecipeDetectorRuleCollection,
    "DetectorRecipeDetectorRuleSummary": DetectorRecipeDetectorRuleSummary,
    "DetectorRecipeSummary": DetectorRecipeSummary,
    "DetectorRule": DetectorRule,
    "DetectorRuleCollection": DetectorRuleCollection,
    "DetectorRuleSummary": DetectorRuleSummary,
    "DetectorSummary": DetectorSummary,
    "EntitiesMapping": EntitiesMapping,
    "EntityDetails": EntityDetails,
    "ExecuteResponderExecutionDetails": ExecuteResponderExecutionDetails,
    "GeographicalLocation": GeographicalLocation,
    "ImpactedResourceCollection": ImpactedResourceCollection,
    "ImpactedResourceSummary": ImpactedResourceSummary,
    "InsightTypeLoggingQueryDetails": InsightTypeLoggingQueryDetails,
    "LoggingEventInfo": LoggingEventInfo,
    "LoggingQueryDataSourceDetails": LoggingQueryDataSourceDetails,
    "LoggingQueryDataSourceSummaryDetails": LoggingQueryDataSourceSummaryDetails,
    "LoggingQueryDetails": LoggingQueryDetails,
    "ManagedList": ManagedList,
    "ManagedListCollection": ManagedListCollection,
    "ManagedListSummary": ManagedListSummary,
    "ManagedListTypeCollection": ManagedListTypeCollection,
    "ManagedListTypeSummary": ManagedListTypeSummary,
    "NoDelayStartPolicy": NoDelayStartPolicy,
    "OperatorSummary": OperatorSummary,
    "PolicyCollection": PolicyCollection,
    "PolicySummary": PolicySummary,
    "PoliticalLocation": PoliticalLocation,
    "Problem": Problem,
    "ProblemAggregation": ProblemAggregation,
    "ProblemAggregationCollection": ProblemAggregationCollection,
    "ProblemCollection": ProblemCollection,
    "ProblemEndpointCollection": ProblemEndpointCollection,
    "ProblemEndpointSummary": ProblemEndpointSummary,
    "ProblemEntityCollection": ProblemEntityCollection,
    "ProblemEntitySummary": ProblemEntitySummary,
    "ProblemHistoryCollection": ProblemHistoryCollection,
    "ProblemHistorySummary": ProblemHistorySummary,
    "ProblemSummary": ProblemSummary,
    "ProblemTrendAggregation": ProblemTrendAggregation,
    "ProblemTrendAggregationCollection": ProblemTrendAggregationCollection,
    "RecommendationSummary": RecommendationSummary,
    "RecommendationSummaryCollection": RecommendationSummaryCollection,
    "RegionStatusDetail": RegionStatusDetail,
    "RemoveCompartmentDetails": RemoveCompartmentDetails,
    "RequestSummarizedTrendResourceRiskScoresDetails": RequestSummarizedTrendResourceRiskScoresDetails,
    "ResourceProfile": ResourceProfile,
    "ResourceProfileCollection": ResourceProfileCollection,
    "ResourceProfileEndpointCollection": ResourceProfileEndpointCollection,
    "ResourceProfileEndpointSummary": ResourceProfileEndpointSummary,
    "ResourceProfileImpactedResourceCollection": ResourceProfileImpactedResourceCollection,
    "ResourceProfileImpactedResourceSummary": ResourceProfileImpactedResourceSummary,
    "ResourceProfileRiskScoreAggregationSummary": ResourceProfileRiskScoreAggregationSummary,
    "ResourceProfileRiskScoreAggregationSummaryCollection": ResourceProfileRiskScoreAggregationSummaryCollection,
    "ResourceProfileSummary": ResourceProfileSummary,
    "ResourceRiskScoreAggregation": ResourceRiskScoreAggregation,
    "ResourceRiskScoreAggregationCollection": ResourceRiskScoreAggregationCollection,
    "ResourceTypeCollection": ResourceTypeCollection,
    "ResourceTypeSummary": ResourceTypeSummary,
    "ResponderActivityCollection": ResponderActivityCollection,
    "ResponderActivitySummary": ResponderActivitySummary,
    "ResponderConfiguration": ResponderConfiguration,
    "ResponderExecution": ResponderExecution,
    "ResponderExecutionAggregation": ResponderExecutionAggregation,
    "ResponderExecutionAggregationCollection": ResponderExecutionAggregationCollection,
    "ResponderExecutionCollection": ResponderExecutionCollection,
    "ResponderExecutionSummary": ResponderExecutionSummary,
    "ResponderExecutionTrendAggregation": ResponderExecutionTrendAggregation,
    "ResponderExecutionTrendAggregationCollection": ResponderExecutionTrendAggregationCollection,
    "ResponderRecipe": ResponderRecipe,
    "ResponderRecipeCollection": ResponderRecipeCollection,
    "ResponderRecipeResponderRule": ResponderRecipeResponderRule,
    "ResponderRecipeResponderRuleCollection": ResponderRecipeResponderRuleCollection,
    "ResponderRecipeResponderRuleSummary": ResponderRecipeResponderRuleSummary,
    "ResponderRecipeSummary": ResponderRecipeSummary,
    "ResponderRule": ResponderRule,
    "ResponderRuleCollection": ResponderRuleCollection,
    "ResponderRuleDetails": ResponderRuleDetails,
    "ResponderRuleExecutionDetails": ResponderRuleExecutionDetails,
    "ResponderRuleSummary": ResponderRuleSummary,
    "RiskScoreAggregation": RiskScoreAggregation,
    "RiskScoreAggregationCollection": RiskScoreAggregationCollection,
    "RuleSummary": RuleSummary,
    "SecurityPolicy": SecurityPolicy,
    "SecurityPolicyCollection": SecurityPolicyCollection,
    "SecurityPolicySummary": SecurityPolicySummary,
    "SecurityRecipe": SecurityRecipe,
    "SecurityRecipeCollection": SecurityRecipeCollection,
    "SecurityRecipeSummary": SecurityRecipeSummary,
    "SecurityScoreAggregation": SecurityScoreAggregation,
    "SecurityScoreAggregationCollection": SecurityScoreAggregationCollection,
    "SecurityScoreTrendAggregation": SecurityScoreTrendAggregation,
    "SecurityScoreTrendAggregationCollection": SecurityScoreTrendAggregationCollection,
    "SecurityZone": SecurityZone,
    "SecurityZoneCollection": SecurityZoneCollection,
    "SecurityZoneSummary": SecurityZoneSummary,
    "SecurityZoneTargetDetails": SecurityZoneTargetDetails,
    "ServiceTypeSummary": ServiceTypeSummary,
    "Sighting": Sighting,
    "SightingCollection": SightingCollection,
    "SightingEndpointCollection": SightingEndpointCollection,
    "SightingEndpointSummary": SightingEndpointSummary,
    "SightingImpactedResourceCollection": SightingImpactedResourceCollection,
    "SightingImpactedResourceSummary": SightingImpactedResourceSummary,
    "SightingSummary": SightingSummary,
    "SightingType": SightingType,
    "SimpleCondition": SimpleCondition,
    "SkipBulkResponderExecutionDetails": SkipBulkResponderExecutionDetails,
    "TacticCollection": TacticCollection,
    "TacticSummary": TacticSummary,
    "Target": Target,
    "TargetCollection": TargetCollection,
    "TargetDetails": TargetDetails,
    "TargetDetectorDetails": TargetDetectorDetails,
    "TargetDetectorRecipe": TargetDetectorRecipe,
    "TargetDetectorRecipeCollection": TargetDetectorRecipeCollection,
    "TargetDetectorRecipeDetectorRule": TargetDetectorRecipeDetectorRule,
    "TargetDetectorRecipeDetectorRuleCollection": TargetDetectorRecipeDetectorRuleCollection,
    "TargetDetectorRecipeDetectorRuleSummary": TargetDetectorRecipeDetectorRuleSummary,
    "TargetDetectorRecipeSummary": TargetDetectorRecipeSummary,
    "TargetIdsSelected": TargetIdsSelected,
    "TargetResourceTypesSelected": TargetResourceTypesSelected,
    "TargetResponderRecipe": TargetResponderRecipe,
    "TargetResponderRecipeCollection": TargetResponderRecipeCollection,
    "TargetResponderRecipeResponderRule": TargetResponderRecipeResponderRule,
    "TargetResponderRecipeResponderRuleCollection": TargetResponderRecipeResponderRuleCollection,
    "TargetResponderRecipeResponderRuleSummary": TargetResponderRecipeResponderRuleSummary,
    "TargetResponderRecipeSummary": TargetResponderRecipeSummary,
    "TargetSelected": TargetSelected,
    "TargetSummary": TargetSummary,
    "TechniqueCollection": TechniqueCollection,
    "TechniqueSummary": TechniqueSummary,
    "TriggerResponderDetails": TriggerResponderDetails,
    "UpdateBulkProblemStatusDetails": UpdateBulkProblemStatusDetails,
    "UpdateConfigurationDetails": UpdateConfigurationDetails,
    "UpdateDataMaskRuleDetails": UpdateDataMaskRuleDetails,
    "UpdateDataSourceDetails": UpdateDataSourceDetails,
    "UpdateDetectorRecipeDetails": UpdateDetectorRecipeDetails,
    "UpdateDetectorRecipeDetectorRule": UpdateDetectorRecipeDetectorRule,
    "UpdateDetectorRecipeDetectorRuleDetails": UpdateDetectorRecipeDetectorRuleDetails,
    "UpdateDetectorRuleDetails": UpdateDetectorRuleDetails,
    "UpdateManagedListDetails": UpdateManagedListDetails,
    "UpdateProblemStatusDetails": UpdateProblemStatusDetails,
    "UpdateResponderRecipeDetails": UpdateResponderRecipeDetails,
    "UpdateResponderRecipeResponderRule": UpdateResponderRecipeResponderRule,
    "UpdateResponderRecipeResponderRuleDetails": UpdateResponderRecipeResponderRuleDetails,
    "UpdateResponderRuleDetails": UpdateResponderRuleDetails,
    "UpdateSecurityPolicyDetails": UpdateSecurityPolicyDetails,
    "UpdateSecurityRecipeDetails": UpdateSecurityRecipeDetails,
    "UpdateSecurityZoneDetails": UpdateSecurityZoneDetails,
    "UpdateTargetDetails": UpdateTargetDetails,
    "UpdateTargetDetectorRecipe": UpdateTargetDetectorRecipe,
    "UpdateTargetDetectorRecipeDetails": UpdateTargetDetectorRecipeDetails,
    "UpdateTargetDetectorRecipeDetectorRuleDetails": UpdateTargetDetectorRecipeDetectorRuleDetails,
    "UpdateTargetDetectorRuleDetails": UpdateTargetDetectorRuleDetails,
    "UpdateTargetRecipeDetectorRuleDetails": UpdateTargetRecipeDetectorRuleDetails,
    "UpdateTargetRecipeResponderRuleDetails": UpdateTargetRecipeResponderRuleDetails,
    "UpdateTargetResponderRecipe": UpdateTargetResponderRecipe,
    "UpdateTargetResponderRecipeDetails": UpdateTargetResponderRecipeDetails,
    "UpdateTargetResponderRecipeResponderRuleDetails": UpdateTargetResponderRecipeResponderRuleDetails,
    "UpdateTargetResponderRuleDetails": UpdateTargetResponderRuleDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}