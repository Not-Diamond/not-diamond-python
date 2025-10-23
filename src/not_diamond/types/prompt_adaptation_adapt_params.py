# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PromptAdaptationAdaptParams", "OriginModel", "TargetModel", "Golden", "TestGolden", "TrainGolden"]


class PromptAdaptationAdaptParams(TypedDict, total=False):
    fields: Required[SequenceNotStr[str]]

    origin_model: Required[OriginModel]

    system_prompt: Required[str]

    target_models: Required[Iterable[TargetModel]]

    template: Required[str]

    evaluation_config: Optional[str]

    evaluation_metric: Optional[str]

    goldens: Optional[Iterable[Golden]]

    origin_model_evaluation_score: Optional[float]

    test_goldens: Optional[Iterable[TestGolden]]

    train_goldens: Optional[Iterable[TrainGolden]]


class OriginModel(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]


class TargetModel(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]


class Golden(TypedDict, total=False):
    fields: Required[Dict[str, str]]

    answer: Optional[str]


class TestGolden(TypedDict, total=False):
    fields: Required[Dict[str, str]]

    answer: Optional[str]


class TrainGolden(TypedDict, total=False):
    fields: Required[Dict[str, str]]

    answer: Optional[str]
