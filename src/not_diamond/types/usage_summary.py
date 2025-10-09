# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["UsageSummary"]


class UsageSummary(BaseModel):
    by_model: Dict[str, object]

    by_provider: Dict[str, object]

    total_calls: int

    total_cost: float

    total_input_tokens: int

    total_output_tokens: int
