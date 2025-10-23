# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["RouterTrainCustomRouterParams"]


class RouterTrainCustomRouterParams(TypedDict, total=False):
    dataset_file: Required[FileTypes]

    language: Required[str]

    llm_providers: Required[str]

    maximize: Required[bool]

    prompt_column: Required[str]

    override: Optional[bool]

    preference_id: Optional[str]
