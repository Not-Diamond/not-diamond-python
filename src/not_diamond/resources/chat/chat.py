# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from .arena import (
    ArenaResource,
    AsyncArenaResource,
    ArenaResourceWithRawResponse,
    AsyncArenaResourceWithRawResponse,
    ArenaResourceWithStreamingResponse,
    AsyncArenaResourceWithStreamingResponse,
)
from .report import (
    ReportResource,
    AsyncReportResource,
    ReportResourceWithRawResponse,
    AsyncReportResourceWithRawResponse,
    ReportResourceWithStreamingResponse,
    AsyncReportResourceWithStreamingResponse,
)
from ...types import chat_select_model_params
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
from .preferences import (
    PreferencesResource,
    AsyncPreferencesResource,
    PreferencesResourceWithRawResponse,
    AsyncPreferencesResourceWithRawResponse,
    PreferencesResourceWithStreamingResponse,
    AsyncPreferencesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def preferences(self) -> PreferencesResource:
        return PreferencesResource(self._client)

    @cached_property
    def report(self) -> ReportResource:
        return ReportResource(self._client)

    @cached_property
    def arena(self) -> ArenaResource:
        return ArenaResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def select_model(
        self,
        *,
        llm_providers: Iterable[chat_select_model_params.LlmProvider],
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
        Token Model Select V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/chat/modelSelect",
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
                chat_select_model_params.ChatSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        return AsyncPreferencesResource(self._client)

    @cached_property
    def report(self) -> AsyncReportResource:
        return AsyncReportResource(self._client)

    @cached_property
    def arena(self) -> AsyncArenaResource:
        return AsyncArenaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def select_model(
        self,
        *,
        llm_providers: Iterable[chat_select_model_params.LlmProvider],
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
        Token Model Select V2

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/chat/modelSelect",
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
                chat_select_model_params.ChatSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.select_model = to_raw_response_wrapper(
            chat.select_model,
        )

    @cached_property
    def preferences(self) -> PreferencesResourceWithRawResponse:
        return PreferencesResourceWithRawResponse(self._chat.preferences)

    @cached_property
    def report(self) -> ReportResourceWithRawResponse:
        return ReportResourceWithRawResponse(self._chat.report)

    @cached_property
    def arena(self) -> ArenaResourceWithRawResponse:
        return ArenaResourceWithRawResponse(self._chat.arena)


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.select_model = async_to_raw_response_wrapper(
            chat.select_model,
        )

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithRawResponse:
        return AsyncPreferencesResourceWithRawResponse(self._chat.preferences)

    @cached_property
    def report(self) -> AsyncReportResourceWithRawResponse:
        return AsyncReportResourceWithRawResponse(self._chat.report)

    @cached_property
    def arena(self) -> AsyncArenaResourceWithRawResponse:
        return AsyncArenaResourceWithRawResponse(self._chat.arena)


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.select_model = to_streamed_response_wrapper(
            chat.select_model,
        )

    @cached_property
    def preferences(self) -> PreferencesResourceWithStreamingResponse:
        return PreferencesResourceWithStreamingResponse(self._chat.preferences)

    @cached_property
    def report(self) -> ReportResourceWithStreamingResponse:
        return ReportResourceWithStreamingResponse(self._chat.report)

    @cached_property
    def arena(self) -> ArenaResourceWithStreamingResponse:
        return ArenaResourceWithStreamingResponse(self._chat.arena)


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.select_model = async_to_streamed_response_wrapper(
            chat.select_model,
        )

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithStreamingResponse:
        return AsyncPreferencesResourceWithStreamingResponse(self._chat.preferences)

    @cached_property
    def report(self) -> AsyncReportResourceWithStreamingResponse:
        return AsyncReportResourceWithStreamingResponse(self._chat.report)

    @cached_property
    def arena(self) -> AsyncArenaResourceWithStreamingResponse:
        return AsyncArenaResourceWithStreamingResponse(self._chat.arena)
