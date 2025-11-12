# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["CustomRouterTrainCustomRouterParams"]


class CustomRouterTrainCustomRouterParams(TypedDict, total=False):
    dataset_file: Required[FileTypes]
    """
    CSV file containing evaluation data with prompt column and score/response
    columns for each model
    """

    language: Required[str]
    """Language of the evaluation data.

    Use 'english' for English-only data or 'multilingual' for multi-language support
    """

    llm_providers: Required[str]
    """JSON string array of LLM providers to train the router on.

    Format: '[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic",
    "model": "claude-sonnet-4-5-20250929"}]'
    """

    maximize: Required[bool]
    """Whether higher scores are better.

    Set to true if higher scores indicate better performance, false otherwise
    """

    prompt_column: Required[str]
    """Name of the column in the CSV file that contains the prompts"""

    override: Optional[bool]
    """Whether to override an existing custom router for this preference_id"""

    preference_id: Optional[str]
    """Optional preference ID to update an existing router.

    If not provided, a new preference will be created
    """
