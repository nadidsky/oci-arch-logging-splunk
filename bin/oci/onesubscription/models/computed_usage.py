# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputedUsage(object):
    """
    Computed Usage Summary object
    """

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "PROMOTION"
    TYPE_PROMOTION = "PROMOTION"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "DO_NOT_BILL"
    TYPE_DO_NOT_BILL = "DO_NOT_BILL"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "USAGE"
    TYPE_USAGE = "USAGE"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "COMMIT"
    TYPE_COMMIT = "COMMIT"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "OVERAGE"
    TYPE_OVERAGE = "OVERAGE"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "PAY_AS_YOU_GO"
    TYPE_PAY_AS_YOU_GO = "PAY_AS_YOU_GO"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "MONTHLY_MINIMUM"
    TYPE_MONTHLY_MINIMUM = "MONTHLY_MINIMUM"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "DELAYED_USAGE_INVOICE_TIMING"
    TYPE_DELAYED_USAGE_INVOICE_TIMING = "DELAYED_USAGE_INVOICE_TIMING"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "DELAYED_USAGE_COMMITMENT_EXP"
    TYPE_DELAYED_USAGE_COMMITMENT_EXP = "DELAYED_USAGE_COMMITMENT_EXP"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "ON_ACCOUNT_CREDIT"
    TYPE_ON_ACCOUNT_CREDIT = "ON_ACCOUNT_CREDIT"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "SERVICE_CREDIT"
    TYPE_SERVICE_CREDIT = "SERVICE_CREDIT"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "COMMITMENT_EXPIRATION"
    TYPE_COMMITMENT_EXPIRATION = "COMMITMENT_EXPIRATION"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "FUNDED_ALLOCATION"
    TYPE_FUNDED_ALLOCATION = "FUNDED_ALLOCATION"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "DONOT_BILL_USAGE_POST_TERMINATION"
    TYPE_DONOT_BILL_USAGE_POST_TERMINATION = "DONOT_BILL_USAGE_POST_TERMINATION"

    #: A constant which can be used with the type property of a ComputedUsage.
    #: This constant has a value of "DELAYED_USAGE_POST_TERMINATION"
    TYPE_DELAYED_USAGE_POST_TERMINATION = "DELAYED_USAGE_POST_TERMINATION"

    def __init__(self, **kwargs):
        """
        Initializes a new ComputedUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_created:
            The value to assign to the time_created property of this ComputedUsage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ComputedUsage.
        :type time_updated: datetime

        :param parent_subscribed_service_id:
            The value to assign to the parent_subscribed_service_id property of this ComputedUsage.
        :type parent_subscribed_service_id: str

        :param parent_product:
            The value to assign to the parent_product property of this ComputedUsage.
        :type parent_product: oci.onesubscription.models.ComputedUsageProduct

        :param plan_number:
            The value to assign to the plan_number property of this ComputedUsage.
        :type plan_number: str

        :param currency_code:
            The value to assign to the currency_code property of this ComputedUsage.
        :type currency_code: str

        :param rate_card_tierd_id:
            The value to assign to the rate_card_tierd_id property of this ComputedUsage.
        :type rate_card_tierd_id: str

        :param rate_card_id:
            The value to assign to the rate_card_id property of this ComputedUsage.
        :type rate_card_id: str

        :param compute_source:
            The value to assign to the compute_source property of this ComputedUsage.
        :type compute_source: str

        :param data_center:
            The value to assign to the data_center property of this ComputedUsage.
        :type data_center: str

        :param mqs_message_id:
            The value to assign to the mqs_message_id property of this ComputedUsage.
        :type mqs_message_id: str

        :param id:
            The value to assign to the id property of this ComputedUsage.
        :type id: str

        :param quantity:
            The value to assign to the quantity property of this ComputedUsage.
        :type quantity: str

        :param usage_number:
            The value to assign to the usage_number property of this ComputedUsage.
        :type usage_number: str

        :param original_usage_number:
            The value to assign to the original_usage_number property of this ComputedUsage.
        :type original_usage_number: str

        :param commitment_service_id:
            The value to assign to the commitment_service_id property of this ComputedUsage.
        :type commitment_service_id: str

        :param is_invoiced:
            The value to assign to the is_invoiced property of this ComputedUsage.
        :type is_invoiced: bool

        :param type:
            The value to assign to the type property of this ComputedUsage.
            Allowed values for this property are: "PROMOTION", "DO_NOT_BILL", "USAGE", "COMMIT", "OVERAGE", "PAY_AS_YOU_GO", "MONTHLY_MINIMUM", "DELAYED_USAGE_INVOICE_TIMING", "DELAYED_USAGE_COMMITMENT_EXP", "ON_ACCOUNT_CREDIT", "SERVICE_CREDIT", "COMMITMENT_EXPIRATION", "FUNDED_ALLOCATION", "DONOT_BILL_USAGE_POST_TERMINATION", "DELAYED_USAGE_POST_TERMINATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param time_of_arrival:
            The value to assign to the time_of_arrival property of this ComputedUsage.
        :type time_of_arrival: datetime

        :param time_metered_on:
            The value to assign to the time_metered_on property of this ComputedUsage.
        :type time_metered_on: datetime

        :param net_unit_price:
            The value to assign to the net_unit_price property of this ComputedUsage.
        :type net_unit_price: str

        :param cost_rounded:
            The value to assign to the cost_rounded property of this ComputedUsage.
        :type cost_rounded: str

        :param cost:
            The value to assign to the cost property of this ComputedUsage.
        :type cost: str

        :param product:
            The value to assign to the product property of this ComputedUsage.
        :type product: oci.onesubscription.models.ComputedUsageProduct

        :param unit_of_measure:
            The value to assign to the unit_of_measure property of this ComputedUsage.
        :type unit_of_measure: str

        """
        self.swagger_types = {
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'parent_subscribed_service_id': 'str',
            'parent_product': 'ComputedUsageProduct',
            'plan_number': 'str',
            'currency_code': 'str',
            'rate_card_tierd_id': 'str',
            'rate_card_id': 'str',
            'compute_source': 'str',
            'data_center': 'str',
            'mqs_message_id': 'str',
            'id': 'str',
            'quantity': 'str',
            'usage_number': 'str',
            'original_usage_number': 'str',
            'commitment_service_id': 'str',
            'is_invoiced': 'bool',
            'type': 'str',
            'time_of_arrival': 'datetime',
            'time_metered_on': 'datetime',
            'net_unit_price': 'str',
            'cost_rounded': 'str',
            'cost': 'str',
            'product': 'ComputedUsageProduct',
            'unit_of_measure': 'str'
        }

        self.attribute_map = {
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'parent_subscribed_service_id': 'parentSubscribedServiceId',
            'parent_product': 'parentProduct',
            'plan_number': 'planNumber',
            'currency_code': 'currencyCode',
            'rate_card_tierd_id': 'rateCardTierdId',
            'rate_card_id': 'rateCardId',
            'compute_source': 'computeSource',
            'data_center': 'dataCenter',
            'mqs_message_id': 'mqsMessageId',
            'id': 'id',
            'quantity': 'quantity',
            'usage_number': 'usageNumber',
            'original_usage_number': 'originalUsageNumber',
            'commitment_service_id': 'commitmentServiceId',
            'is_invoiced': 'isInvoiced',
            'type': 'type',
            'time_of_arrival': 'timeOfArrival',
            'time_metered_on': 'timeMeteredOn',
            'net_unit_price': 'netUnitPrice',
            'cost_rounded': 'costRounded',
            'cost': 'cost',
            'product': 'product',
            'unit_of_measure': 'unitOfMeasure'
        }

        self._time_created = None
        self._time_updated = None
        self._parent_subscribed_service_id = None
        self._parent_product = None
        self._plan_number = None
        self._currency_code = None
        self._rate_card_tierd_id = None
        self._rate_card_id = None
        self._compute_source = None
        self._data_center = None
        self._mqs_message_id = None
        self._id = None
        self._quantity = None
        self._usage_number = None
        self._original_usage_number = None
        self._commitment_service_id = None
        self._is_invoiced = None
        self._type = None
        self._time_of_arrival = None
        self._time_metered_on = None
        self._net_unit_price = None
        self._cost_rounded = None
        self._cost = None
        self._product = None
        self._unit_of_measure = None

    @property
    def time_created(self):
        """
        Gets the time_created of this ComputedUsage.
        Computed Usage created time, expressed in RFC 3339 timestamp format.


        :return: The time_created of this ComputedUsage.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ComputedUsage.
        Computed Usage created time, expressed in RFC 3339 timestamp format.


        :param time_created: The time_created of this ComputedUsage.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ComputedUsage.
        Computed Usage updated time, expressed in RFC 3339 timestamp format.


        :return: The time_updated of this ComputedUsage.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ComputedUsage.
        Computed Usage updated time, expressed in RFC 3339 timestamp format.


        :param time_updated: The time_updated of this ComputedUsage.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def parent_subscribed_service_id(self):
        """
        Gets the parent_subscribed_service_id of this ComputedUsage.
        Subscribed service line parent id


        :return: The parent_subscribed_service_id of this ComputedUsage.
        :rtype: str
        """
        return self._parent_subscribed_service_id

    @parent_subscribed_service_id.setter
    def parent_subscribed_service_id(self, parent_subscribed_service_id):
        """
        Sets the parent_subscribed_service_id of this ComputedUsage.
        Subscribed service line parent id


        :param parent_subscribed_service_id: The parent_subscribed_service_id of this ComputedUsage.
        :type: str
        """
        self._parent_subscribed_service_id = parent_subscribed_service_id

    @property
    def parent_product(self):
        """
        Gets the parent_product of this ComputedUsage.

        :return: The parent_product of this ComputedUsage.
        :rtype: oci.onesubscription.models.ComputedUsageProduct
        """
        return self._parent_product

    @parent_product.setter
    def parent_product(self, parent_product):
        """
        Sets the parent_product of this ComputedUsage.

        :param parent_product: The parent_product of this ComputedUsage.
        :type: oci.onesubscription.models.ComputedUsageProduct
        """
        self._parent_product = parent_product

    @property
    def plan_number(self):
        """
        Gets the plan_number of this ComputedUsage.
        Subscription plan number


        :return: The plan_number of this ComputedUsage.
        :rtype: str
        """
        return self._plan_number

    @plan_number.setter
    def plan_number(self, plan_number):
        """
        Sets the plan_number of this ComputedUsage.
        Subscription plan number


        :param plan_number: The plan_number of this ComputedUsage.
        :type: str
        """
        self._plan_number = plan_number

    @property
    def currency_code(self):
        """
        Gets the currency_code of this ComputedUsage.
        Currency code


        :return: The currency_code of this ComputedUsage.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this ComputedUsage.
        Currency code


        :param currency_code: The currency_code of this ComputedUsage.
        :type: str
        """
        self._currency_code = currency_code

    @property
    def rate_card_tierd_id(self):
        """
        Gets the rate_card_tierd_id of this ComputedUsage.
        References the tier in the ratecard for that usage (OCI will be using the same reference to cross-reference for correctness on the usage csv report), comes from Entity OBSCNTR_IPT_PRODUCTTIER.


        :return: The rate_card_tierd_id of this ComputedUsage.
        :rtype: str
        """
        return self._rate_card_tierd_id

    @rate_card_tierd_id.setter
    def rate_card_tierd_id(self, rate_card_tierd_id):
        """
        Sets the rate_card_tierd_id of this ComputedUsage.
        References the tier in the ratecard for that usage (OCI will be using the same reference to cross-reference for correctness on the usage csv report), comes from Entity OBSCNTR_IPT_PRODUCTTIER.


        :param rate_card_tierd_id: The rate_card_tierd_id of this ComputedUsage.
        :type: str
        """
        self._rate_card_tierd_id = rate_card_tierd_id

    @property
    def rate_card_id(self):
        """
        Gets the rate_card_id of this ComputedUsage.
        Ratecard Id at subscribed service level


        :return: The rate_card_id of this ComputedUsage.
        :rtype: str
        """
        return self._rate_card_id

    @rate_card_id.setter
    def rate_card_id(self, rate_card_id):
        """
        Sets the rate_card_id of this ComputedUsage.
        Ratecard Id at subscribed service level


        :param rate_card_id: The rate_card_id of this ComputedUsage.
        :type: str
        """
        self._rate_card_id = rate_card_id

    @property
    def compute_source(self):
        """
        Gets the compute_source of this ComputedUsage.
        SPM Internal compute records source .


        :return: The compute_source of this ComputedUsage.
        :rtype: str
        """
        return self._compute_source

    @compute_source.setter
    def compute_source(self, compute_source):
        """
        Sets the compute_source of this ComputedUsage.
        SPM Internal compute records source .


        :param compute_source: The compute_source of this ComputedUsage.
        :type: str
        """
        self._compute_source = compute_source

    @property
    def data_center(self):
        """
        Gets the data_center of this ComputedUsage.
        Data Center Attribute as sent by MQS to SPM.


        :return: The data_center of this ComputedUsage.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """
        Sets the data_center of this ComputedUsage.
        Data Center Attribute as sent by MQS to SPM.


        :param data_center: The data_center of this ComputedUsage.
        :type: str
        """
        self._data_center = data_center

    @property
    def mqs_message_id(self):
        """
        Gets the mqs_message_id of this ComputedUsage.
        MQS Identfier send to SPM , SPM does not transform this attribute and is received as is.


        :return: The mqs_message_id of this ComputedUsage.
        :rtype: str
        """
        return self._mqs_message_id

    @mqs_message_id.setter
    def mqs_message_id(self, mqs_message_id):
        """
        Sets the mqs_message_id of this ComputedUsage.
        MQS Identfier send to SPM , SPM does not transform this attribute and is received as is.


        :param mqs_message_id: The mqs_message_id of this ComputedUsage.
        :type: str
        """
        self._mqs_message_id = mqs_message_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ComputedUsage.
        SPM Internal computed usage Id , 32 character string


        :return: The id of this ComputedUsage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComputedUsage.
        SPM Internal computed usage Id , 32 character string


        :param id: The id of this ComputedUsage.
        :type: str
        """
        self._id = id

    @property
    def quantity(self):
        """
        Gets the quantity of this ComputedUsage.
        Total Quantity that was used for computation


        :return: The quantity of this ComputedUsage.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this ComputedUsage.
        Total Quantity that was used for computation


        :param quantity: The quantity of this ComputedUsage.
        :type: str
        """
        self._quantity = quantity

    @property
    def usage_number(self):
        """
        Gets the usage_number of this ComputedUsage.
        SPM Internal usage Line number identifier in SPM coming from Metered Services entity.


        :return: The usage_number of this ComputedUsage.
        :rtype: str
        """
        return self._usage_number

    @usage_number.setter
    def usage_number(self, usage_number):
        """
        Sets the usage_number of this ComputedUsage.
        SPM Internal usage Line number identifier in SPM coming from Metered Services entity.


        :param usage_number: The usage_number of this ComputedUsage.
        :type: str
        """
        self._usage_number = usage_number

    @property
    def original_usage_number(self):
        """
        Gets the original_usage_number of this ComputedUsage.
        SPM Internal Original usage Line number identifier in SPM coming from Metered Services entity.


        :return: The original_usage_number of this ComputedUsage.
        :rtype: str
        """
        return self._original_usage_number

    @original_usage_number.setter
    def original_usage_number(self, original_usage_number):
        """
        Sets the original_usage_number of this ComputedUsage.
        SPM Internal Original usage Line number identifier in SPM coming from Metered Services entity.


        :param original_usage_number: The original_usage_number of this ComputedUsage.
        :type: str
        """
        self._original_usage_number = original_usage_number

    @property
    def commitment_service_id(self):
        """
        Gets the commitment_service_id of this ComputedUsage.
        Subscribed service commitmentId.


        :return: The commitment_service_id of this ComputedUsage.
        :rtype: str
        """
        return self._commitment_service_id

    @commitment_service_id.setter
    def commitment_service_id(self, commitment_service_id):
        """
        Sets the commitment_service_id of this ComputedUsage.
        Subscribed service commitmentId.


        :param commitment_service_id: The commitment_service_id of this ComputedUsage.
        :type: str
        """
        self._commitment_service_id = commitment_service_id

    @property
    def is_invoiced(self):
        """
        Gets the is_invoiced of this ComputedUsage.
        Invoicing status for the aggregated compute usage


        :return: The is_invoiced of this ComputedUsage.
        :rtype: bool
        """
        return self._is_invoiced

    @is_invoiced.setter
    def is_invoiced(self, is_invoiced):
        """
        Sets the is_invoiced of this ComputedUsage.
        Invoicing status for the aggregated compute usage


        :param is_invoiced: The is_invoiced of this ComputedUsage.
        :type: bool
        """
        self._is_invoiced = is_invoiced

    @property
    def type(self):
        """
        Gets the type of this ComputedUsage.
        Usage compute type in SPM.

        Allowed values for this property are: "PROMOTION", "DO_NOT_BILL", "USAGE", "COMMIT", "OVERAGE", "PAY_AS_YOU_GO", "MONTHLY_MINIMUM", "DELAYED_USAGE_INVOICE_TIMING", "DELAYED_USAGE_COMMITMENT_EXP", "ON_ACCOUNT_CREDIT", "SERVICE_CREDIT", "COMMITMENT_EXPIRATION", "FUNDED_ALLOCATION", "DONOT_BILL_USAGE_POST_TERMINATION", "DELAYED_USAGE_POST_TERMINATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ComputedUsage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ComputedUsage.
        Usage compute type in SPM.


        :param type: The type of this ComputedUsage.
        :type: str
        """
        allowed_values = ["PROMOTION", "DO_NOT_BILL", "USAGE", "COMMIT", "OVERAGE", "PAY_AS_YOU_GO", "MONTHLY_MINIMUM", "DELAYED_USAGE_INVOICE_TIMING", "DELAYED_USAGE_COMMITMENT_EXP", "ON_ACCOUNT_CREDIT", "SERVICE_CREDIT", "COMMITMENT_EXPIRATION", "FUNDED_ALLOCATION", "DONOT_BILL_USAGE_POST_TERMINATION", "DELAYED_USAGE_POST_TERMINATION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def time_of_arrival(self):
        """
        Gets the time_of_arrival of this ComputedUsage.
        Usae computation date, expressed in RFC 3339 timestamp format.


        :return: The time_of_arrival of this ComputedUsage.
        :rtype: datetime
        """
        return self._time_of_arrival

    @time_of_arrival.setter
    def time_of_arrival(self, time_of_arrival):
        """
        Sets the time_of_arrival of this ComputedUsage.
        Usae computation date, expressed in RFC 3339 timestamp format.


        :param time_of_arrival: The time_of_arrival of this ComputedUsage.
        :type: datetime
        """
        self._time_of_arrival = time_of_arrival

    @property
    def time_metered_on(self):
        """
        Gets the time_metered_on of this ComputedUsage.
        Metered Service date, expressed in RFC 3339 timestamp format.


        :return: The time_metered_on of this ComputedUsage.
        :rtype: datetime
        """
        return self._time_metered_on

    @time_metered_on.setter
    def time_metered_on(self, time_metered_on):
        """
        Sets the time_metered_on of this ComputedUsage.
        Metered Service date, expressed in RFC 3339 timestamp format.


        :param time_metered_on: The time_metered_on of this ComputedUsage.
        :type: datetime
        """
        self._time_metered_on = time_metered_on

    @property
    def net_unit_price(self):
        """
        Gets the net_unit_price of this ComputedUsage.
        Net Unit Price for the product in consideration, price actual.


        :return: The net_unit_price of this ComputedUsage.
        :rtype: str
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this ComputedUsage.
        Net Unit Price for the product in consideration, price actual.


        :param net_unit_price: The net_unit_price of this ComputedUsage.
        :type: str
        """
        self._net_unit_price = net_unit_price

    @property
    def cost_rounded(self):
        """
        Gets the cost_rounded of this ComputedUsage.
        Computed Line Amount rounded.


        :return: The cost_rounded of this ComputedUsage.
        :rtype: str
        """
        return self._cost_rounded

    @cost_rounded.setter
    def cost_rounded(self, cost_rounded):
        """
        Sets the cost_rounded of this ComputedUsage.
        Computed Line Amount rounded.


        :param cost_rounded: The cost_rounded of this ComputedUsage.
        :type: str
        """
        self._cost_rounded = cost_rounded

    @property
    def cost(self):
        """
        Gets the cost of this ComputedUsage.
        Computed Line Amount not rounded


        :return: The cost of this ComputedUsage.
        :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this ComputedUsage.
        Computed Line Amount not rounded


        :param cost: The cost of this ComputedUsage.
        :type: str
        """
        self._cost = cost

    @property
    def product(self):
        """
        Gets the product of this ComputedUsage.

        :return: The product of this ComputedUsage.
        :rtype: oci.onesubscription.models.ComputedUsageProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this ComputedUsage.

        :param product: The product of this ComputedUsage.
        :type: oci.onesubscription.models.ComputedUsageProduct
        """
        self._product = product

    @property
    def unit_of_measure(self):
        """
        Gets the unit_of_measure of this ComputedUsage.
        Unit of Messure


        :return: The unit_of_measure of this ComputedUsage.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this ComputedUsage.
        Unit of Messure


        :param unit_of_measure: The unit_of_measure of this ComputedUsage.
        :type: str
        """
        self._unit_of_measure = unit_of_measure

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other