# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .request_provider_param import RequestProviderParam

__all__ = ["MetricReportLatencyParams"]


class MetricReportLatencyParams(TypedDict, total=False):
    feedback: Required[Dict[str, object]]

    provider: Required[RequestProviderParam]

    session_id: Required[str]
