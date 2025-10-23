# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PromptEstimateAdaptLlmRequestsResponse"]


class PromptEstimateAdaptLlmRequestsResponse(BaseModel):
    num_llm_requests_estimated: int
