# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from ..prompt.request_provider_param import RequestProviderParam

__all__ = ["MetricSubmitFeedbackParams"]


class MetricSubmitFeedbackParams(TypedDict, total=False):
    feedback: Required[Dict[str, object]]
    """Feedback dictionary with 'accuracy' key (0 for thumbs down, 1 for thumbs up)"""

    provider: Required[RequestProviderParam]
    """The provider that was selected by the router"""

    session_id: Required[str]
    """Session ID returned from POST /v2/modelRouter/modelSelect"""
