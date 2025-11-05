# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["PznSubmitSurveyResponseParams"]


class PznSubmitSurveyResponseParams(TypedDict, total=False):
    constraint_priorities: Required[str]
    """JSON string of constraint priorities object"""

    email: Required[str]
    """User email address"""

    llm_providers: Required[str]
    """JSON string of LLM providers array"""

    use_case_desc: Required[str]
    """Description of the user's use case"""

    user_id: Required[str]
    """User ID from Supabase"""

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]

    additional_preferences: Optional[str]
    """Optional additional preferences text"""

    dataset_file: Optional[FileTypes]
    """Optional CSV file with evaluation dataset"""

    name: Optional[str]
    """Optional preference name"""

    prompt_file: Optional[FileTypes]
    """Optional CSV file with prompts"""

    prompts: Optional[str]
    """Optional JSON string of prompts array"""
