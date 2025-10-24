# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ..._base_client import make_request_options
from ...types.client import report_evaluate_hallucination_params

__all__ = ["ReportResource", "AsyncReportResource"]


class ReportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return ReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return ReportResourceWithStreamingResponse(self)

    def evaluate_hallucination(
        self,
        *,
        context: str,
        prompt: str,
        provider: report_evaluate_hallucination_params.Provider,
        response: str,
        cost: Optional[float] | Omit = omit,
        latency: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Evaluate Hallucination

        Args:
          provider: Model for specifying an LLM provider in API requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/report/hallucination",
            body=maybe_transform(
                {
                    "context": context,
                    "prompt": prompt,
                    "provider": provider,
                    "response": response,
                    "cost": cost,
                    "latency": latency,
                },
                report_evaluate_hallucination_params.ReportEvaluateHallucinationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncReportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncReportResourceWithStreamingResponse(self)

    async def evaluate_hallucination(
        self,
        *,
        context: str,
        prompt: str,
        provider: report_evaluate_hallucination_params.Provider,
        response: str,
        cost: Optional[float] | Omit = omit,
        latency: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Evaluate Hallucination

        Args:
          provider: Model for specifying an LLM provider in API requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/report/hallucination",
            body=await async_maybe_transform(
                {
                    "context": context,
                    "prompt": prompt,
                    "provider": provider,
                    "response": response,
                    "cost": cost,
                    "latency": latency,
                },
                report_evaluate_hallucination_params.ReportEvaluateHallucinationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ReportResourceWithRawResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.evaluate_hallucination = to_raw_response_wrapper(
            report.evaluate_hallucination,
        )


class AsyncReportResourceWithRawResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.evaluate_hallucination = async_to_raw_response_wrapper(
            report.evaluate_hallucination,
        )


class ReportResourceWithStreamingResponse:
    def __init__(self, report: ReportResource) -> None:
        self._report = report

        self.evaluate_hallucination = to_streamed_response_wrapper(
            report.evaluate_hallucination,
        )


class AsyncReportResourceWithStreamingResponse:
    def __init__(self, report: AsyncReportResource) -> None:
        self._report = report

        self.evaluate_hallucination = async_to_streamed_response_wrapper(
            report.evaluate_hallucination,
        )
