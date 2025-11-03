# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PromptAdaptationAdaptParams", "TargetModel", "Golden", "OriginModel", "TestGolden", "TrainGolden"]


class PromptAdaptationAdaptParams(TypedDict, total=False):
    fields: Required[SequenceNotStr[str]]
    """List of field names that will be substituted into the template.

    Must match keys in golden records
    """

    system_prompt: Required[str]
    """System prompt to use with the origin model.

    This sets the context and role for the LLM
    """

    target_models: Required[Iterable[TargetModel]]
    """List of models to adapt the prompt for.

    Maximum count depends on your subscription tier
    """

    template: Required[str]
    """User message template with placeholders for fields.

    Use curly braces for field substitution
    """

    evaluation_config: Optional[str]

    evaluation_metric: Optional[str]

    goldens: Optional[Iterable[Golden]]
    """Training examples (legacy parameter).

    Use train_goldens and test_goldens for better control
    """

    origin_model: Optional[OriginModel]
    """Model for specifying an LLM provider in API requests."""

    origin_model_evaluation_score: Optional[float]
    """Optional baseline score for the origin model"""

    test_goldens: Optional[Iterable[TestGolden]]
    """Test examples for evaluation. Required if train_goldens is provided"""

    train_goldens: Optional[Iterable[TrainGolden]]
    """Training examples for prompt optimization. Minimum 5 examples required"""


class TargetModel(TypedDict, total=False):
    model: Required[str]
    """Model name (e.g., 'gpt-4o', 'claude-sonnet-4-5-20250929')"""

    provider: Required[str]
    """Provider name (e.g., 'openai', 'anthropic', 'google')"""

    context_length: Optional[int]
    """Maximum context length for the model (required for custom models)"""

    input_price: Optional[float]
    """Input token price per million tokens in USD (required for custom models)"""

    is_custom: bool
    """Whether this is a custom model not in Not Diamond's supported model list"""

    latency: Optional[float]
    """Average latency in seconds (required for custom models)"""

    output_price: Optional[float]
    """Output token price per million tokens in USD (required for custom models)"""


class Golden(TypedDict, total=False):
    fields: Required[Dict[str, str]]
    """Dictionary mapping field names to their values.

    Keys must match the fields specified in the template
    """

    answer: Optional[str]
    """Expected answer for supervised evaluation.

    Required for supervised metrics, optional for unsupervised
    """


class OriginModel(TypedDict, total=False):
    model: Required[str]
    """Model name (e.g., 'gpt-4o', 'claude-sonnet-4-5-20250929')"""

    provider: Required[str]
    """Provider name (e.g., 'openai', 'anthropic', 'google')"""

    context_length: Optional[int]
    """Maximum context length for the model (required for custom models)"""

    input_price: Optional[float]
    """Input token price per million tokens in USD (required for custom models)"""

    is_custom: bool
    """Whether this is a custom model not in Not Diamond's supported model list"""

    latency: Optional[float]
    """Average latency in seconds (required for custom models)"""

    output_price: Optional[float]
    """Output token price per million tokens in USD (required for custom models)"""


class TestGolden(TypedDict, total=False):
    fields: Required[Dict[str, str]]
    """Dictionary mapping field names to their values.

    Keys must match the fields specified in the template
    """

    answer: Optional[str]
    """Expected answer for supervised evaluation.

    Required for supervised metrics, optional for unsupervised
    """


class TrainGolden(TypedDict, total=False):
    fields: Required[Dict[str, str]]
    """Dictionary mapping field names to their values.

    Keys must match the fields specified in the template
    """

    answer: Optional[str]
    """Expected answer for supervised evaluation.

    Required for supervised metrics, optional for unsupervised
    """
