# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PreferenceCreateParams"]


class PreferenceCreateParams(TypedDict, total=False):
    user_id: Required[str]

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]

    name: Optional[str]

    samples: Iterable[Dict[str, object]]
