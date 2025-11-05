# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import model_router_select_model_params, model_router_open_hands_select_params
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

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return ModelRouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelRouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return ModelRouterResourceWithStreamingResponse(self)

    def open_hands_select(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Openhands Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/modelRouter/openHandsRouter",
            body=maybe_transform(body, model_router_open_hands_select_params.ModelRouterOpenHandsSelectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def select_model(
        self,
        *,
        body: object,
        type: Optional[str] | Omit = omit,
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
          type: Optional format type. Use 'openrouter' to accept and return OpenRouter-format
              model identifiers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/modelRouter/modelSelect",
            body=maybe_transform(body, model_router_select_model_params.ModelRouterSelectModelParams),
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

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelRouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelRouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return AsyncModelRouterResourceWithStreamingResponse(self)

    async def open_hands_select(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Openhands Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/modelRouter/openHandsRouter",
            body=await async_maybe_transform(
                body, model_router_open_hands_select_params.ModelRouterOpenHandsSelectParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def select_model(
        self,
        *,
        body: object,
        type: Optional[str] | Omit = omit,
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
          type: Optional format type. Use 'openrouter' to accept and return OpenRouter-format
              model identifiers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/modelRouter/modelSelect",
            body=await async_maybe_transform(body, model_router_select_model_params.ModelRouterSelectModelParams),
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

        self.open_hands_select = to_raw_response_wrapper(
            model_router.open_hands_select,
        )
        self.select_model = to_raw_response_wrapper(
            model_router.select_model,
        )


class AsyncModelRouterResourceWithRawResponse:
    def __init__(self, model_router: AsyncModelRouterResource) -> None:
        self._model_router = model_router

        self.open_hands_select = async_to_raw_response_wrapper(
            model_router.open_hands_select,
        )
        self.select_model = async_to_raw_response_wrapper(
            model_router.select_model,
        )


class ModelRouterResourceWithStreamingResponse:
    def __init__(self, model_router: ModelRouterResource) -> None:
        self._model_router = model_router

        self.open_hands_select = to_streamed_response_wrapper(
            model_router.open_hands_select,
        )
        self.select_model = to_streamed_response_wrapper(
            model_router.select_model,
        )


class AsyncModelRouterResourceWithStreamingResponse:
    def __init__(self, model_router: AsyncModelRouterResource) -> None:
        self._model_router = model_router

        self.open_hands_select = async_to_streamed_response_wrapper(
            model_router.open_hands_select,
        )
        self.select_model = async_to_streamed_response_wrapper(
            model_router.select_model,
        )
