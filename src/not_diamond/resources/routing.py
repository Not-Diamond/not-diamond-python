# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, Optional, cast

import httpx

from ..types import (
    routing_select_model_params,
    routing_train_custom_router_params,
    routing_create_survey_response_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.routing_select_model_response import RoutingSelectModelResponse
from ..types.routing_train_custom_router_response import RoutingTrainCustomRouterResponse

__all__ = ["RoutingResource", "AsyncRoutingResource"]


class RoutingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return RoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return RoutingResourceWithStreamingResponse(self)

    def create_survey_response(
        self,
        *,
        constraint_priorities: str,
        email: str,
        llm_providers: str,
        use_case_desc: str,
        user_id: str,
        x_token: str,
        additional_preferences: Optional[str] | Omit = omit,
        dataset_file: Optional[FileTypes] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt_file: Optional[FileTypes] | Omit = omit,
        prompts: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Survey Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "constraint_priorities": constraint_priorities,
                "email": email,
                "llm_providers": llm_providers,
                "use_case_desc": use_case_desc,
                "user_id": user_id,
                "additional_preferences": additional_preferences,
                "dataset_file": dataset_file,
                "name": name,
                "prompt_file": prompt_file,
                "prompts": prompts,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["prompt_file"], ["dataset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            "/v2/pzn/surveyResponse",
            body=maybe_transform(body, routing_create_survey_response_params.RoutingCreateSurveyResponseParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def select_model(
        self,
        *,
        llm_providers: Iterable[routing_select_model_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        type: Optional[str] | Omit = omit,
        hash_content: bool | Omit = omit,
        max_model_depth: Optional[int] | Omit = omit,
        metric: str | Omit = omit,
        preference_id: Optional[str] | Omit = omit,
        previous_session: Optional[str] | Omit = omit,
        tools: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        tradeoff: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingSelectModelResponse:
        """
        Select the optimal LLM to handle your query based on Not Diamond's routing
        algorithm.

        This endpoint analyzes your messages and returns the best-suited model from your
        specified providers. The router considers factors like query complexity, model
        capabilities, cost, and latency based on your preferences.

        **Key Features:**

        - Intelligent routing across multiple LLM providers
        - Support for custom routers trained on your evaluation data
        - Optional cost/latency optimization
        - Function calling support for compatible models
        - Privacy-preserving content hashing

        **Usage:**

        1. Pass your messages in OpenAI format (array of objects with 'role' and
           'content')
        2. Specify which LLM providers you want to route between
        3. Optionally provide a preference_id for personalized routing
        4. Receive a recommended model and session_id
        5. Use the session_id to submit feedback and improve routing

        **Related Endpoints:**

        - `POST /v2/preferences/userPreferenceCreate` - Create a preference ID for
          personalized routing
        - `POST /v2/report/metrics/feedback` - Submit feedback on routing decisions
        - `POST /v2/pzn/trainCustomRouter` - Train a custom router on your evaluation
          data

        Args:
          llm_providers: List of LLM providers to route between. Specify at least one provider in format
              {provider, model}

          messages: Array of message objects in OpenAI format (with 'role' and 'content' keys)

          type: Optional format type. Use 'openrouter' to accept and return OpenRouter-format
              model identifiers

          hash_content: Whether to hash message content for privacy

          max_model_depth: Maximum number of models to consider for routing. If not specified, considers
              all provided models

          metric: Optimization metric for model selection

          preference_id: Preference ID for personalized routing. Create one via POST
              /v2/preferences/userPreferenceCreate

          previous_session: Previous session ID to link related requests

          tools: OpenAI-format function calling tools

          tradeoff: Optimization tradeoff strategy. Use 'cost' to prioritize cost savings or
              'latency' to prioritize speed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/modelRouter/modelSelect",
            body=maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "hash_content": hash_content,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                routing_select_model_params.RoutingSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, routing_select_model_params.RoutingSelectModelParams),
            ),
            cast_to=RoutingSelectModelResponse,
        )

    def train_custom_router(
        self,
        *,
        dataset_file: FileTypes,
        language: str,
        llm_providers: str,
        maximize: bool,
        prompt_column: str,
        override: Optional[bool] | Omit = omit,
        preference_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingTrainCustomRouterResponse:
        """
        Train a custom router on your evaluation data to optimize routing for your
        specific use case.

        This endpoint allows you to train a domain-specific router that learns which
        models perform best for different types of queries in your application. The
        router analyzes your evaluation dataset, clusters similar queries, and learns
        model performance patterns.

        **Training Process:**

        1. Upload a CSV file with your evaluation data
        2. Specify which models to route between
        3. Define the evaluation metric (score column)
        4. The system trains asynchronously and returns a preference_id
        5. Use the preference_id in model_select() calls once training completes

        **Dataset Requirements:**

        - Format: CSV file
        - Minimum samples: 25 (more is better for accuracy)
        - Required columns:
          - Prompt column (specified in prompt_column parameter)
          - For each model: `{provider}/{model}/score` and `{provider}/{model}/response`

        **Example CSV structure:**

        ```
        prompt,openai/gpt-4o/score,openai/gpt-4o/response,anthropic/claude-sonnet-4-5-20250929/score,anthropic/claude-sonnet-4-5-20250929/response
        "Explain quantum computing",0.95,"Quantum computing uses...",0.87,"Quantum computers leverage..."
        "Write a Python function",0.82,"def my_function()...",0.91,"Here's a Python function..."
        ```

        **Model Selection:**

        - Specify standard models: `{"provider": "openai", "model": "gpt-4o"}`
        - Or custom models with pricing:
          `{"provider": "custom", "model": "my-model", "is_custom": true, "input_price": 10.0, "output_price": 30.0, "context_length": 8192, "latency": 1.5}`

        **Training Time:**

        - Training is asynchronous and typically takes 5-15 minutes
        - Larger datasets or more models take longer
        - You'll receive a preference_id immediately
        - Check training status by attempting to use the preference_id in model_select()

        **Best Practices:**

        1. Use diverse, representative examples from your production workload
        2. Include at least 50-100 samples for best results
        3. Ensure consistent evaluation metrics across all models
        4. Use the same models you plan to route between in production

        **Related Documentation:** See
        https://docs.notdiamond.ai/docs/adapting-prompts-to-new-models for detailed
        guide.

        Args:
          dataset_file: CSV file containing evaluation data with prompt column and score/response
              columns for each model

          language: Language of the evaluation data. Use 'english' for English-only data or
              'multilingual' for multi-language support

          llm_providers:
              JSON string array of LLM providers to train the router on. Format:
              '[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model":
              "claude-sonnet-4-5-20250929"}]'

          maximize: Whether higher scores are better. Set to true if higher scores indicate better
              performance, false otherwise

          prompt_column: Name of the column in the CSV file that contains the prompts

          override: Whether to override an existing custom router for this preference_id

          preference_id: Optional preference ID to update an existing router. If not provided, a new
              preference will be created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "dataset_file": dataset_file,
                "language": language,
                "llm_providers": llm_providers,
                "maximize": maximize,
                "prompt_column": prompt_column,
                "override": override,
                "preference_id": preference_id,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["dataset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v2/pzn/trainCustomRouter",
            body=maybe_transform(body, routing_train_custom_router_params.RoutingTrainCustomRouterParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingTrainCustomRouterResponse,
        )


class AsyncRoutingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncRoutingResourceWithStreamingResponse(self)

    async def create_survey_response(
        self,
        *,
        constraint_priorities: str,
        email: str,
        llm_providers: str,
        use_case_desc: str,
        user_id: str,
        x_token: str,
        additional_preferences: Optional[str] | Omit = omit,
        dataset_file: Optional[FileTypes] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt_file: Optional[FileTypes] | Omit = omit,
        prompts: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Survey Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "constraint_priorities": constraint_priorities,
                "email": email,
                "llm_providers": llm_providers,
                "use_case_desc": use_case_desc,
                "user_id": user_id,
                "additional_preferences": additional_preferences,
                "dataset_file": dataset_file,
                "name": name,
                "prompt_file": prompt_file,
                "prompts": prompts,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["prompt_file"], ["dataset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            "/v2/pzn/surveyResponse",
            body=await async_maybe_transform(
                body, routing_create_survey_response_params.RoutingCreateSurveyResponseParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def select_model(
        self,
        *,
        llm_providers: Iterable[routing_select_model_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        type: Optional[str] | Omit = omit,
        hash_content: bool | Omit = omit,
        max_model_depth: Optional[int] | Omit = omit,
        metric: str | Omit = omit,
        preference_id: Optional[str] | Omit = omit,
        previous_session: Optional[str] | Omit = omit,
        tools: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        tradeoff: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingSelectModelResponse:
        """
        Select the optimal LLM to handle your query based on Not Diamond's routing
        algorithm.

        This endpoint analyzes your messages and returns the best-suited model from your
        specified providers. The router considers factors like query complexity, model
        capabilities, cost, and latency based on your preferences.

        **Key Features:**

        - Intelligent routing across multiple LLM providers
        - Support for custom routers trained on your evaluation data
        - Optional cost/latency optimization
        - Function calling support for compatible models
        - Privacy-preserving content hashing

        **Usage:**

        1. Pass your messages in OpenAI format (array of objects with 'role' and
           'content')
        2. Specify which LLM providers you want to route between
        3. Optionally provide a preference_id for personalized routing
        4. Receive a recommended model and session_id
        5. Use the session_id to submit feedback and improve routing

        **Related Endpoints:**

        - `POST /v2/preferences/userPreferenceCreate` - Create a preference ID for
          personalized routing
        - `POST /v2/report/metrics/feedback` - Submit feedback on routing decisions
        - `POST /v2/pzn/trainCustomRouter` - Train a custom router on your evaluation
          data

        Args:
          llm_providers: List of LLM providers to route between. Specify at least one provider in format
              {provider, model}

          messages: Array of message objects in OpenAI format (with 'role' and 'content' keys)

          type: Optional format type. Use 'openrouter' to accept and return OpenRouter-format
              model identifiers

          hash_content: Whether to hash message content for privacy

          max_model_depth: Maximum number of models to consider for routing. If not specified, considers
              all provided models

          metric: Optimization metric for model selection

          preference_id: Preference ID for personalized routing. Create one via POST
              /v2/preferences/userPreferenceCreate

          previous_session: Previous session ID to link related requests

          tools: OpenAI-format function calling tools

          tradeoff: Optimization tradeoff strategy. Use 'cost' to prioritize cost savings or
              'latency' to prioritize speed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/modelRouter/modelSelect",
            body=await async_maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "hash_content": hash_content,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                routing_select_model_params.RoutingSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, routing_select_model_params.RoutingSelectModelParams),
            ),
            cast_to=RoutingSelectModelResponse,
        )

    async def train_custom_router(
        self,
        *,
        dataset_file: FileTypes,
        language: str,
        llm_providers: str,
        maximize: bool,
        prompt_column: str,
        override: Optional[bool] | Omit = omit,
        preference_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoutingTrainCustomRouterResponse:
        """
        Train a custom router on your evaluation data to optimize routing for your
        specific use case.

        This endpoint allows you to train a domain-specific router that learns which
        models perform best for different types of queries in your application. The
        router analyzes your evaluation dataset, clusters similar queries, and learns
        model performance patterns.

        **Training Process:**

        1. Upload a CSV file with your evaluation data
        2. Specify which models to route between
        3. Define the evaluation metric (score column)
        4. The system trains asynchronously and returns a preference_id
        5. Use the preference_id in model_select() calls once training completes

        **Dataset Requirements:**

        - Format: CSV file
        - Minimum samples: 25 (more is better for accuracy)
        - Required columns:
          - Prompt column (specified in prompt_column parameter)
          - For each model: `{provider}/{model}/score` and `{provider}/{model}/response`

        **Example CSV structure:**

        ```
        prompt,openai/gpt-4o/score,openai/gpt-4o/response,anthropic/claude-sonnet-4-5-20250929/score,anthropic/claude-sonnet-4-5-20250929/response
        "Explain quantum computing",0.95,"Quantum computing uses...",0.87,"Quantum computers leverage..."
        "Write a Python function",0.82,"def my_function()...",0.91,"Here's a Python function..."
        ```

        **Model Selection:**

        - Specify standard models: `{"provider": "openai", "model": "gpt-4o"}`
        - Or custom models with pricing:
          `{"provider": "custom", "model": "my-model", "is_custom": true, "input_price": 10.0, "output_price": 30.0, "context_length": 8192, "latency": 1.5}`

        **Training Time:**

        - Training is asynchronous and typically takes 5-15 minutes
        - Larger datasets or more models take longer
        - You'll receive a preference_id immediately
        - Check training status by attempting to use the preference_id in model_select()

        **Best Practices:**

        1. Use diverse, representative examples from your production workload
        2. Include at least 50-100 samples for best results
        3. Ensure consistent evaluation metrics across all models
        4. Use the same models you plan to route between in production

        **Related Documentation:** See
        https://docs.notdiamond.ai/docs/adapting-prompts-to-new-models for detailed
        guide.

        Args:
          dataset_file: CSV file containing evaluation data with prompt column and score/response
              columns for each model

          language: Language of the evaluation data. Use 'english' for English-only data or
              'multilingual' for multi-language support

          llm_providers:
              JSON string array of LLM providers to train the router on. Format:
              '[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model":
              "claude-sonnet-4-5-20250929"}]'

          maximize: Whether higher scores are better. Set to true if higher scores indicate better
              performance, false otherwise

          prompt_column: Name of the column in the CSV file that contains the prompts

          override: Whether to override an existing custom router for this preference_id

          preference_id: Optional preference ID to update an existing router. If not provided, a new
              preference will be created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "dataset_file": dataset_file,
                "language": language,
                "llm_providers": llm_providers,
                "maximize": maximize,
                "prompt_column": prompt_column,
                "override": override,
                "preference_id": preference_id,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["dataset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v2/pzn/trainCustomRouter",
            body=await async_maybe_transform(body, routing_train_custom_router_params.RoutingTrainCustomRouterParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutingTrainCustomRouterResponse,
        )


class RoutingResourceWithRawResponse:
    def __init__(self, routing: RoutingResource) -> None:
        self._routing = routing

        self.create_survey_response = to_raw_response_wrapper(
            routing.create_survey_response,
        )
        self.select_model = to_raw_response_wrapper(
            routing.select_model,
        )
        self.train_custom_router = to_raw_response_wrapper(
            routing.train_custom_router,
        )


class AsyncRoutingResourceWithRawResponse:
    def __init__(self, routing: AsyncRoutingResource) -> None:
        self._routing = routing

        self.create_survey_response = async_to_raw_response_wrapper(
            routing.create_survey_response,
        )
        self.select_model = async_to_raw_response_wrapper(
            routing.select_model,
        )
        self.train_custom_router = async_to_raw_response_wrapper(
            routing.train_custom_router,
        )


class RoutingResourceWithStreamingResponse:
    def __init__(self, routing: RoutingResource) -> None:
        self._routing = routing

        self.create_survey_response = to_streamed_response_wrapper(
            routing.create_survey_response,
        )
        self.select_model = to_streamed_response_wrapper(
            routing.select_model,
        )
        self.train_custom_router = to_streamed_response_wrapper(
            routing.train_custom_router,
        )


class AsyncRoutingResourceWithStreamingResponse:
    def __init__(self, routing: AsyncRoutingResource) -> None:
        self._routing = routing

        self.create_survey_response = async_to_streamed_response_wrapper(
            routing.create_survey_response,
        )
        self.select_model = async_to_streamed_response_wrapper(
            routing.select_model,
        )
        self.train_custom_router = async_to_streamed_response_wrapper(
            routing.train_custom_router,
        )
