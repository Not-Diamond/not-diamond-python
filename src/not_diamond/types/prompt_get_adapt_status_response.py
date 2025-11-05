# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .job_status import JobStatus

__all__ = ["PromptGetAdaptStatusResponse"]


class PromptGetAdaptStatusResponse(BaseModel):
    adaptation_run_id: str
    """Unique identifier for this adaptation run.

    Use this to poll status and retrieve optimized prompts when complete
    """

    status: JobStatus
    """Current status of the adaptation run.

    Poll until this is 'completed' or 'failed'
    """

    queue_position: Optional[int] = None
    """Position in queue when status is 'queued'.

    Lower numbers process sooner. Null when not queued
    """
