# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LlmUsageRetrieveMonthlyParams"]


class LlmUsageRetrieveMonthlyParams(TypedDict, total=False):
    months: int
    """Number of months to retrieve (max 12)"""
