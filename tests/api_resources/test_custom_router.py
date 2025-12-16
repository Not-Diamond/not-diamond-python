# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from notdiamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from notdiamond.types import CustomRouterTrainCustomRouterResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomRouter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_train_custom_router(self, client: NotDiamond) -> None:
        custom_router = client.custom_router.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )
        assert_matches_type(CustomRouterTrainCustomRouterResponse, custom_router, path=["response"])

    @parametrize
    def test_method_train_custom_router_with_all_params(self, client: NotDiamond) -> None:
        custom_router = client.custom_router.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
            override=True,
            preference_id="preference_id",
        )
        assert_matches_type(CustomRouterTrainCustomRouterResponse, custom_router, path=["response"])

    @parametrize
    def test_raw_response_train_custom_router(self, client: NotDiamond) -> None:
        response = client.custom_router.with_raw_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_router = response.parse()
        assert_matches_type(CustomRouterTrainCustomRouterResponse, custom_router, path=["response"])

    @parametrize
    def test_streaming_response_train_custom_router(self, client: NotDiamond) -> None:
        with client.custom_router.with_streaming_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_router = response.parse()
            assert_matches_type(CustomRouterTrainCustomRouterResponse, custom_router, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomRouter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_train_custom_router(self, async_client: AsyncNotDiamond) -> None:
        custom_router = await async_client.custom_router.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )
        assert_matches_type(CustomRouterTrainCustomRouterResponse, custom_router, path=["response"])

    @parametrize
    async def test_method_train_custom_router_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        custom_router = await async_client.custom_router.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
            override=True,
            preference_id="preference_id",
        )
        assert_matches_type(CustomRouterTrainCustomRouterResponse, custom_router, path=["response"])

    @parametrize
    async def test_raw_response_train_custom_router(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.custom_router.with_raw_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_router = await response.parse()
        assert_matches_type(CustomRouterTrainCustomRouterResponse, custom_router, path=["response"])

    @parametrize
    async def test_streaming_response_train_custom_router(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.custom_router.with_streaming_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_router = await response.parse()
            assert_matches_type(CustomRouterTrainCustomRouterResponse, custom_router, path=["response"])

        assert cast(Any, response.is_closed) is True
