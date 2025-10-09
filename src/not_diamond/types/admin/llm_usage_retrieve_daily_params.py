# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LlmUsageRetrieveDailyParams"]


class LlmUsageRetrieveDailyParams(TypedDict, total=False):
    end_date: Required[str]
    """End date in YYYY-MM-DD format"""

    start_date: Required[str]
    """Start date in YYYY-MM-DD format"""

    user_id: Required[str]
    """User ID to get usage for"""

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]

    metric: str
    """Metric to aggregate: 'cost' or 'calls'"""

    subscription_date: Optional[str]
    """Subscription date (ISO format) to filter out pre-subscription usage"""
