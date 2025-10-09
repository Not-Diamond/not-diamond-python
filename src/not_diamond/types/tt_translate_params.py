# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from .report.request_provider_param import RequestProviderParam

__all__ = ["TtTranslateParams"]


class TtTranslateParams(TypedDict, total=False):
    llm_providers: Required[Iterable[RequestProviderParam]]

    messages: Required[Iterable[Dict[str, str]]]

    source_language: Required[str]

    target_language: Required[str]
