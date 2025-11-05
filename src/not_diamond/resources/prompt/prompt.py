# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .adapt import (
    AdaptResource,
    AsyncAdaptResource,
    AdaptResourceWithRawResponse,
    AsyncAdaptResourceWithRawResponse,
    AdaptResourceWithStreamingResponse,
    AsyncAdaptResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.prompt_get_adapt_status_response import PromptGetAdaptStatusResponse
from ...types.prompt_get_adapt_results_response import PromptGetAdaptResultsResponse

__all__ = ["PromptResource", "AsyncPromptResource"]


class PromptResource(SyncAPIResource):
    @cached_property
    def adapt(self) -> AdaptResource:
        return AdaptResource(self._client)

    @cached_property
    def with_raw_response(self) -> PromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return PromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return PromptResourceWithStreamingResponse(self)

    def get_adapt_results(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptGetAdaptResultsResponse:
        """
        Retrieve the complete results of a prompt adaptation run, including optimized
        prompts for all target models.

        This endpoint returns the adapted prompts and evaluation metrics for each target
        model in your adaptation request. Call this endpoint after the adaptation status
        is 'completed' to get your optimized prompts.

        **Response Structure:**

        - **origin_model**: Baseline performance of your original prompt on the origin
          model
          - Includes: system_prompt, user_message_template, score, evaluation metrics,
            cost
        - **target_models**: Array of results for each target model
          - Includes: optimized system_prompt, user_message_template, template_fields
          - pre_optimization_score: Performance before adaptation
          - post_optimization_score: Performance after adaptation
          - Evaluation metrics and cost information

        **Using Adapted Prompts:**

        1. Extract the `system_prompt` and `user_message_template` from each target
           model result
        2. Use `user_message_template_fields` to know which fields to substitute
        3. Apply the optimized prompts when calling the respective target models
        4. Compare pre/post optimization scores to see improvement

        **Evaluation Scores:**

        - Scores range from 0-10 (higher is better)
        - Compare origin_model score with target_models pre_optimization_score for
          baseline
        - Compare pre_optimization_score with post_optimization_score to see improvement
          from adaptation
        - Typical improvements range from 5-30% on evaluation metrics

        **Status Handling:**

        - If adaptation is still processing, target model results will have
          `result_status: "processing"`
        - Only completed target models will have system_prompt and template values
        - Failed target models will have `result_status: "failed"` with null values

        **Cost Information:**

        - Each model result includes cost in USD for the adaptation process
        - Costs vary based on model pricing and number of evaluation examples
        - Typical range: $0.10 - $2.00 per target model

        **Best Practices:**

        1. Wait for status 'completed' before calling this endpoint
        2. Check result_status for each target model
        3. Validate that post_optimization_score > pre_optimization_score
        4. Save optimized prompts for production use
        5. A/B test adapted prompts against originals in production

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return self._get(
            f"/v2/prompt/adaptResults/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetAdaptResultsResponse,
        )

    def get_adapt_status(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptGetAdaptStatusResponse:
        """
        Check the status of a prompt adaptation run.

        Use this endpoint to poll the status of your adaptation request. Processing is
        asynchronous, so you'll need to check periodically until the status indicates
        completion.

        **Status Values:**

        - `created`: Initial state, not yet processing
        - `queued`: Waiting for processing capacity (check queue_position)
        - `processing`: Currently optimizing prompts
        - `completed`: All target models have been processed successfully
        - `failed`: One or more target models failed to process

        **Polling Recommendations:**

        - Poll every 30-60 seconds during processing
        - Check queue_position if status is 'queued' to estimate wait time
        - Stop polling once status is 'completed' or 'failed'
        - Use GET /v2/prompt/adaptResults to retrieve results after completion

        **Queue Position:**

        - Only present when status is 'queued'
        - Lower numbers mean earlier processing (position 1 is next)
        - Typical wait time: 1-5 minutes per position

        **Note:** This endpoint only returns status information. To get the actual
        adapted prompts and evaluation results, use GET /v2/prompt/adaptResults once
        status is 'completed'.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return self._get(
            f"/v2/prompt/adaptStatus/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetAdaptStatusResponse,
        )


class AsyncPromptResource(AsyncAPIResource):
    @cached_property
    def adapt(self) -> AsyncAdaptResource:
        return AsyncAdaptResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncPromptResourceWithStreamingResponse(self)

    async def get_adapt_results(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptGetAdaptResultsResponse:
        """
        Retrieve the complete results of a prompt adaptation run, including optimized
        prompts for all target models.

        This endpoint returns the adapted prompts and evaluation metrics for each target
        model in your adaptation request. Call this endpoint after the adaptation status
        is 'completed' to get your optimized prompts.

        **Response Structure:**

        - **origin_model**: Baseline performance of your original prompt on the origin
          model
          - Includes: system_prompt, user_message_template, score, evaluation metrics,
            cost
        - **target_models**: Array of results for each target model
          - Includes: optimized system_prompt, user_message_template, template_fields
          - pre_optimization_score: Performance before adaptation
          - post_optimization_score: Performance after adaptation
          - Evaluation metrics and cost information

        **Using Adapted Prompts:**

        1. Extract the `system_prompt` and `user_message_template` from each target
           model result
        2. Use `user_message_template_fields` to know which fields to substitute
        3. Apply the optimized prompts when calling the respective target models
        4. Compare pre/post optimization scores to see improvement

        **Evaluation Scores:**

        - Scores range from 0-10 (higher is better)
        - Compare origin_model score with target_models pre_optimization_score for
          baseline
        - Compare pre_optimization_score with post_optimization_score to see improvement
          from adaptation
        - Typical improvements range from 5-30% on evaluation metrics

        **Status Handling:**

        - If adaptation is still processing, target model results will have
          `result_status: "processing"`
        - Only completed target models will have system_prompt and template values
        - Failed target models will have `result_status: "failed"` with null values

        **Cost Information:**

        - Each model result includes cost in USD for the adaptation process
        - Costs vary based on model pricing and number of evaluation examples
        - Typical range: $0.10 - $2.00 per target model

        **Best Practices:**

        1. Wait for status 'completed' before calling this endpoint
        2. Check result_status for each target model
        3. Validate that post_optimization_score > pre_optimization_score
        4. Save optimized prompts for production use
        5. A/B test adapted prompts against originals in production

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return await self._get(
            f"/v2/prompt/adaptResults/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetAdaptResultsResponse,
        )

    async def get_adapt_status(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptGetAdaptStatusResponse:
        """
        Check the status of a prompt adaptation run.

        Use this endpoint to poll the status of your adaptation request. Processing is
        asynchronous, so you'll need to check periodically until the status indicates
        completion.

        **Status Values:**

        - `created`: Initial state, not yet processing
        - `queued`: Waiting for processing capacity (check queue_position)
        - `processing`: Currently optimizing prompts
        - `completed`: All target models have been processed successfully
        - `failed`: One or more target models failed to process

        **Polling Recommendations:**

        - Poll every 30-60 seconds during processing
        - Check queue_position if status is 'queued' to estimate wait time
        - Stop polling once status is 'completed' or 'failed'
        - Use GET /v2/prompt/adaptResults to retrieve results after completion

        **Queue Position:**

        - Only present when status is 'queued'
        - Lower numbers mean earlier processing (position 1 is next)
        - Typical wait time: 1-5 minutes per position

        **Note:** This endpoint only returns status information. To get the actual
        adapted prompts and evaluation results, use GET /v2/prompt/adaptResults once
        status is 'completed'.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return await self._get(
            f"/v2/prompt/adaptStatus/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetAdaptStatusResponse,
        )


class PromptResourceWithRawResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.get_adapt_results = to_raw_response_wrapper(
            prompt.get_adapt_results,
        )
        self.get_adapt_status = to_raw_response_wrapper(
            prompt.get_adapt_status,
        )

    @cached_property
    def adapt(self) -> AdaptResourceWithRawResponse:
        return AdaptResourceWithRawResponse(self._prompt.adapt)


class AsyncPromptResourceWithRawResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.get_adapt_results = async_to_raw_response_wrapper(
            prompt.get_adapt_results,
        )
        self.get_adapt_status = async_to_raw_response_wrapper(
            prompt.get_adapt_status,
        )

    @cached_property
    def adapt(self) -> AsyncAdaptResourceWithRawResponse:
        return AsyncAdaptResourceWithRawResponse(self._prompt.adapt)


class PromptResourceWithStreamingResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.get_adapt_results = to_streamed_response_wrapper(
            prompt.get_adapt_results,
        )
        self.get_adapt_status = to_streamed_response_wrapper(
            prompt.get_adapt_status,
        )

    @cached_property
    def adapt(self) -> AdaptResourceWithStreamingResponse:
        return AdaptResourceWithStreamingResponse(self._prompt.adapt)


class AsyncPromptResourceWithStreamingResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.get_adapt_results = async_to_streamed_response_wrapper(
            prompt.get_adapt_results,
        )
        self.get_adapt_status = async_to_streamed_response_wrapper(
            prompt.get_adapt_status,
        )

    @cached_property
    def adapt(self) -> AsyncAdaptResourceWithStreamingResponse:
        return AsyncAdaptResourceWithStreamingResponse(self._prompt.adapt)
