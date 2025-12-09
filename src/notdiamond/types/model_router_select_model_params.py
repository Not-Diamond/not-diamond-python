# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .request_provider_param import RequestProviderParam

__all__ = ["ModelRouterSelectModelParams", "LlmProvider", "LlmProviderOpenRouterProvider"]


class ModelRouterSelectModelParams(TypedDict, total=False):
    llm_providers: Required[Iterable[LlmProvider]]
    """List of LLM providers to route between.

    Specify at least one provider in format {provider, model}
    """

    messages: Required[Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str]]
    """Array of message objects in OpenAI format (with 'role' and 'content' keys)"""

    type: Optional[str]
    """Optional format type.

    Use 'openrouter' to accept and return OpenRouter-format model identifiers
    """

    hash_content: bool
    """Whether to hash message content for privacy"""

    max_model_depth: Optional[int]
    """Maximum number of models to consider for routing.

    If not specified, considers all provided models
    """

    metric: str
    """Optimization metric for model selection"""

    preference_id: Optional[str]
    """Preference ID for personalized routing.

    Create one via POST /v2/preferences/userPreferenceCreate
    """

    previous_session: Optional[str]
    """Previous session ID to link related requests"""

    tools: Optional[Iterable[Dict[str, object]]]
    """OpenAI-format function calling tools"""

    tradeoff: Optional[str]
    """Optimization tradeoff strategy.

    Use 'cost' to prioritize cost savings or 'latency' to prioritize speed
    """


class LlmProviderOpenRouterProvider(TypedDict, total=False):
    """Model for specifying an LLM provider using OpenRouter format.

    Used in model routing requests when you want to specify providers using the
    OpenRouter naming convention (combined 'provider/model' format). This is an
    alternative to the standard RequestProvider which uses separate provider and
    model fields.

    **When to use:**
    - When working with OpenRouter-compatible systems
    - When you prefer the unified 'provider/model' format
    - For models accessed via OpenRouter proxy
    """

    model: Required[str]
    """
    OpenRouter model identifier in 'provider/model' format (e.g., 'openai/gpt-4o',
    'anthropic/claude-sonnet-4-5-20250929')
    """

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


LlmProvider: TypeAlias = Union[RequestProviderParam, LlmProviderOpenRouterProvider]
