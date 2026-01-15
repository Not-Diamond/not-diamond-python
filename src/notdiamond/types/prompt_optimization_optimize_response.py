# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PromptOptimizationOptimizeResponse"]


class PromptOptimizationOptimizeResponse(BaseModel):
    """Response model for POST /v2/prompt/optimize endpoint.

    Returned immediately after submitting a prompt optimization request. The optimization
    process runs asynchronously, so use the returned optimization_run_id to track progress
    and retrieve results when complete.

    **Next steps:**
    1. Store the optimization_run_id
    2. Poll GET /v2/prompt/optimizeStatus/{optimization_run_id} to check progress
    3. When status is 'completed', retrieve optimized prompts from GET /v2/prompt/optimizeResults/{optimization_run_id}
    4. Use the optimized prompts with your target models
    """

    optimization_run_id: str
    """Unique identifier for this optimization run.

    Use this to poll status and retrieve optimized prompts when complete
    """
