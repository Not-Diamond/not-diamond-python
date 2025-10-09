# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptimizer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_frontend_arena_models(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.get_frontend_arena_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_frontend_arena_models_with_all_params(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.get_frontend_arena_models(
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
            user_id="user_id",
            x_token="x-token",
            hash_content=True,
            image_gen=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_frontend_arena_models(self, client: NotDiamond) -> None:
        response = client.optimizer.with_raw_response.get_frontend_arena_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimizer = response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_frontend_arena_models(self, client: NotDiamond) -> None:
        with client.optimizer.with_streaming_response.get_frontend_arena_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimizer = response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_frontend_hash_model(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.select_frontend_hash_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_frontend_hash_model_with_all_params(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.select_frontend_hash_model(
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
            user_id="user_id",
            x_token="x-token",
            hash_content=True,
            image_gen=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_select_frontend_hash_model(self, client: NotDiamond) -> None:
        response = client.optimizer.with_raw_response.select_frontend_hash_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimizer = response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_select_frontend_hash_model(self, client: NotDiamond) -> None:
        with client.optimizer.with_streaming_response.select_frontend_hash_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimizer = response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_hash_model(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.select_hash_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_hash_model_with_all_params(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.select_hash_model(
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
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_select_hash_model(self, client: NotDiamond) -> None:
        response = client.optimizer.with_raw_response.select_hash_model(
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
        optimizer = response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_select_hash_model(self, client: NotDiamond) -> None:
        with client.optimizer.with_streaming_response.select_hash_model(
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

            optimizer = response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.select_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model_with_all_params(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.select_model(
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
            type="type",
            hash_content=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_select_model(self, client: NotDiamond) -> None:
        response = client.optimizer.with_raw_response.select_model(
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
        optimizer = response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_select_model(self, client: NotDiamond) -> None:
        with client.optimizer.with_streaming_response.select_model(
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

            optimizer = response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_userid_model(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.select_userid_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_userid_model_with_all_params(self, client: NotDiamond) -> None:
        optimizer = client.optimizer.select_userid_model(
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
            user_id="user_id",
            x_token="x-token",
            hash_content=True,
            image_gen=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_select_userid_model(self, client: NotDiamond) -> None:
        response = client.optimizer.with_raw_response.select_userid_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimizer = response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_select_userid_model(self, client: NotDiamond) -> None:
        with client.optimizer.with_streaming_response.select_userid_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimizer = response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOptimizer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_frontend_arena_models(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.get_frontend_arena_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_frontend_arena_models_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.get_frontend_arena_models(
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
            user_id="user_id",
            x_token="x-token",
            hash_content=True,
            image_gen=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_frontend_arena_models(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.optimizer.with_raw_response.get_frontend_arena_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimizer = await response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_frontend_arena_models(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.optimizer.with_streaming_response.get_frontend_arena_models(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimizer = await response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_frontend_hash_model(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.select_frontend_hash_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_frontend_hash_model_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.select_frontend_hash_model(
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
            user_id="user_id",
            x_token="x-token",
            hash_content=True,
            image_gen=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_select_frontend_hash_model(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.optimizer.with_raw_response.select_frontend_hash_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimizer = await response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_select_frontend_hash_model(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.optimizer.with_streaming_response.select_frontend_hash_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimizer = await response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_hash_model(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.select_hash_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_hash_model_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.select_hash_model(
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
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_select_hash_model(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.optimizer.with_raw_response.select_hash_model(
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
        optimizer = await response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_select_hash_model(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.optimizer.with_streaming_response.select_hash_model(
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

            optimizer = await response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.select_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.select_model(
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
            type="type",
            hash_content=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.optimizer.with_raw_response.select_model(
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
        optimizer = await response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.optimizer.with_streaming_response.select_model(
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

            optimizer = await response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_userid_model(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.select_userid_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_userid_model_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        optimizer = await async_client.optimizer.select_userid_model(
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
            user_id="user_id",
            x_token="x-token",
            hash_content=True,
            image_gen=True,
            max_model_depth=0,
            metric="metric",
            preference_id="preference_id",
            previous_session="previous_session",
            tools=[{"foo": "bar"}],
            tradeoff="tradeoff",
        )
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_select_userid_model(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.optimizer.with_raw_response.select_userid_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        optimizer = await response.parse()
        assert_matches_type(object, optimizer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_select_userid_model(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.optimizer.with_streaming_response.select_userid_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            optimizer = await response.parse()
            assert_matches_type(object, optimizer, path=["response"])

        assert cast(Any, response.is_closed) is True
