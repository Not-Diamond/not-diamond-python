# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["PromptAdaptationRetrieveCostsResponse", "UsageRecord"]


class UsageRecord(BaseModel):
    id: str

    adaptation_run_id: str

    input_cost: float

    input_tokens: int

    model: str

    organization_id: str

    output_cost: float

    output_tokens: int

    provider: str

    task_type: str

    timestamp: float

    total_cost: float

    user_id: str


class PromptAdaptationRetrieveCostsResponse(BaseModel):
    adaptation_run_id: str

    total_cost: float

    usage_records: List[UsageRecord]
