# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LlmUsageRetrieveDailyParams"]


class LlmUsageRetrieveDailyParams(TypedDict, total=False):
    end_date: Required[str]
    """End date in YYYY-MM-DD format"""

    start_date: Required[str]
    """Start date in YYYY-MM-DD format"""

    metric: str
    """Metric to aggregate: 'cost' or 'calls'"""
