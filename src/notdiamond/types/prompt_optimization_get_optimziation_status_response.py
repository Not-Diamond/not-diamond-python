# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .job_status import JobStatus

__all__ = ["PromptOptimizationGetOptimziationStatusResponse"]


class PromptOptimizationGetOptimziationStatusResponse(BaseModel):
    """Response model for GET /v2/prompt/optimizeStatus/{optimization_run_id} endpoint.

    Returns the current status of an asynchronous prompt optimization job. Poll this
    endpoint periodically to track progress. When status is 'completed', you can
    retrieve the optimized prompts using the /optimizeResults endpoint.

    **Status values:**
    - **created**: Job has been initialized
    - **queued**: Waiting in queue (check queue_position for your place in line)
    - **processing**: Currently running optimization
    - **completed**: Finished successfully, results available via /optimizeResults
    - **failed**: Encountered an error during processing

    **Polling recommendations:**
    - Poll every 30-60 seconds while status is incomplete
    - Stop polling once status is 'completed' or 'failed'
    - Optimization typically takes 10-30 minutes total
    """

    optimization_run_id: str
    """Unique identifier for this optimization run.

    Use this to poll status and retrieve optimized prompts when complete
    """

    status: JobStatus
    """Current status of the optimization run.

    Poll until this is 'completed' or 'failed'
    """

    queue_position: Optional[int] = None
    """Position in queue when status is 'queued'.

    Lower numbers process sooner. Null when not queued
    """
