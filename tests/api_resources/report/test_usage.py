# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_llm_costs(self, client: NotDiamond) -> None:
        usage = client.report.usage.report_llm_costs(
            x_token="x-token",
        )
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report_llm_costs(self, client: NotDiamond) -> None:
        response = client.report.usage.with_raw_response.report_llm_costs(
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report_llm_costs(self, client: NotDiamond) -> None:
        with client.report.usage.with_streaming_response.report_llm_costs(
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(object, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_report_usage(self, client: NotDiamond) -> None:
        usage = client.report.usage.report_usage(
            x_token="x-token",
        )
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_report_usage(self, client: NotDiamond) -> None:
        response = client.report.usage.with_raw_response.report_usage(
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_report_usage(self, client: NotDiamond) -> None:
        with client.report.usage.with_streaming_response.report_usage(
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(object, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_llm_reporting(self, client: NotDiamond) -> None:
        usage = client.report.usage.test_llm_reporting(
            x_token="x-token",
        )
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_llm_reporting(self, client: NotDiamond) -> None:
        response = client.report.usage.with_raw_response.test_llm_reporting(
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_llm_reporting(self, client: NotDiamond) -> None:
        with client.report.usage.with_streaming_response.test_llm_reporting(
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(object, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_llm_costs(self, async_client: AsyncNotDiamond) -> None:
        usage = await async_client.report.usage.report_llm_costs(
            x_token="x-token",
        )
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report_llm_costs(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.usage.with_raw_response.report_llm_costs(
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report_llm_costs(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.usage.with_streaming_response.report_llm_costs(
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(object, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_report_usage(self, async_client: AsyncNotDiamond) -> None:
        usage = await async_client.report.usage.report_usage(
            x_token="x-token",
        )
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_report_usage(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.usage.with_raw_response.report_usage(
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_report_usage(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.usage.with_streaming_response.report_usage(
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(object, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_llm_reporting(self, async_client: AsyncNotDiamond) -> None:
        usage = await async_client.report.usage.test_llm_reporting(
            x_token="x-token",
        )
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_llm_reporting(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.report.usage.with_raw_response.test_llm_reporting(
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(object, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_llm_reporting(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.report.usage.with_streaming_response.test_llm_reporting(
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(object, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
