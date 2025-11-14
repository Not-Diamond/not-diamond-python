# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["MetricSubmitFeedbackResponse"]


class MetricSubmitFeedbackResponse(BaseModel):
    feedback: Dict[str, object]
    """The processed feedback"""

    session_id: str
    """The session ID for which feedback was submitted"""
