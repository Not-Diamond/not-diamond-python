# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import report_latency_params, report_submit_feedback_params, report_evaluate_hallucination_params
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
from ..types.report_submit_feedback_response import ReportSubmitFeedbackResponse

__all__ = ["ReportResource", "AsyncReportResource"]


class ReportResource(SyncAPIResource):
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

    def evaluate_hallucination(
        self,
        *,
        context: str,
        prompt: str,
        provider: report_evaluate_hallucination_params.Provider,
        response: str,
        cost: Optional[float] | Omit = omit,
        latency: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Evaluate Hallucination

        Args:
          provider: Model for specifying an LLM provider in API requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/report/hallucination",
            body=maybe_transform(
                {
                    "context": context,
                    "prompt": prompt,
                    "provider": provider,
                    "response": response,
                    "cost": cost,
                    "latency": latency,
                },
                report_evaluate_hallucination_params.ReportEvaluateHallucinationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def latency(
        self,
        *,
        feedback: Dict[str, object],
        provider: report_latency_params.Provider,
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
          feedback: Feedback dictionary with 'accuracy' key (0 for thumbs down, 1 for thumbs up)

          provider: The provider that was selected by the router

          session_id: Session ID returned from POST /v2/modelRouter/modelSelect

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
                report_latency_params.ReportLatencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def submit_feedback(
        self,
        *,
        feedback: Dict[str, object],
        provider: report_submit_feedback_params.Provider,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportSubmitFeedbackResponse:
        """
        Submit feedback on a routing decision to improve future recommendations.

        This endpoint allows you to provide feedback on whether the router selected the
        right model for your query. Your feedback is used to:

        1. Personalize routing decisions for your preference_id
        2. Improve the overall routing quality
        3. Train and refine custom routers

        **Feedback Format:**

        - `accuracy: 1` - Thumbs up (the model performed well)
        - `accuracy: 0` - Thumbs down (the model did not perform well)

        **Requirements:**

        - You must have used a preference_id in the original model_select() call
        - The session_id must be valid and belong to your account
        - The provider must match one of the providers returned by model_select()

        **How Feedback Works:** When you submit thumbs down, the router will:

        - Decrease the ranking of the selected model for similar queries
        - Consider alternative models more favorably

        When you submit thumbs up, the router will:

        - Increase the ranking of the selected model for similar queries
        - Prioritize this model for similar future requests

        **Note:** Feedback requires a valid preference_id. Create one via POST
        /v2/preferences/userPreferenceCreate

        Args:
          feedback: Feedback dictionary with 'accuracy' key (0 for thumbs down, 1 for thumbs up)

          provider: The provider that was selected by the router

          session_id: Session ID returned from POST /v2/modelRouter/modelSelect

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
                report_submit_feedback_params.ReportSubmitFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportSubmitFeedbackResponse,
        )


class AsyncReportResource(AsyncAPIResource):
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

    async def evaluate_hallucination(
        self,
        *,
        context: str,
        prompt: str,
        provider: report_evaluate_hallucination_params.Provider,
        response: str,
        cost: Optional[float] | Omit = omit,
        latency: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Evaluate Hallucination

        Args:
          provider: Model for specifying an LLM provider in API requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/report/hallucination",
            body=await async_maybe_transform(
                {
                    "context": context,
                    "prompt": prompt,
                    "provider": provider,
                    "response": response,
                    "cost": cost,
                    "latency": latency,
                },
                report_evaluate_hallucination_params.ReportEvaluateHallucinationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def latency(
        self,
        *,
        feedback: Dict[str, object],
        provider: report_latency_params.Provider,
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
          feedback: Feedback dictionary with 'accuracy' key (0 for thumbs down, 1 for thumbs up)

          provider: The provider that was selected by the router

          session_id: Session ID returned from POST /v2/modelRouter/modelSelect

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
                report_latency_params.ReportLatencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def submit_feedback(
        self,
        *,
        feedback: Dict[str, object],
        provider: report_submit_feedback_params.Provider,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportSubmitFeedbackResponse:
        """
        Submit feedback on a routing decision to improve future recommendations.

        This endpoint allows you to provide feedback on whether the router selected the
        right model for your query. Your feedback is used to:

        1. Personalize routing decisions for your preference_id
        2. Improve the overall routing quality
        3. Train and refine custom routers

        **Feedback Format:**

        - `accuracy: 1` - Thumbs up (the model performed well)
        - `accuracy: 0` - Thumbs down (the model did not perform well)

        **Requirements:**

        - You must have used a preference_id in the original model_select() call
        - The session_id must be valid and belong to your account
        - The provider must match one of the providers returned by model_select()

        **How Feedback Works:** When you submit thumbs down, the router will:

        - Decrease the ranking of the selected model for similar queries
        - Consider alternative models more favorably

        When you submit thumbs up, the router will:

        - Increase the ranking of the selected model for similar queries
        - Prioritize this model for similar future requests

        **Note:** Feedback requires a valid preference_id. Create one via POST
        /v2/preferences/userPreferenceCreate

        Args:
          feedback: Feedback dictionary with 'accuracy' key (0 for thumbs down, 1 for thumbs up)

          provider: The provider that was selected by the router

          session_id: Session ID returned from POST /v2/modelRouter/modelSelect

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
                report_submit_feedback_params.ReportSubmitFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportSubmitFeedbackResponse,
        )


class ReportResourceWithRawResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.evaluate_hallucination = to_raw_response_wrapper(
            report.evaluate_hallucination,
        )
        self.latency = to_raw_response_wrapper(
            report.latency,
        )
        self.submit_feedback = to_raw_response_wrapper(
            report.submit_feedback,
        )


class AsyncReportResourceWithRawResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.evaluate_hallucination = async_to_raw_response_wrapper(
            report.evaluate_hallucination,
        )
        self.latency = async_to_raw_response_wrapper(
            report.latency,
        )
        self.submit_feedback = async_to_raw_response_wrapper(
            report.submit_feedback,
        )


class ReportResourceWithStreamingResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.evaluate_hallucination = to_streamed_response_wrapper(
            report.evaluate_hallucination,
        )
        self.latency = to_streamed_response_wrapper(
            report.latency,
        )
        self.submit_feedback = to_streamed_response_wrapper(
            report.submit_feedback,
        )


class AsyncReportResourceWithStreamingResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.evaluate_hallucination = async_to_streamed_response_wrapper(
            report.evaluate_hallucination,
        )
        self.latency = async_to_streamed_response_wrapper(
            report.latency,
        )
        self.submit_feedback = async_to_streamed_response_wrapper(
            report.submit_feedback,
        )
