# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.proxy import secret_upsert_params
from ..._base_client import make_request_options

__all__ = ["SecretResource", "AsyncSecretResource"]


class SecretResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return SecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return SecretResourceWithStreamingResponse(self)

    def delete(
        self,
        provider: str,
        *,
        user_id: str,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete Proxy Secret Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._delete(
            f"/v2/proxy/secret/delete/{user_id}/{provider}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def upsert(
        self,
        *,
        name: str,
        provider: str,
        secret: str,
        user_id: str,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Upsert Proxy Secret Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._post(
            "/v2/proxy/secret",
            body=maybe_transform(
                {
                    "name": name,
                    "provider": provider,
                    "secret": secret,
                    "user_id": user_id,
                },
                secret_upsert_params.SecretUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSecretResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/not-diamond-python#with_streaming_response
        """
        return AsyncSecretResourceWithStreamingResponse(self)

    async def delete(
        self,
        provider: str,
        *,
        user_id: str,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete Proxy Secret Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._delete(
            f"/v2/proxy/secret/delete/{user_id}/{provider}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def upsert(
        self,
        *,
        name: str,
        provider: str,
        secret: str,
        user_id: str,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Upsert Proxy Secret Route

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._post(
            "/v2/proxy/secret",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "provider": provider,
                    "secret": secret,
                    "user_id": user_id,
                },
                secret_upsert_params.SecretUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SecretResourceWithRawResponse:
    def __init__(self, secret: SecretResource) -> None:
        self._secret = secret

        self.delete = to_raw_response_wrapper(
            secret.delete,
        )
        self.upsert = to_raw_response_wrapper(
            secret.upsert,
        )


class AsyncSecretResourceWithRawResponse:
    def __init__(self, secret: AsyncSecretResource) -> None:
        self._secret = secret

        self.delete = async_to_raw_response_wrapper(
            secret.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            secret.upsert,
        )


class SecretResourceWithStreamingResponse:
    def __init__(self, secret: SecretResource) -> None:
        self._secret = secret

        self.delete = to_streamed_response_wrapper(
            secret.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            secret.upsert,
        )


class AsyncSecretResourceWithStreamingResponse:
    def __init__(self, secret: AsyncSecretResource) -> None:
        self._secret = secret

        self.delete = async_to_streamed_response_wrapper(
            secret.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            secret.upsert,
        )
