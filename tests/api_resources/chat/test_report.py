# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_regenerate_report(self, client: NotDiamond) -> None:
        report = client.chat.report.regenerate_report(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_regenerate_report_with_all_params(self, client: NotDiamond) -> None:
        report = client.chat.report.regenerate_report(
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
            user_id="user_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_regenerate_report(self, client: NotDiamond) -> None:
        response = client.chat.report.with_raw_response.regenerate_report(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_regenerate_report(self, client: NotDiamond) -> None:
        with client.chat.report.with_streaming_response.regenerate_report(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(object, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_thumbs(self, client: NotDiamond) -> None:
        report = client.chat.report.report_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_thumbs_with_all_params(self, client: NotDiamond) -> None:
        report = client.chat.report.report_thumbs(
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
            user_id="user_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report_thumbs(self, client: NotDiamond) -> None:
        response = client.chat.report.with_raw_response.report_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report_thumbs(self, client: NotDiamond) -> None:
        with client.chat.report.with_streaming_response.report_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(object, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_regenerate_report(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.chat.report.regenerate_report(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_regenerate_report_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.chat.report.regenerate_report(
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
            user_id="user_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_regenerate_report(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.chat.report.with_raw_response.regenerate_report(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_regenerate_report(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.chat.report.with_streaming_response.regenerate_report(
            provider={
                "model": "model",
                "provider": "provider",
            },
            regenerated=True,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(object, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_thumbs(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.chat.report.report_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_thumbs_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        report = await async_client.chat.report.report_thumbs(
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
            user_id="user_id",
        )
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report_thumbs(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.chat.report.with_raw_response.report_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(object, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report_thumbs(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.chat.report.with_streaming_response.report_thumbs(
            provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
            thumbs=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(object, report, path=["response"])

        assert cast(Any, response.is_closed) is True
