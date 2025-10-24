# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .report import (
    ReportResource,
    AsyncReportResource,
    ReportResourceWithRawResponse,
    AsyncReportResourceWithRawResponse,
    ReportResourceWithStreamingResponse,
    AsyncReportResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ClientResource", "AsyncClientResource"]


class ClientResource(SyncAPIResource):
    @cached_property
    def report(self) -> ReportResource:
        return ReportResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return ClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return ClientResourceWithStreamingResponse(self)


class AsyncClientResource(AsyncAPIResource):
    @cached_property
    def report(self) -> AsyncReportResource:
        return AsyncReportResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncClientResourceWithStreamingResponse(self)


class ClientResourceWithRawResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

    @cached_property
    def report(self) -> ReportResourceWithRawResponse:
        return ReportResourceWithRawResponse(self._client.report)


class AsyncClientResourceWithRawResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

    @cached_property
    def report(self) -> AsyncReportResourceWithRawResponse:
        return AsyncReportResourceWithRawResponse(self._client.report)


class ClientResourceWithStreamingResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

    @cached_property
    def report(self) -> ReportResourceWithStreamingResponse:
        return ReportResourceWithStreamingResponse(self._client.report)


class AsyncClientResourceWithStreamingResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

    @cached_property
    def report(self) -> AsyncReportResourceWithStreamingResponse:
        return AsyncReportResourceWithStreamingResponse(self._client.report)
