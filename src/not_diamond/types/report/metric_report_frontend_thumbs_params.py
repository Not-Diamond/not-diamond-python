# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .request_provider_param import RequestProviderParam

__all__ = ["MetricReportFrontendThumbsParams"]


class MetricReportFrontendThumbsParams(TypedDict, total=False):
    provider: Required[RequestProviderParam]

    session_id: Required[str]

    thumbs: Required[int]

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]

    user_id: Optional[str]
