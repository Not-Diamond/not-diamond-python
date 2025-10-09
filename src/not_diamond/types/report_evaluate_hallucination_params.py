# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .report.request_provider_param import RequestProviderParam

__all__ = ["ReportEvaluateHallucinationParams"]


class ReportEvaluateHallucinationParams(TypedDict, total=False):
    context: Required[str]

    prompt: Required[str]

    provider: Required[RequestProviderParam]

    response: Required[str]

    cost: Optional[float]

    latency: Optional[float]
