# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["AdaptGetCostsResponse", "UsageRecord"]


class UsageRecord(BaseModel):
    id: str
    """Unique identifier for this usage record"""

    adaptation_run_id: str
    """Adaptation run ID this usage is associated with"""

    input_cost: float
    """Cost of input tokens in USD"""

    input_tokens: int
    """Number of input tokens consumed"""

    model: str
    """Model name (e.g., 'gpt-4', 'claude-3-opus-20240229')"""

    organization_id: str
    """Organization ID associated with the request"""

    output_cost: float
    """Cost of output tokens in USD"""

    output_tokens: int
    """Number of output tokens generated"""

    provider: str
    """LLM provider (e.g., 'openai', 'anthropic', 'google')"""

    task_type: str
    """Type of task (e.g., 'optimization', 'evaluation')"""

    timestamp: float
    """Unix timestamp when the request was made"""

    total_cost: float
    """Total cost (input + output) in USD"""

    user_id: str
    """User ID who made the request"""


class AdaptGetCostsResponse(BaseModel):
    adaptation_run_id: str
    """Unique identifier for the adaptation run"""

    total_cost: float
    """Total cost in USD across all LLM requests in this adaptation run"""

    usage_records: List[UsageRecord]
    """Detailed usage records for each LLM request made during the adaptation"""
