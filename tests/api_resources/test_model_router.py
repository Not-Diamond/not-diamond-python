# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from notdiamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from notdiamond.types import ModelRouterSelectModelResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModelRouter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_select_model(self, client: NotDiamond) -> None:
        model_router = client.model_router.select_model(
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
                    "model": "gemini-2.5-flash",
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
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @parametrize
    def test_method_select_model_with_all_params(self, client: NotDiamond) -> None:
        model_router = client.model_router.select_model(
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
                    "model": "gemini-2.5-flash",
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
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @parametrize
    def test_raw_response_select_model(self, client: NotDiamond) -> None:
        response = client.model_router.with_raw_response.select_model(
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
                    "model": "gemini-2.5-flash",
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
        model_router = response.parse()
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @parametrize
    def test_streaming_response_select_model(self, client: NotDiamond) -> None:
        with client.model_router.with_streaming_response.select_model(
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
                    "model": "gemini-2.5-flash",
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

            model_router = response.parse()
            assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModelRouter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_select_model(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.select_model(
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
                    "model": "gemini-2.5-flash",
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
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @parametrize
    async def test_method_select_model_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.select_model(
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
                    "model": "gemini-2.5-flash",
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
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @parametrize
    async def test_raw_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.model_router.with_raw_response.select_model(
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
                    "model": "gemini-2.5-flash",
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
        model_router = await response.parse()
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @parametrize
    async def test_streaming_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.model_router.with_streaming_response.select_model(
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
                    "model": "gemini-2.5-flash",
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

            model_router = await response.parse()
            assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True
