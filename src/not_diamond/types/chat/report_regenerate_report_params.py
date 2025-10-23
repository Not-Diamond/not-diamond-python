# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReportRegenerateReportParams", "Provider"]


class ReportRegenerateReportParams(TypedDict, total=False):
    provider: Required[Provider]

    regenerated: Required[bool]

    session_id: Required[str]

    user_id: Optional[str]


class Provider(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]
