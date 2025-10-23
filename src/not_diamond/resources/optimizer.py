# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from ..types import (
    optimizer_select_model_params,
    optimizer_select_hash_model_params,
    optimizer_select_userid_model_params,
    optimizer_get_frontend_arena_models_params,
    optimizer_select_frontend_hash_model_params,
)
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

__all__ = ["OptimizerResource", "AsyncOptimizerResource"]


class OptimizerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptimizerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return OptimizerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptimizerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return OptimizerResourceWithStreamingResponse(self)

    def get_frontend_arena_models(
        self,
        *,
        llm_providers: Iterable[optimizer_get_frontend_arena_models_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        user_id: str,
        x_token: str,
        hash_content: bool | Omit = omit,
        image_gen: bool | Omit = omit,
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
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._post(
            "/v2/optimizer/frontendArenaModels",
            body=maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "user_id": user_id,
                    "hash_content": hash_content,
                    "image_gen": image_gen,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                optimizer_get_frontend_arena_models_params.OptimizerGetFrontendArenaModelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def select_frontend_hash_model(
        self,
        *,
        llm_providers: Iterable[optimizer_select_frontend_hash_model_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        user_id: str,
        x_token: str,
        hash_content: bool | Omit = omit,
        image_gen: bool | Omit = omit,
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
        Frontend Hash Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._post(
            "/v2/optimizer/frontendHashModelSelect",
            body=maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "user_id": user_id,
                    "hash_content": hash_content,
                    "image_gen": image_gen,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                optimizer_select_frontend_hash_model_params.OptimizerSelectFrontendHashModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def select_hash_model(
        self,
        *,
        llm_providers: Iterable[optimizer_select_hash_model_params.LlmProvider],
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
        Hash Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/optimizer/hashModelSelect",
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
                optimizer_select_hash_model_params.OptimizerSelectHashModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def select_model(
        self,
        *,
        llm_providers: Iterable[optimizer_select_model_params.LlmProvider],
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
            "/v2/optimizer/modelSelect",
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
                optimizer_select_model_params.OptimizerSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, optimizer_select_model_params.OptimizerSelectModelParams),
            ),
            cast_to=object,
        )

    def select_userid_model(
        self,
        *,
        llm_providers: Iterable[optimizer_select_userid_model_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        user_id: str,
        x_token: str,
        hash_content: bool | Omit = omit,
        image_gen: bool | Omit = omit,
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
        Userid Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._post(
            "/v2/optimizer/userIDModelSelect",
            body=maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "user_id": user_id,
                    "hash_content": hash_content,
                    "image_gen": image_gen,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                optimizer_select_userid_model_params.OptimizerSelectUseridModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOptimizerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptimizerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptimizerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptimizerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncOptimizerResourceWithStreamingResponse(self)

    async def get_frontend_arena_models(
        self,
        *,
        llm_providers: Iterable[optimizer_get_frontend_arena_models_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        user_id: str,
        x_token: str,
        hash_content: bool | Omit = omit,
        image_gen: bool | Omit = omit,
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
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._post(
            "/v2/optimizer/frontendArenaModels",
            body=await async_maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "user_id": user_id,
                    "hash_content": hash_content,
                    "image_gen": image_gen,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                optimizer_get_frontend_arena_models_params.OptimizerGetFrontendArenaModelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def select_frontend_hash_model(
        self,
        *,
        llm_providers: Iterable[optimizer_select_frontend_hash_model_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        user_id: str,
        x_token: str,
        hash_content: bool | Omit = omit,
        image_gen: bool | Omit = omit,
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
        Frontend Hash Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._post(
            "/v2/optimizer/frontendHashModelSelect",
            body=await async_maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "user_id": user_id,
                    "hash_content": hash_content,
                    "image_gen": image_gen,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                optimizer_select_frontend_hash_model_params.OptimizerSelectFrontendHashModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def select_hash_model(
        self,
        *,
        llm_providers: Iterable[optimizer_select_hash_model_params.LlmProvider],
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
        Hash Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/optimizer/hashModelSelect",
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
                optimizer_select_hash_model_params.OptimizerSelectHashModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def select_model(
        self,
        *,
        llm_providers: Iterable[optimizer_select_model_params.LlmProvider],
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
            "/v2/optimizer/modelSelect",
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
                optimizer_select_model_params.OptimizerSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, optimizer_select_model_params.OptimizerSelectModelParams
                ),
            ),
            cast_to=object,
        )

    async def select_userid_model(
        self,
        *,
        llm_providers: Iterable[optimizer_select_userid_model_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        user_id: str,
        x_token: str,
        hash_content: bool | Omit = omit,
        image_gen: bool | Omit = omit,
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
        Userid Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._post(
            "/v2/optimizer/userIDModelSelect",
            body=await async_maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "user_id": user_id,
                    "hash_content": hash_content,
                    "image_gen": image_gen,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                optimizer_select_userid_model_params.OptimizerSelectUseridModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OptimizerResourceWithRawResponse:
    def __init__(self, optimizer: OptimizerResource) -> None:
        self._optimizer = optimizer

        self.get_frontend_arena_models = to_raw_response_wrapper(
            optimizer.get_frontend_arena_models,
        )
        self.select_frontend_hash_model = to_raw_response_wrapper(
            optimizer.select_frontend_hash_model,
        )
        self.select_hash_model = to_raw_response_wrapper(
            optimizer.select_hash_model,
        )
        self.select_model = to_raw_response_wrapper(
            optimizer.select_model,
        )
        self.select_userid_model = to_raw_response_wrapper(
            optimizer.select_userid_model,
        )


class AsyncOptimizerResourceWithRawResponse:
    def __init__(self, optimizer: AsyncOptimizerResource) -> None:
        self._optimizer = optimizer

        self.get_frontend_arena_models = async_to_raw_response_wrapper(
            optimizer.get_frontend_arena_models,
        )
        self.select_frontend_hash_model = async_to_raw_response_wrapper(
            optimizer.select_frontend_hash_model,
        )
        self.select_hash_model = async_to_raw_response_wrapper(
            optimizer.select_hash_model,
        )
        self.select_model = async_to_raw_response_wrapper(
            optimizer.select_model,
        )
        self.select_userid_model = async_to_raw_response_wrapper(
            optimizer.select_userid_model,
        )


class OptimizerResourceWithStreamingResponse:
    def __init__(self, optimizer: OptimizerResource) -> None:
        self._optimizer = optimizer

        self.get_frontend_arena_models = to_streamed_response_wrapper(
            optimizer.get_frontend_arena_models,
        )
        self.select_frontend_hash_model = to_streamed_response_wrapper(
            optimizer.select_frontend_hash_model,
        )
        self.select_hash_model = to_streamed_response_wrapper(
            optimizer.select_hash_model,
        )
        self.select_model = to_streamed_response_wrapper(
            optimizer.select_model,
        )
        self.select_userid_model = to_streamed_response_wrapper(
            optimizer.select_userid_model,
        )


class AsyncOptimizerResourceWithStreamingResponse:
    def __init__(self, optimizer: AsyncOptimizerResource) -> None:
        self._optimizer = optimizer

        self.get_frontend_arena_models = async_to_streamed_response_wrapper(
            optimizer.get_frontend_arena_models,
        )
        self.select_frontend_hash_model = async_to_streamed_response_wrapper(
            optimizer.select_frontend_hash_model,
        )
        self.select_hash_model = async_to_streamed_response_wrapper(
            optimizer.select_hash_model,
        )
        self.select_model = async_to_streamed_response_wrapper(
            optimizer.select_model,
        )
        self.select_userid_model = async_to_streamed_response_wrapper(
            optimizer.select_userid_model,
        )
