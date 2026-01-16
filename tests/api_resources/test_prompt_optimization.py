# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from notdiamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from notdiamond.types import (
    PromptOptimizationOptimizeResponse,
    PromptOptimizationRetrieveCostsResponse,
    PromptOptimizationGetOptimziationStatusResponse,
    PromptOptimizationGetOptimizationResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromptOptimization:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_optimization_results(self, client: NotDiamond) -> None:
        prompt_optimization = client.prompt_optimization.get_optimization_results(
            "optimization_run_id",
        )
        assert_matches_type(PromptOptimizationGetOptimizationResultsResponse, prompt_optimization, path=["response"])

    @parametrize
    def test_raw_response_get_optimization_results(self, client: NotDiamond) -> None:
        response = client.prompt_optimization.with_raw_response.get_optimization_results(
            "optimization_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization = response.parse()
        assert_matches_type(PromptOptimizationGetOptimizationResultsResponse, prompt_optimization, path=["response"])

    @parametrize
    def test_streaming_response_get_optimization_results(self, client: NotDiamond) -> None:
        with client.prompt_optimization.with_streaming_response.get_optimization_results(
            "optimization_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization = response.parse()
            assert_matches_type(
                PromptOptimizationGetOptimizationResultsResponse, prompt_optimization, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_optimization_results(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `optimization_run_id` but received ''"):
            client.prompt_optimization.with_raw_response.get_optimization_results(
                "",
            )

    @parametrize
    def test_method_get_optimziation_status(self, client: NotDiamond) -> None:
        prompt_optimization = client.prompt_optimization.get_optimziation_status(
            "optimization_run_id",
        )
        assert_matches_type(PromptOptimizationGetOptimziationStatusResponse, prompt_optimization, path=["response"])

    @parametrize
    def test_raw_response_get_optimziation_status(self, client: NotDiamond) -> None:
        response = client.prompt_optimization.with_raw_response.get_optimziation_status(
            "optimization_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization = response.parse()
        assert_matches_type(PromptOptimizationGetOptimziationStatusResponse, prompt_optimization, path=["response"])

    @parametrize
    def test_streaming_response_get_optimziation_status(self, client: NotDiamond) -> None:
        with client.prompt_optimization.with_streaming_response.get_optimziation_status(
            "optimization_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization = response.parse()
            assert_matches_type(PromptOptimizationGetOptimziationStatusResponse, prompt_optimization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_optimziation_status(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `optimization_run_id` but received ''"):
            client.prompt_optimization.with_raw_response.get_optimziation_status(
                "",
            )

    @parametrize
    def test_method_optimize(self, client: NotDiamond) -> None:
        prompt_optimization = client.prompt_optimization.optimize(
            fields=["question"],
            system_prompt="You are a mathematical assistant that counts digits accurately.",
            target_models=[
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-2.5-flash",
                    "provider": "google",
                },
            ],
            template="Question: {question}\nAnswer:",
        )
        assert_matches_type(PromptOptimizationOptimizeResponse, prompt_optimization, path=["response"])

    @parametrize
    def test_method_optimize_with_all_params(self, client: NotDiamond) -> None:
        prompt_optimization = client.prompt_optimization.optimize(
            fields=["question"],
            system_prompt="You are a mathematical assistant that counts digits accurately.",
            target_models=[
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
                {
                    "model": "gemini-2.5-flash",
                    "provider": "google",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
            ],
            template="Question: {question}\nAnswer:",
            evaluation_config="evaluation_config",
            evaluation_metric="LLMaaJ:Sem_Sim_1",
            goldens=[
                {
                    "fields": {
                        "context": "Basic arithmetic",
                        "question": "What is 2+2?",
                    },
                    "answer": "4",
                }
            ],
            origin_model={
                "model": "gpt-4o",
                "provider": "openai",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            origin_model_evaluation_score=0,
            prototype_mode=True,
            test_goldens=[
                {
                    "fields": {"question": "How many digits are in (9876543210*123456)?"},
                    "answer": "15",
                },
                {
                    "fields": {"question": "How many odd digits are in (135*579*246)?"},
                    "answer": "8",
                },
                {
                    "fields": {"question": "How often does the number '42' appear in the digits of (123456789*42)?"},
                    "answer": "1",
                },
                {
                    "fields": {"question": "How many even digits are in (1111*2222*3333)?"},
                    "answer": "10",
                },
                {
                    "fields": {"question": "How many 9s are in (999999*888888)?"},
                    "answer": "11",
                },
            ],
            train_goldens=[
                {
                    "fields": {"question": "How many digits are in (23874045494*2789392485)?"},
                    "answer": "20",
                },
                {
                    "fields": {"question": "How many odd digits are in (999*777*555*333*111)?"},
                    "answer": "10",
                },
                {
                    "fields": {"question": "How often does the number '17' appear in the digits of (287558*17)?"},
                    "answer": "0",
                },
                {
                    "fields": {"question": "How many even digits are in (222*444*666*888)?"},
                    "answer": "16",
                },
                {
                    "fields": {"question": "How many 0s are in (1234567890*1357908642)?"},
                    "answer": "2",
                },
            ],
        )
        assert_matches_type(PromptOptimizationOptimizeResponse, prompt_optimization, path=["response"])

    @parametrize
    def test_raw_response_optimize(self, client: NotDiamond) -> None:
        response = client.prompt_optimization.with_raw_response.optimize(
            fields=["question"],
            system_prompt="You are a mathematical assistant that counts digits accurately.",
            target_models=[
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-2.5-flash",
                    "provider": "google",
                },
            ],
            template="Question: {question}\nAnswer:",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization = response.parse()
        assert_matches_type(PromptOptimizationOptimizeResponse, prompt_optimization, path=["response"])

    @parametrize
    def test_streaming_response_optimize(self, client: NotDiamond) -> None:
        with client.prompt_optimization.with_streaming_response.optimize(
            fields=["question"],
            system_prompt="You are a mathematical assistant that counts digits accurately.",
            target_models=[
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-2.5-flash",
                    "provider": "google",
                },
            ],
            template="Question: {question}\nAnswer:",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization = response.parse()
            assert_matches_type(PromptOptimizationOptimizeResponse, prompt_optimization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_costs(self, client: NotDiamond) -> None:
        prompt_optimization = client.prompt_optimization.retrieve_costs(
            "optimization_run_id",
        )
        assert_matches_type(PromptOptimizationRetrieveCostsResponse, prompt_optimization, path=["response"])

    @parametrize
    def test_raw_response_retrieve_costs(self, client: NotDiamond) -> None:
        response = client.prompt_optimization.with_raw_response.retrieve_costs(
            "optimization_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization = response.parse()
        assert_matches_type(PromptOptimizationRetrieveCostsResponse, prompt_optimization, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_costs(self, client: NotDiamond) -> None:
        with client.prompt_optimization.with_streaming_response.retrieve_costs(
            "optimization_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization = response.parse()
            assert_matches_type(PromptOptimizationRetrieveCostsResponse, prompt_optimization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_costs(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `optimization_run_id` but received ''"):
            client.prompt_optimization.with_raw_response.retrieve_costs(
                "",
            )


class TestAsyncPromptOptimization:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_optimization_results(self, async_client: AsyncNotDiamond) -> None:
        prompt_optimization = await async_client.prompt_optimization.get_optimization_results(
            "optimization_run_id",
        )
        assert_matches_type(PromptOptimizationGetOptimizationResultsResponse, prompt_optimization, path=["response"])

    @parametrize
    async def test_raw_response_get_optimization_results(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt_optimization.with_raw_response.get_optimization_results(
            "optimization_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization = await response.parse()
        assert_matches_type(PromptOptimizationGetOptimizationResultsResponse, prompt_optimization, path=["response"])

    @parametrize
    async def test_streaming_response_get_optimization_results(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt_optimization.with_streaming_response.get_optimization_results(
            "optimization_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization = await response.parse()
            assert_matches_type(
                PromptOptimizationGetOptimizationResultsResponse, prompt_optimization, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_optimization_results(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `optimization_run_id` but received ''"):
            await async_client.prompt_optimization.with_raw_response.get_optimization_results(
                "",
            )

    @parametrize
    async def test_method_get_optimziation_status(self, async_client: AsyncNotDiamond) -> None:
        prompt_optimization = await async_client.prompt_optimization.get_optimziation_status(
            "optimization_run_id",
        )
        assert_matches_type(PromptOptimizationGetOptimziationStatusResponse, prompt_optimization, path=["response"])

    @parametrize
    async def test_raw_response_get_optimziation_status(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt_optimization.with_raw_response.get_optimziation_status(
            "optimization_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization = await response.parse()
        assert_matches_type(PromptOptimizationGetOptimziationStatusResponse, prompt_optimization, path=["response"])

    @parametrize
    async def test_streaming_response_get_optimziation_status(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt_optimization.with_streaming_response.get_optimziation_status(
            "optimization_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization = await response.parse()
            assert_matches_type(PromptOptimizationGetOptimziationStatusResponse, prompt_optimization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_optimziation_status(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `optimization_run_id` but received ''"):
            await async_client.prompt_optimization.with_raw_response.get_optimziation_status(
                "",
            )

    @parametrize
    async def test_method_optimize(self, async_client: AsyncNotDiamond) -> None:
        prompt_optimization = await async_client.prompt_optimization.optimize(
            fields=["question"],
            system_prompt="You are a mathematical assistant that counts digits accurately.",
            target_models=[
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-2.5-flash",
                    "provider": "google",
                },
            ],
            template="Question: {question}\nAnswer:",
        )
        assert_matches_type(PromptOptimizationOptimizeResponse, prompt_optimization, path=["response"])

    @parametrize
    async def test_method_optimize_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        prompt_optimization = await async_client.prompt_optimization.optimize(
            fields=["question"],
            system_prompt="You are a mathematical assistant that counts digits accurately.",
            target_models=[
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
                {
                    "model": "gemini-2.5-flash",
                    "provider": "google",
                    "context_length": 0,
                    "input_price": 0,
                    "is_custom": True,
                    "latency": 0,
                    "output_price": 0,
                },
            ],
            template="Question: {question}\nAnswer:",
            evaluation_config="evaluation_config",
            evaluation_metric="LLMaaJ:Sem_Sim_1",
            goldens=[
                {
                    "fields": {
                        "context": "Basic arithmetic",
                        "question": "What is 2+2?",
                    },
                    "answer": "4",
                }
            ],
            origin_model={
                "model": "gpt-4o",
                "provider": "openai",
                "context_length": 0,
                "input_price": 0,
                "is_custom": True,
                "latency": 0,
                "output_price": 0,
            },
            origin_model_evaluation_score=0,
            prototype_mode=True,
            test_goldens=[
                {
                    "fields": {"question": "How many digits are in (9876543210*123456)?"},
                    "answer": "15",
                },
                {
                    "fields": {"question": "How many odd digits are in (135*579*246)?"},
                    "answer": "8",
                },
                {
                    "fields": {"question": "How often does the number '42' appear in the digits of (123456789*42)?"},
                    "answer": "1",
                },
                {
                    "fields": {"question": "How many even digits are in (1111*2222*3333)?"},
                    "answer": "10",
                },
                {
                    "fields": {"question": "How many 9s are in (999999*888888)?"},
                    "answer": "11",
                },
            ],
            train_goldens=[
                {
                    "fields": {"question": "How many digits are in (23874045494*2789392485)?"},
                    "answer": "20",
                },
                {
                    "fields": {"question": "How many odd digits are in (999*777*555*333*111)?"},
                    "answer": "10",
                },
                {
                    "fields": {"question": "How often does the number '17' appear in the digits of (287558*17)?"},
                    "answer": "0",
                },
                {
                    "fields": {"question": "How many even digits are in (222*444*666*888)?"},
                    "answer": "16",
                },
                {
                    "fields": {"question": "How many 0s are in (1234567890*1357908642)?"},
                    "answer": "2",
                },
            ],
        )
        assert_matches_type(PromptOptimizationOptimizeResponse, prompt_optimization, path=["response"])

    @parametrize
    async def test_raw_response_optimize(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt_optimization.with_raw_response.optimize(
            fields=["question"],
            system_prompt="You are a mathematical assistant that counts digits accurately.",
            target_models=[
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-2.5-flash",
                    "provider": "google",
                },
            ],
            template="Question: {question}\nAnswer:",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization = await response.parse()
        assert_matches_type(PromptOptimizationOptimizeResponse, prompt_optimization, path=["response"])

    @parametrize
    async def test_streaming_response_optimize(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt_optimization.with_streaming_response.optimize(
            fields=["question"],
            system_prompt="You are a mathematical assistant that counts digits accurately.",
            target_models=[
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-2.5-flash",
                    "provider": "google",
                },
            ],
            template="Question: {question}\nAnswer:",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization = await response.parse()
            assert_matches_type(PromptOptimizationOptimizeResponse, prompt_optimization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_costs(self, async_client: AsyncNotDiamond) -> None:
        prompt_optimization = await async_client.prompt_optimization.retrieve_costs(
            "optimization_run_id",
        )
        assert_matches_type(PromptOptimizationRetrieveCostsResponse, prompt_optimization, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_costs(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt_optimization.with_raw_response.retrieve_costs(
            "optimization_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_optimization = await response.parse()
        assert_matches_type(PromptOptimizationRetrieveCostsResponse, prompt_optimization, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_costs(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt_optimization.with_streaming_response.retrieve_costs(
            "optimization_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_optimization = await response.parse()
            assert_matches_type(PromptOptimizationRetrieveCostsResponse, prompt_optimization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_costs(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `optimization_run_id` but received ''"):
            await async_client.prompt_optimization.with_raw_response.retrieve_costs(
                "",
            )
