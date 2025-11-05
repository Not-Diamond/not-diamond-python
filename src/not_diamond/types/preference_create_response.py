# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PreferenceCreateResponse"]


class PreferenceCreateResponse(BaseModel):
    preference_id: str
    """Unique identifier for the newly created preference.

    Use this in the 'preference_id' parameter of model_select() calls to enable
    personalized routing
    """
