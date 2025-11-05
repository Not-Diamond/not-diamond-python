# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ModelListResponse", "DeprecatedModel", "Model"]


class DeprecatedModel(BaseModel):
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


class Model(BaseModel):
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


class ModelListResponse(BaseModel):
    deprecated_models: List[DeprecatedModel]
    """List of deprecated models that are no longer recommended but may still work"""

    models: List[Model]
    """List of active/supported text generation models with their metadata"""

    total: int
    """Total count of active models in the response"""
