# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    openrouter_only: bool
    """Return only OpenRouter-supported models"""

    provider: Optional[SequenceNotStr[str]]
    """Filter by provider name(s).

    Can specify multiple providers (e.g., 'openai', 'anthropic')
    """
