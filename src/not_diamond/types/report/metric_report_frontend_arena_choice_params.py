# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MetricReportFrontendArenaChoiceParams", "PreferredProvider", "RejectedProvider"]


class MetricReportFrontendArenaChoiceParams(TypedDict, total=False):
    preferred_provider: Required[PreferredProvider]

    rejected_provider: Required[RejectedProvider]

    session_id: Required[str]

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]

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
