# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    llm_usage_retrieve_params,
    llm_usage_retrieve_daily_params,
    llm_usage_retrieve_monthly_params,
    llm_usage_retrieve_summary_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.usage_summary import UsageSummary
from ..types.llm_usage_retrieve_response import LlmUsageRetrieveResponse
from ..types.llm_usage_retrieve_daily_response import LlmUsageRetrieveDailyResponse
from ..types.llm_usage_retrieve_monthly_response import LlmUsageRetrieveMonthlyResponse

__all__ = ["LlmUsageResource", "AsyncLlmUsageResource"]


class LlmUsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LlmUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return LlmUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return LlmUsageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        end_time: Optional[float] | Omit = omit,
        limit: int | Omit = omit,
        start_time: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LlmUsageRetrieveResponse:
        """
        Get LLM usage records for the authenticated user

        Args:
          end_time: End timestamp (Unix time)

          limit: Maximum number of records to return

          start_time: Start timestamp (Unix time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/llm-usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "limit": limit,
                        "start_time": start_time,
                    },
                    llm_usage_retrieve_params.LlmUsageRetrieveParams,
                ),
            ),
            cast_to=LlmUsageRetrieveResponse,
        )

    def retrieve_daily(
        self,
        *,
        end_date: str,
        start_date: str,
        metric: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LlmUsageRetrieveDailyResponse:
        """
        Get daily LLM usage data aggregated by cost or calls for PA usage dashboard

        Args:
          end_date: End date in YYYY-MM-DD format

          start_date: Start date in YYYY-MM-DD format

          metric: Metric to aggregate: 'cost' or 'calls'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/llm-usage/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "metric": metric,
                    },
                    llm_usage_retrieve_daily_params.LlmUsageRetrieveDailyParams,
                ),
            ),
            cast_to=LlmUsageRetrieveDailyResponse,
        )

    def retrieve_monthly(
        self,
        *,
        months: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LlmUsageRetrieveMonthlyResponse:
        """
        Get monthly LLM usage aggregated data for the last N months

        Returns usage data for the trailing N complete or partial months ending with the
        current month. For example, if called in November 2024 with months=6, returns
        data for June-November 2024.

        Args:
          months: Number of months to retrieve (max 12)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/llm-usage/monthly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"months": months}, llm_usage_retrieve_monthly_params.LlmUsageRetrieveMonthlyParams
                ),
            ),
            cast_to=LlmUsageRetrieveMonthlyResponse,
        )

    def retrieve_summary(
        self,
        *,
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
        Get a summary of LLM usage costs for the authenticated user

        Args:
          end_time: End timestamp (Unix time)

          start_time: Start timestamp (Unix time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/llm-usage/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLlmUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return AsyncLlmUsageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        end_time: Optional[float] | Omit = omit,
        limit: int | Omit = omit,
        start_time: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LlmUsageRetrieveResponse:
        """
        Get LLM usage records for the authenticated user

        Args:
          end_time: End timestamp (Unix time)

          limit: Maximum number of records to return

          start_time: Start timestamp (Unix time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/llm-usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "limit": limit,
                        "start_time": start_time,
                    },
                    llm_usage_retrieve_params.LlmUsageRetrieveParams,
                ),
            ),
            cast_to=LlmUsageRetrieveResponse,
        )

    async def retrieve_daily(
        self,
        *,
        end_date: str,
        start_date: str,
        metric: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LlmUsageRetrieveDailyResponse:
        """
        Get daily LLM usage data aggregated by cost or calls for PA usage dashboard

        Args:
          end_date: End date in YYYY-MM-DD format

          start_date: Start date in YYYY-MM-DD format

          metric: Metric to aggregate: 'cost' or 'calls'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/llm-usage/daily",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "metric": metric,
                    },
                    llm_usage_retrieve_daily_params.LlmUsageRetrieveDailyParams,
                ),
            ),
            cast_to=LlmUsageRetrieveDailyResponse,
        )

    async def retrieve_monthly(
        self,
        *,
        months: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LlmUsageRetrieveMonthlyResponse:
        """
        Get monthly LLM usage aggregated data for the last N months

        Returns usage data for the trailing N complete or partial months ending with the
        current month. For example, if called in November 2024 with months=6, returns
        data for June-November 2024.

        Args:
          months: Number of months to retrieve (max 12)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/llm-usage/monthly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"months": months}, llm_usage_retrieve_monthly_params.LlmUsageRetrieveMonthlyParams
                ),
            ),
            cast_to=LlmUsageRetrieveMonthlyResponse,
        )

    async def retrieve_summary(
        self,
        *,
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
        Get a summary of LLM usage costs for the authenticated user

        Args:
          end_time: End timestamp (Unix time)

          start_time: Start timestamp (Unix time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/llm-usage/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
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

        self.retrieve = to_raw_response_wrapper(
            llm_usage.retrieve,
        )
        self.retrieve_daily = to_raw_response_wrapper(
            llm_usage.retrieve_daily,
        )
        self.retrieve_monthly = to_raw_response_wrapper(
            llm_usage.retrieve_monthly,
        )
        self.retrieve_summary = to_raw_response_wrapper(
            llm_usage.retrieve_summary,
        )


class AsyncLlmUsageResourceWithRawResponse:
    def __init__(self, llm_usage: AsyncLlmUsageResource) -> None:
        self._llm_usage = llm_usage

        self.retrieve = async_to_raw_response_wrapper(
            llm_usage.retrieve,
        )
        self.retrieve_daily = async_to_raw_response_wrapper(
            llm_usage.retrieve_daily,
        )
        self.retrieve_monthly = async_to_raw_response_wrapper(
            llm_usage.retrieve_monthly,
        )
        self.retrieve_summary = async_to_raw_response_wrapper(
            llm_usage.retrieve_summary,
        )


class LlmUsageResourceWithStreamingResponse:
    def __init__(self, llm_usage: LlmUsageResource) -> None:
        self._llm_usage = llm_usage

        self.retrieve = to_streamed_response_wrapper(
            llm_usage.retrieve,
        )
        self.retrieve_daily = to_streamed_response_wrapper(
            llm_usage.retrieve_daily,
        )
        self.retrieve_monthly = to_streamed_response_wrapper(
            llm_usage.retrieve_monthly,
        )
        self.retrieve_summary = to_streamed_response_wrapper(
            llm_usage.retrieve_summary,
        )


class AsyncLlmUsageResourceWithStreamingResponse:
    def __init__(self, llm_usage: AsyncLlmUsageResource) -> None:
        self._llm_usage = llm_usage

        self.retrieve = async_to_streamed_response_wrapper(
            llm_usage.retrieve,
        )
        self.retrieve_daily = async_to_streamed_response_wrapper(
            llm_usage.retrieve_daily,
        )
        self.retrieve_monthly = async_to_streamed_response_wrapper(
            llm_usage.retrieve_monthly,
        )
        self.retrieve_summary = async_to_streamed_response_wrapper(
            llm_usage.retrieve_summary,
        )
