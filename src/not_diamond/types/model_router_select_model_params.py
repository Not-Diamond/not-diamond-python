# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ModelRouterSelectModelParams"]


class ModelRouterSelectModelParams(TypedDict, total=False):
    body: Required[object]

    type: Optional[str]
    """Optional format type.

    Use 'openrouter' to accept and return OpenRouter-format model identifiers
    """
