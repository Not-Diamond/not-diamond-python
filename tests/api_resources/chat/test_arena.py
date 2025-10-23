# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArena:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_choice(self, client: NotDiamond) -> None:
        arena = client.chat.arena.create_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_choice_with_all_params(self, client: NotDiamond) -> None:
        arena = client.chat.arena.create_choice(
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
            user_id="user_id",
        )
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_choice(self, client: NotDiamond) -> None:
        response = client.chat.arena.with_raw_response.create_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arena = response.parse()
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_choice(self, client: NotDiamond) -> None:
        with client.chat.arena.with_streaming_response.create_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arena = response.parse()
            assert_matches_type(object, arena, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_models(self, client: NotDiamond) -> None:
        arena = client.chat.arena.create_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_models_with_all_params(self, client: NotDiamond) -> None:
        arena = client.chat.arena.create_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                }
            ],
            messages=[{"foo": "string"}],
            hash_content=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_models(self, client: NotDiamond) -> None:
        response = client.chat.arena.with_raw_response.create_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arena = response.parse()
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_models(self, client: NotDiamond) -> None:
        with client.chat.arena.with_streaming_response.create_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arena = response.parse()
            assert_matches_type(object, arena, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncArena:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_choice(self, async_client: AsyncNotDiamond) -> None:
        arena = await async_client.chat.arena.create_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_choice_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        arena = await async_client.chat.arena.create_choice(
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
            user_id="user_id",
        )
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_choice(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.chat.arena.with_raw_response.create_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arena = await response.parse()
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_choice(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.chat.arena.with_streaming_response.create_choice(
            preferred_provider={
                "model": "model",
                "provider": "provider",
            },
            rejected_provider={
                "model": "model",
                "provider": "provider",
            },
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arena = await response.parse()
            assert_matches_type(object, arena, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_models(self, async_client: AsyncNotDiamond) -> None:
        arena = await async_client.chat.arena.create_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_models_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        arena = await async_client.chat.arena.create_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                }
            ],
            messages=[{"foo": "string"}],
            hash_content=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_models(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.chat.arena.with_raw_response.create_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arena = await response.parse()
        assert_matches_type(object, arena, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_models(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.chat.arena.with_streaming_response.create_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arena = await response.parse()
            assert_matches_type(object, arena, path=["response"])

        assert cast(Any, response.is_closed) is True
