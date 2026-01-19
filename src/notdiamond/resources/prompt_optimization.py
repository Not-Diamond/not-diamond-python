# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import prompt_optimization_optimize_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.golden_record_param import GoldenRecordParam
from ..types.request_provider_param import RequestProviderParam
from ..types.prompt_optimization_optimize_response import PromptOptimizationOptimizeResponse
from ..types.prompt_optimization_retrieve_costs_response import PromptOptimizationRetrieveCostsResponse
from ..types.prompt_optimization_get_optimziation_status_response import PromptOptimizationGetOptimziationStatusResponse
from ..types.prompt_optimization_get_optimization_results_response import (
    PromptOptimizationGetOptimizationResultsResponse,
)

__all__ = ["PromptOptimizationResource", "AsyncPromptOptimizationResource"]


class PromptOptimizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptOptimizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return PromptOptimizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptOptimizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return PromptOptimizationResourceWithStreamingResponse(self)

    def get_optimization_results(
        self,
        optimization_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptOptimizationGetOptimizationResultsResponse:
        """
        Retrieve the complete results of a prompt optimization run, including optimized
        prompts for all target models.

        This endpoint returns the optimized prompts and evaluation metrics for each
        target model in your optimization request. Call this endpoint after the
        optimization status is 'completed' to get your optimized prompts.

        **Response Structure:**

        - **origin_model**: Baseline performance of your original prompt on the origin
          model
          - Includes: system_prompt, user_message_template, score, evaluation metrics,
            cost
        - **target_models**: Array of results for each target model
          - Includes: optimized system_prompt, user_message_template, template_fields
          - pre_optimization_score: Performance before optimization
          - post_optimization_score: Performance after optimization
          - Evaluation metrics and cost information

        **Using Optimized Prompts:**

        1. Extract the `system_prompt` and `user_message_template` from each target
           model result
        2. Use `user_message_template_fields` to know which fields to substitute
        3. Apply the optimized prompts when calling the respective target models
        4. Compare pre/post optimization scores to see improvement

        **Status Handling:**

        - If optimization is still processing, target model results will have
          `result_status: "processing"`
        - Only completed target models will have system_prompt and template values
        - Failed target models will have `result_status: "failed"` with null values

        **Cost Information:**

        - Each model result includes cost in USD for the optimization process
        - Costs vary based on model pricing and number of evaluation examples
        - Typical range: $0.10 - $2.00 per target model

        **Best Practices:**

        1. Wait for status 'completed' before calling this endpoint
        2. Check result_status for each target model
        3. Validate that post_optimization_score > pre_optimization_score
        4. Save optimized prompts for production use
        5. A/B test optimized prompts against originals in production

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not optimization_run_id:
            raise ValueError(
                f"Expected a non-empty value for `optimization_run_id` but received {optimization_run_id!r}"
            )
        return self._get(
            f"/v2/prompt/optimizeResults/{optimization_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationGetOptimizationResultsResponse,
        )

    def get_optimziation_status(
        self,
        optimization_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptOptimizationGetOptimziationStatusResponse:
        """
        Check the status of a prompt optimization run.

        Use this endpoint to poll the status of your optimization request. Processing is
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
        - Use GET /v2/prompt/optimizeResults to retrieve results after completion

        **Queue Position:**

        - Only present when status is 'queued'
        - Lower numbers mean earlier processing (position 1 is next)
        - Typical wait time: 1-5 minutes per position

        **Note:** This endpoint only returns status information. To get the actual
        optimized prompts and evaluation results, use GET /v2/prompt/optimizeResults
        once status is 'completed'.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not optimization_run_id:
            raise ValueError(
                f"Expected a non-empty value for `optimization_run_id` but received {optimization_run_id!r}"
            )
        return self._get(
            f"/v2/prompt/optimizeStatus/{optimization_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationGetOptimziationStatusResponse,
        )

    def optimize(
        self,
        *,
        fields: SequenceNotStr[str],
        system_prompt: str,
        target_models: Iterable[RequestProviderParam],
        template: str,
        evaluation_config: Optional[str] | Omit = omit,
        evaluation_metric: Optional[str] | Omit = omit,
        goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        origin_model: Optional[RequestProviderParam] | Omit = omit,
        origin_model_evaluation_score: Optional[float] | Omit = omit,
        prototype_mode: bool | Omit = omit,
        test_goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        train_goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptOptimizationOptimizeResponse:
        """
        Optimize your prompt from one LLM to work optimally across different target
        LLMs.

        This endpoint automatically optimizes your prompt (system prompt + user message
        template) to improve accuracy on your use case across various models. Each model
        has unique characteristics, and what works well for GPT-5 might not work as well
        for Claude or Gemini.

        **How Prompt Optimization Works:**

        1. You provide your current prompt and optionally your current origin model
        2. You specify the target models you want to optimize your prompt to
        3. You provide evaluation examples (golden records) with expected answers
        4. The system runs optimization to find the best prompt for each target model
        5. You receive optimized prompts that perform well on your target models

        **Evaluation Metrics:** Choose either a standard metric or provide custom
        evaluation:

        - **Standard metrics**: LLMaaJ:Sem_Sim_1 (semantic similarity), JSON_Match
        - **Custom evaluation**: Provide evaluation_config with your own LLM judge,
          prompt, and cutoff

        **Dataset Requirements:**

        - Minimum 25 examples in train_goldens (more examples = better optimization)
        - **Prototype mode**: Set `prototype_mode: true` to use as few as 3 examples for
          prototyping
          - Recommended when you don't have enough data yet to build a proof-of-concept
          - Note: Performance may be degraded compared to standard mode (25+ examples)
          - Trade-off: Faster iteration with less data vs. potentially less
            generalizability
        - Each example must have fields matching your template placeholders
        - Supervised evaluation requires 'answer' field in each golden record
        - Unsupervised evaluation can work without answers

        **Training Time:**

        - Processing is asynchronous and typically takes 10-30 minutes
        - Time depends on: number of target models, dataset size, model availability
        - Use the returned optimization_run_id to check status and retrieve results

        **Example Workflow:**

        ```
        1. POST /v2/prompt/optimize - Submit optimization request
        2. GET /v2/prompt/optimizeStatus/{id} - Poll status until completed
        3. GET /v2/prompt/optimizeResults/{id} - Retrieve optimized prompts
        4. Use optimized prompts in production with target models
        ```

        Args:
          fields: List of field names that will be substituted into the template. Must match keys
              in golden records

          system_prompt: System prompt to use with the origin model. This sets the context and role for
              the LLM

          target_models: List of models to optimize the prompt for. Maximum count depends on your
              subscription tier (Free: 1, Starter: 3, Startup: 5, Enterprise: 10)

          template: User message template with placeholders for fields. Use curly braces for field
              substitution

          goldens: Training examples (legacy parameter). Use train_goldens and test_goldens for
              better control. Minimum 25 examples (or 3 with prototype_mode=true)

          origin_model: Model for specifying an LLM provider in API requests.

          origin_model_evaluation_score: Optional baseline score for the origin model. If provided, can skip origin model
              evaluation

          prototype_mode: Enable prototype mode to use as few as 3 training examples (instead of 25).
              Note: Performance may be degraded with fewer examples. Recommended for
              prototyping AI applications when you don't have enough data yet

          test_goldens: Test examples for evaluation. Required if train_goldens is provided. Used to
              measure final performance on held-out data

          train_goldens: Training examples for prompt optimization. Minimum 25 examples required (or 3
              with prototype_mode=true). Cannot be used with 'goldens' parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/prompt/optimize",
            body=maybe_transform(
                {
                    "fields": fields,
                    "system_prompt": system_prompt,
                    "target_models": target_models,
                    "template": template,
                    "evaluation_config": evaluation_config,
                    "evaluation_metric": evaluation_metric,
                    "goldens": goldens,
                    "origin_model": origin_model,
                    "origin_model_evaluation_score": origin_model_evaluation_score,
                    "prototype_mode": prototype_mode,
                    "test_goldens": test_goldens,
                    "train_goldens": train_goldens,
                },
                prompt_optimization_optimize_params.PromptOptimizationOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationOptimizeResponse,
        )

    def retrieve_costs(
        self,
        optimization_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptOptimizationRetrieveCostsResponse:
        """
        Get LLM usage costs for a specific prompt optimization run.

        This endpoint returns the total cost and detailed usage records for all LLM
        requests made during a prompt optimization run. Use this to track costs
        associated with optimizing prompts for different target models.

        **Cost Breakdown:**

        - Total cost across all models used in the optimization
        - Individual usage records with provider, model, tokens, and costs
        - Timestamps for each LLM request

        **Access Control:**

        - Only accessible by the user who created the optimization run
        - Requires prompt optimization access

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not optimization_run_id:
            raise ValueError(
                f"Expected a non-empty value for `optimization_run_id` but received {optimization_run_id!r}"
            )
        return self._get(
            f"/v2/prompt/optimize/{optimization_run_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationRetrieveCostsResponse,
        )


class AsyncPromptOptimizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptOptimizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptOptimizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptOptimizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncPromptOptimizationResourceWithStreamingResponse(self)

    async def get_optimization_results(
        self,
        optimization_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptOptimizationGetOptimizationResultsResponse:
        """
        Retrieve the complete results of a prompt optimization run, including optimized
        prompts for all target models.

        This endpoint returns the optimized prompts and evaluation metrics for each
        target model in your optimization request. Call this endpoint after the
        optimization status is 'completed' to get your optimized prompts.

        **Response Structure:**

        - **origin_model**: Baseline performance of your original prompt on the origin
          model
          - Includes: system_prompt, user_message_template, score, evaluation metrics,
            cost
        - **target_models**: Array of results for each target model
          - Includes: optimized system_prompt, user_message_template, template_fields
          - pre_optimization_score: Performance before optimization
          - post_optimization_score: Performance after optimization
          - Evaluation metrics and cost information

        **Using Optimized Prompts:**

        1. Extract the `system_prompt` and `user_message_template` from each target
           model result
        2. Use `user_message_template_fields` to know which fields to substitute
        3. Apply the optimized prompts when calling the respective target models
        4. Compare pre/post optimization scores to see improvement

        **Status Handling:**

        - If optimization is still processing, target model results will have
          `result_status: "processing"`
        - Only completed target models will have system_prompt and template values
        - Failed target models will have `result_status: "failed"` with null values

        **Cost Information:**

        - Each model result includes cost in USD for the optimization process
        - Costs vary based on model pricing and number of evaluation examples
        - Typical range: $0.10 - $2.00 per target model

        **Best Practices:**

        1. Wait for status 'completed' before calling this endpoint
        2. Check result_status for each target model
        3. Validate that post_optimization_score > pre_optimization_score
        4. Save optimized prompts for production use
        5. A/B test optimized prompts against originals in production

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not optimization_run_id:
            raise ValueError(
                f"Expected a non-empty value for `optimization_run_id` but received {optimization_run_id!r}"
            )
        return await self._get(
            f"/v2/prompt/optimizeResults/{optimization_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationGetOptimizationResultsResponse,
        )

    async def get_optimziation_status(
        self,
        optimization_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptOptimizationGetOptimziationStatusResponse:
        """
        Check the status of a prompt optimization run.

        Use this endpoint to poll the status of your optimization request. Processing is
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
        - Use GET /v2/prompt/optimizeResults to retrieve results after completion

        **Queue Position:**

        - Only present when status is 'queued'
        - Lower numbers mean earlier processing (position 1 is next)
        - Typical wait time: 1-5 minutes per position

        **Note:** This endpoint only returns status information. To get the actual
        optimized prompts and evaluation results, use GET /v2/prompt/optimizeResults
        once status is 'completed'.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not optimization_run_id:
            raise ValueError(
                f"Expected a non-empty value for `optimization_run_id` but received {optimization_run_id!r}"
            )
        return await self._get(
            f"/v2/prompt/optimizeStatus/{optimization_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationGetOptimziationStatusResponse,
        )

    async def optimize(
        self,
        *,
        fields: SequenceNotStr[str],
        system_prompt: str,
        target_models: Iterable[RequestProviderParam],
        template: str,
        evaluation_config: Optional[str] | Omit = omit,
        evaluation_metric: Optional[str] | Omit = omit,
        goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        origin_model: Optional[RequestProviderParam] | Omit = omit,
        origin_model_evaluation_score: Optional[float] | Omit = omit,
        prototype_mode: bool | Omit = omit,
        test_goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        train_goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptOptimizationOptimizeResponse:
        """
        Optimize your prompt from one LLM to work optimally across different target
        LLMs.

        This endpoint automatically optimizes your prompt (system prompt + user message
        template) to improve accuracy on your use case across various models. Each model
        has unique characteristics, and what works well for GPT-5 might not work as well
        for Claude or Gemini.

        **How Prompt Optimization Works:**

        1. You provide your current prompt and optionally your current origin model
        2. You specify the target models you want to optimize your prompt to
        3. You provide evaluation examples (golden records) with expected answers
        4. The system runs optimization to find the best prompt for each target model
        5. You receive optimized prompts that perform well on your target models

        **Evaluation Metrics:** Choose either a standard metric or provide custom
        evaluation:

        - **Standard metrics**: LLMaaJ:Sem_Sim_1 (semantic similarity), JSON_Match
        - **Custom evaluation**: Provide evaluation_config with your own LLM judge,
          prompt, and cutoff

        **Dataset Requirements:**

        - Minimum 25 examples in train_goldens (more examples = better optimization)
        - **Prototype mode**: Set `prototype_mode: true` to use as few as 3 examples for
          prototyping
          - Recommended when you don't have enough data yet to build a proof-of-concept
          - Note: Performance may be degraded compared to standard mode (25+ examples)
          - Trade-off: Faster iteration with less data vs. potentially less
            generalizability
        - Each example must have fields matching your template placeholders
        - Supervised evaluation requires 'answer' field in each golden record
        - Unsupervised evaluation can work without answers

        **Training Time:**

        - Processing is asynchronous and typically takes 10-30 minutes
        - Time depends on: number of target models, dataset size, model availability
        - Use the returned optimization_run_id to check status and retrieve results

        **Example Workflow:**

        ```
        1. POST /v2/prompt/optimize - Submit optimization request
        2. GET /v2/prompt/optimizeStatus/{id} - Poll status until completed
        3. GET /v2/prompt/optimizeResults/{id} - Retrieve optimized prompts
        4. Use optimized prompts in production with target models
        ```

        Args:
          fields: List of field names that will be substituted into the template. Must match keys
              in golden records

          system_prompt: System prompt to use with the origin model. This sets the context and role for
              the LLM

          target_models: List of models to optimize the prompt for. Maximum count depends on your
              subscription tier (Free: 1, Starter: 3, Startup: 5, Enterprise: 10)

          template: User message template with placeholders for fields. Use curly braces for field
              substitution

          goldens: Training examples (legacy parameter). Use train_goldens and test_goldens for
              better control. Minimum 25 examples (or 3 with prototype_mode=true)

          origin_model: Model for specifying an LLM provider in API requests.

          origin_model_evaluation_score: Optional baseline score for the origin model. If provided, can skip origin model
              evaluation

          prototype_mode: Enable prototype mode to use as few as 3 training examples (instead of 25).
              Note: Performance may be degraded with fewer examples. Recommended for
              prototyping AI applications when you don't have enough data yet

          test_goldens: Test examples for evaluation. Required if train_goldens is provided. Used to
              measure final performance on held-out data

          train_goldens: Training examples for prompt optimization. Minimum 25 examples required (or 3
              with prototype_mode=true). Cannot be used with 'goldens' parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/prompt/optimize",
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "system_prompt": system_prompt,
                    "target_models": target_models,
                    "template": template,
                    "evaluation_config": evaluation_config,
                    "evaluation_metric": evaluation_metric,
                    "goldens": goldens,
                    "origin_model": origin_model,
                    "origin_model_evaluation_score": origin_model_evaluation_score,
                    "prototype_mode": prototype_mode,
                    "test_goldens": test_goldens,
                    "train_goldens": train_goldens,
                },
                prompt_optimization_optimize_params.PromptOptimizationOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationOptimizeResponse,
        )

    async def retrieve_costs(
        self,
        optimization_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptOptimizationRetrieveCostsResponse:
        """
        Get LLM usage costs for a specific prompt optimization run.

        This endpoint returns the total cost and detailed usage records for all LLM
        requests made during a prompt optimization run. Use this to track costs
        associated with optimizing prompts for different target models.

        **Cost Breakdown:**

        - Total cost across all models used in the optimization
        - Individual usage records with provider, model, tokens, and costs
        - Timestamps for each LLM request

        **Access Control:**

        - Only accessible by the user who created the optimization run
        - Requires prompt optimization access

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not optimization_run_id:
            raise ValueError(
                f"Expected a non-empty value for `optimization_run_id` but received {optimization_run_id!r}"
            )
        return await self._get(
            f"/v2/prompt/optimize/{optimization_run_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptOptimizationRetrieveCostsResponse,
        )


class PromptOptimizationResourceWithRawResponse:
    def __init__(self, prompt_optimization: PromptOptimizationResource) -> None:
        self._prompt_optimization = prompt_optimization

        self.get_optimization_results = to_raw_response_wrapper(
            prompt_optimization.get_optimization_results,
        )
        self.get_optimziation_status = to_raw_response_wrapper(
            prompt_optimization.get_optimziation_status,
        )
        self.optimize = to_raw_response_wrapper(
            prompt_optimization.optimize,
        )
        self.retrieve_costs = to_raw_response_wrapper(
            prompt_optimization.retrieve_costs,
        )


class AsyncPromptOptimizationResourceWithRawResponse:
    def __init__(self, prompt_optimization: AsyncPromptOptimizationResource) -> None:
        self._prompt_optimization = prompt_optimization

        self.get_optimization_results = async_to_raw_response_wrapper(
            prompt_optimization.get_optimization_results,
        )
        self.get_optimziation_status = async_to_raw_response_wrapper(
            prompt_optimization.get_optimziation_status,
        )
        self.optimize = async_to_raw_response_wrapper(
            prompt_optimization.optimize,
        )
        self.retrieve_costs = async_to_raw_response_wrapper(
            prompt_optimization.retrieve_costs,
        )


class PromptOptimizationResourceWithStreamingResponse:
    def __init__(self, prompt_optimization: PromptOptimizationResource) -> None:
        self._prompt_optimization = prompt_optimization

        self.get_optimization_results = to_streamed_response_wrapper(
            prompt_optimization.get_optimization_results,
        )
        self.get_optimziation_status = to_streamed_response_wrapper(
            prompt_optimization.get_optimziation_status,
        )
        self.optimize = to_streamed_response_wrapper(
            prompt_optimization.optimize,
        )
        self.retrieve_costs = to_streamed_response_wrapper(
            prompt_optimization.retrieve_costs,
        )


class AsyncPromptOptimizationResourceWithStreamingResponse:
    def __init__(self, prompt_optimization: AsyncPromptOptimizationResource) -> None:
        self._prompt_optimization = prompt_optimization

        self.get_optimization_results = async_to_streamed_response_wrapper(
            prompt_optimization.get_optimization_results,
        )
        self.get_optimziation_status = async_to_streamed_response_wrapper(
            prompt_optimization.get_optimziation_status,
        )
        self.optimize = async_to_streamed_response_wrapper(
            prompt_optimization.optimize,
        )
        self.retrieve_costs = async_to_streamed_response_wrapper(
            prompt_optimization.retrieve_costs,
        )
