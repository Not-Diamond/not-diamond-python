# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import (
    RoutingSelectModelResponse,
    RoutingTrainCustomRouterResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRouting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_survey_response(self, client: NotDiamond) -> None:
        routing = client.routing.create_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_survey_response_with_all_params(self, client: NotDiamond) -> None:
        routing = client.routing.create_survey_response(
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
        assert_matches_type(object, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_survey_response(self, client: NotDiamond) -> None:
        response = client.routing.with_raw_response.create_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(object, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_survey_response(self, client: NotDiamond) -> None:
        with client.routing.with_streaming_response.create_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(object, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model(self, client: NotDiamond) -> None:
        routing = client.routing.select_model(
            llm_providers=[
                {
                    "model": "gpt-4o",
                    "provider": "openai",
                },
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-1.5-pro",
                    "provider": "google",
                },
            ],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Explain quantum computing in simple terms",
                },
            ],
        )
        assert_matches_type(RoutingSelectModelResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model_with_all_params(self, client: NotDiamond) -> None:
        routing = client.routing.select_model(
            llm_providers=[
                {
                    "model": "gpt-4o",
                    "provider": "openai",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
                {
                    "model": "gemini-1.5-pro",
                    "provider": "google",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
            ],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Explain quantum computing in simple terms",
                },
            ],
            type="type",
            hash_content=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="cost",
        )
        assert_matches_type(RoutingSelectModelResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_select_model(self, client: NotDiamond) -> None:
        response = client.routing.with_raw_response.select_model(
            llm_providers=[
                {
                    "model": "gpt-4o",
                    "provider": "openai",
                },
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-1.5-pro",
                    "provider": "google",
                },
            ],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Explain quantum computing in simple terms",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(RoutingSelectModelResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_select_model(self, client: NotDiamond) -> None:
        with client.routing.with_streaming_response.select_model(
            llm_providers=[
                {
                    "model": "gpt-4o",
                    "provider": "openai",
                },
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-1.5-pro",
                    "provider": "google",
                },
            ],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Explain quantum computing in simple terms",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(RoutingSelectModelResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_train_custom_router(self, client: NotDiamond) -> None:
        routing = client.routing.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )
        assert_matches_type(RoutingTrainCustomRouterResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_train_custom_router_with_all_params(self, client: NotDiamond) -> None:
        routing = client.routing.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
            override=True,
            preference_id="preference_id",
        )
        assert_matches_type(RoutingTrainCustomRouterResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_train_custom_router(self, client: NotDiamond) -> None:
        response = client.routing.with_raw_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(RoutingTrainCustomRouterResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_train_custom_router(self, client: NotDiamond) -> None:
        with client.routing.with_streaming_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(RoutingTrainCustomRouterResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRouting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_survey_response(self, async_client: AsyncNotDiamond) -> None:
        routing = await async_client.routing.create_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_survey_response_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        routing = await async_client.routing.create_survey_response(
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
        assert_matches_type(object, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_survey_response(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.routing.with_raw_response.create_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(object, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_survey_response(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.routing.with_streaming_response.create_survey_response(
            constraint_priorities="constraint_priorities",
            email="email",
            llm_providers="llm_providers",
            use_case_desc="use_case_desc",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(object, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model(self, async_client: AsyncNotDiamond) -> None:
        routing = await async_client.routing.select_model(
            llm_providers=[
                {
                    "model": "gpt-4o",
                    "provider": "openai",
                },
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-1.5-pro",
                    "provider": "google",
                },
            ],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Explain quantum computing in simple terms",
                },
            ],
        )
        assert_matches_type(RoutingSelectModelResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        routing = await async_client.routing.select_model(
            llm_providers=[
                {
                    "model": "gpt-4o",
                    "provider": "openai",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
                {
                    "model": "gemini-1.5-pro",
                    "provider": "google",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
            ],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Explain quantum computing in simple terms",
                },
            ],
            type="type",
            hash_content=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="cost",
        )
        assert_matches_type(RoutingSelectModelResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.routing.with_raw_response.select_model(
            llm_providers=[
                {
                    "model": "gpt-4o",
                    "provider": "openai",
                },
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-1.5-pro",
                    "provider": "google",
                },
            ],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Explain quantum computing in simple terms",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(RoutingSelectModelResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.routing.with_streaming_response.select_model(
            llm_providers=[
                {
                    "model": "gpt-4o",
                    "provider": "openai",
                },
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-1.5-pro",
                    "provider": "google",
                },
            ],
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Explain quantum computing in simple terms",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(RoutingSelectModelResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_train_custom_router(self, async_client: AsyncNotDiamond) -> None:
        routing = await async_client.routing.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )
        assert_matches_type(RoutingTrainCustomRouterResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_train_custom_router_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        routing = await async_client.routing.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
            override=True,
            preference_id="preference_id",
        )
        assert_matches_type(RoutingTrainCustomRouterResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_train_custom_router(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.routing.with_raw_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(RoutingTrainCustomRouterResponse, routing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_train_custom_router(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.routing.with_streaming_response.train_custom_router(
            dataset_file=b"raw file contents",
            language="english",
            llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
            maximize=True,
            prompt_column="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(RoutingTrainCustomRouterResponse, routing, path=["response"])

        assert cast(Any, response.is_closed) is True
