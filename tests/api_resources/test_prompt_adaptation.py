# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from not_diamond import NotDiamond, AsyncNotDiamond
from tests.utils import assert_matches_type
from not_diamond.types import (
    PromptAdaptationCreateResponse,
    PromptAdaptationGetCostsResponse,
    PromptAdaptationGetAdaptStatusResponse,
    PromptAdaptationGetAdaptResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromptAdaptation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: NotDiamond) -> None:
        prompt_adaptation = client.prompt_adaptation.create(
            fields=["question"],
            system_prompt="You are a helpful assistant that answers questions accurately.",
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
        assert_matches_type(PromptAdaptationCreateResponse, prompt_adaptation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: NotDiamond) -> None:
        prompt_adaptation = client.prompt_adaptation.create(
            fields=["question"],
            system_prompt="You are a helpful assistant that answers questions accurately.",
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
            evaluation_metric="LLMaaJ:Sem_Sim_3",
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
            test_goldens=[
                {
                    "fields": {"question": "What is 3*3?"},
                    "answer": "9",
                },
                {
                    "fields": {"question": "What is the largest ocean?"},
                    "answer": "Pacific Ocean",
                },
            ],
            train_goldens=[
                {
                    "fields": {"question": "What is 2+2?"},
                    "answer": "4",
                },
                {
                    "fields": {"question": "What is the capital of France?"},
                    "answer": "Paris",
                },
                {
                    "fields": {"question": "Who wrote Romeo and Juliet?"},
                    "answer": "William Shakespeare",
                },
                {
                    "fields": {"question": "What is H2O?"},
                    "answer": "Water",
                },
                {
                    "fields": {"question": "How many continents are there?"},
                    "answer": "7",
                },
            ],
        )
        assert_matches_type(PromptAdaptationCreateResponse, prompt_adaptation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: NotDiamond) -> None:
        response = client.prompt_adaptation.with_raw_response.create(
            fields=["question"],
            system_prompt="You are a helpful assistant that answers questions accurately.",
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
        prompt_adaptation = response.parse()
        assert_matches_type(PromptAdaptationCreateResponse, prompt_adaptation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: NotDiamond) -> None:
        with client.prompt_adaptation.with_streaming_response.create(
            fields=["question"],
            system_prompt="You are a helpful assistant that answers questions accurately.",
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

            prompt_adaptation = response.parse()
            assert_matches_type(PromptAdaptationCreateResponse, prompt_adaptation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_adapt_results(self, client: NotDiamond) -> None:
        prompt_adaptation = client.prompt_adaptation.get_adapt_results(
            "adaptation_run_id",
        )
        assert_matches_type(PromptAdaptationGetAdaptResultsResponse, prompt_adaptation, path=["response"])

    @parametrize
    def test_raw_response_get_adapt_results(self, client: NotDiamond) -> None:
        response = client.prompt_adaptation.with_raw_response.get_adapt_results(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_adaptation = response.parse()
        assert_matches_type(PromptAdaptationGetAdaptResultsResponse, prompt_adaptation, path=["response"])

    @parametrize
    def test_streaming_response_get_adapt_results(self, client: NotDiamond) -> None:
        with client.prompt_adaptation.with_streaming_response.get_adapt_results(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_adaptation = response.parse()
            assert_matches_type(PromptAdaptationGetAdaptResultsResponse, prompt_adaptation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_adapt_results(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            client.prompt_adaptation.with_raw_response.get_adapt_results(
                "",
            )

    @parametrize
    def test_method_get_adapt_status(self, client: NotDiamond) -> None:
        prompt_adaptation = client.prompt_adaptation.get_adapt_status(
            "adaptation_run_id",
        )
        assert_matches_type(PromptAdaptationGetAdaptStatusResponse, prompt_adaptation, path=["response"])

    @parametrize
    def test_raw_response_get_adapt_status(self, client: NotDiamond) -> None:
        response = client.prompt_adaptation.with_raw_response.get_adapt_status(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_adaptation = response.parse()
        assert_matches_type(PromptAdaptationGetAdaptStatusResponse, prompt_adaptation, path=["response"])

    @parametrize
    def test_streaming_response_get_adapt_status(self, client: NotDiamond) -> None:
        with client.prompt_adaptation.with_streaming_response.get_adapt_status(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_adaptation = response.parse()
            assert_matches_type(PromptAdaptationGetAdaptStatusResponse, prompt_adaptation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_adapt_status(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            client.prompt_adaptation.with_raw_response.get_adapt_status(
                "",
            )

    @parametrize
    def test_method_get_costs(self, client: NotDiamond) -> None:
        prompt_adaptation = client.prompt_adaptation.get_costs(
            "adaptation_run_id",
        )
        assert_matches_type(PromptAdaptationGetCostsResponse, prompt_adaptation, path=["response"])

    @parametrize
    def test_raw_response_get_costs(self, client: NotDiamond) -> None:
        response = client.prompt_adaptation.with_raw_response.get_costs(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_adaptation = response.parse()
        assert_matches_type(PromptAdaptationGetCostsResponse, prompt_adaptation, path=["response"])

    @parametrize
    def test_streaming_response_get_costs(self, client: NotDiamond) -> None:
        with client.prompt_adaptation.with_streaming_response.get_costs(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_adaptation = response.parse()
            assert_matches_type(PromptAdaptationGetCostsResponse, prompt_adaptation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_costs(self, client: NotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            client.prompt_adaptation.with_raw_response.get_costs(
                "",
            )


class TestAsyncPromptAdaptation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncNotDiamond) -> None:
        prompt_adaptation = await async_client.prompt_adaptation.create(
            fields=["question"],
            system_prompt="You are a helpful assistant that answers questions accurately.",
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
        assert_matches_type(PromptAdaptationCreateResponse, prompt_adaptation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncNotDiamond) -> None:
        prompt_adaptation = await async_client.prompt_adaptation.create(
            fields=["question"],
            system_prompt="You are a helpful assistant that answers questions accurately.",
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
            evaluation_metric="LLMaaJ:Sem_Sim_3",
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
            test_goldens=[
                {
                    "fields": {"question": "What is 3*3?"},
                    "answer": "9",
                },
                {
                    "fields": {"question": "What is the largest ocean?"},
                    "answer": "Pacific Ocean",
                },
            ],
            train_goldens=[
                {
                    "fields": {"question": "What is 2+2?"},
                    "answer": "4",
                },
                {
                    "fields": {"question": "What is the capital of France?"},
                    "answer": "Paris",
                },
                {
                    "fields": {"question": "Who wrote Romeo and Juliet?"},
                    "answer": "William Shakespeare",
                },
                {
                    "fields": {"question": "What is H2O?"},
                    "answer": "Water",
                },
                {
                    "fields": {"question": "How many continents are there?"},
                    "answer": "7",
                },
            ],
        )
        assert_matches_type(PromptAdaptationCreateResponse, prompt_adaptation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt_adaptation.with_raw_response.create(
            fields=["question"],
            system_prompt="You are a helpful assistant that answers questions accurately.",
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
        prompt_adaptation = await response.parse()
        assert_matches_type(PromptAdaptationCreateResponse, prompt_adaptation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt_adaptation.with_streaming_response.create(
            fields=["question"],
            system_prompt="You are a helpful assistant that answers questions accurately.",
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

            prompt_adaptation = await response.parse()
            assert_matches_type(PromptAdaptationCreateResponse, prompt_adaptation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        prompt_adaptation = await async_client.prompt_adaptation.get_adapt_results(
            "adaptation_run_id",
        )
        assert_matches_type(PromptAdaptationGetAdaptResultsResponse, prompt_adaptation, path=["response"])

    @parametrize
    async def test_raw_response_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt_adaptation.with_raw_response.get_adapt_results(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_adaptation = await response.parse()
        assert_matches_type(PromptAdaptationGetAdaptResultsResponse, prompt_adaptation, path=["response"])

    @parametrize
    async def test_streaming_response_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt_adaptation.with_streaming_response.get_adapt_results(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_adaptation = await response.parse()
            assert_matches_type(PromptAdaptationGetAdaptResultsResponse, prompt_adaptation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_adapt_results(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            await async_client.prompt_adaptation.with_raw_response.get_adapt_results(
                "",
            )

    @parametrize
    async def test_method_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        prompt_adaptation = await async_client.prompt_adaptation.get_adapt_status(
            "adaptation_run_id",
        )
        assert_matches_type(PromptAdaptationGetAdaptStatusResponse, prompt_adaptation, path=["response"])

    @parametrize
    async def test_raw_response_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt_adaptation.with_raw_response.get_adapt_status(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_adaptation = await response.parse()
        assert_matches_type(PromptAdaptationGetAdaptStatusResponse, prompt_adaptation, path=["response"])

    @parametrize
    async def test_streaming_response_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt_adaptation.with_streaming_response.get_adapt_status(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_adaptation = await response.parse()
            assert_matches_type(PromptAdaptationGetAdaptStatusResponse, prompt_adaptation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_adapt_status(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            await async_client.prompt_adaptation.with_raw_response.get_adapt_status(
                "",
            )

    @parametrize
    async def test_method_get_costs(self, async_client: AsyncNotDiamond) -> None:
        prompt_adaptation = await async_client.prompt_adaptation.get_costs(
            "adaptation_run_id",
        )
        assert_matches_type(PromptAdaptationGetCostsResponse, prompt_adaptation, path=["response"])

    @parametrize
    async def test_raw_response_get_costs(self, async_client: AsyncNotDiamond) -> None:
        response = await async_client.prompt_adaptation.with_raw_response.get_costs(
            "adaptation_run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_adaptation = await response.parse()
        assert_matches_type(PromptAdaptationGetCostsResponse, prompt_adaptation, path=["response"])

    @parametrize
    async def test_streaming_response_get_costs(self, async_client: AsyncNotDiamond) -> None:
        async with async_client.prompt_adaptation.with_streaming_response.get_costs(
            "adaptation_run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_adaptation = await response.parse()
            assert_matches_type(PromptAdaptationGetCostsResponse, prompt_adaptation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_costs(self, async_client: AsyncNotDiamond) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `adaptation_run_id` but received ''"):
            await async_client.prompt_adaptation.with_raw_response.get_costs(
                "",
            )
