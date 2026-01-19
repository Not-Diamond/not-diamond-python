# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .golden_record_param import GoldenRecordParam
from .request_provider_param import RequestProviderParam

__all__ = ["PromptOptimizationOptimizeParams"]


class PromptOptimizationOptimizeParams(TypedDict, total=False):
    fields: Required[SequenceNotStr[str]]
    """List of field names that will be substituted into the template.

    Must match keys in golden records
    """

    system_prompt: Required[str]
    """System prompt to use with the origin model.

    This sets the context and role for the LLM
    """

    target_models: Required[Iterable[RequestProviderParam]]
    """List of models to optimize the prompt for.

    Maximum count depends on your subscription tier (Free: 1, Starter: 3, Startup:
    5, Enterprise: 10)
    """

    template: Required[str]
    """User message template with placeholders for fields.

    Use curly braces for field substitution
    """

    evaluation_config: Optional[str]

    evaluation_metric: Optional[str]

    goldens: Optional[Iterable[GoldenRecordParam]]
    """Training examples (legacy parameter).

    Use train_goldens and test_goldens for better control. Minimum 25 examples (or 3
    with prototype_mode=true)
    """

    origin_model: Optional[RequestProviderParam]
    """Model for specifying an LLM provider in API requests."""

    origin_model_evaluation_score: Optional[float]
    """Optional baseline score for the origin model.

    If provided, can skip origin model evaluation
    """

    prototype_mode: bool
    """Enable prototype mode to use as few as 3 training examples (instead of 25).

    Note: Performance may be degraded with fewer examples. Recommended for
    prototyping AI applications when you don't have enough data yet
    """

    test_goldens: Optional[Iterable[GoldenRecordParam]]
    """Test examples for evaluation.

    Required if train_goldens is provided. Used to measure final performance on
    held-out data
    """

    train_goldens: Optional[Iterable[GoldenRecordParam]]
    """Training examples for prompt optimization.

    Minimum 25 examples required (or 3 with prototype_mode=true). Cannot be used
    with 'goldens' parameter
    """
