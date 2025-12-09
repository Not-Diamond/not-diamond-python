# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PromptAdaptationAdaptResponse"]


class PromptAdaptationAdaptResponse(BaseModel):
    """Response model for POST /v2/prompt/adapt endpoint.

    Returned immediately after submitting a prompt adaptation request. The adaptation
    process runs asynchronously, so use the returned adaptation_run_id to track progress
    and retrieve results when complete.

    **Next steps:**
    1. Store the adaptation_run_id
    2. Poll GET /v2/prompt/adaptStatus/{adaptation_run_id} to check progress
    3. When status is 'completed', retrieve optimized prompts from GET /v2/prompt/adaptResults/{adaptation_run_id}
    4. Use the optimized prompts with your target models
    """

    adaptation_run_id: str
    """Unique identifier for this adaptation run.

    Use this to poll status and retrieve optimized prompts when complete
    """
