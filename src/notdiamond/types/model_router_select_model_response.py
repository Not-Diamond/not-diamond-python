# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ModelRouterSelectModelResponse", "Provider"]


class Provider(BaseModel):
    """Selected LLM provider information from model selection endpoints.

    Part of ModelSelectResponse. Contains the provider and model that Not Diamond's
    routing algorithm selected as optimal for your query. Use these values to make
    your LLM API call to the recommended model.
    """

    model: str
    """
    Model identifier for the selected model (e.g., 'gpt-4o',
    'claude-3-opus-20240229')
    """

    provider: str
    """Provider name for the selected model (e.g., 'openai', 'anthropic', 'google')"""


class ModelRouterSelectModelResponse(BaseModel):
    """Response from model selection endpoint."""

    providers: List[Provider]
    """List containing the selected provider"""

    session_id: str
    """Unique session ID for this routing decision"""
