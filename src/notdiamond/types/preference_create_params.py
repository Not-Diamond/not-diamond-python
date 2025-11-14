# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PreferenceCreateParams"]


class PreferenceCreateParams(TypedDict, total=False):
    name: Optional[str]
    """Optional name for the preference.

    If not provided, an auto-generated timestamp will be used. Use descriptive names
    like 'Production API' or 'Customer Support Bot' for easy identification
    """
