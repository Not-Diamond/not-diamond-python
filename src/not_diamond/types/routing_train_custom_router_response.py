# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RoutingTrainCustomRouterResponse"]


class RoutingTrainCustomRouterResponse(BaseModel):
    preference_id: str
    """Unique identifier for the custom router.

    Use this in model_select() calls to enable routing with your custom-trained
    router
    """
