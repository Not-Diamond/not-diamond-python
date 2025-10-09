# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chat import arena_create_choice_params, arena_create_models_params
from ..._base_client import make_request_options
from ...types.report.request_provider_param import RequestProviderParam

__all__ = ["ArenaResource", "AsyncArenaResource"]


class ArenaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArenaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return ArenaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArenaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return ArenaResourceWithStreamingResponse(self)

    def create_choice(
        self,
        *,
        preferred_provider: RequestProviderParam,
        rejected_provider: RequestProviderParam,
        session_id: str,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Frontend Arena Choice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/chat/arena/arenaChoice",
            body=maybe_transform(
                {
                    "preferred_provider": preferred_provider,
                    "rejected_provider": rejected_provider,
                    "session_id": session_id,
                    "user_id": user_id,
                },
                arena_create_choice_params.ArenaCreateChoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_models(
        self,
        *,
        llm_providers: Iterable[arena_create_models_params.LlmProvider],
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
        Frontend Arena Models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/chat/arena/arenaModels",
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
                arena_create_models_params.ArenaCreateModelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncArenaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArenaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArenaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArenaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return AsyncArenaResourceWithStreamingResponse(self)

    async def create_choice(
        self,
        *,
        preferred_provider: RequestProviderParam,
        rejected_provider: RequestProviderParam,
        session_id: str,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Frontend Arena Choice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/chat/arena/arenaChoice",
            body=await async_maybe_transform(
                {
                    "preferred_provider": preferred_provider,
                    "rejected_provider": rejected_provider,
                    "session_id": session_id,
                    "user_id": user_id,
                },
                arena_create_choice_params.ArenaCreateChoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_models(
        self,
        *,
        llm_providers: Iterable[arena_create_models_params.LlmProvider],
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
        Frontend Arena Models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/chat/arena/arenaModels",
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
                arena_create_models_params.ArenaCreateModelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ArenaResourceWithRawResponse:
    def __init__(self, arena: ArenaResource) -> None:
        self._arena = arena

        self.create_choice = to_raw_response_wrapper(
            arena.create_choice,
        )
        self.create_models = to_raw_response_wrapper(
            arena.create_models,
        )


class AsyncArenaResourceWithRawResponse:
    def __init__(self, arena: AsyncArenaResource) -> None:
        self._arena = arena

        self.create_choice = async_to_raw_response_wrapper(
            arena.create_choice,
        )
        self.create_models = async_to_raw_response_wrapper(
            arena.create_models,
        )


class ArenaResourceWithStreamingResponse:
    def __init__(self, arena: ArenaResource) -> None:
        self._arena = arena

        self.create_choice = to_streamed_response_wrapper(
            arena.create_choice,
        )
        self.create_models = to_streamed_response_wrapper(
            arena.create_models,
        )


class AsyncArenaResourceWithStreamingResponse:
    def __init__(self, arena: AsyncArenaResource) -> None:
        self._arena = arena

        self.create_choice = async_to_streamed_response_wrapper(
            arena.create_choice,
        )
        self.create_models = async_to_streamed_response_wrapper(
            arena.create_models,
        )
