# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from ..types import model_router_select_model_params, model_router_select_open_hands_params
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

    def check_health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Simple health check endpoint with OTEL tracing"""
        return self._get(
            "/v2/modelRouter/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

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
    ) -> object:
        """
        Token Model Select

        Args:
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
            cast_to=object,
        )

    def select_open_hands(
        self,
        *,
        llm_providers: Iterable[model_router_select_open_hands_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
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
                model_router_select_open_hands_params.ModelRouterSelectOpenHandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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

    async def check_health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Simple health check endpoint with OTEL tracing"""
        return await self._get(
            "/v2/modelRouter/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

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
    ) -> object:
        """
        Token Model Select

        Args:
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
            cast_to=object,
        )

    async def select_open_hands(
        self,
        *,
        llm_providers: Iterable[model_router_select_open_hands_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
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
                model_router_select_open_hands_params.ModelRouterSelectOpenHandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ModelRouterResourceWithRawResponse:
    def __init__(self, model_router: ModelRouterResource) -> None:
        self._model_router = model_router

        self.check_health = to_raw_response_wrapper(
            model_router.check_health,
        )
        self.select_model = to_raw_response_wrapper(
            model_router.select_model,
        )
        self.select_open_hands = to_raw_response_wrapper(
            model_router.select_open_hands,
        )


class AsyncModelRouterResourceWithRawResponse:
    def __init__(self, model_router: AsyncModelRouterResource) -> None:
        self._model_router = model_router

        self.check_health = async_to_raw_response_wrapper(
            model_router.check_health,
        )
        self.select_model = async_to_raw_response_wrapper(
            model_router.select_model,
        )
        self.select_open_hands = async_to_raw_response_wrapper(
            model_router.select_open_hands,
        )


class ModelRouterResourceWithStreamingResponse:
    def __init__(self, model_router: ModelRouterResource) -> None:
        self._model_router = model_router

        self.check_health = to_streamed_response_wrapper(
            model_router.check_health,
        )
        self.select_model = to_streamed_response_wrapper(
            model_router.select_model,
        )
        self.select_open_hands = to_streamed_response_wrapper(
            model_router.select_open_hands,
        )


class AsyncModelRouterResourceWithStreamingResponse:
    def __init__(self, model_router: AsyncModelRouterResource) -> None:
        self._model_router = model_router

        self.check_health = async_to_streamed_response_wrapper(
            model_router.check_health,
        )
        self.select_model = async_to_streamed_response_wrapper(
            model_router.select_model,
        )
        self.select_open_hands = async_to_streamed_response_wrapper(
            model_router.select_open_hands,
        )
