# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModelRouter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_health_check(self, client: NotDiamond) -> None:
        model_router = client.model_router.health_check()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_health_check(self, client: NotDiamond) -> None:
        response = client.model_router.with_raw_response.health_check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model_router = response.parse()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_health_check(self, client: NotDiamond) -> None:
        with client.model_router.with_streaming_response.health_check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model_router = response.parse()
            assert_matches_type(object, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_hands(self, client: NotDiamond) -> None:
        model_router = client.model_router.open_hands(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_hands_with_all_params(self, client: NotDiamond) -> None:
        model_router = client.model_router.open_hands(
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
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_open_hands(self, client: NotDiamond) -> None:
        response = client.model_router.with_raw_response.open_hands(
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
        model_router = response.parse()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_open_hands(self, client: NotDiamond) -> None:
        with client.model_router.with_streaming_response.open_hands(
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

            model_router = response.parse()
            assert_matches_type(object, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model(self, client: NotDiamond) -> None:
        model_router = client.model_router.select_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_select_model_with_all_params(self, client: NotDiamond) -> None:
        model_router = client.model_router.select_model(
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
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_select_model(self, client: NotDiamond) -> None:
        response = client.model_router.with_raw_response.select_model(
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
        model_router = response.parse()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_select_model(self, client: NotDiamond) -> None:
        with client.model_router.with_streaming_response.select_model(
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

            model_router = response.parse()
            assert_matches_type(object, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModelRouter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_health_check(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.health_check()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_health_check(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.model_router.with_raw_response.health_check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model_router = await response.parse()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_health_check(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.model_router.with_streaming_response.health_check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model_router = await response.parse()
            assert_matches_type(object, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_hands(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.open_hands(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_hands_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.open_hands(
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
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_open_hands(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.model_router.with_raw_response.open_hands(
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
        model_router = await response.parse()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_open_hands(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.model_router.with_streaming_response.open_hands(
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

            model_router = await response.parse()
            assert_matches_type(object, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.select_model(
            llm_providers=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            messages=[{"foo": "string"}],
        )
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_select_model_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        model_router = await async_client.model_router.select_model(
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
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.model_router.with_raw_response.select_model(
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
        model_router = await response.parse()
        assert_matches_type(object, model_router, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_select_model(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.model_router.with_streaming_response.select_model(
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

            model_router = await response.parse()
            assert_matches_type(object, model_router, path=["response"])

        assert cast(Any, response.is_closed) is True
