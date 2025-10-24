# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .adaptation_run_results import AdaptationRunResults

__all__ = ["PromptAdaptationGetAdaptRunsResponse"]

PromptAdaptationGetAdaptRunsResponse: TypeAlias = List[AdaptationRunResults]
