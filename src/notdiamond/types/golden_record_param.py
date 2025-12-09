# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["GoldenRecordParam"]


class GoldenRecordParam(TypedDict, total=False):
    """A training or test example for prompt adaptation."""

    fields: Required[Dict[str, str]]
    """Dictionary mapping field names to their values.

    Keys must match the fields specified in the template
    """

    answer: Optional[str]
    """Expected answer for supervised evaluation.

    Required for supervised metrics, optional for unsupervised
    """
