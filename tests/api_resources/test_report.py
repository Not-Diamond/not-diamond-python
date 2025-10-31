# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import (
    ReportSubmitFeedbackResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_evaluate_hallucination(self, client: NotDiamond) -> None:
        report = client.report.evaluate_hallucination(
            context="context",
            prompt="prompt",
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            response="response",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_evaluate_hallucination_with_all_params(self, client: NotDiamond) -> None:
        report = client.report.evaluate_hallucination(
            context="context",
            prompt="prompt",
            provider={
                "model": "gpt-4o",
                "provider": "openai",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            response="response",
            cost=0,
            latency=0,
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_evaluate_hallucination(self, client: NotDiamond) -> None:
        response = client.report.with_raw_response.evaluate_hallucination(
            context="context",
            prompt="prompt",
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            response="response",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_evaluate_hallucination(self, client: NotDiamond) -> None:
        with client.report.with_streaming_response.evaluate_hallucination(
            context="context",
            prompt="prompt",
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            response="response",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(object, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_latency(self, client: NotDiamond) -> None:
        report = client.report.latency(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="session_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_latency_with_all_params(self, client: NotDiamond) -> None:
        report = client.report.latency(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_latency(self, client: NotDiamond) -> None:
        response = client.report.with_raw_response.latency(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_latency(self, client: NotDiamond) -> None:
        with client.report.with_streaming_response.latency(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(object, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_feedback(self, client: NotDiamond) -> None:
        report = client.report.submit_feedback(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ReportSubmitFeedbackResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_feedback_with_all_params(self, client: NotDiamond) -> None:
        report = client.report.submit_feedback(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ReportSubmitFeedbackResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_feedback(self, client: NotDiamond) -> None:
        response = client.report.with_raw_response.submit_feedback(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportSubmitFeedbackResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_feedback(self, client: NotDiamond) -> None:
        with client.report.with_streaming_response.submit_feedback(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportSubmitFeedbackResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_evaluate_hallucination(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.report.evaluate_hallucination(
            context="context",
            prompt="prompt",
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            response="response",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_evaluate_hallucination_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.report.evaluate_hallucination(
            context="context",
            prompt="prompt",
            provider={
                "model": "gpt-4o",
                "provider": "openai",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            response="response",
            cost=0,
            latency=0,
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_evaluate_hallucination(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.with_raw_response.evaluate_hallucination(
            context="context",
            prompt="prompt",
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            response="response",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_evaluate_hallucination(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.with_streaming_response.evaluate_hallucination(
            context="context",
            prompt="prompt",
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            response="response",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(object, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_latency(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.report.latency(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="session_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_latency_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.report.latency(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_latency(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.with_raw_response.latency(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_latency(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.with_streaming_response.latency(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(object, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_feedback(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.report.submit_feedback(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ReportSubmitFeedbackResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_feedback_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.report.submit_feedback(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(ReportSubmitFeedbackResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_feedback(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.with_raw_response.submit_feedback(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportSubmitFeedbackResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_feedback(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.with_streaming_response.submit_feedback(
            feedback={"accuracy": "bar"},
            provider={
                "model": "gpt-4o",
                "provider": "openai",
            },
            session_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportSubmitFeedbackResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True
