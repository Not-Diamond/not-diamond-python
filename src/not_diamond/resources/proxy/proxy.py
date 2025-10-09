# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .secret import (
    SecretResource,
    AsyncSecretResource,
    SecretResourceWithRawResponse,
    AsyncSecretResourceWithRawResponse,
    SecretResourceWithStreamingResponse,
    AsyncSecretResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["ProxyResource", "AsyncProxyResource"]


class ProxyResource(SyncAPIResource):
    @cached_property
    def secret(self) -> SecretResource:
        return SecretResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProxyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return ProxyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return ProxyResourceWithStreamingResponse(self)

    def retrieve_auth(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Proxy Auth Route"""
        return self._get(
            "/v2/proxy/auth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_secrets(
        self,
        user_id: str,
        *,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get Proxy Secrets Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._get(
            f"/v2/proxy/secrets/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncProxyResource(AsyncAPIResource):
    @cached_property
    def secret(self) -> AsyncSecretResource:
        return AsyncSecretResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProxyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProxyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return AsyncProxyResourceWithStreamingResponse(self)

    async def retrieve_auth(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Proxy Auth Route"""
        return await self._get(
            "/v2/proxy/auth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_secrets(
        self,
        user_id: str,
        *,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get Proxy Secrets Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._get(
            f"/v2/proxy/secrets/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ProxyResourceWithRawResponse:
    def __init__(self, proxy: ProxyResource) -> None:
        self._proxy = proxy

        self.retrieve_auth = to_raw_response_wrapper(
            proxy.retrieve_auth,
        )
        self.retrieve_secrets = to_raw_response_wrapper(
            proxy.retrieve_secrets,
        )

    @cached_property
    def secret(self) -> SecretResourceWithRawResponse:
        return SecretResourceWithRawResponse(self._proxy.secret)


class AsyncProxyResourceWithRawResponse:
    def __init__(self, proxy: AsyncProxyResource) -> None:
        self._proxy = proxy

        self.retrieve_auth = async_to_raw_response_wrapper(
            proxy.retrieve_auth,
        )
        self.retrieve_secrets = async_to_raw_response_wrapper(
            proxy.retrieve_secrets,
        )

    @cached_property
    def secret(self) -> AsyncSecretResourceWithRawResponse:
        return AsyncSecretResourceWithRawResponse(self._proxy.secret)


class ProxyResourceWithStreamingResponse:
    def __init__(self, proxy: ProxyResource) -> None:
        self._proxy = proxy

        self.retrieve_auth = to_streamed_response_wrapper(
            proxy.retrieve_auth,
        )
        self.retrieve_secrets = to_streamed_response_wrapper(
            proxy.retrieve_secrets,
        )

    @cached_property
    def secret(self) -> SecretResourceWithStreamingResponse:
        return SecretResourceWithStreamingResponse(self._proxy.secret)


class AsyncProxyResourceWithStreamingResponse:
    def __init__(self, proxy: AsyncProxyResource) -> None:
        self._proxy = proxy

        self.retrieve_auth = async_to_streamed_response_wrapper(
            proxy.retrieve_auth,
        )
        self.retrieve_secrets = async_to_streamed_response_wrapper(
            proxy.retrieve_secrets,
        )

    @cached_property
    def secret(self) -> AsyncSecretResourceWithStreamingResponse:
        return AsyncSecretResourceWithStreamingResponse(self._proxy.secret)
