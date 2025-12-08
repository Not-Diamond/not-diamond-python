# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from ..types import model_router_select_model_params
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
from ..types.model_router_select_model_response import ModelRouterSelectModelResponse

__all__ = ["ModelRouterResource", "AsyncModelRouterResource"]


class ModelRouterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelRouterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return ModelRouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelRouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return ModelRouterResourceWithStreamingResponse(self)

    def select_model(
        self,
        *,
        llm_providers: Iterable[model_router_select_model_params.LlmProvider],
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
    ) -> ModelRouterSelectModelResponse:
        """
        Select the optimal LLM to handle your query based on Not Diamond's routing
        algorithm.

        This endpoint analyzes your messages and returns the best-suited model from your
        specified models. The router considers factors like query complexity, model
        capabilities, cost, and latency based on your preferences.

        **Key Features:**

        - Intelligent routing across multiple LLM providers
        - Support for custom routers trained on your evaluation data
        - Optional cost/latency optimization
        - Function calling support for compatible models

        **Usage:**

        1. Pass your messages in OpenAI format (array of objects with 'role' and
           'content')
        2. Specify which LLM providers you want to route between
        3. Optionally provide a preference_id to use a custom router that you've trained
        4. Receive a recommended model and session_id
        5. Use the session_id to submit feedback and improve routing

        **Related Endpoints:**

        - `POST /v2/preferences/userPreferenceCreate` - Create a preference ID for
          personalized routing
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
                model_router_select_model_params.ModelRouterSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, model_router_select_model_params.ModelRouterSelectModelParams),
            ),
            cast_to=ModelRouterSelectModelResponse,
        )


class AsyncModelRouterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelRouterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelRouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelRouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncModelRouterResourceWithStreamingResponse(self)

    async def select_model(
        self,
        *,
        llm_providers: Iterable[model_router_select_model_params.LlmProvider],
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
    ) -> ModelRouterSelectModelResponse:
        """
        Select the optimal LLM to handle your query based on Not Diamond's routing
        algorithm.

        This endpoint analyzes your messages and returns the best-suited model from your
        specified models. The router considers factors like query complexity, model
        capabilities, cost, and latency based on your preferences.

        **Key Features:**

        - Intelligent routing across multiple LLM providers
        - Support for custom routers trained on your evaluation data
        - Optional cost/latency optimization
        - Function calling support for compatible models

        **Usage:**

        1. Pass your messages in OpenAI format (array of objects with 'role' and
           'content')
        2. Specify which LLM providers you want to route between
        3. Optionally provide a preference_id to use a custom router that you've trained
        4. Receive a recommended model and session_id
        5. Use the session_id to submit feedback and improve routing

        **Related Endpoints:**

        - `POST /v2/preferences/userPreferenceCreate` - Create a preference ID for
          personalized routing
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
                model_router_select_model_params.ModelRouterSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, model_router_select_model_params.ModelRouterSelectModelParams
                ),
            ),
            cast_to=ModelRouterSelectModelResponse,
        )


class ModelRouterResourceWithRawResponse:
    def __init__(self, model_router: ModelRouterResource) -> None:
        self._model_router = model_router

        self.select_model = to_raw_response_wrapper(
            model_router.select_model,
        )


class AsyncModelRouterResourceWithRawResponse:
    def __init__(self, model_router: AsyncModelRouterResource) -> None:
        self._model_router = model_router

        self.select_model = async_to_raw_response_wrapper(
            model_router.select_model,
        )


class ModelRouterResourceWithStreamingResponse:
    def __init__(self, model_router: ModelRouterResource) -> None:
        self._model_router = model_router

        self.select_model = to_streamed_response_wrapper(
            model_router.select_model,
        )


class AsyncModelRouterResourceWithStreamingResponse:
    def __init__(self, model_router: AsyncModelRouterResource) -> None:
        self._model_router = model_router

        self.select_model = async_to_streamed_response_wrapper(
            model_router.select_model,
        )
