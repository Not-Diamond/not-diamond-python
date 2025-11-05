# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.report import metric_submit_feedback_params
from ...types.prompt.request_provider_param import RequestProviderParam
from ...types.report.metric_submit_feedback_response import MetricSubmitFeedbackResponse

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

    def submit_feedback(
        self,
        *,
        feedback: Dict[str, object],
        provider: RequestProviderParam,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricSubmitFeedbackResponse:
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
                metric_submit_feedback_params.MetricSubmitFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricSubmitFeedbackResponse,
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

    async def submit_feedback(
        self,
        *,
        feedback: Dict[str, object],
        provider: RequestProviderParam,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricSubmitFeedbackResponse:
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
                metric_submit_feedback_params.MetricSubmitFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricSubmitFeedbackResponse,
        )


class MetricsResourceWithRawResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.submit_feedback = to_raw_response_wrapper(
            metrics.submit_feedback,
        )


class AsyncMetricsResourceWithRawResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.submit_feedback = async_to_raw_response_wrapper(
            metrics.submit_feedback,
        )


class MetricsResourceWithStreamingResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.submit_feedback = to_streamed_response_wrapper(
            metrics.submit_feedback,
        )


class AsyncMetricsResourceWithStreamingResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.submit_feedback = async_to_streamed_response_wrapper(
            metrics.submit_feedback,
        )
