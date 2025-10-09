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
from ..types.adaptation_run_retrieve_costs_response import AdaptationRunRetrieveCostsResponse

__all__ = ["AdaptationRunsResource", "AsyncAdaptationRunsResource"]


class AdaptationRunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdaptationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AdaptationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdaptationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AdaptationRunsResourceWithStreamingResponse(self)

    def retrieve_costs(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptationRunRetrieveCostsResponse:
        """
        Get LLM costs for a specific adaptation run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return self._get(
            f"/v1/adaptation-runs/{adaptation_run_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptationRunRetrieveCostsResponse,
        )


class AsyncAdaptationRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdaptationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdaptationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdaptationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncAdaptationRunsResourceWithStreamingResponse(self)

    async def retrieve_costs(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptationRunRetrieveCostsResponse:
        """
        Get LLM costs for a specific adaptation run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return await self._get(
            f"/v1/adaptation-runs/{adaptation_run_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptationRunRetrieveCostsResponse,
        )


class AdaptationRunsResourceWithRawResponse:
    def __init__(self, adaptation_runs: AdaptationRunsResource) -> None:
        self._adaptation_runs = adaptation_runs

        self.retrieve_costs = to_raw_response_wrapper(
            adaptation_runs.retrieve_costs,
        )


class AsyncAdaptationRunsResourceWithRawResponse:
    def __init__(self, adaptation_runs: AsyncAdaptationRunsResource) -> None:
        self._adaptation_runs = adaptation_runs

        self.retrieve_costs = async_to_raw_response_wrapper(
            adaptation_runs.retrieve_costs,
        )


class AdaptationRunsResourceWithStreamingResponse:
    def __init__(self, adaptation_runs: AdaptationRunsResource) -> None:
        self._adaptation_runs = adaptation_runs

        self.retrieve_costs = to_streamed_response_wrapper(
            adaptation_runs.retrieve_costs,
        )


class AsyncAdaptationRunsResourceWithStreamingResponse:
    def __init__(self, adaptation_runs: AsyncAdaptationRunsResource) -> None:
        self._adaptation_runs = adaptation_runs

        self.retrieve_costs = async_to_streamed_response_wrapper(
            adaptation_runs.retrieve_costs,
        )
