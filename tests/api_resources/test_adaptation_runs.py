# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import AdaptationRunRetrieveCostsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdaptationRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_costs(self, client: NotDiamond) -> None:
        adaptation_run = client.adaptation_runs.retrieve_costs(
            "adaptation_run_id",
        )
        assert_matches_type(AdaptationRunRetrieveCostsResponse, adaptation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_costs(self, client: NotDiamond) -> None:
        response = client.adaptation_runs.with_raw_response.retrieve_costs(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        adaptation_run = response.parse()
        assert_matches_type(AdaptationRunRetrieveCostsResponse, adaptation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_costs(self, client: NotDiamond) -> None:
        with client.adaptation_runs.with_streaming_response.retrieve_costs(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            adaptation_run = response.parse()
            assert_matches_type(AdaptationRunRetrieveCostsResponse, adaptation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_costs(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            client.adaptation_runs.with_raw_response.retrieve_costs(
                "",
            )


class TestAsyncAdaptationRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_costs(self, async_client: AsyncNotDiamond) -> None:
        adaptation_run = await async_client.adaptation_runs.retrieve_costs(
            "adaptation_run_id",
        )
        assert_matches_type(AdaptationRunRetrieveCostsResponse, adaptation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_costs(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.adaptation_runs.with_raw_response.retrieve_costs(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        adaptation_run = await response.parse()
        assert_matches_type(AdaptationRunRetrieveCostsResponse, adaptation_run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_costs(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.adaptation_runs.with_streaming_response.retrieve_costs(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            adaptation_run = await response.parse()
            assert_matches_type(AdaptationRunRetrieveCostsResponse, adaptation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_costs(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            await async_client.adaptation_runs.with_raw_response.retrieve_costs(
                "",
            )
