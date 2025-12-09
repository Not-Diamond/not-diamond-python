# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PreferenceCreateResponse"]


class PreferenceCreateResponse(BaseModel):
    """Response model for POST /v2/preferences/userPreferenceCreate endpoint.

    Returns the newly created preference ID which can be used to enable personalized
    LLM routing. Store this ID and include it in subsequent model_select() calls to
    activate personalized routing based on your feedback and usage patterns.

    **Next steps after creation:**
    1. Use the preference_id in POST /v2/modelRouter/modelSelect requests
    2. Submit feedback on routing decisions to improve accuracy
    3. Optionally train a custom router using your evaluation data
    """

    preference_id: str
    """Unique identifier for the newly created preference.

    Use this in the 'preference_id' parameter of model_select() calls to enable
    personalized routing
    """
