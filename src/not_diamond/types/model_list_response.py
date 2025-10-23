# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ModelListResponse", "DeprecatedModel", "Model"]


class DeprecatedModel(BaseModel):
    context_length: int

    input_price: float

    model: str

    output_price: float

    provider: str

    openrouter_model: Optional[str] = None


class Model(BaseModel):
    context_length: int

    input_price: float

    model: str

    output_price: float

    provider: str

    openrouter_model: Optional[str] = None


class ModelListResponse(BaseModel):
    deprecated_models: List[DeprecatedModel]

    models: List[Model]

    total: int
