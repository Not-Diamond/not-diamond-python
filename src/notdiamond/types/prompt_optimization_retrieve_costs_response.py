# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["PromptOptimizationRetrieveCostsResponse", "UsageRecord"]


class UsageRecord(BaseModel):
    """Individual LLM usage record with token counts and cost breakdown.

    Returned by GET /llm-usage endpoint and included in AdaptationRunCostResponse.
    Each record represents a single LLM API call with detailed usage metrics.
    """

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
    """
    Type of task: 'pre-optimization evaluation', 'optimization', or
    'post-optimization evaluation'
    """

    timestamp: float
    """Unix timestamp when the request was made"""

    total_cost: float
    """Total cost (input + output) in USD"""

    user_id: str
    """User ID who made the request"""


class PromptOptimizationRetrieveCostsResponse(BaseModel):
    """Response model for GET /v2/prompt/optimize/{optimization_run_id}/costs endpoint.

    Contains the total LLM costs and detailed usage records for a prompt adaptation run.
    Use this to track costs associated with optimizing prompts for different target models.
    """

    optimization_run_id: str
    """Unique identifier for the adaptation run"""

    total_cost: float
    """Total cost in USD across all LLM requests in this adaptation run"""

    usage_records: List[UsageRecord]
    """Detailed usage records for each LLM request made during the adaptation"""
