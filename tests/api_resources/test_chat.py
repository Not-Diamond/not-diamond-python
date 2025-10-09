# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model(self, client: NotDiamond) -> None:
        chat = client.chat.select_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model_with_all_params(self, client: NotDiamond) -> None:
        chat = client.chat.select_model(
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
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_select_model(self, client: NotDiamond) -> None:
        response = client.chat.with_raw_response.select_model(
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
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_select_model(self, client: NotDiamond) -> None:
        with client.chat.with_streaming_response.select_model(
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

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model(self, async_client: AsyncNotDiamond) -> None:
        chat = await async_client.chat.select_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        chat = await async_client.chat.select_model(
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
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.chat.with_raw_response.select_model(
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
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.chat.with_streaming_response.select_model(
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

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
