# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from notdiamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from notdiamond.types import PreferenceCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: NotDiamond) -> None:
        preference = client.preferences.create()
        assert_matches_type(PreferenceCreateResponse, preference, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: NotDiamond) -> None:
        preference = client.preferences.create(
            name="name",
        )
        assert_matches_type(PreferenceCreateResponse, preference, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: NotDiamond) -> None:
        response = client.preferences.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceCreateResponse, preference, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: NotDiamond) -> None:
        with client.preferences.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceCreateResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: NotDiamond) -> None:
        preference = client.preferences.update(
            preference_id="preference_id",
        )
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: NotDiamond) -> None:
        preference = client.preferences.update(
            preference_id="preference_id",
            name="name",
        )
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: NotDiamond) -> None:
        response = client.preferences.with_raw_response.update(
            preference_id="preference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: NotDiamond) -> None:
        with client.preferences.with_streaming_response.update(
            preference_id="preference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: NotDiamond) -> None:
        preference = client.preferences.delete(
            "preference_id",
        )
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: NotDiamond) -> None:
        response = client.preferences.with_raw_response.delete(
            "preference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: NotDiamond) -> None:
        with client.preferences.with_streaming_response.delete(
            "preference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preference_id` but received ''"):
            client.preferences.with_raw_response.delete(
                "",
            )


class TestAsyncPreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.create()
        assert_matches_type(PreferenceCreateResponse, preference, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.create(
            name="name",
        )
        assert_matches_type(PreferenceCreateResponse, preference, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.preferences.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceCreateResponse, preference, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.preferences.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceCreateResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.update(
            preference_id="preference_id",
        )
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.update(
            preference_id="preference_id",
            name="name",
        )
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.preferences.with_raw_response.update(
            preference_id="preference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.preferences.with_streaming_response.update(
            preference_id="preference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.delete(
            "preference_id",
        )
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.preferences.with_raw_response.delete(
            "preference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(object, preference, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.preferences.with_streaming_response.delete(
            "preference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preference_id` but received ''"):
            await async_client.preferences.with_raw_response.delete(
                "",
            )
