# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import (
    PromptAdaptResponse,
    AdaptationRunResults,
    PromptGetAdaptRunsResponse,
    PromptGetAdaptStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompt:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_adapt(self, client: NotDiamond) -> None:
        prompt = client.prompt.adapt(
            fields=["string"],
            goldens=[{"fields": {"foo": "string"}}],
            origin_model={
                "model": "model",
                "provider": "provider",
            },
            system_prompt="system_prompt",
            target_models=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            template="template",
        )
        assert_matches_type(PromptAdaptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_adapt_with_all_params(self, client: NotDiamond) -> None:
        prompt = client.prompt.adapt(
            fields=["string"],
            goldens=[
                {
                    "fields": {"foo": "string"},
                    "answer": "answer",
                }
            ],
            origin_model={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            system_prompt="system_prompt",
            target_models=[
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
            template="template",
            evaluation_config="evaluation_config",
            evaluation_metric="evaluation_metric",
            origin_model_evaluation_score=0,
        )
        assert_matches_type(PromptAdaptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_adapt(self, client: NotDiamond) -> None:
        response = client.prompt.with_raw_response.adapt(
            fields=["string"],
            goldens=[{"fields": {"foo": "string"}}],
            origin_model={
                "model": "model",
                "provider": "provider",
            },
            system_prompt="system_prompt",
            target_models=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptAdaptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_adapt(self, client: NotDiamond) -> None:
        with client.prompt.with_streaming_response.adapt(
            fields=["string"],
            goldens=[{"fields": {"foo": "string"}}],
            origin_model={
                "model": "model",
                "provider": "provider",
            },
            system_prompt="system_prompt",
            target_models=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptAdaptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_adapt_results(self, client: NotDiamond) -> None:
        prompt = client.prompt.get_adapt_results(
            "adaptation_run_id",
        )
        assert_matches_type(AdaptationRunResults, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_adapt_results(self, client: NotDiamond) -> None:
        response = client.prompt.with_raw_response.get_adapt_results(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(AdaptationRunResults, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_adapt_results(self, client: NotDiamond) -> None:
        with client.prompt.with_streaming_response.get_adapt_results(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(AdaptationRunResults, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_adapt_results(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            client.prompt.with_raw_response.get_adapt_results(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_adapt_run_results(self, client: NotDiamond) -> None:
        prompt = client.prompt.get_adapt_run_results(
            adaptation_run_id="adaptation_run_id",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(AdaptationRunResults, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_adapt_run_results(self, client: NotDiamond) -> None:
        response = client.prompt.with_raw_response.get_adapt_run_results(
            adaptation_run_id="adaptation_run_id",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(AdaptationRunResults, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_adapt_run_results(self, client: NotDiamond) -> None:
        with client.prompt.with_streaming_response.get_adapt_run_results(
            adaptation_run_id="adaptation_run_id",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(AdaptationRunResults, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_adapt_run_results(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.prompt.with_raw_response.get_adapt_run_results(
                adaptation_run_id="adaptation_run_id",
                user_id="",
                x_token="x-token",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            client.prompt.with_raw_response.get_adapt_run_results(
                adaptation_run_id="",
                user_id="user_id",
                x_token="x-token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_adapt_runs(self, client: NotDiamond) -> None:
        prompt = client.prompt.get_adapt_runs(
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(PromptGetAdaptRunsResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_adapt_runs(self, client: NotDiamond) -> None:
        response = client.prompt.with_raw_response.get_adapt_runs(
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptGetAdaptRunsResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_adapt_runs(self, client: NotDiamond) -> None:
        with client.prompt.with_streaming_response.get_adapt_runs(
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptGetAdaptRunsResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_adapt_runs(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.prompt.with_raw_response.get_adapt_runs(
                user_id="",
                x_token="x-token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_adapt_status(self, client: NotDiamond) -> None:
        prompt = client.prompt.get_adapt_status(
            "adaptation_run_id",
        )
        assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_adapt_status(self, client: NotDiamond) -> None:
        response = client.prompt.with_raw_response.get_adapt_status(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_adapt_status(self, client: NotDiamond) -> None:
        with client.prompt.with_streaming_response.get_adapt_status(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_adapt_status(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            client.prompt.with_raw_response.get_adapt_status(
                "",
            )


class TestAsyncPrompt:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_adapt(self, async_client: AsyncNotDiamond) -> None:
        prompt = await async_client.prompt.adapt(
            fields=["string"],
            goldens=[{"fields": {"foo": "string"}}],
            origin_model={
                "model": "model",
                "provider": "provider",
            },
            system_prompt="system_prompt",
            target_models=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            template="template",
        )
        assert_matches_type(PromptAdaptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_adapt_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        prompt = await async_client.prompt.adapt(
            fields=["string"],
            goldens=[
                {
                    "fields": {"foo": "string"},
                    "answer": "answer",
                }
            ],
            origin_model={
                "model": "model",
                "provider": "provider",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            system_prompt="system_prompt",
            target_models=[
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
            template="template",
            evaluation_config="evaluation_config",
            evaluation_metric="evaluation_metric",
            origin_model_evaluation_score=0,
        )
        assert_matches_type(PromptAdaptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_adapt(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt.with_raw_response.adapt(
            fields=["string"],
            goldens=[{"fields": {"foo": "string"}}],
            origin_model={
                "model": "model",
                "provider": "provider",
            },
            system_prompt="system_prompt",
            target_models=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptAdaptResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_adapt(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt.with_streaming_response.adapt(
            fields=["string"],
            goldens=[{"fields": {"foo": "string"}}],
            origin_model={
                "model": "model",
                "provider": "provider",
            },
            system_prompt="system_prompt",
            target_models=[
                {
                    "model": "model",
                    "provider": "provider",
                }
            ],
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptAdaptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        prompt = await async_client.prompt.get_adapt_results(
            "adaptation_run_id",
        )
        assert_matches_type(AdaptationRunResults, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt.with_raw_response.get_adapt_results(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(AdaptationRunResults, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt.with_streaming_response.get_adapt_results(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(AdaptationRunResults, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            await async_client.prompt.with_raw_response.get_adapt_results(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_adapt_run_results(self, async_client: AsyncNotDiamond) -> None:
        prompt = await async_client.prompt.get_adapt_run_results(
            adaptation_run_id="adaptation_run_id",
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(AdaptationRunResults, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_adapt_run_results(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt.with_raw_response.get_adapt_run_results(
            adaptation_run_id="adaptation_run_id",
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(AdaptationRunResults, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_adapt_run_results(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt.with_streaming_response.get_adapt_run_results(
            adaptation_run_id="adaptation_run_id",
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(AdaptationRunResults, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_adapt_run_results(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.prompt.with_raw_response.get_adapt_run_results(
                adaptation_run_id="adaptation_run_id",
                user_id="",
                x_token="x-token",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            await async_client.prompt.with_raw_response.get_adapt_run_results(
                adaptation_run_id="",
                user_id="user_id",
                x_token="x-token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_adapt_runs(self, async_client: AsyncNotDiamond) -> None:
        prompt = await async_client.prompt.get_adapt_runs(
            user_id="user_id",
            x_token="x-token",
        )
        assert_matches_type(PromptGetAdaptRunsResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_adapt_runs(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt.with_raw_response.get_adapt_runs(
            user_id="user_id",
            x_token="x-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptGetAdaptRunsResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_adapt_runs(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt.with_streaming_response.get_adapt_runs(
            user_id="user_id",
            x_token="x-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptGetAdaptRunsResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_adapt_runs(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.prompt.with_raw_response.get_adapt_runs(
                user_id="",
                x_token="x-token",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        prompt = await async_client.prompt.get_adapt_status(
            "adaptation_run_id",
        )
        assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt.with_raw_response.get_adapt_status(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt.with_streaming_response.get_adapt_status(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptGetAdaptStatusResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            await async_client.prompt.with_raw_response.get_adapt_status(
                "",
            )
