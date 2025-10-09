# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .job_status import JobStatus

__all__ = ["PromptGetAdaptStatusResponse"]


class PromptGetAdaptStatusResponse(BaseModel):
    adaptation_run_id: str

    status: JobStatus
