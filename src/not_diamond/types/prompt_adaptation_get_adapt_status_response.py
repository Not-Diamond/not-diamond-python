# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .job_status import JobStatus

__all__ = ["PromptAdaptationGetAdaptStatusResponse"]


class PromptAdaptationGetAdaptStatusResponse(BaseModel):
    adaptation_run_id: str
    """Unique ID for this adaptation run.

    Use this to check status and retrieve results
    """

    status: JobStatus
    """
    Current status of the adaptation run (created, queued, processing, completed, or
    failed)
    """

    queue_position: Optional[int] = None
    """Position in queue if status is 'queued'. Lower numbers mean earlier processing"""
