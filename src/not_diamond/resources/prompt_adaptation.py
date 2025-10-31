# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import prompt_adaptation_adapt_params
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
from ..types.adaptation_run_results import AdaptationRunResults
from ..types.prompt_adaptation_adapt_response import PromptAdaptationAdaptResponse
from ..types.prompt_adaptation_get_adapt_runs_response import PromptAdaptationGetAdaptRunsResponse
from ..types.prompt_adaptation_retrieve_costs_response import PromptAdaptationRetrieveCostsResponse
from ..types.prompt_adaptation_get_adapt_status_response import PromptAdaptationGetAdaptStatusResponse

__all__ = ["PromptAdaptationResource", "AsyncPromptAdaptationResource"]


class PromptAdaptationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptAdaptationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return PromptAdaptationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptAdaptationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return PromptAdaptationResourceWithStreamingResponse(self)

    def adapt(
        self,
        *,
        fields: SequenceNotStr[str],
        system_prompt: str,
        target_models: Iterable[prompt_adaptation_adapt_params.TargetModel],
        template: str,
        evaluation_config: Optional[str] | Omit = omit,
        evaluation_metric: Optional[str] | Omit = omit,
        goldens: Optional[Iterable[prompt_adaptation_adapt_params.Golden]] | Omit = omit,
        origin_model: Optional[prompt_adaptation_adapt_params.OriginModel] | Omit = omit,
        origin_model_evaluation_score: Optional[float] | Omit = omit,
        test_goldens: Optional[Iterable[prompt_adaptation_adapt_params.TestGolden]] | Omit = omit,
        train_goldens: Optional[Iterable[prompt_adaptation_adapt_params.TrainGolden]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAdaptationAdaptResponse:
        """
        Adapt your prompt from one LLM to work optimally across different target LLMs.

        This endpoint automatically optimizes your prompt (system prompt + user message
        template) to achieve better performance when switching between different
        language models. Each model has unique characteristics, and what works well for
        GPT-4 might not work as well for Claude or Gemini.

        **How Prompt Adaptation Works:**

        1. You provide your current prompt optimized for an origin model
        2. You specify target models you want to adapt to
        3. You provide evaluation examples (golden records) with expected answers
        4. The system runs optimization to find the best prompt for each target model
        5. You receive adapted prompts that perform well on your target models

        **Evaluation Metrics:** Choose either a standard metric or provide custom
        evaluation:

        - **Standard metrics**: LLMaaJ:SQL, LLMaaJ:Sem_Sim_1/3/10 (semantic similarity),
          JSON_Match
        - **Custom evaluation**: Provide evaluation_config with your own LLM judge,
          prompt, and cutoff

        **Dataset Requirements:**

        - Minimum 5 examples in train_goldens (more examples = better adaptation)
        - Each example must have fields matching your template placeholders
        - Supervised evaluation requires 'answer' field in each golden record
        - Unsupervised evaluation can work without answers

        **Training Time:**

        - Processing is asynchronous and typically takes 10-30 minutes
        - Time depends on: number of target models, dataset size, model availability
        - Use the returned adaptation_run_id to check status and retrieve results

        **Subscription Tiers:**

        - Free: 1 target model
        - Starter: 3 target models
        - Startup: 5 target models
        - Enterprise: 10 target models

        **Best Practices:**

        1. Use diverse, representative examples from your production workload
        2. Include 10-20 examples for best results (5 minimum)
        3. Ensure consistent evaluation across all examples
        4. Test both train_goldens and test_goldens split for validation
        5. Use the same model versions you'll use in production

        **Example Workflow:**

        ```
        1. POST /v2/prompt/adapt - Submit adaptation request
        2. GET /v2/prompt/adaptStatus/{id} - Poll status until completed
        3. GET /v2/prompt/adaptResults/{id} - Retrieve optimized prompts
        4. Use optimized prompts in production with target models
        ```

        **Related Documentation:** See
        https://docs.notdiamond.ai/docs/adapting-prompts-to-new-models for detailed
        guide.

        Args:
          fields: List of field names that will be substituted into the template. Must match keys
              in golden records

          system_prompt: System prompt to use with the origin model. This sets the context and role for
              the LLM

          target_models: List of models to adapt the prompt for. Maximum count depends on your
              subscription tier

          template: User message template with placeholders for fields. Use curly braces for field
              substitution

          goldens: Training examples (legacy parameter). Use train_goldens and test_goldens for
              better control

          origin_model: Model for specifying an LLM provider in API requests.

          origin_model_evaluation_score: Optional baseline score for the origin model

          test_goldens: Test examples for evaluation. Required if train_goldens is provided

          train_goldens: Training examples for prompt optimization. Minimum 5 examples required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/prompt/adapt",
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
                    "test_goldens": test_goldens,
                    "train_goldens": train_goldens,
                },
                prompt_adaptation_adapt_params.PromptAdaptationAdaptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAdaptationAdaptResponse,
        )

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
    ) -> AdaptationRunResults:
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
            cast_to=AdaptationRunResults,
        )

    def get_adapt_run_results(
        self,
        adaptation_run_id: str,
        *,
        user_id: str,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptationRunResults:
        """
        Get Adapt Run Results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._get(
            f"/v2/prompt/frontendAdaptRunResults/{user_id}/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptationRunResults,
        )

    def get_adapt_runs(
        self,
        user_id: str,
        *,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAdaptationGetAdaptRunsResponse:
        """
        Get Adapt Runs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._get(
            f"/v2/prompt/frontendAdaptRuns/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAdaptationGetAdaptRunsResponse,
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
    ) -> PromptAdaptationGetAdaptStatusResponse:
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
            cast_to=PromptAdaptationGetAdaptStatusResponse,
        )

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
    ) -> PromptAdaptationRetrieveCostsResponse:
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
            cast_to=PromptAdaptationRetrieveCostsResponse,
        )


class AsyncPromptAdaptationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptAdaptationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptAdaptationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptAdaptationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncPromptAdaptationResourceWithStreamingResponse(self)

    async def adapt(
        self,
        *,
        fields: SequenceNotStr[str],
        system_prompt: str,
        target_models: Iterable[prompt_adaptation_adapt_params.TargetModel],
        template: str,
        evaluation_config: Optional[str] | Omit = omit,
        evaluation_metric: Optional[str] | Omit = omit,
        goldens: Optional[Iterable[prompt_adaptation_adapt_params.Golden]] | Omit = omit,
        origin_model: Optional[prompt_adaptation_adapt_params.OriginModel] | Omit = omit,
        origin_model_evaluation_score: Optional[float] | Omit = omit,
        test_goldens: Optional[Iterable[prompt_adaptation_adapt_params.TestGolden]] | Omit = omit,
        train_goldens: Optional[Iterable[prompt_adaptation_adapt_params.TrainGolden]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAdaptationAdaptResponse:
        """
        Adapt your prompt from one LLM to work optimally across different target LLMs.

        This endpoint automatically optimizes your prompt (system prompt + user message
        template) to achieve better performance when switching between different
        language models. Each model has unique characteristics, and what works well for
        GPT-4 might not work as well for Claude or Gemini.

        **How Prompt Adaptation Works:**

        1. You provide your current prompt optimized for an origin model
        2. You specify target models you want to adapt to
        3. You provide evaluation examples (golden records) with expected answers
        4. The system runs optimization to find the best prompt for each target model
        5. You receive adapted prompts that perform well on your target models

        **Evaluation Metrics:** Choose either a standard metric or provide custom
        evaluation:

        - **Standard metrics**: LLMaaJ:SQL, LLMaaJ:Sem_Sim_1/3/10 (semantic similarity),
          JSON_Match
        - **Custom evaluation**: Provide evaluation_config with your own LLM judge,
          prompt, and cutoff

        **Dataset Requirements:**

        - Minimum 5 examples in train_goldens (more examples = better adaptation)
        - Each example must have fields matching your template placeholders
        - Supervised evaluation requires 'answer' field in each golden record
        - Unsupervised evaluation can work without answers

        **Training Time:**

        - Processing is asynchronous and typically takes 10-30 minutes
        - Time depends on: number of target models, dataset size, model availability
        - Use the returned adaptation_run_id to check status and retrieve results

        **Subscription Tiers:**

        - Free: 1 target model
        - Starter: 3 target models
        - Startup: 5 target models
        - Enterprise: 10 target models

        **Best Practices:**

        1. Use diverse, representative examples from your production workload
        2. Include 10-20 examples for best results (5 minimum)
        3. Ensure consistent evaluation across all examples
        4. Test both train_goldens and test_goldens split for validation
        5. Use the same model versions you'll use in production

        **Example Workflow:**

        ```
        1. POST /v2/prompt/adapt - Submit adaptation request
        2. GET /v2/prompt/adaptStatus/{id} - Poll status until completed
        3. GET /v2/prompt/adaptResults/{id} - Retrieve optimized prompts
        4. Use optimized prompts in production with target models
        ```

        **Related Documentation:** See
        https://docs.notdiamond.ai/docs/adapting-prompts-to-new-models for detailed
        guide.

        Args:
          fields: List of field names that will be substituted into the template. Must match keys
              in golden records

          system_prompt: System prompt to use with the origin model. This sets the context and role for
              the LLM

          target_models: List of models to adapt the prompt for. Maximum count depends on your
              subscription tier

          template: User message template with placeholders for fields. Use curly braces for field
              substitution

          goldens: Training examples (legacy parameter). Use train_goldens and test_goldens for
              better control

          origin_model: Model for specifying an LLM provider in API requests.

          origin_model_evaluation_score: Optional baseline score for the origin model

          test_goldens: Test examples for evaluation. Required if train_goldens is provided

          train_goldens: Training examples for prompt optimization. Minimum 5 examples required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/prompt/adapt",
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
                    "test_goldens": test_goldens,
                    "train_goldens": train_goldens,
                },
                prompt_adaptation_adapt_params.PromptAdaptationAdaptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAdaptationAdaptResponse,
        )

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
    ) -> AdaptationRunResults:
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
            cast_to=AdaptationRunResults,
        )

    async def get_adapt_run_results(
        self,
        adaptation_run_id: str,
        *,
        user_id: str,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptationRunResults:
        """
        Get Adapt Run Results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._get(
            f"/v2/prompt/frontendAdaptRunResults/{user_id}/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptationRunResults,
        )

    async def get_adapt_runs(
        self,
        user_id: str,
        *,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAdaptationGetAdaptRunsResponse:
        """
        Get Adapt Runs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._get(
            f"/v2/prompt/frontendAdaptRuns/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAdaptationGetAdaptRunsResponse,
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
    ) -> PromptAdaptationGetAdaptStatusResponse:
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
            cast_to=PromptAdaptationGetAdaptStatusResponse,
        )

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
    ) -> PromptAdaptationRetrieveCostsResponse:
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
            cast_to=PromptAdaptationRetrieveCostsResponse,
        )


class PromptAdaptationResourceWithRawResponse:
    def __init__(self, prompt_adaptation: PromptAdaptationResource) -> None:
        self._prompt_adaptation = prompt_adaptation

        self.adapt = to_raw_response_wrapper(
            prompt_adaptation.adapt,
        )
        self.get_adapt_results = to_raw_response_wrapper(
            prompt_adaptation.get_adapt_results,
        )
        self.get_adapt_run_results = to_raw_response_wrapper(
            prompt_adaptation.get_adapt_run_results,
        )
        self.get_adapt_runs = to_raw_response_wrapper(
            prompt_adaptation.get_adapt_runs,
        )
        self.get_adapt_status = to_raw_response_wrapper(
            prompt_adaptation.get_adapt_status,
        )
        self.retrieve_costs = to_raw_response_wrapper(
            prompt_adaptation.retrieve_costs,
        )


class AsyncPromptAdaptationResourceWithRawResponse:
    def __init__(self, prompt_adaptation: AsyncPromptAdaptationResource) -> None:
        self._prompt_adaptation = prompt_adaptation

        self.adapt = async_to_raw_response_wrapper(
            prompt_adaptation.adapt,
        )
        self.get_adapt_results = async_to_raw_response_wrapper(
            prompt_adaptation.get_adapt_results,
        )
        self.get_adapt_run_results = async_to_raw_response_wrapper(
            prompt_adaptation.get_adapt_run_results,
        )
        self.get_adapt_runs = async_to_raw_response_wrapper(
            prompt_adaptation.get_adapt_runs,
        )
        self.get_adapt_status = async_to_raw_response_wrapper(
            prompt_adaptation.get_adapt_status,
        )
        self.retrieve_costs = async_to_raw_response_wrapper(
            prompt_adaptation.retrieve_costs,
        )


class PromptAdaptationResourceWithStreamingResponse:
    def __init__(self, prompt_adaptation: PromptAdaptationResource) -> None:
        self._prompt_adaptation = prompt_adaptation

        self.adapt = to_streamed_response_wrapper(
            prompt_adaptation.adapt,
        )
        self.get_adapt_results = to_streamed_response_wrapper(
            prompt_adaptation.get_adapt_results,
        )
        self.get_adapt_run_results = to_streamed_response_wrapper(
            prompt_adaptation.get_adapt_run_results,
        )
        self.get_adapt_runs = to_streamed_response_wrapper(
            prompt_adaptation.get_adapt_runs,
        )
        self.get_adapt_status = to_streamed_response_wrapper(
            prompt_adaptation.get_adapt_status,
        )
        self.retrieve_costs = to_streamed_response_wrapper(
            prompt_adaptation.retrieve_costs,
        )


class AsyncPromptAdaptationResourceWithStreamingResponse:
    def __init__(self, prompt_adaptation: AsyncPromptAdaptationResource) -> None:
        self._prompt_adaptation = prompt_adaptation

        self.adapt = async_to_streamed_response_wrapper(
            prompt_adaptation.adapt,
        )
        self.get_adapt_results = async_to_streamed_response_wrapper(
            prompt_adaptation.get_adapt_results,
        )
        self.get_adapt_run_results = async_to_streamed_response_wrapper(
            prompt_adaptation.get_adapt_run_results,
        )
        self.get_adapt_runs = async_to_streamed_response_wrapper(
            prompt_adaptation.get_adapt_runs,
        )
        self.get_adapt_status = async_to_streamed_response_wrapper(
            prompt_adaptation.get_adapt_status,
        )
        self.retrieve_costs = async_to_streamed_response_wrapper(
            prompt_adaptation.retrieve_costs,
        )
