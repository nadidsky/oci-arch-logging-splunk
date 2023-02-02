# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SpanSnapshot(object):
    """
    Definition of a span snapshot object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SpanSnapshot object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this SpanSnapshot.
        :type key: str

        :param span_name:
            The value to assign to the span_name property of this SpanSnapshot.
        :type span_name: str

        :param time_started:
            The value to assign to the time_started property of this SpanSnapshot.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this SpanSnapshot.
        :type time_ended: datetime

        :param span_snapshot_details:
            The value to assign to the span_snapshot_details property of this SpanSnapshot.
        :type span_snapshot_details: list[oci.apm_traces.models.SnapshotDetail]

        :param thread_snapshots:
            The value to assign to the thread_snapshots property of this SpanSnapshot.
        :type thread_snapshots: list[oci.apm_traces.models.ThreadSnapshot]

        :param children:
            The value to assign to the children property of this SpanSnapshot.
        :type children: list[oci.apm_traces.models.SpanSnapshot]

        """
        self.swagger_types = {
            'key': 'str',
            'span_name': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'span_snapshot_details': 'list[SnapshotDetail]',
            'thread_snapshots': 'list[ThreadSnapshot]',
            'children': 'list[SpanSnapshot]'
        }

        self.attribute_map = {
            'key': 'key',
            'span_name': 'spanName',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'span_snapshot_details': 'spanSnapshotDetails',
            'thread_snapshots': 'threadSnapshots',
            'children': 'children'
        }

        self._key = None
        self._span_name = None
        self._time_started = None
        self._time_ended = None
        self._span_snapshot_details = None
        self._thread_snapshots = None
        self._children = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this SpanSnapshot.
        Unique identifier (spanId) for the trace span.


        :return: The key of this SpanSnapshot.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SpanSnapshot.
        Unique identifier (spanId) for the trace span.


        :param key: The key of this SpanSnapshot.
        :type: str
        """
        self._key = key

    @property
    def span_name(self):
        """
        Gets the span_name of this SpanSnapshot.
        Span name associated with the trace.


        :return: The span_name of this SpanSnapshot.
        :rtype: str
        """
        return self._span_name

    @span_name.setter
    def span_name(self, span_name):
        """
        Sets the span_name of this SpanSnapshot.
        Span name associated with the trace.


        :param span_name: The span_name of this SpanSnapshot.
        :type: str
        """
        self._span_name = span_name

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this SpanSnapshot.
        Start time of the span.


        :return: The time_started of this SpanSnapshot.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this SpanSnapshot.
        Start time of the span.


        :param time_started: The time_started of this SpanSnapshot.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        **[Required]** Gets the time_ended of this SpanSnapshot.
        End time of the span.


        :return: The time_ended of this SpanSnapshot.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this SpanSnapshot.
        End time of the span.


        :param time_ended: The time_ended of this SpanSnapshot.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def span_snapshot_details(self):
        """
        Gets the span_snapshot_details of this SpanSnapshot.
        Span snapshots properties.


        :return: The span_snapshot_details of this SpanSnapshot.
        :rtype: list[oci.apm_traces.models.SnapshotDetail]
        """
        return self._span_snapshot_details

    @span_snapshot_details.setter
    def span_snapshot_details(self, span_snapshot_details):
        """
        Sets the span_snapshot_details of this SpanSnapshot.
        Span snapshots properties.


        :param span_snapshot_details: The span_snapshot_details of this SpanSnapshot.
        :type: list[oci.apm_traces.models.SnapshotDetail]
        """
        self._span_snapshot_details = span_snapshot_details

    @property
    def thread_snapshots(self):
        """
        Gets the thread_snapshots of this SpanSnapshot.
        Thread snapshots.


        :return: The thread_snapshots of this SpanSnapshot.
        :rtype: list[oci.apm_traces.models.ThreadSnapshot]
        """
        return self._thread_snapshots

    @thread_snapshots.setter
    def thread_snapshots(self, thread_snapshots):
        """
        Sets the thread_snapshots of this SpanSnapshot.
        Thread snapshots.


        :param thread_snapshots: The thread_snapshots of this SpanSnapshot.
        :type: list[oci.apm_traces.models.ThreadSnapshot]
        """
        self._thread_snapshots = thread_snapshots

    @property
    def children(self):
        """
        Gets the children of this SpanSnapshot.
        An array of child span snapshots.


        :return: The children of this SpanSnapshot.
        :rtype: list[oci.apm_traces.models.SpanSnapshot]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this SpanSnapshot.
        An array of child span snapshots.


        :param children: The children of this SpanSnapshot.
        :type: list[oci.apm_traces.models.SpanSnapshot]
        """
        self._children = children

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other