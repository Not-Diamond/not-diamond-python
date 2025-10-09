# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..report.request_provider_param import RequestProviderParam

__all__ = ["ArenaCreateChoiceParams"]


class ArenaCreateChoiceParams(TypedDict, total=False):
    preferred_provider: Required[RequestProviderParam]

    rejected_provider: Required[RequestProviderParam]

    session_id: Required[str]

    user_id: Optional[str]
