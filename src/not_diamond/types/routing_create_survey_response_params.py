# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["RoutingCreateSurveyResponseParams"]


class RoutingCreateSurveyResponseParams(TypedDict, total=False):
    constraint_priorities: Required[str]

    email: Required[str]

    llm_providers: Required[str]

    use_case_desc: Required[str]

    user_id: Required[str]

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]

    additional_preferences: Optional[str]

    dataset_file: Optional[FileTypes]

    name: Optional[str]

    prompt_file: Optional[FileTypes]

    prompts: Optional[str]
