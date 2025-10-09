# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .job_status import JobStatus

__all__ = ["PromptGetAdaptStatusResponse"]


class PromptGetAdaptStatusResponse(BaseModel):
    adaptation_run_id: str

    status: JobStatus

    queue_position: Optional[int] = None
