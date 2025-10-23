# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ReportReportThumbsParams", "Provider"]


class ReportReportThumbsParams(TypedDict, total=False):
    provider: Required[Provider]

    session_id: Required[str]

    thumbs: Required[int]

    user_id: Optional[str]


class Provider(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]
