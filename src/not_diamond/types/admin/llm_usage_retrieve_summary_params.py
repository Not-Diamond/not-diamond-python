# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LlmUsageRetrieveSummaryParams"]


class LlmUsageRetrieveSummaryParams(TypedDict, total=False):
    user_id: Required[str]
    """User ID to get usage for"""

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]

    end_time: Optional[float]
    """End timestamp (Unix time)"""

    start_time: Optional[float]
    """Start timestamp (Unix time)"""
