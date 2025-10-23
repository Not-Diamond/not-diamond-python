# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "OptimizerSelectUseridModelParams",
    "LlmProvider",
    "LlmProviderRequestProvider",
    "LlmProviderOpenRouterProvider",
]


class OptimizerSelectUseridModelParams(TypedDict, total=False):
    llm_providers: Required[Iterable[LlmProvider]]

    messages: Required[Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str]]

    user_id: Required[str]

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]

    hash_content: bool

    image_gen: bool

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
