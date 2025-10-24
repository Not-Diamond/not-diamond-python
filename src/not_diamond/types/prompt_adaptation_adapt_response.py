# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PromptAdaptationAdaptResponse"]


class PromptAdaptationAdaptResponse(BaseModel):
    adaptation_run_id: str
    """Unique ID for this adaptation run.

    Use this to check status and retrieve results
    """
