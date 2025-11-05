# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import (
    ModelRouterSelectModelResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModelRouter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_hands_select(self, client: NotDiamond) -> None:
        model_router = client.model_router.open_hands_select(
            body={},
        )
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_open_hands_select(self, client: NotDiamond) -> None:
        response = client.model_router.with_raw_response.open_hands_select(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model_router = response.parse()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_open_hands_select(self, client: NotDiamond) -> None:
        with client.model_router.with_streaming_response.open_hands_select(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model_router = response.parse()
            assert_matches_type(object, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model(self, client: NotDiamond) -> None:
        model_router = client.model_router.select_model(
            body={
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant.",
                    },
                    {
                        "role": "user",
                        "content": "Explain quantum computing in simple terms",
                    },
                ],
                "llm_providers": [
                    {
                        "provider": "openai",
                        "model": "gpt-4o",
                    },
                    {
                        "provider": "anthropic",
                        "model": "claude-sonnet-4-5-20250929",
                    },
                    {
                        "provider": "google",
                        "model": "gemini-1.5-pro",
                    },
                ],
            },
        )
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model_with_all_params(self, client: NotDiamond) -> None:
        model_router = client.model_router.select_model(
            body={
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant.",
                    },
                    {
                        "role": "user",
                        "content": "Explain quantum computing in simple terms",
                    },
                ],
                "llm_providers": [
                    {
                        "provider": "openai",
                        "model": "gpt-4o",
                    },
                    {
                        "provider": "anthropic",
                        "model": "claude-sonnet-4-5-20250929",
                    },
                    {
                        "provider": "google",
                        "model": "gemini-1.5-pro",
                    },
                ],
            },
            type="type",
        )
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_select_model(self, client: NotDiamond) -> None:
        response = client.model_router.with_raw_response.select_model(
            body={
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant.",
                    },
                    {
                        "role": "user",
                        "content": "Explain quantum computing in simple terms",
                    },
                ],
                "llm_providers": [
                    {
                        "provider": "openai",
                        "model": "gpt-4o",
                    },
                    {
                        "provider": "anthropic",
                        "model": "claude-sonnet-4-5-20250929",
                    },
                    {
                        "provider": "google",
                        "model": "gemini-1.5-pro",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model_router = response.parse()
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_select_model(self, client: NotDiamond) -> None:
        with client.model_router.with_streaming_response.select_model(
            body={
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant.",
                    },
                    {
                        "role": "user",
                        "content": "Explain quantum computing in simple terms",
                    },
                ],
                "llm_providers": [
                    {
                        "provider": "openai",
                        "model": "gpt-4o",
                    },
                    {
                        "provider": "anthropic",
                        "model": "claude-sonnet-4-5-20250929",
                    },
                    {
                        "provider": "google",
                        "model": "gemini-1.5-pro",
                    },
                ],
            },
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_hands_select(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.open_hands_select(
            body={},
        )
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_open_hands_select(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.model_router.with_raw_response.open_hands_select(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model_router = await response.parse()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_open_hands_select(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.model_router.with_streaming_response.open_hands_select(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model_router = await response.parse()
            assert_matches_type(object, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.select_model(
            body={
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant.",
                    },
                    {
                        "role": "user",
                        "content": "Explain quantum computing in simple terms",
                    },
                ],
                "llm_providers": [
                    {
                        "provider": "openai",
                        "model": "gpt-4o",
                    },
                    {
                        "provider": "anthropic",
                        "model": "claude-sonnet-4-5-20250929",
                    },
                    {
                        "provider": "google",
                        "model": "gemini-1.5-pro",
                    },
                ],
            },
        )
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.select_model(
            body={
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant.",
                    },
                    {
                        "role": "user",
                        "content": "Explain quantum computing in simple terms",
                    },
                ],
                "llm_providers": [
                    {
                        "provider": "openai",
                        "model": "gpt-4o",
                    },
                    {
                        "provider": "anthropic",
                        "model": "claude-sonnet-4-5-20250929",
                    },
                    {
                        "provider": "google",
                        "model": "gemini-1.5-pro",
                    },
                ],
            },
            type="type",
        )
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.model_router.with_raw_response.select_model(
            body={
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant.",
                    },
                    {
                        "role": "user",
                        "content": "Explain quantum computing in simple terms",
                    },
                ],
                "llm_providers": [
                    {
                        "provider": "openai",
                        "model": "gpt-4o",
                    },
                    {
                        "provider": "anthropic",
                        "model": "claude-sonnet-4-5-20250929",
                    },
                    {
                        "provider": "google",
                        "model": "gemini-1.5-pro",
                    },
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model_router = await response.parse()
        assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.model_router.with_streaming_response.select_model(
            body={
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant.",
                    },
                    {
                        "role": "user",
                        "content": "Explain quantum computing in simple terms",
                    },
                ],
                "llm_providers": [
                    {
                        "provider": "openai",
                        "model": "gpt-4o",
                    },
                    {
                        "provider": "anthropic",
                        "model": "claude-sonnet-4-5-20250929",
                    },
                    {
                        "provider": "google",
                        "model": "gemini-1.5-pro",
                    },
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model_router = await response.parse()
            assert_matches_type(ModelRouterSelectModelResponse, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True
