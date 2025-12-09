# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomRouterTrainCustomRouterResponse"]


class CustomRouterTrainCustomRouterResponse(BaseModel):
    """Response model for POST /v2/pzn/trainCustomRouter endpoint.

    Returned immediately after submitting a custom router training request. The training
    process runs asynchronously (typically 5-15 minutes), so use the returned preference_id
    to make routing calls once training completes.

    **Next steps:**
    1. Store the preference_id
    2. Wait for training to complete (typically 5-15 minutes)
    3. Use this preference_id in POST /v2/modelRouter/modelSelect requests
    4. The router will use your custom-trained model to make routing decisions

    **How to use the preference_id:**
    - Include it in the 'preference_id' field of model_select() calls
    - The system automatically uses your custom router once training is complete
    - No need to poll status - you can start using it immediately (will use default until ready)
    """

    preference_id: str
    """Unique identifier for the custom router.

    Use this in model_select() calls to enable routing with your custom-trained
    router
    """
