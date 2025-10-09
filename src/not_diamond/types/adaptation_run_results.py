# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .job_status import JobStatus

__all__ = ["AdaptationRunResults", "OriginModel", "TargetModel"]


class OriginModel(BaseModel):
    cost: Optional[float] = None

    evals: Optional[Dict[str, object]] = None

    api_model_name: str = FieldInfo(alias="model_name")

    result_status: Optional[JobStatus] = None

    score: Optional[float] = None

    system_prompt: Optional[str] = None

    user_message_template: Optional[str] = None


class TargetModel(BaseModel):
    cost: Optional[float] = None

    api_model_name: str = FieldInfo(alias="model_name")

    post_optimization_evals: Optional[Dict[str, object]] = None

    post_optimization_score: Optional[float] = None

    pre_optimization_evals: Optional[Dict[str, object]] = None

    pre_optimization_score: Optional[float] = None

    result_status: Optional[JobStatus] = None

    system_prompt: Optional[str] = None

    user_message_template: Optional[str] = None

    user_message_template_fields: Optional[List[str]] = None


class AdaptationRunResults(BaseModel):
    id: str

    created_at: datetime

    job_status: JobStatus

    origin_model: OriginModel

    target_models: List[TargetModel]

    updated_at: Optional[datetime] = None

    evaluation_config: Optional[str] = None

    evaluation_metric: Optional[str] = None
