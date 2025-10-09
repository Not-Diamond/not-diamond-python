# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .open_router_provider_param import OpenRouterProviderParam
from .report.request_provider_param import RequestProviderParam

__all__ = ["ChatSelectModelParams", "LlmProvider"]


class ChatSelectModelParams(TypedDict, total=False):
    llm_providers: Required[Iterable[LlmProvider]]

    messages: Required[Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str]]

    hash_content: bool

    max_model_depth: Optional[int]

    metric: str

    preference_id: Optional[str]

    previous_session: Optional[str]

    tools: Optional[Iterable[Dict[str, object]]]

    tradeoff: Optional[str]


LlmProvider: TypeAlias = Union[RequestProviderParam, OpenRouterProviderParam]
