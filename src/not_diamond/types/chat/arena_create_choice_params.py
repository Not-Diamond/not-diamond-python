# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ArenaCreateChoiceParams", "PreferredProvider", "RejectedProvider"]


class ArenaCreateChoiceParams(TypedDict, total=False):
    preferred_provider: Required[PreferredProvider]

    rejected_provider: Required[RejectedProvider]

    session_id: Required[str]

    user_id: Optional[str]


class PreferredProvider(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]


class RejectedProvider(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]
