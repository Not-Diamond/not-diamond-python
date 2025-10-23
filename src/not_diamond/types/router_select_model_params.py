# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["RouterSelectModelParams", "LlmProvider", "LlmProviderRequestProvider", "LlmProviderOpenRouterProvider"]


class RouterSelectModelParams(TypedDict, total=False):
    llm_providers: Required[Iterable[LlmProvider]]

    messages: Required[Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str]]

    type: Optional[str]

    hash_content: bool

    max_model_depth: Optional[int]

    metric: str

    preference_id: Optional[str]

    previous_session: Optional[str]

    tools: Optional[Iterable[Dict[str, object]]]

    tradeoff: Optional[str]


class LlmProviderRequestProvider(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]


class LlmProviderOpenRouterProvider(TypedDict, total=False):
    model: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]


LlmProvider: TypeAlias = Union[LlmProviderRequestProvider, LlmProviderOpenRouterProvider]
