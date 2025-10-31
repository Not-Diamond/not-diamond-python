# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .job_status import JobStatus

__all__ = ["AdaptationRunResults", "TargetModel", "OriginModel"]


class TargetModel(BaseModel):
    cost: Optional[float] = None

    api_model_name: str = FieldInfo(alias="model_name")

    post_optimization_evals: Optional[Dict[str, object]] = None

    post_optimization_score: Optional[float] = None

    pre_optimization_evals: Optional[Dict[str, object]] = None

    pre_optimization_score: Optional[float] = None

    result_status: Optional[JobStatus] = None
    """Status of this specific target model adaptation"""

    system_prompt: Optional[str] = None
    """Optimized system prompt for this target model"""

    task_type: Optional[str] = None

    user_message_template: Optional[str] = None
    """Optimized user message template for this target model"""

    user_message_template_fields: Optional[List[str]] = None
    """Field names used in the optimized template"""


class OriginModel(BaseModel):
    cost: Optional[float] = None

    evals: Optional[Dict[str, object]] = None

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)

    result_status: Optional[JobStatus] = None

    score: Optional[float] = None

    system_prompt: Optional[str] = None

    user_message_template: Optional[str] = None


class AdaptationRunResults(BaseModel):
    id: str
    """Unique ID for this adaptation run"""

    created_at: datetime
    """Timestamp when this adaptation run was created"""

    job_status: JobStatus
    """Overall status of the adaptation run"""

    target_models: List[TargetModel]
    """Results for each target model with optimized prompts"""

    updated_at: Optional[datetime] = None
    """Timestamp of last update to this adaptation run"""

    evaluation_config: Optional[str] = None

    evaluation_metric: Optional[str] = None

    llm_request_metrics: Optional[Dict[str, float]] = None
    """Metrics for the LLM requests made during the adaptation run"""

    origin_model: Optional[OriginModel] = None
    """Results for the origin model (baseline performance)"""
