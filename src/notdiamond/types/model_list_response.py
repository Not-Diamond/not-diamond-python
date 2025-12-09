# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .model import Model
from .._models import BaseModel

__all__ = ["ModelListResponse"]


class ModelListResponse(BaseModel):
    """Response model for GET /v2/models endpoint.

    Returns a list of all supported text generation models with their metadata,
    separated into active and deprecated models.
    """

    deprecated_models: List[Model]
    """List of deprecated models that are no longer recommended but may still work"""

    models: List[Model]
    """List of active/supported text generation models with their metadata"""

    total: int
    """Total count of active models in the response"""
