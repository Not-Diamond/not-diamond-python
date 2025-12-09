# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Model"]


class Model(BaseModel):
    """Response model for a single LLM model from GET /v2/models endpoint.

    Contains metadata about a supported text generation model including pricing,
    context limits, and availability information.
    """

    context_length: int
    """Maximum context window size in tokens"""

    input_price: float
    """Price per million input tokens in USD"""

    model: str
    """Model identifier (e.g., 'gpt-4', 'claude-3-opus-20240229')"""

    output_price: float
    """Price per million output tokens in USD"""

    provider: str
    """Provider name (e.g., 'openai', 'anthropic', 'google')"""

    openrouter_model: Optional[str] = None
    """OpenRouter model identifier if available, null if not supported via OpenRouter"""
