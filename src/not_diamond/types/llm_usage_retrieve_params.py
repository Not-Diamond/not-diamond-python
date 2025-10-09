# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LlmUsageRetrieveParams"]


class LlmUsageRetrieveParams(TypedDict, total=False):
    end_time: Optional[float]
    """End timestamp (Unix time)"""

    limit: int
    """Maximum number of records to return"""

    start_time: Optional[float]
    """Start timestamp (Unix time)"""
