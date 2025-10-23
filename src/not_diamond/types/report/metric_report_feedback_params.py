# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MetricReportFeedbackParams", "Provider"]


class MetricReportFeedbackParams(TypedDict, total=False):
    feedback: Required[Dict[str, object]]

    provider: Required[Provider]

    session_id: Required[str]


class Provider(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    context_length: Optional[int]

    input_price: Optional[float]

    is_custom: bool

    latency: Optional[float]

    output_price: Optional[float]
