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

__all__ = ["PosthogDebugResource", "AsyncPosthogDebugResource"]


class PosthogDebugResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PosthogDebugResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return PosthogDebugResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PosthogDebugResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return PosthogDebugResourceWithStreamingResponse(self)

    def trigger(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Trigger Posthog"""
        return self._get(
            "/posthog-debug",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPosthogDebugResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPosthogDebugResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPosthogDebugResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPosthogDebugResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncPosthogDebugResourceWithStreamingResponse(self)

    async def trigger(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Trigger Posthog"""
        return await self._get(
            "/posthog-debug",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PosthogDebugResourceWithRawResponse:
    def __init__(self, posthog_debug: PosthogDebugResource) -> None:
        self._posthog_debug = posthog_debug

        self.trigger = to_raw_response_wrapper(
            posthog_debug.trigger,
        )


class AsyncPosthogDebugResourceWithRawResponse:
    def __init__(self, posthog_debug: AsyncPosthogDebugResource) -> None:
        self._posthog_debug = posthog_debug

        self.trigger = async_to_raw_response_wrapper(
            posthog_debug.trigger,
        )


class PosthogDebugResourceWithStreamingResponse:
    def __init__(self, posthog_debug: PosthogDebugResource) -> None:
        self._posthog_debug = posthog_debug

        self.trigger = to_streamed_response_wrapper(
            posthog_debug.trigger,
        )


class AsyncPosthogDebugResourceWithStreamingResponse:
    def __init__(self, posthog_debug: AsyncPosthogDebugResource) -> None:
        self._posthog_debug = posthog_debug

        self.trigger = async_to_streamed_response_wrapper(
            posthog_debug.trigger,
        )
