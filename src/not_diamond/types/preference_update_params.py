# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PreferenceUpdateParams"]


class PreferenceUpdateParams(TypedDict, total=False):
    preference_id: Required[str]

    user_id: Required[str]

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]

    name: Optional[str]

    preference_weights: Optional[Dict[str, object]]

    samples: Iterable[Dict[str, object]]
