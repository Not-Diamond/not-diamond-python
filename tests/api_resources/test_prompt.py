# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import PromptGetAdaptStatusResponse, PromptGetAdaptResultsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompt:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_adapt_results(self, client: NotDiamond) -> None:
        prompt = client.prompt.get_adapt_results(
            "adaptation_run_id",
        )
        assert_matches_type(PromptGetAdaptResultsResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_get_adapt_results(self, client: NotDiamond) -> None:
        response = client.prompt.with_raw_response.get_adapt_results(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptGetAdaptResultsResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get_adapt_results(self, client: NotDiamond) -> None:
        with client.prompt.with_streaming_response.get_adapt_results(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptGetAdaptResultsResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_adapt_results(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            client.prompt.with_raw_response.get_adapt_results(
                "",
            )

    @parametrize
    def test_method_get_adapt_status(self, client: NotDiamond) -> None:
        prompt = client.prompt.get_adapt_status(
            "adaptation_run_id",
        )
        assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_get_adapt_status(self, client: NotDiamond) -> None:
        response = client.prompt.with_raw_response.get_adapt_status(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get_adapt_status(self, client: NotDiamond) -> None:
        with client.prompt.with_streaming_response.get_adapt_status(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_adapt_status(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            client.prompt.with_raw_response.get_adapt_status(
                "",
            )


class TestAsyncPrompt:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        prompt = await async_client.prompt.get_adapt_results(
            "adaptation_run_id",
        )
        assert_matches_type(PromptGetAdaptResultsResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt.with_raw_response.get_adapt_results(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptGetAdaptResultsResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt.with_streaming_response.get_adapt_results(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptGetAdaptResultsResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            await async_client.prompt.with_raw_response.get_adapt_results(
                "",
            )

    @parametrize
    async def test_method_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        prompt = await async_client.prompt.get_adapt_status(
            "adaptation_run_id",
        )
        assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt.with_raw_response.get_adapt_status(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt.with_streaming_response.get_adapt_status(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            await async_client.prompt.with_raw_response.get_adapt_status(
                "",
            )
