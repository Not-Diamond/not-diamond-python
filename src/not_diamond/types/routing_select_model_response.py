# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RoutingSelectModelResponse", "Provider"]


class Provider(BaseModel):
    model: str
    """Model name"""

    provider: str
    """Provider name"""


class RoutingSelectModelResponse(BaseModel):
    providers: List[Provider]
    """List containing the selected provider"""

    session_id: str
    """Unique session ID for this routing decision"""
