# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PreferenceCreateUserPreferenceResponse"]


class PreferenceCreateUserPreferenceResponse(BaseModel):
    preference_id: str
    """The newly created preference ID.

    Use this in model_select() calls for personalized routing
    """
