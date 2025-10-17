# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import prompt_adapt_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.prompt_adapt_response import PromptAdaptResponse
from ..types.adaptation_run_results import AdaptationRunResults
from ..types.prompt_get_adapt_runs_response import PromptGetAdaptRunsResponse
from ..types.prompt_get_adapt_status_response import PromptGetAdaptStatusResponse

__all__ = ["PromptResource", "AsyncPromptResource"]


class PromptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return PromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return PromptResourceWithStreamingResponse(self)

    def adapt(
        self,
        *,
        fields: SequenceNotStr[str],
        origin_model: prompt_adapt_params.OriginModel,
        system_prompt: str,
        target_models: Iterable[prompt_adapt_params.TargetModel],
        template: str,
        evaluation_config: Optional[str] | Omit = omit,
        evaluation_metric: Optional[str] | Omit = omit,
        goldens: Optional[Iterable[prompt_adapt_params.Golden]] | Omit = omit,
        origin_model_evaluation_score: Optional[float] | Omit = omit,
        test_goldens: Optional[Iterable[prompt_adapt_params.TestGolden]] | Omit = omit,
        train_goldens: Optional[Iterable[prompt_adapt_params.TrainGolden]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAdaptResponse:
        """
        Adapt Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/prompt/adapt",
            body=maybe_transform(
                {
                    "fields": fields,
                    "origin_model": origin_model,
                    "system_prompt": system_prompt,
                    "target_models": target_models,
                    "template": template,
                    "evaluation_config": evaluation_config,
                    "evaluation_metric": evaluation_metric,
                    "goldens": goldens,
                    "origin_model_evaluation_score": origin_model_evaluation_score,
                    "test_goldens": test_goldens,
                    "train_goldens": train_goldens,
                },
                prompt_adapt_params.PromptAdaptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAdaptResponse,
        )

    def get_adapt_results(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptationRunResults:
        """
        Get Adapt Results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return self._get(
            f"/v2/prompt/adaptResults/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptationRunResults,
        )

    def get_adapt_run_results(
        self,
        adaptation_run_id: str,
        *,
        user_id: str,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptationRunResults:
        """
        Get Adapt Run Results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return self._get(
            f"/v2/prompt/frontendAdaptRunResults/{user_id}/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptationRunResults,
        )

    def get_adapt_runs(
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
    ) -> PromptGetAdaptRunsResponse:
        """
        Get Adapt Runs

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
            f"/v2/prompt/frontendAdaptRuns/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetAdaptRunsResponse,
        )

    def get_adapt_status(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptGetAdaptStatusResponse:
        """
        Get Adapt Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return self._get(
            f"/v2/prompt/adaptStatus/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetAdaptStatusResponse,
        )


class AsyncPromptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncPromptResourceWithStreamingResponse(self)

    async def adapt(
        self,
        *,
        fields: SequenceNotStr[str],
        origin_model: prompt_adapt_params.OriginModel,
        system_prompt: str,
        target_models: Iterable[prompt_adapt_params.TargetModel],
        template: str,
        evaluation_config: Optional[str] | Omit = omit,
        evaluation_metric: Optional[str] | Omit = omit,
        goldens: Optional[Iterable[prompt_adapt_params.Golden]] | Omit = omit,
        origin_model_evaluation_score: Optional[float] | Omit = omit,
        test_goldens: Optional[Iterable[prompt_adapt_params.TestGolden]] | Omit = omit,
        train_goldens: Optional[Iterable[prompt_adapt_params.TrainGolden]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAdaptResponse:
        """
        Adapt Prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/prompt/adapt",
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "origin_model": origin_model,
                    "system_prompt": system_prompt,
                    "target_models": target_models,
                    "template": template,
                    "evaluation_config": evaluation_config,
                    "evaluation_metric": evaluation_metric,
                    "goldens": goldens,
                    "origin_model_evaluation_score": origin_model_evaluation_score,
                    "test_goldens": test_goldens,
                    "train_goldens": train_goldens,
                },
                prompt_adapt_params.PromptAdaptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAdaptResponse,
        )

    async def get_adapt_results(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptationRunResults:
        """
        Get Adapt Results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return await self._get(
            f"/v2/prompt/adaptResults/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptationRunResults,
        )

    async def get_adapt_run_results(
        self,
        adaptation_run_id: str,
        *,
        user_id: str,
        x_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdaptationRunResults:
        """
        Get Adapt Run Results

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        return await self._get(
            f"/v2/prompt/frontendAdaptRunResults/{user_id}/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdaptationRunResults,
        )

    async def get_adapt_runs(
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
    ) -> PromptGetAdaptRunsResponse:
        """
        Get Adapt Runs

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
            f"/v2/prompt/frontendAdaptRuns/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetAdaptRunsResponse,
        )

    async def get_adapt_status(
        self,
        adaptation_run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptGetAdaptStatusResponse:
        """
        Get Adapt Status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not adaptation_run_id:
            raise ValueError(f"Expected a non-empty value for `adaptation_run_id` but received {adaptation_run_id!r}")
        return await self._get(
            f"/v2/prompt/adaptStatus/{adaptation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptGetAdaptStatusResponse,
        )


class PromptResourceWithRawResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.adapt = to_raw_response_wrapper(
            prompt.adapt,
        )
        self.get_adapt_results = to_raw_response_wrapper(
            prompt.get_adapt_results,
        )
        self.get_adapt_run_results = to_raw_response_wrapper(
            prompt.get_adapt_run_results,
        )
        self.get_adapt_runs = to_raw_response_wrapper(
            prompt.get_adapt_runs,
        )
        self.get_adapt_status = to_raw_response_wrapper(
            prompt.get_adapt_status,
        )


class AsyncPromptResourceWithRawResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.adapt = async_to_raw_response_wrapper(
            prompt.adapt,
        )
        self.get_adapt_results = async_to_raw_response_wrapper(
            prompt.get_adapt_results,
        )
        self.get_adapt_run_results = async_to_raw_response_wrapper(
            prompt.get_adapt_run_results,
        )
        self.get_adapt_runs = async_to_raw_response_wrapper(
            prompt.get_adapt_runs,
        )
        self.get_adapt_status = async_to_raw_response_wrapper(
            prompt.get_adapt_status,
        )


class PromptResourceWithStreamingResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.adapt = to_streamed_response_wrapper(
            prompt.adapt,
        )
        self.get_adapt_results = to_streamed_response_wrapper(
            prompt.get_adapt_results,
        )
        self.get_adapt_run_results = to_streamed_response_wrapper(
            prompt.get_adapt_run_results,
        )
        self.get_adapt_runs = to_streamed_response_wrapper(
            prompt.get_adapt_runs,
        )
        self.get_adapt_status = to_streamed_response_wrapper(
            prompt.get_adapt_status,
        )


class AsyncPromptResourceWithStreamingResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.adapt = async_to_streamed_response_wrapper(
            prompt.adapt,
        )
        self.get_adapt_results = async_to_streamed_response_wrapper(
            prompt.get_adapt_results,
        )
        self.get_adapt_run_results = async_to_streamed_response_wrapper(
            prompt.get_adapt_run_results,
        )
        self.get_adapt_runs = async_to_streamed_response_wrapper(
            prompt.get_adapt_runs,
        )
        self.get_adapt_status = async_to_streamed_response_wrapper(
            prompt.get_adapt_status,
        )
