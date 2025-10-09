# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecret:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: NotDiamond) -> None:
        secret = client.proxy.secret.delete(
            provider="provider",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: NotDiamond) -> None:
        response = client.proxy.secret.with_raw_response.delete(
            provider="provider",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: NotDiamond) -> None:
        with client.proxy.secret.with_streaming_response.delete(
            provider="provider",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.proxy.secret.with_raw_response.delete(
                provider="provider",
                user_id="",
                x_token="x-token",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.proxy.secret.with_raw_response.delete(
                provider="",
                user_id="user_id",
                x_token="x-token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: NotDiamond) -> None:
        secret = client.proxy.secret.upsert(
            name="name",
            provider="provider",
            secret="secret",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: NotDiamond) -> None:
        response = client.proxy.secret.with_raw_response.upsert(
            name="name",
            provider="provider",
            secret="secret",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: NotDiamond) -> None:
        with client.proxy.secret.with_streaming_response.upsert(
            name="name",
            provider="provider",
            secret="secret",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSecret:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncNotDiamond) -> None:
        secret = await async_client.proxy.secret.delete(
            provider="provider",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.proxy.secret.with_raw_response.delete(
            provider="provider",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.proxy.secret.with_streaming_response.delete(
            provider="provider",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.proxy.secret.with_raw_response.delete(
                provider="provider",
                user_id="",
                x_token="x-token",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.proxy.secret.with_raw_response.delete(
                provider="",
                user_id="user_id",
                x_token="x-token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncNotDiamond) -> None:
        secret = await async_client.proxy.secret.upsert(
            name="name",
            provider="provider",
            secret="secret",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.proxy.secret.with_raw_response.upsert(
            name="name",
            provider="provider",
            secret="secret",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(object, secret, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.proxy.secret.with_streaming_response.upsert(
            name="name",
            provider="provider",
            secret="secret",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(object, secret, path=["response"])

        assert cast(Any, response.is_closed) is True
