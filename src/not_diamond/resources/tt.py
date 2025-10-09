# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import tt_translate_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.report.request_provider_param import RequestProviderParam

__all__ = ["TtResource", "AsyncTtResource"]


class TtResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TtResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return TtResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TtResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return TtResourceWithStreamingResponse(self)

    def translate(
        self,
        *,
        llm_providers: Iterable[RequestProviderParam],
        messages: Iterable[Dict[str, str]],
        source_language: str,
        target_language: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Tt Translation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/TT/translate",
            body=maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "source_language": source_language,
                    "target_language": target_language,
                },
                tt_translate_params.TtTranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTtResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTtResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTtResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTtResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncTtResourceWithStreamingResponse(self)

    async def translate(
        self,
        *,
        llm_providers: Iterable[RequestProviderParam],
        messages: Iterable[Dict[str, str]],
        source_language: str,
        target_language: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Tt Translation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/TT/translate",
            body=await async_maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "source_language": source_language,
                    "target_language": target_language,
                },
                tt_translate_params.TtTranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TtResourceWithRawResponse:
    def __init__(self, tt: TtResource) -> None:
        self._tt = tt

        self.translate = to_raw_response_wrapper(
            tt.translate,
        )


class AsyncTtResourceWithRawResponse:
    def __init__(self, tt: AsyncTtResource) -> None:
        self._tt = tt

        self.translate = async_to_raw_response_wrapper(
            tt.translate,
        )


class TtResourceWithStreamingResponse:
    def __init__(self, tt: TtResource) -> None:
        self._tt = tt

        self.translate = to_streamed_response_wrapper(
            tt.translate,
        )


class AsyncTtResourceWithStreamingResponse:
    def __init__(self, tt: AsyncTtResource) -> None:
        self._tt = tt

        self.translate = async_to_streamed_response_wrapper(
            tt.translate,
        )
