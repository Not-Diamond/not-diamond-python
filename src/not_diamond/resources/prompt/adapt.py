# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.prompt import adapt_create_params
from ...types.prompt.golden_record_param import GoldenRecordParam
from ...types.prompt.adapt_create_response import AdaptCreateResponse
from ...types.prompt.request_provider_param import RequestProviderParam
from ...types.prompt.adapt_get_costs_response import AdaptGetCostsResponse

__all__ = ["AdaptResource", "AsyncAdaptResource"]


class AdaptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdaptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AdaptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdaptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AdaptResourceWithStreamingResponse(self)

    def create(
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
        test_goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        train_goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptCreateResponse:
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

        - Minimum 25 examples in train_goldens (more examples = better adaptation)
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
        2. Include examples for best results (25 minimum)
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
              subscription tier (Free: 1, Starter: 3, Startup: 5, Enterprise: 10)

          template: User message template with placeholders for fields. Use curly braces for field
              substitution

          goldens: Training examples (legacy parameter). Use train_goldens and test_goldens for
              better control. Minimum 25 examples

          origin_model: Model for specifying an LLM provider in API requests.

          origin_model_evaluation_score: Optional baseline score for the origin model. If provided, can skip origin model
              evaluation

          test_goldens: Test examples for evaluation. Required if train_goldens is provided. Used to
              measure final performance on held-out data

          train_goldens: Training examples for prompt optimization. Minimum 25 examples required. Cannot
              be used with 'goldens' parameter

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
                adapt_create_params.AdaptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptCreateResponse,
        )

    def get_costs(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptGetCostsResponse:
        """
        Get LLM usage costs for a specific prompt adaptation run.

        This endpoint returns the total cost and detailed usage records for all LLM
        requests made during a prompt adaptation run. Use this to track costs associated
        with optimizing prompts for different target models.

        **Cost Breakdown:**

        - Total cost across all models used in the adaptation
        - Individual usage records with provider, model, tokens, and costs
        - Timestamps for each LLM request
        - Task type (e.g., optimization, evaluation)

        **Access Control:**

        - Only accessible by the user who created the adaptation run
        - Requires prompt adaptation access

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return self._get(
            f"/v2/prompt/adapt/{adaptation_run_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptGetCostsResponse,
        )


class AsyncAdaptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdaptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdaptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdaptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncAdaptResourceWithStreamingResponse(self)

    async def create(
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
        test_goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        train_goldens: Optional[Iterable[GoldenRecordParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptCreateResponse:
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

        - Minimum 25 examples in train_goldens (more examples = better adaptation)
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
        2. Include examples for best results (25 minimum)
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
              subscription tier (Free: 1, Starter: 3, Startup: 5, Enterprise: 10)

          template: User message template with placeholders for fields. Use curly braces for field
              substitution

          goldens: Training examples (legacy parameter). Use train_goldens and test_goldens for
              better control. Minimum 25 examples

          origin_model: Model for specifying an LLM provider in API requests.

          origin_model_evaluation_score: Optional baseline score for the origin model. If provided, can skip origin model
              evaluation

          test_goldens: Test examples for evaluation. Required if train_goldens is provided. Used to
              measure final performance on held-out data

          train_goldens: Training examples for prompt optimization. Minimum 25 examples required. Cannot
              be used with 'goldens' parameter

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
                adapt_create_params.AdaptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptCreateResponse,
        )

    async def get_costs(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptGetCostsResponse:
        """
        Get LLM usage costs for a specific prompt adaptation run.

        This endpoint returns the total cost and detailed usage records for all LLM
        requests made during a prompt adaptation run. Use this to track costs associated
        with optimizing prompts for different target models.

        **Cost Breakdown:**

        - Total cost across all models used in the adaptation
        - Individual usage records with provider, model, tokens, and costs
        - Timestamps for each LLM request
        - Task type (e.g., optimization, evaluation)

        **Access Control:**

        - Only accessible by the user who created the adaptation run
        - Requires prompt adaptation access

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return await self._get(
            f"/v2/prompt/adapt/{adaptation_run_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptGetCostsResponse,
        )


class AdaptResourceWithRawResponse:
    def __init__(self, adapt: AdaptResource) -> None:
        self._adapt = adapt

        self.create = to_raw_response_wrapper(
            adapt.create,
        )
        self.get_costs = to_raw_response_wrapper(
            adapt.get_costs,
        )


class AsyncAdaptResourceWithRawResponse:
    def __init__(self, adapt: AsyncAdaptResource) -> None:
        self._adapt = adapt

        self.create = async_to_raw_response_wrapper(
            adapt.create,
        )
        self.get_costs = async_to_raw_response_wrapper(
            adapt.get_costs,
        )


class AdaptResourceWithStreamingResponse:
    def __init__(self, adapt: AdaptResource) -> None:
        self._adapt = adapt

        self.create = to_streamed_response_wrapper(
            adapt.create,
        )
        self.get_costs = to_streamed_response_wrapper(
            adapt.get_costs,
        )


class AsyncAdaptResourceWithStreamingResponse:
    def __init__(self, adapt: AsyncAdaptResource) -> None:
        self._adapt = adapt

        self.create = async_to_streamed_response_wrapper(
            adapt.create,
        )
        self.get_costs = async_to_streamed_response_wrapper(
            adapt.get_costs,
        )
