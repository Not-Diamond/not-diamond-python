# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import (
    PznTrainCustomRouterResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPzn:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_submit_survey_response(self, client: NotDiamond) -> None:
        pzn = client.pzn.submit_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, pzn, path=["response"])

    @parametrize
    def test_method_submit_survey_response_with_all_params(self, client: NotDiamond) -> None:
        pzn = client.pzn.submit_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
            additional_preferences="additional_preferences",
            dataset_file=b"raw file contents",
            name="name",
            prompt_file=b"raw file contents",
            prompts="prompts",
        )
        assert_matches_type(object, pzn, path=["response"])

    @parametrize
    def test_raw_response_submit_survey_response(self, client: NotDiamond) -> None:
        response = client.pzn.with_raw_response.submit_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pzn = response.parse()
        assert_matches_type(object, pzn, path=["response"])

    @parametrize
    def test_streaming_response_submit_survey_response(self, client: NotDiamond) -> None:
        with client.pzn.with_streaming_response.submit_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pzn = response.parse()
            assert_matches_type(object, pzn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_train_custom_router(self, client: NotDiamond) -> None:
        pzn = client.pzn.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )
        assert_matches_type(PznTrainCustomRouterResponse, pzn, path=["response"])

    @parametrize
    def test_method_train_custom_router_with_all_params(self, client: NotDiamond) -> None:
        pzn = client.pzn.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
            override=True,
            preference_id="preference_id",
        )
        assert_matches_type(PznTrainCustomRouterResponse, pzn, path=["response"])

    @parametrize
    def test_raw_response_train_custom_router(self, client: NotDiamond) -> None:
        response = client.pzn.with_raw_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pzn = response.parse()
        assert_matches_type(PznTrainCustomRouterResponse, pzn, path=["response"])

    @parametrize
    def test_streaming_response_train_custom_router(self, client: NotDiamond) -> None:
        with client.pzn.with_streaming_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pzn = response.parse()
            assert_matches_type(PznTrainCustomRouterResponse, pzn, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPzn:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_submit_survey_response(self, async_client: AsyncNotDiamond) -> None:
        pzn = await async_client.pzn.submit_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, pzn, path=["response"])

    @parametrize
    async def test_method_submit_survey_response_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        pzn = await async_client.pzn.submit_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
            additional_preferences="additional_preferences",
            dataset_file=b"raw file contents",
            name="name",
            prompt_file=b"raw file contents",
            prompts="prompts",
        )
        assert_matches_type(object, pzn, path=["response"])

    @parametrize
    async def test_raw_response_submit_survey_response(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.pzn.with_raw_response.submit_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pzn = await response.parse()
        assert_matches_type(object, pzn, path=["response"])

    @parametrize
    async def test_streaming_response_submit_survey_response(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.pzn.with_streaming_response.submit_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pzn = await response.parse()
            assert_matches_type(object, pzn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_train_custom_router(self, async_client: AsyncNotDiamond) -> None:
        pzn = await async_client.pzn.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )
        assert_matches_type(PznTrainCustomRouterResponse, pzn, path=["response"])

    @parametrize
    async def test_method_train_custom_router_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        pzn = await async_client.pzn.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
            override=True,
            preference_id="preference_id",
        )
        assert_matches_type(PznTrainCustomRouterResponse, pzn, path=["response"])

    @parametrize
    async def test_raw_response_train_custom_router(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.pzn.with_raw_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pzn = await response.parse()
        assert_matches_type(PznTrainCustomRouterResponse, pzn, path=["response"])

    @parametrize
    async def test_streaming_response_train_custom_router(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.pzn.with_streaming_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pzn = await response.parse()
            assert_matches_type(PznTrainCustomRouterResponse, pzn, path=["response"])

        assert cast(Any, response.is_closed) is True
