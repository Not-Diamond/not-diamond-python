# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PreferenceDeleteParams"]


class PreferenceDeleteParams(TypedDict, total=False):
    preference_id: Required[str]

    user_id: Required[str]

    x_token: Required[Annotated[str, PropertyInfo(alias="x-token")]]
