# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PromptEstimateAdaptLlmRequestsParams", "TargetModel", "OriginModel"]


class PromptEstimateAdaptLlmRequestsParams(TypedDict, total=False):
    target_models: Required[Iterable[TargetModel]]

    num_goldens: Optional[int]

    num_test_goldens: Optional[int]

    num_train_goldens: Optional[int]

    origin_model: Optional[OriginModel]


class TargetModel(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]


class OriginModel(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]
