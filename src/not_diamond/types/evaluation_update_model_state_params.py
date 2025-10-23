# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvaluationUpdateModelStateParams"]


class EvaluationUpdateModelStateParams(TypedDict, total=False):
    body: Required[Dict[str, object]]

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]
