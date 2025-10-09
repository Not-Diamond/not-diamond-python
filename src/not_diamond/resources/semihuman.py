# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from ..types import semihuman_route_params
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
from ..types.semihuman_route_response import SemihumanRouteResponse

__all__ = ["SemihumanResource", "AsyncSemihumanResource"]


class SemihumanResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SemihumanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return SemihumanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SemihumanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return SemihumanResourceWithStreamingResponse(self)

    def route(
        self,
        *,
        llm_providers: Iterable[semihuman_route_params.LlmProvider],
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
    ) -> SemihumanRouteResponse:
        """
        Route Semihuman

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/semihuman/modelSelect",
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
                semihuman_route_params.SemihumanRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SemihumanRouteResponse,
        )


class AsyncSemihumanResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSemihumanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSemihumanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSemihumanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return AsyncSemihumanResourceWithStreamingResponse(self)

    async def route(
        self,
        *,
        llm_providers: Iterable[semihuman_route_params.LlmProvider],
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
    ) -> SemihumanRouteResponse:
        """
        Route Semihuman

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/semihuman/modelSelect",
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
                semihuman_route_params.SemihumanRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SemihumanRouteResponse,
        )


class SemihumanResourceWithRawResponse:
    def __init__(self, semihuman: SemihumanResource) -> None:
        self._semihuman = semihuman

        self.route = to_raw_response_wrapper(
            semihuman.route,
        )


class AsyncSemihumanResourceWithRawResponse:
    def __init__(self, semihuman: AsyncSemihumanResource) -> None:
        self._semihuman = semihuman

        self.route = async_to_raw_response_wrapper(
            semihuman.route,
        )


class SemihumanResourceWithStreamingResponse:
    def __init__(self, semihuman: SemihumanResource) -> None:
        self._semihuman = semihuman

        self.route = to_streamed_response_wrapper(
            semihuman.route,
        )


class AsyncSemihumanResourceWithStreamingResponse:
    def __init__(self, semihuman: AsyncSemihumanResource) -> None:
        self._semihuman = semihuman

        self.route = async_to_streamed_response_wrapper(
            semihuman.route,
        )
