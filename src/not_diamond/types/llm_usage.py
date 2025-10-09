# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["LlmUsage"]


class LlmUsage(BaseModel):
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
