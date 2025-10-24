# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import (
    PreferenceCreateUserPreferenceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: NotDiamond) -> None:
        preference = client.preferences.retrieve(
            preference_id="preference_id",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: NotDiamond) -> None:
        response = client.preferences.with_raw_response.retrieve(
            preference_id="preference_id",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: NotDiamond) -> None:
        with client.preferences.with_streaming_response.retrieve(
            preference_id="preference_id",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.preferences.with_raw_response.retrieve(
                preference_id="preference_id",
                user_id="",
                x_token="x-token",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preference_id` but received ''"):
            client.preferences.with_raw_response.retrieve(
                preference_id="",
                user_id="user_id",
                x_token="x-token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_user_preference(self, client: NotDiamond) -> None:
        preference = client.preferences.create_user_preference()
        assert_matches_type(PreferenceCreateUserPreferenceResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_user_preference_with_all_params(self, client: NotDiamond) -> None:
        preference = client.preferences.create_user_preference(
            name="name",
        )
        assert_matches_type(PreferenceCreateUserPreferenceResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_user_preference(self, client: NotDiamond) -> None:
        response = client.preferences.with_raw_response.create_user_preference()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceCreateUserPreferenceResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_user_preference(self, client: NotDiamond) -> None:
        with client.preferences.with_streaming_response.create_user_preference() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceCreateUserPreferenceResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_user_preference(self, client: NotDiamond) -> None:
        preference = client.preferences.delete_user_preference(
            "preference_id",
        )
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_user_preference(self, client: NotDiamond) -> None:
        response = client.preferences.with_raw_response.delete_user_preference(
            "preference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_user_preference(self, client: NotDiamond) -> None:
        with client.preferences.with_streaming_response.delete_user_preference(
            "preference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_user_preference(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preference_id` but received ''"):
            client.preferences.with_raw_response.delete_user_preference(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_user_preference(self, client: NotDiamond) -> None:
        preference = client.preferences.update_user_preference(
            preference_id="preference_id",
        )
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_user_preference_with_all_params(self, client: NotDiamond) -> None:
        preference = client.preferences.update_user_preference(
            preference_id="preference_id",
            name="name",
        )
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_user_preference(self, client: NotDiamond) -> None:
        response = client.preferences.with_raw_response.update_user_preference(
            preference_id="preference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_user_preference(self, client: NotDiamond) -> None:
        with client.preferences.with_streaming_response.update_user_preference(
            preference_id="preference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.retrieve(
            preference_id="preference_id",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.preferences.with_raw_response.retrieve(
            preference_id="preference_id",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.preferences.with_streaming_response.retrieve(
            preference_id="preference_id",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.preferences.with_raw_response.retrieve(
                preference_id="preference_id",
                user_id="",
                x_token="x-token",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preference_id` but received ''"):
            await async_client.preferences.with_raw_response.retrieve(
                preference_id="",
                user_id="user_id",
                x_token="x-token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_user_preference(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.create_user_preference()
        assert_matches_type(PreferenceCreateUserPreferenceResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_user_preference_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.create_user_preference(
            name="name",
        )
        assert_matches_type(PreferenceCreateUserPreferenceResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_user_preference(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.preferences.with_raw_response.create_user_preference()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceCreateUserPreferenceResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_user_preference(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.preferences.with_streaming_response.create_user_preference() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceCreateUserPreferenceResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_user_preference(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.delete_user_preference(
            "preference_id",
        )
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_user_preference(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.preferences.with_raw_response.delete_user_preference(
            "preference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_user_preference(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.preferences.with_streaming_response.delete_user_preference(
            "preference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_user_preference(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preference_id` but received ''"):
            await async_client.preferences.with_raw_response.delete_user_preference(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_user_preference(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.update_user_preference(
            preference_id="preference_id",
        )
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_user_preference_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        preference = await async_client.preferences.update_user_preference(
            preference_id="preference_id",
            name="name",
        )
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_user_preference(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.preferences.with_raw_response.update_user_preference(
            preference_id="preference_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(object, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_user_preference(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.preferences.with_streaming_response.update_user_preference(
            preference_id="preference_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(object, preference, path=["response"])

        assert cast(Any, response.is_closed) is True
