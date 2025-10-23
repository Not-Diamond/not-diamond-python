# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_feedback(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_feedback(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_feedback_with_all_params(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_feedback(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report_feedback(self, client: NotDiamond) -> None:
        response = client.report.metrics.with_raw_response.report_feedback(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report_feedback(self, client: NotDiamond) -> None:
        with client.report.metrics.with_streaming_response.report_feedback(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_frontend_arena_choice(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_frontend_arena_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            x_token="x-token",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_frontend_arena_choice_with_all_params(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_frontend_arena_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
            x_token="x-token",
            user_id="user_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report_frontend_arena_choice(self, client: NotDiamond) -> None:
        response = client.report.metrics.with_raw_response.report_frontend_arena_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report_frontend_arena_choice(self, client: NotDiamond) -> None:
        with client.report.metrics.with_streaming_response.report_frontend_arena_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_frontend_regenerated(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_frontend_regenerated(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
            x_token="x-token",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_frontend_regenerated_with_all_params(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_frontend_regenerated(
            provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            regenerated=True,
            session_id="session_id",
            x_token="x-token",
            user_id="user_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report_frontend_regenerated(self, client: NotDiamond) -> None:
        response = client.report.metrics.with_raw_response.report_frontend_regenerated(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report_frontend_regenerated(self, client: NotDiamond) -> None:
        with client.report.metrics.with_streaming_response.report_frontend_regenerated(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_frontend_thumbs(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_frontend_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
            x_token="x-token",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_frontend_thumbs_with_all_params(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_frontend_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
            thumbs=0,
            x_token="x-token",
            user_id="user_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report_frontend_thumbs(self, client: NotDiamond) -> None:
        response = client.report.metrics.with_raw_response.report_frontend_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report_frontend_thumbs(self, client: NotDiamond) -> None:
        with client.report.metrics.with_streaming_response.report_frontend_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_latency(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_latency(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_latency_with_all_params(self, client: NotDiamond) -> None:
        metric = client.report.metrics.report_latency(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report_latency(self, client: NotDiamond) -> None:
        response = client.report.metrics.with_raw_response.report_latency(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report_latency(self, client: NotDiamond) -> None:
        with client.report.metrics.with_streaming_response.report_latency(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_feedback(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_feedback(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_feedback_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_feedback(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report_feedback(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.metrics.with_raw_response.report_feedback(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report_feedback(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.metrics.with_streaming_response.report_feedback(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_frontend_arena_choice(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_frontend_arena_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            x_token="x-token",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_frontend_arena_choice_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_frontend_arena_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
            x_token="x-token",
            user_id="user_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report_frontend_arena_choice(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.metrics.with_raw_response.report_frontend_arena_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report_frontend_arena_choice(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.metrics.with_streaming_response.report_frontend_arena_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_frontend_regenerated(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_frontend_regenerated(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
            x_token="x-token",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_frontend_regenerated_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_frontend_regenerated(
            provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            regenerated=True,
            session_id="session_id",
            x_token="x-token",
            user_id="user_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report_frontend_regenerated(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.metrics.with_raw_response.report_frontend_regenerated(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report_frontend_regenerated(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.metrics.with_streaming_response.report_frontend_regenerated(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_frontend_thumbs(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_frontend_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
            x_token="x-token",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_frontend_thumbs_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_frontend_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
            thumbs=0,
            x_token="x-token",
            user_id="user_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report_frontend_thumbs(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.metrics.with_raw_response.report_frontend_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report_frontend_thumbs(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.metrics.with_streaming_response.report_frontend_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_latency(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_latency(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_latency_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        metric = await async_client.report.metrics.report_latency(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            session_id="session_id",
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report_latency(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.metrics.with_raw_response.report_latency(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report_latency(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.metrics.with_streaming_response.report_latency(
            feedback={"foo": "bar"},
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True
