# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AdaptCreateResponse"]


class AdaptCreateResponse(BaseModel):
    adaptation_run_id: str
    """Unique identifier for this adaptation run.

    Use this to poll status and retrieve optimized prompts when complete
    """
