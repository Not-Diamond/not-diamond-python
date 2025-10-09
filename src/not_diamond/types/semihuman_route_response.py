# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SemihumanRouteResponse"]


class SemihumanRouteResponse(BaseModel):
    model: str

    provider: str

    context_length: Optional[int] = None

    input_price: Optional[float] = None

    is_custom: Optional[bool] = None

    is_image_gen: Optional[bool] = None

    latency: Optional[float] = None

    names: Optional[List[object]] = None

    openrouter_model: Optional[str] = None

    output_price: Optional[float] = None

    preference_id: Optional[str] = None

    timestamp: Optional[float] = None
