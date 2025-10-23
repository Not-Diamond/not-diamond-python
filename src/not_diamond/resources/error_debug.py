# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ErrorDebugResource", "AsyncErrorDebugResource"]


class ErrorDebugResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ErrorDebugResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return ErrorDebugResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ErrorDebugResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return ErrorDebugResourceWithStreamingResponse(self)

    def trigger_error(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Test error tracking via OpenTelemetry + Datadog"""
        return self._get(
            "/error-debug",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncErrorDebugResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncErrorDebugResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncErrorDebugResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncErrorDebugResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncErrorDebugResourceWithStreamingResponse(self)

    async def trigger_error(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Test error tracking via OpenTelemetry + Datadog"""
        return await self._get(
            "/error-debug",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ErrorDebugResourceWithRawResponse:
    def __init__(self, error_debug: ErrorDebugResource) -> None:
        self._error_debug = error_debug

        self.trigger_error = to_raw_response_wrapper(
            error_debug.trigger_error,
        )


class AsyncErrorDebugResourceWithRawResponse:
    def __init__(self, error_debug: AsyncErrorDebugResource) -> None:
        self._error_debug = error_debug

        self.trigger_error = async_to_raw_response_wrapper(
            error_debug.trigger_error,
        )


class ErrorDebugResourceWithStreamingResponse:
    def __init__(self, error_debug: ErrorDebugResource) -> None:
        self._error_debug = error_debug

        self.trigger_error = to_streamed_response_wrapper(
            error_debug.trigger_error,
        )


class AsyncErrorDebugResourceWithStreamingResponse:
    def __init__(self, error_debug: AsyncErrorDebugResource) -> None:
        self._error_debug = error_debug

        self.trigger_error = async_to_streamed_response_wrapper(
            error_debug.trigger_error,
        )
