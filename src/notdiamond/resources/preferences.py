# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import preference_create_params, preference_update_params
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
from ..types.preference_create_response import PreferenceCreateResponse

__all__ = ["PreferencesResource", "AsyncPreferencesResource"]


class PreferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return PreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return PreferencesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCreateResponse:
        """
        Create a new preference ID for personalized LLM routing.

        A preference ID enables personalized routing by tracking your feedback and
        learning your preferences over time. Once created, you can:

        1. Use it in model_select() calls to get personalized routing decisions
        2. Train a custom router specific to your use case

        **Workflow:**

        1. Create a preference ID (this endpoint)
        2. Use the preference_id in POST /v2/modelRouter/modelSelect requests
        3. Optionally train a custom router via POST /v2/pzn/trainCustomRouter

        **Benefits:**

        - Personalized routing for your specific use case
        - Ability to train custom routers on your evaluation data

        **Note:** If you don't provide a preference_id in model_select() calls, the
        default router will be used.

        Args:
          name: Optional name for the preference. If not provided, an auto-generated timestamp
              will be used. Use descriptive names like 'Production API' or 'Customer Support
              Bot' for easy identification

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/preferences/userPreferenceCreate",
            body=maybe_transform({"name": name}, preference_create_params.PreferenceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCreateResponse,
        )

    def update(
        self,
        *,
        preference_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update User Preference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v2/preferences/userPreferenceUpdate",
            body=maybe_transform(
                {
                    "preference_id": preference_id,
                    "name": name,
                },
                preference_update_params.PreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete(
        self,
        preference_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete User Preference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not preference_id:
            raise ValueError(f"Expected a non-empty value for `preference_id` but received {preference_id!r}")
        return self._delete(
            f"/v2/preferences/userPreferenceDelete/{preference_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPreferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncPreferencesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCreateResponse:
        """
        Create a new preference ID for personalized LLM routing.

        A preference ID enables personalized routing by tracking your feedback and
        learning your preferences over time. Once created, you can:

        1. Use it in model_select() calls to get personalized routing decisions
        2. Train a custom router specific to your use case

        **Workflow:**

        1. Create a preference ID (this endpoint)
        2. Use the preference_id in POST /v2/modelRouter/modelSelect requests
        3. Optionally train a custom router via POST /v2/pzn/trainCustomRouter

        **Benefits:**

        - Personalized routing for your specific use case
        - Ability to train custom routers on your evaluation data

        **Note:** If you don't provide a preference_id in model_select() calls, the
        default router will be used.

        Args:
          name: Optional name for the preference. If not provided, an auto-generated timestamp
              will be used. Use descriptive names like 'Production API' or 'Customer Support
              Bot' for easy identification

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/preferences/userPreferenceCreate",
            body=await async_maybe_transform({"name": name}, preference_create_params.PreferenceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCreateResponse,
        )

    async def update(
        self,
        *,
        preference_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update User Preference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v2/preferences/userPreferenceUpdate",
            body=await async_maybe_transform(
                {
                    "preference_id": preference_id,
                    "name": name,
                },
                preference_update_params.PreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete(
        self,
        preference_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete User Preference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not preference_id:
            raise ValueError(f"Expected a non-empty value for `preference_id` but received {preference_id!r}")
        return await self._delete(
            f"/v2/preferences/userPreferenceDelete/{preference_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PreferencesResourceWithRawResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.create = to_raw_response_wrapper(
            preferences.create,
        )
        self.update = to_raw_response_wrapper(
            preferences.update,
        )
        self.delete = to_raw_response_wrapper(
            preferences.delete,
        )


class AsyncPreferencesResourceWithRawResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.create = async_to_raw_response_wrapper(
            preferences.create,
        )
        self.update = async_to_raw_response_wrapper(
            preferences.update,
        )
        self.delete = async_to_raw_response_wrapper(
            preferences.delete,
        )


class PreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.create = to_streamed_response_wrapper(
            preferences.create,
        )
        self.update = to_streamed_response_wrapper(
            preferences.update,
        )
        self.delete = to_streamed_response_wrapper(
            preferences.delete,
        )


class AsyncPreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.create = async_to_streamed_response_wrapper(
            preferences.create,
        )
        self.update = async_to_streamed_response_wrapper(
            preferences.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            preferences.delete,
        )
