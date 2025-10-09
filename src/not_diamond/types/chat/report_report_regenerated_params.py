# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..report.request_provider_param import RequestProviderParam

__all__ = ["ReportReportRegeneratedParams"]


class ReportReportRegeneratedParams(TypedDict, total=False):
    provider: Required[RequestProviderParam]

    regenerated: Required[bool]

    session_id: Required[str]

    user_id: Optional[str]
