# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PreferenceCreateUserPreferenceParams"]


class PreferenceCreateUserPreferenceParams(TypedDict, total=False):
    name: Optional[str]
    """Optional name for the preference"""
