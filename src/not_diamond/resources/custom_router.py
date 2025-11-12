# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from ..types import custom_router_train_custom_router_params
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
from ..types.custom_router_train_custom_router_response import CustomRouterTrainCustomRouterResponse

__all__ = ["CustomRouterResource", "AsyncCustomRouterResource"]


class CustomRouterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomRouterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return CustomRouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomRouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return CustomRouterResourceWithStreamingResponse(self)

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
    ) -> CustomRouterTrainCustomRouterResponse:
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
            body=maybe_transform(body, custom_router_train_custom_router_params.CustomRouterTrainCustomRouterParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomRouterTrainCustomRouterResponse,
        )


class AsyncCustomRouterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomRouterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomRouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomRouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncCustomRouterResourceWithStreamingResponse(self)

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
    ) -> CustomRouterTrainCustomRouterResponse:
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
            body=await async_maybe_transform(
                body, custom_router_train_custom_router_params.CustomRouterTrainCustomRouterParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomRouterTrainCustomRouterResponse,
        )


class CustomRouterResourceWithRawResponse:
    def __init__(self, custom_router: CustomRouterResource) -> None:
        self._custom_router = custom_router

        self.train_custom_router = to_raw_response_wrapper(
            custom_router.train_custom_router,
        )


class AsyncCustomRouterResourceWithRawResponse:
    def __init__(self, custom_router: AsyncCustomRouterResource) -> None:
        self._custom_router = custom_router

        self.train_custom_router = async_to_raw_response_wrapper(
            custom_router.train_custom_router,
        )


class CustomRouterResourceWithStreamingResponse:
    def __init__(self, custom_router: CustomRouterResource) -> None:
        self._custom_router = custom_router

        self.train_custom_router = to_streamed_response_wrapper(
            custom_router.train_custom_router,
        )


class AsyncCustomRouterResourceWithStreamingResponse:
    def __init__(self, custom_router: AsyncCustomRouterResource) -> None:
        self._custom_router = custom_router

        self.train_custom_router = async_to_streamed_response_wrapper(
            custom_router.train_custom_router,
        )
