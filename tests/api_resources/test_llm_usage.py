# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import (
    LlmUsageRetrieveResponse,
    LlmUsageRetrieveDailyResponse,
    LlmUsageRetrieveMonthlyResponse,
    LlmUsageRetrieveSummaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLlmUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: NotDiamond) -> None:
        llm_usage = client.llm_usage.retrieve()
        assert_matches_type(LlmUsageRetrieveResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: NotDiamond) -> None:
        llm_usage = client.llm_usage.retrieve(
            end_time=0,
            limit=0,
            start_time=0,
        )
        assert_matches_type(LlmUsageRetrieveResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: NotDiamond) -> None:
        response = client.llm_usage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_usage = response.parse()
        assert_matches_type(LlmUsageRetrieveResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: NotDiamond) -> None:
        with client.llm_usage.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_usage = response.parse()
            assert_matches_type(LlmUsageRetrieveResponse, llm_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_daily(self, client: NotDiamond) -> None:
        llm_usage = client.llm_usage.retrieve_daily(
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(LlmUsageRetrieveDailyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_daily_with_all_params(self, client: NotDiamond) -> None:
        llm_usage = client.llm_usage.retrieve_daily(
            end_date="end_date",
            start_date="start_date",
            metric="metric",
        )
        assert_matches_type(LlmUsageRetrieveDailyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_daily(self, client: NotDiamond) -> None:
        response = client.llm_usage.with_raw_response.retrieve_daily(
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_usage = response.parse()
        assert_matches_type(LlmUsageRetrieveDailyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_daily(self, client: NotDiamond) -> None:
        with client.llm_usage.with_streaming_response.retrieve_daily(
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_usage = response.parse()
            assert_matches_type(LlmUsageRetrieveDailyResponse, llm_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_monthly(self, client: NotDiamond) -> None:
        llm_usage = client.llm_usage.retrieve_monthly()
        assert_matches_type(LlmUsageRetrieveMonthlyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_monthly_with_all_params(self, client: NotDiamond) -> None:
        llm_usage = client.llm_usage.retrieve_monthly(
            months=0,
        )
        assert_matches_type(LlmUsageRetrieveMonthlyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_monthly(self, client: NotDiamond) -> None:
        response = client.llm_usage.with_raw_response.retrieve_monthly()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_usage = response.parse()
        assert_matches_type(LlmUsageRetrieveMonthlyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_monthly(self, client: NotDiamond) -> None:
        with client.llm_usage.with_streaming_response.retrieve_monthly() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_usage = response.parse()
            assert_matches_type(LlmUsageRetrieveMonthlyResponse, llm_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_summary(self, client: NotDiamond) -> None:
        llm_usage = client.llm_usage.retrieve_summary()
        assert_matches_type(LlmUsageRetrieveSummaryResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_summary_with_all_params(self, client: NotDiamond) -> None:
        llm_usage = client.llm_usage.retrieve_summary(
            end_time=0,
            start_time=0,
        )
        assert_matches_type(LlmUsageRetrieveSummaryResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_summary(self, client: NotDiamond) -> None:
        response = client.llm_usage.with_raw_response.retrieve_summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_usage = response.parse()
        assert_matches_type(LlmUsageRetrieveSummaryResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_summary(self, client: NotDiamond) -> None:
        with client.llm_usage.with_streaming_response.retrieve_summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_usage = response.parse()
            assert_matches_type(LlmUsageRetrieveSummaryResponse, llm_usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLlmUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNotDiamond) -> None:
        llm_usage = await async_client.llm_usage.retrieve()
        assert_matches_type(LlmUsageRetrieveResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        llm_usage = await async_client.llm_usage.retrieve(
            end_time=0,
            limit=0,
            start_time=0,
        )
        assert_matches_type(LlmUsageRetrieveResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.llm_usage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_usage = await response.parse()
        assert_matches_type(LlmUsageRetrieveResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.llm_usage.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_usage = await response.parse()
            assert_matches_type(LlmUsageRetrieveResponse, llm_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_daily(self, async_client: AsyncNotDiamond) -> None:
        llm_usage = await async_client.llm_usage.retrieve_daily(
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(LlmUsageRetrieveDailyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_daily_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        llm_usage = await async_client.llm_usage.retrieve_daily(
            end_date="end_date",
            start_date="start_date",
            metric="metric",
        )
        assert_matches_type(LlmUsageRetrieveDailyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_daily(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.llm_usage.with_raw_response.retrieve_daily(
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_usage = await response.parse()
        assert_matches_type(LlmUsageRetrieveDailyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_daily(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.llm_usage.with_streaming_response.retrieve_daily(
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_usage = await response.parse()
            assert_matches_type(LlmUsageRetrieveDailyResponse, llm_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_monthly(self, async_client: AsyncNotDiamond) -> None:
        llm_usage = await async_client.llm_usage.retrieve_monthly()
        assert_matches_type(LlmUsageRetrieveMonthlyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_monthly_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        llm_usage = await async_client.llm_usage.retrieve_monthly(
            months=0,
        )
        assert_matches_type(LlmUsageRetrieveMonthlyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_monthly(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.llm_usage.with_raw_response.retrieve_monthly()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_usage = await response.parse()
        assert_matches_type(LlmUsageRetrieveMonthlyResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_monthly(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.llm_usage.with_streaming_response.retrieve_monthly() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_usage = await response.parse()
            assert_matches_type(LlmUsageRetrieveMonthlyResponse, llm_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_summary(self, async_client: AsyncNotDiamond) -> None:
        llm_usage = await async_client.llm_usage.retrieve_summary()
        assert_matches_type(LlmUsageRetrieveSummaryResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_summary_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        llm_usage = await async_client.llm_usage.retrieve_summary(
            end_time=0,
            start_time=0,
        )
        assert_matches_type(LlmUsageRetrieveSummaryResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_summary(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.llm_usage.with_raw_response.retrieve_summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm_usage = await response.parse()
        assert_matches_type(LlmUsageRetrieveSummaryResponse, llm_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_summary(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.llm_usage.with_streaming_response.retrieve_summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm_usage = await response.parse()
            assert_matches_type(LlmUsageRetrieveSummaryResponse, llm_usage, path=["response"])

        assert cast(Any, response.is_closed) is True
