# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import llm_usage_retrieve_daily_params, llm_usage_retrieve_summary_params
from ..._base_client import make_request_options
from ...types.usage_summary import UsageSummary
from ...types.admin.llm_usage_retrieve_daily_response import LlmUsageRetrieveDailyResponse

__all__ = ["LlmUsageResource", "AsyncLlmUsageResource"]


class LlmUsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LlmUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return LlmUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return LlmUsageResourceWithStreamingResponse(self)

    def retrieve_daily(
        self,
        *,
        end_date: str,
        start_date: str,
        user_id: str,
        x_token: str,
        metric: str | Omit = omit,
        subscription_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LlmUsageRetrieveDailyResponse:
        """
        Admin endpoint to get daily LLM usage data for dashboard

        If subscription_date is provided, filters out any usage before that date. This
        is used to hide pre-upgrade LLM costs when a free tier user upgrades to Starter.

        Args:
          end_date: End date in YYYY-MM-DD format

          start_date: Start date in YYYY-MM-DD format

          user_id: User ID to get usage for

          metric: Metric to aggregate: 'cost' or 'calls'

          subscription_date: Subscription date (ISO format) to filter out pre-subscription usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._get(
            "/v1/admin/llm-usage/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "user_id": user_id,
                        "metric": metric,
                        "subscription_date": subscription_date,
                    },
                    llm_usage_retrieve_daily_params.LlmUsageRetrieveDailyParams,
                ),
            ),
            cast_to=LlmUsageRetrieveDailyResponse,
        )

    def retrieve_summary(
        self,
        *,
        user_id: str,
        x_token: str,
        end_time: Optional[float] | Omit = omit,
        start_time: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageSummary:
        """
        Admin endpoint to get LLM usage summary for dashboard

        Args:
          user_id: User ID to get usage for

          end_time: End timestamp (Unix time)

          start_time: Start timestamp (Unix time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._get(
            "/v1/admin/llm-usage/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "user_id": user_id,
                        "end_time": end_time,
                        "start_time": start_time,
                    },
                    llm_usage_retrieve_summary_params.LlmUsageRetrieveSummaryParams,
                ),
            ),
            cast_to=UsageSummary,
        )


class AsyncLlmUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLlmUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLlmUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncLlmUsageResourceWithStreamingResponse(self)

    async def retrieve_daily(
        self,
        *,
        end_date: str,
        start_date: str,
        user_id: str,
        x_token: str,
        metric: str | Omit = omit,
        subscription_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LlmUsageRetrieveDailyResponse:
        """
        Admin endpoint to get daily LLM usage data for dashboard

        If subscription_date is provided, filters out any usage before that date. This
        is used to hide pre-upgrade LLM costs when a free tier user upgrades to Starter.

        Args:
          end_date: End date in YYYY-MM-DD format

          start_date: Start date in YYYY-MM-DD format

          user_id: User ID to get usage for

          metric: Metric to aggregate: 'cost' or 'calls'

          subscription_date: Subscription date (ISO format) to filter out pre-subscription usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._get(
            "/v1/admin/llm-usage/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "user_id": user_id,
                        "metric": metric,
                        "subscription_date": subscription_date,
                    },
                    llm_usage_retrieve_daily_params.LlmUsageRetrieveDailyParams,
                ),
            ),
            cast_to=LlmUsageRetrieveDailyResponse,
        )

    async def retrieve_summary(
        self,
        *,
        user_id: str,
        x_token: str,
        end_time: Optional[float] | Omit = omit,
        start_time: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageSummary:
        """
        Admin endpoint to get LLM usage summary for dashboard

        Args:
          user_id: User ID to get usage for

          end_time: End timestamp (Unix time)

          start_time: Start timestamp (Unix time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._get(
            "/v1/admin/llm-usage/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "user_id": user_id,
                        "end_time": end_time,
                        "start_time": start_time,
                    },
                    llm_usage_retrieve_summary_params.LlmUsageRetrieveSummaryParams,
                ),
            ),
            cast_to=UsageSummary,
        )


class LlmUsageResourceWithRawResponse:
    def __init__(self, llm_usage: LlmUsageResource) -> None:
        self._llm_usage = llm_usage

        self.retrieve_daily = to_raw_response_wrapper(
            llm_usage.retrieve_daily,
        )
        self.retrieve_summary = to_raw_response_wrapper(
            llm_usage.retrieve_summary,
        )


class AsyncLlmUsageResourceWithRawResponse:
    def __init__(self, llm_usage: AsyncLlmUsageResource) -> None:
        self._llm_usage = llm_usage

        self.retrieve_daily = async_to_raw_response_wrapper(
            llm_usage.retrieve_daily,
        )
        self.retrieve_summary = async_to_raw_response_wrapper(
            llm_usage.retrieve_summary,
        )


class LlmUsageResourceWithStreamingResponse:
    def __init__(self, llm_usage: LlmUsageResource) -> None:
        self._llm_usage = llm_usage

        self.retrieve_daily = to_streamed_response_wrapper(
            llm_usage.retrieve_daily,
        )
        self.retrieve_summary = to_streamed_response_wrapper(
            llm_usage.retrieve_summary,
        )


class AsyncLlmUsageResourceWithStreamingResponse:
    def __init__(self, llm_usage: AsyncLlmUsageResource) -> None:
        self._llm_usage = llm_usage

        self.retrieve_daily = async_to_streamed_response_wrapper(
            llm_usage.retrieve_daily,
        )
        self.retrieve_summary = async_to_streamed_response_wrapper(
            llm_usage.retrieve_summary,
        )
