# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types.report import MetricSubmitFeedbackResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_feedback(self, client: NotDiamond) -> None:
        metric = client.report.metrics.submit_feedback(
            body={
                "session_id": "550e8400-e29b-41d4-a716-446655440000",
                "provider": {
                    "provider": "openai",
                    "model": "gpt-4o",
                },
                "feedback": {"accuracy": 1},
            },
        )
        assert_matches_type(MetricSubmitFeedbackResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_feedback(self, client: NotDiamond) -> None:
        response = client.report.metrics.with_raw_response.submit_feedback(
            body={
                "session_id": "550e8400-e29b-41d4-a716-446655440000",
                "provider": {
                    "provider": "openai",
                    "model": "gpt-4o",
                },
                "feedback": {"accuracy": 1},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricSubmitFeedbackResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_feedback(self, client: NotDiamond) -> None:
        with client.report.metrics.with_streaming_response.submit_feedback(
            body={
                "session_id": "550e8400-e29b-41d4-a716-446655440000",
                "provider": {
                    "provider": "openai",
                    "model": "gpt-4o",
                },
                "feedback": {"accuracy": 1},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricSubmitFeedbackResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_feedback(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.submit_feedback(
            body={
                "session_id": "550e8400-e29b-41d4-a716-446655440000",
                "provider": {
                    "provider": "openai",
                    "model": "gpt-4o",
                },
                "feedback": {"accuracy": 1},
            },
        )
        assert_matches_type(MetricSubmitFeedbackResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_feedback(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.metrics.with_raw_response.submit_feedback(
            body={
                "session_id": "550e8400-e29b-41d4-a716-446655440000",
                "provider": {
                    "provider": "openai",
                    "model": "gpt-4o",
                },
                "feedback": {"accuracy": 1},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricSubmitFeedbackResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_feedback(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.metrics.with_streaming_response.submit_feedback(
            body={
                "session_id": "550e8400-e29b-41d4-a716-446655440000",
                "provider": {
                    "provider": "openai",
                    "model": "gpt-4o",
                },
                "feedback": {"accuracy": 1},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricSubmitFeedbackResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True
