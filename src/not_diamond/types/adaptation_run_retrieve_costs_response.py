# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .llm_usage import LlmUsage

__all__ = ["AdaptationRunRetrieveCostsResponse"]


class AdaptationRunRetrieveCostsResponse(BaseModel):
    adaptation_run_id: str

    total_cost: float

    usage_records: List[LlmUsage]
