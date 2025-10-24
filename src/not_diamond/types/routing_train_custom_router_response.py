# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RoutingTrainCustomRouterResponse"]


class RoutingTrainCustomRouterResponse(BaseModel):
    preference_id: str
    """The preference ID for the custom router.

    Training happens asynchronously - use this ID to check status and make routing
    calls once training is complete
    """
