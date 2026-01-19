# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .job_status import JobStatus

__all__ = ["PromptOptimizationGetOptimizationResultsResponse", "TargetModel", "OriginModel"]


class TargetModel(BaseModel):
    """Optimized prompt results for a single target model in prompt adaptation.

    Part of AdaptationRunResultsResponse. Contains the optimized system prompt and
    user message template for a specific target model, along with performance scores
    before and after optimization. Use these optimized prompts with the target model
    to achieve better performance than the original prompt.

    **Key metrics:**
    - **pre_optimization_score**: Performance with original prompt on this target model
    - **post_optimization_score**: Performance with optimized prompt on this target model
    - **Score improvement**: post - pre shows how much optimization helped

    **Usage:**
    1. Extract the optimized system_prompt and user_message_template
    2. Replace placeholders in user_message_template using fields from your data
    3. Use these prompts when calling this target model
    4. Compare pre/post scores to see improvement gained
    """

    cost: Optional[float] = None

    api_model_name: str = FieldInfo(alias="model_name")

    post_optimization_evals: Optional[Dict[str, object]] = None

    post_optimization_score: Optional[float] = None

    pre_optimization_evals: Optional[Dict[str, object]] = None

    pre_optimization_score: Optional[float] = None

    task_type: Optional[str] = None

    result_status: Optional[JobStatus] = None
    """
    Status enum for asynchronous jobs (prompt adaptation, custom router training,
    etc.).

    Represents the current state of a long-running operation:

    - **created**: Job has been initialized but not yet queued
    - **queued**: Job is waiting in the queue to be processed
    - **processing**: Job is currently being executed
    - **completed**: Job finished successfully and results are available
    - **failed**: Job encountered an error and did not complete
    - **cancelled**: Job was cancelled due to a restart operation
    """

    system_prompt: Optional[str] = None
    """Optimized system prompt for this target model.

    Use this as the system message in your LLM calls
    """

    user_message_template: Optional[str] = None
    """Optimized user message template with placeholders.

    Substitute fields using your data before calling the LLM
    """

    user_message_template_fields: Optional[List[str]] = None
    """
    List of field names to substitute in the template (e.g., ['question',
    'context']). These match the curly-brace placeholders in user_message_template
    """


class OriginModel(BaseModel):
    """Baseline results for the origin model in prompt adaptation.

    Part of AdaptationRunResultsResponse. Contains the performance metrics and prompt
    configuration for your original prompt on the origin model. This serves as the
    baseline to compare against optimized prompts for target models.

    **Fields include:**
    - Original system prompt and user message template
    - Baseline performance score and evaluation metrics
    - Cost of running the baseline evaluation
    - Job status for the origin model evaluation
    """

    cost: Optional[float] = None

    evals: Optional[Dict[str, object]] = None

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)

    score: Optional[float] = None

    result_status: Optional[JobStatus] = None
    """
    Status enum for asynchronous jobs (prompt adaptation, custom router training,
    etc.).

    Represents the current state of a long-running operation:

    - **created**: Job has been initialized but not yet queued
    - **queued**: Job is waiting in the queue to be processed
    - **processing**: Job is currently being executed
    - **completed**: Job finished successfully and results are available
    - **failed**: Job encountered an error and did not complete
    - **cancelled**: Job was cancelled due to a restart operation
    """

    system_prompt: Optional[str] = None
    """Original system prompt used for the origin model"""

    user_message_template: Optional[str] = None
    """Original user message template used for the origin model"""


class PromptOptimizationGetOptimizationResultsResponse(BaseModel):
    """
    Response model for GET /v2/prompt/optimizeResults/{optimization_run_id} endpoint.

    Contains the complete results of a prompt adaptation run, including optimized prompts
    and evaluation metrics for all target models. Use this to retrieve your adapted prompts
    after the adaptation status is 'completed'.

    The response includes:
    - Baseline performance of your original prompt on the origin model
    - Optimized prompts for each target model with pre/post optimization scores
    - Evaluation metrics and cost information for each model
    """

    id: str
    """Unique ID for this adaptation run"""

    created_at: datetime
    """Timestamp when this adaptation run was created"""

    job_status: JobStatus
    """Overall status of the adaptation run (queued, running, completed, failed)"""

    target_models: List[TargetModel]
    """Results for each target model with optimized prompts and improvement scores"""

    updated_at: Optional[datetime] = None
    """Timestamp of last update to this adaptation run"""

    evaluation_config: Optional[str] = None

    evaluation_metric: Optional[str] = None

    llm_request_metrics: Optional[List[Dict[str, object]]] = None
    """Metrics for the LLM requests made during the adaptation run.

    List of {model: str, num_requests: int}.
    """

    origin_model: Optional[OriginModel] = None
    """Baseline results for the origin model in prompt adaptation.

    Part of AdaptationRunResultsResponse. Contains the performance metrics and
    prompt configuration for your original prompt on the origin model. This serves
    as the baseline to compare against optimized prompts for target models.

    **Fields include:**

    - Original system prompt and user message template
    - Baseline performance score and evaluation metrics
    - Cost of running the baseline evaluation
    - Job status for the origin model evaluation
    """

    prototype_mode: Optional[bool] = None
    """
    Whether this adaptation run was created with prototype mode (3-24 training
    examples allowed). Prototype mode may have degraded performance compared to
    standard mode (25+ examples)
    """
