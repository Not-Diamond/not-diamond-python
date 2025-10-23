# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

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
from ..._base_client import make_request_options
from ...types.report import (
    metric_report_latency_params,
    metric_report_feedback_params,
    metric_report_frontend_thumbs_params,
    metric_report_frontend_regenerated_params,
    metric_report_frontend_arena_choice_params,
)

__all__ = ["MetricsResource", "AsyncMetricsResource"]


class MetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return MetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return MetricsResourceWithStreamingResponse(self)

    def report_feedback(
        self,
        *,
        feedback: Dict[str, object],
        provider: metric_report_feedback_params.Provider,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Report Feedback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/report/metrics/feedback",
            body=maybe_transform(
                {
                    "feedback": feedback,
                    "provider": provider,
                    "session_id": session_id,
                },
                metric_report_feedback_params.MetricReportFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def report_frontend_arena_choice(
        self,
        *,
        preferred_provider: metric_report_frontend_arena_choice_params.PreferredProvider,
        rejected_provider: metric_report_frontend_arena_choice_params.RejectedProvider,
        session_id: str,
        x_token: str,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Frontend Arena Choice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._post(
            "/v2/report/metrics/frontendArenaChoice",
            body=maybe_transform(
                {
                    "preferred_provider": preferred_provider,
                    "rejected_provider": rejected_provider,
                    "session_id": session_id,
                    "user_id": user_id,
                },
                metric_report_frontend_arena_choice_params.MetricReportFrontendArenaChoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def report_frontend_regenerated(
        self,
        *,
        provider: metric_report_frontend_regenerated_params.Provider,
        regenerated: bool,
        session_id: str,
        x_token: str,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Frontend Report Regenerated

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._post(
            "/v2/report/metrics/frontendRegenerated",
            body=maybe_transform(
                {
                    "provider": provider,
                    "regenerated": regenerated,
                    "session_id": session_id,
                    "user_id": user_id,
                },
                metric_report_frontend_regenerated_params.MetricReportFrontendRegeneratedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def report_frontend_thumbs(
        self,
        *,
        provider: metric_report_frontend_thumbs_params.Provider,
        session_id: str,
        thumbs: int,
        x_token: str,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Frontend Report Thumbs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._post(
            "/v2/report/metrics/frontendThumbsUpDown",
            body=maybe_transform(
                {
                    "provider": provider,
                    "session_id": session_id,
                    "thumbs": thumbs,
                    "user_id": user_id,
                },
                metric_report_frontend_thumbs_params.MetricReportFrontendThumbsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def report_latency(
        self,
        *,
        feedback: Dict[str, object],
        provider: metric_report_latency_params.Provider,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Report Latency

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/report/metrics/latency",
            body=maybe_transform(
                {
                    "feedback": feedback,
                    "provider": provider,
                    "session_id": session_id,
                },
                metric_report_latency_params.MetricReportLatencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncMetricsResourceWithStreamingResponse(self)

    async def report_feedback(
        self,
        *,
        feedback: Dict[str, object],
        provider: metric_report_feedback_params.Provider,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Report Feedback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/report/metrics/feedback",
            body=await async_maybe_transform(
                {
                    "feedback": feedback,
                    "provider": provider,
                    "session_id": session_id,
                },
                metric_report_feedback_params.MetricReportFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def report_frontend_arena_choice(
        self,
        *,
        preferred_provider: metric_report_frontend_arena_choice_params.PreferredProvider,
        rejected_provider: metric_report_frontend_arena_choice_params.RejectedProvider,
        session_id: str,
        x_token: str,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Frontend Arena Choice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._post(
            "/v2/report/metrics/frontendArenaChoice",
            body=await async_maybe_transform(
                {
                    "preferred_provider": preferred_provider,
                    "rejected_provider": rejected_provider,
                    "session_id": session_id,
                    "user_id": user_id,
                },
                metric_report_frontend_arena_choice_params.MetricReportFrontendArenaChoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def report_frontend_regenerated(
        self,
        *,
        provider: metric_report_frontend_regenerated_params.Provider,
        regenerated: bool,
        session_id: str,
        x_token: str,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Frontend Report Regenerated

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._post(
            "/v2/report/metrics/frontendRegenerated",
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "regenerated": regenerated,
                    "session_id": session_id,
                    "user_id": user_id,
                },
                metric_report_frontend_regenerated_params.MetricReportFrontendRegeneratedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def report_frontend_thumbs(
        self,
        *,
        provider: metric_report_frontend_thumbs_params.Provider,
        session_id: str,
        thumbs: int,
        x_token: str,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Frontend Report Thumbs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._post(
            "/v2/report/metrics/frontendThumbsUpDown",
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "session_id": session_id,
                    "thumbs": thumbs,
                    "user_id": user_id,
                },
                metric_report_frontend_thumbs_params.MetricReportFrontendThumbsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def report_latency(
        self,
        *,
        feedback: Dict[str, object],
        provider: metric_report_latency_params.Provider,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Report Latency

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/report/metrics/latency",
            body=await async_maybe_transform(
                {
                    "feedback": feedback,
                    "provider": provider,
                    "session_id": session_id,
                },
                metric_report_latency_params.MetricReportLatencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class MetricsResourceWithRawResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.report_feedback = to_raw_response_wrapper(
            metrics.report_feedback,
        )
        self.report_frontend_arena_choice = to_raw_response_wrapper(
            metrics.report_frontend_arena_choice,
        )
        self.report_frontend_regenerated = to_raw_response_wrapper(
            metrics.report_frontend_regenerated,
        )
        self.report_frontend_thumbs = to_raw_response_wrapper(
            metrics.report_frontend_thumbs,
        )
        self.report_latency = to_raw_response_wrapper(
            metrics.report_latency,
        )


class AsyncMetricsResourceWithRawResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.report_feedback = async_to_raw_response_wrapper(
            metrics.report_feedback,
        )
        self.report_frontend_arena_choice = async_to_raw_response_wrapper(
            metrics.report_frontend_arena_choice,
        )
        self.report_frontend_regenerated = async_to_raw_response_wrapper(
            metrics.report_frontend_regenerated,
        )
        self.report_frontend_thumbs = async_to_raw_response_wrapper(
            metrics.report_frontend_thumbs,
        )
        self.report_latency = async_to_raw_response_wrapper(
            metrics.report_latency,
        )


class MetricsResourceWithStreamingResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.report_feedback = to_streamed_response_wrapper(
            metrics.report_feedback,
        )
        self.report_frontend_arena_choice = to_streamed_response_wrapper(
            metrics.report_frontend_arena_choice,
        )
        self.report_frontend_regenerated = to_streamed_response_wrapper(
            metrics.report_frontend_regenerated,
        )
        self.report_frontend_thumbs = to_streamed_response_wrapper(
            metrics.report_frontend_thumbs,
        )
        self.report_latency = to_streamed_response_wrapper(
            metrics.report_latency,
        )


class AsyncMetricsResourceWithStreamingResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.report_feedback = async_to_streamed_response_wrapper(
            metrics.report_feedback,
        )
        self.report_frontend_arena_choice = async_to_streamed_response_wrapper(
            metrics.report_frontend_arena_choice,
        )
        self.report_frontend_regenerated = async_to_streamed_response_wrapper(
            metrics.report_frontend_regenerated,
        )
        self.report_frontend_thumbs = async_to_streamed_response_wrapper(
            metrics.report_frontend_thumbs,
        )
        self.report_latency = async_to_streamed_response_wrapper(
            metrics.report_latency,
        )
