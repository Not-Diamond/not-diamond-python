# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestErrorDebug:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_error(self, client: NotDiamond) -> None:
        error_debug = client.error_debug.trigger_error()
        assert_matches_type(object, error_debug, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_trigger_error(self, client: NotDiamond) -> None:
        response = client.error_debug.with_raw_response.trigger_error()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        error_debug = response.parse()
        assert_matches_type(object, error_debug, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_trigger_error(self, client: NotDiamond) -> None:
        with client.error_debug.with_streaming_response.trigger_error() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            error_debug = response.parse()
            assert_matches_type(object, error_debug, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncErrorDebug:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_error(self, async_client: AsyncNotDiamond) -> None:
        error_debug = await async_client.error_debug.trigger_error()
        assert_matches_type(object, error_debug, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_trigger_error(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.error_debug.with_raw_response.trigger_error()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        error_debug = await response.parse()
        assert_matches_type(object, error_debug, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_error(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.error_debug.with_streaming_response.trigger_error() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            error_debug = await response.parse()
            assert_matches_type(object, error_debug, path=["response"])

        assert cast(Any, response.is_closed) is True
