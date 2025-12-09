# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RequestProviderParam"]


class RequestProviderParam(TypedDict, total=False):
    """Model for specifying an LLM provider in API requests."""

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
