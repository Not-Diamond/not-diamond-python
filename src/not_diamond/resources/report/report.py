# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ReportResource", "AsyncReportResource"]


class ReportResource(SyncAPIResource):
    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return ReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return ReportResourceWithStreamingResponse(self)


class AsyncReportResource(AsyncAPIResource):
    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncReportResourceWithStreamingResponse(self)


class ReportResourceWithRawResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._report.metrics)


class AsyncReportResourceWithRawResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._report.metrics)


class ReportResourceWithStreamingResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._report.metrics)


class AsyncReportResourceWithStreamingResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._report.metrics)
