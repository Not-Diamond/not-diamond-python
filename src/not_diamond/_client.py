# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import (
    tt,
    pzn,
    health,
    prompt,
    api_keys,
    llm_usage,
    semihuman,
    error_debug,
    evaluations,
    preferences,
    model_router,
    posthog_debug,
    adaptation_runs,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.chat import chat
from .resources.admin import admin
from .resources.proxy import proxy
from .resources.report import report
from .types.retrieve_root_response import RetrieveRootResponse

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "NotDiamond",
    "AsyncNotDiamond",
    "Client",
    "AsyncClient",
]


class NotDiamond(SyncAPIClient):
    model_router: model_router.ModelRouterResource
    evaluations: evaluations.EvaluationsResource
    report: report.ReportResource
    preferences: preferences.PreferencesResource
    proxy: proxy.ProxyResource
    prompt: prompt.PromptResource
    pzn: pzn.PznResource
    chat: chat.ChatResource
    tt: tt.TtResource
    semihuman: semihuman.SemihumanResource
    api_keys: api_keys.APIKeysResource
    llm_usage: llm_usage.LlmUsageResource
    adaptation_runs: adaptation_runs.AdaptationRunsResource
    admin: admin.AdminResource
    health: health.HealthResource
    error_debug: error_debug.ErrorDebugResource
    posthog_debug: posthog_debug.PosthogDebugResource
    with_raw_response: NotDiamondWithRawResponse
    with_streaming_response: NotDiamondWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous NotDiamond client instance.

        This automatically infers the `api_key` argument from the `NOT_DIAMOND_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("NOT_DIAMOND_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NOT_DIAMOND_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.model_router = model_router.ModelRouterResource(self)
        self.evaluations = evaluations.EvaluationsResource(self)
        self.report = report.ReportResource(self)
        self.preferences = preferences.PreferencesResource(self)
        self.proxy = proxy.ProxyResource(self)
        self.prompt = prompt.PromptResource(self)
        self.pzn = pzn.PznResource(self)
        self.chat = chat.ChatResource(self)
        self.tt = tt.TtResource(self)
        self.semihuman = semihuman.SemihumanResource(self)
        self.api_keys = api_keys.APIKeysResource(self)
        self.llm_usage = llm_usage.LlmUsageResource(self)
        self.adaptation_runs = adaptation_runs.AdaptationRunsResource(self)
        self.admin = admin.AdminResource(self)
        self.health = health.HealthResource(self)
        self.error_debug = error_debug.ErrorDebugResource(self)
        self.posthog_debug = posthog_debug.PosthogDebugResource(self)
        self.with_raw_response = NotDiamondWithRawResponse(self)
        self.with_streaming_response = NotDiamondWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def retrieve_root(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrieveRootResponse:
        """Returns welcome message."""
        return self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveRootResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncNotDiamond(AsyncAPIClient):
    model_router: model_router.AsyncModelRouterResource
    evaluations: evaluations.AsyncEvaluationsResource
    report: report.AsyncReportResource
    preferences: preferences.AsyncPreferencesResource
    proxy: proxy.AsyncProxyResource
    prompt: prompt.AsyncPromptResource
    pzn: pzn.AsyncPznResource
    chat: chat.AsyncChatResource
    tt: tt.AsyncTtResource
    semihuman: semihuman.AsyncSemihumanResource
    api_keys: api_keys.AsyncAPIKeysResource
    llm_usage: llm_usage.AsyncLlmUsageResource
    adaptation_runs: adaptation_runs.AsyncAdaptationRunsResource
    admin: admin.AsyncAdminResource
    health: health.AsyncHealthResource
    error_debug: error_debug.AsyncErrorDebugResource
    posthog_debug: posthog_debug.AsyncPosthogDebugResource
    with_raw_response: AsyncNotDiamondWithRawResponse
    with_streaming_response: AsyncNotDiamondWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncNotDiamond client instance.

        This automatically infers the `api_key` argument from the `NOT_DIAMOND_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("NOT_DIAMOND_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NOT_DIAMOND_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.model_router = model_router.AsyncModelRouterResource(self)
        self.evaluations = evaluations.AsyncEvaluationsResource(self)
        self.report = report.AsyncReportResource(self)
        self.preferences = preferences.AsyncPreferencesResource(self)
        self.proxy = proxy.AsyncProxyResource(self)
        self.prompt = prompt.AsyncPromptResource(self)
        self.pzn = pzn.AsyncPznResource(self)
        self.chat = chat.AsyncChatResource(self)
        self.tt = tt.AsyncTtResource(self)
        self.semihuman = semihuman.AsyncSemihumanResource(self)
        self.api_keys = api_keys.AsyncAPIKeysResource(self)
        self.llm_usage = llm_usage.AsyncLlmUsageResource(self)
        self.adaptation_runs = adaptation_runs.AsyncAdaptationRunsResource(self)
        self.admin = admin.AsyncAdminResource(self)
        self.health = health.AsyncHealthResource(self)
        self.error_debug = error_debug.AsyncErrorDebugResource(self)
        self.posthog_debug = posthog_debug.AsyncPosthogDebugResource(self)
        self.with_raw_response = AsyncNotDiamondWithRawResponse(self)
        self.with_streaming_response = AsyncNotDiamondWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def retrieve_root(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrieveRootResponse:
        """Returns welcome message."""
        return await self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveRootResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class NotDiamondWithRawResponse:
    def __init__(self, client: NotDiamond) -> None:
        self.model_router = model_router.ModelRouterResourceWithRawResponse(client.model_router)
        self.evaluations = evaluations.EvaluationsResourceWithRawResponse(client.evaluations)
        self.report = report.ReportResourceWithRawResponse(client.report)
        self.preferences = preferences.PreferencesResourceWithRawResponse(client.preferences)
        self.proxy = proxy.ProxyResourceWithRawResponse(client.proxy)
        self.prompt = prompt.PromptResourceWithRawResponse(client.prompt)
        self.pzn = pzn.PznResourceWithRawResponse(client.pzn)
        self.chat = chat.ChatResourceWithRawResponse(client.chat)
        self.tt = tt.TtResourceWithRawResponse(client.tt)
        self.semihuman = semihuman.SemihumanResourceWithRawResponse(client.semihuman)
        self.api_keys = api_keys.APIKeysResourceWithRawResponse(client.api_keys)
        self.llm_usage = llm_usage.LlmUsageResourceWithRawResponse(client.llm_usage)
        self.adaptation_runs = adaptation_runs.AdaptationRunsResourceWithRawResponse(client.adaptation_runs)
        self.admin = admin.AdminResourceWithRawResponse(client.admin)
        self.health = health.HealthResourceWithRawResponse(client.health)
        self.error_debug = error_debug.ErrorDebugResourceWithRawResponse(client.error_debug)
        self.posthog_debug = posthog_debug.PosthogDebugResourceWithRawResponse(client.posthog_debug)

        self.retrieve_root = to_raw_response_wrapper(
            client.retrieve_root,
        )


class AsyncNotDiamondWithRawResponse:
    def __init__(self, client: AsyncNotDiamond) -> None:
        self.model_router = model_router.AsyncModelRouterResourceWithRawResponse(client.model_router)
        self.evaluations = evaluations.AsyncEvaluationsResourceWithRawResponse(client.evaluations)
        self.report = report.AsyncReportResourceWithRawResponse(client.report)
        self.preferences = preferences.AsyncPreferencesResourceWithRawResponse(client.preferences)
        self.proxy = proxy.AsyncProxyResourceWithRawResponse(client.proxy)
        self.prompt = prompt.AsyncPromptResourceWithRawResponse(client.prompt)
        self.pzn = pzn.AsyncPznResourceWithRawResponse(client.pzn)
        self.chat = chat.AsyncChatResourceWithRawResponse(client.chat)
        self.tt = tt.AsyncTtResourceWithRawResponse(client.tt)
        self.semihuman = semihuman.AsyncSemihumanResourceWithRawResponse(client.semihuman)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithRawResponse(client.api_keys)
        self.llm_usage = llm_usage.AsyncLlmUsageResourceWithRawResponse(client.llm_usage)
        self.adaptation_runs = adaptation_runs.AsyncAdaptationRunsResourceWithRawResponse(client.adaptation_runs)
        self.admin = admin.AsyncAdminResourceWithRawResponse(client.admin)
        self.health = health.AsyncHealthResourceWithRawResponse(client.health)
        self.error_debug = error_debug.AsyncErrorDebugResourceWithRawResponse(client.error_debug)
        self.posthog_debug = posthog_debug.AsyncPosthogDebugResourceWithRawResponse(client.posthog_debug)

        self.retrieve_root = async_to_raw_response_wrapper(
            client.retrieve_root,
        )


class NotDiamondWithStreamedResponse:
    def __init__(self, client: NotDiamond) -> None:
        self.model_router = model_router.ModelRouterResourceWithStreamingResponse(client.model_router)
        self.evaluations = evaluations.EvaluationsResourceWithStreamingResponse(client.evaluations)
        self.report = report.ReportResourceWithStreamingResponse(client.report)
        self.preferences = preferences.PreferencesResourceWithStreamingResponse(client.preferences)
        self.proxy = proxy.ProxyResourceWithStreamingResponse(client.proxy)
        self.prompt = prompt.PromptResourceWithStreamingResponse(client.prompt)
        self.pzn = pzn.PznResourceWithStreamingResponse(client.pzn)
        self.chat = chat.ChatResourceWithStreamingResponse(client.chat)
        self.tt = tt.TtResourceWithStreamingResponse(client.tt)
        self.semihuman = semihuman.SemihumanResourceWithStreamingResponse(client.semihuman)
        self.api_keys = api_keys.APIKeysResourceWithStreamingResponse(client.api_keys)
        self.llm_usage = llm_usage.LlmUsageResourceWithStreamingResponse(client.llm_usage)
        self.adaptation_runs = adaptation_runs.AdaptationRunsResourceWithStreamingResponse(client.adaptation_runs)
        self.admin = admin.AdminResourceWithStreamingResponse(client.admin)
        self.health = health.HealthResourceWithStreamingResponse(client.health)
        self.error_debug = error_debug.ErrorDebugResourceWithStreamingResponse(client.error_debug)
        self.posthog_debug = posthog_debug.PosthogDebugResourceWithStreamingResponse(client.posthog_debug)

        self.retrieve_root = to_streamed_response_wrapper(
            client.retrieve_root,
        )


class AsyncNotDiamondWithStreamedResponse:
    def __init__(self, client: AsyncNotDiamond) -> None:
        self.model_router = model_router.AsyncModelRouterResourceWithStreamingResponse(client.model_router)
        self.evaluations = evaluations.AsyncEvaluationsResourceWithStreamingResponse(client.evaluations)
        self.report = report.AsyncReportResourceWithStreamingResponse(client.report)
        self.preferences = preferences.AsyncPreferencesResourceWithStreamingResponse(client.preferences)
        self.proxy = proxy.AsyncProxyResourceWithStreamingResponse(client.proxy)
        self.prompt = prompt.AsyncPromptResourceWithStreamingResponse(client.prompt)
        self.pzn = pzn.AsyncPznResourceWithStreamingResponse(client.pzn)
        self.chat = chat.AsyncChatResourceWithStreamingResponse(client.chat)
        self.tt = tt.AsyncTtResourceWithStreamingResponse(client.tt)
        self.semihuman = semihuman.AsyncSemihumanResourceWithStreamingResponse(client.semihuman)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithStreamingResponse(client.api_keys)
        self.llm_usage = llm_usage.AsyncLlmUsageResourceWithStreamingResponse(client.llm_usage)
        self.adaptation_runs = adaptation_runs.AsyncAdaptationRunsResourceWithStreamingResponse(client.adaptation_runs)
        self.admin = admin.AsyncAdminResourceWithStreamingResponse(client.admin)
        self.health = health.AsyncHealthResourceWithStreamingResponse(client.health)
        self.error_debug = error_debug.AsyncErrorDebugResourceWithStreamingResponse(client.error_debug)
        self.posthog_debug = posthog_debug.AsyncPosthogDebugResourceWithStreamingResponse(client.posthog_debug)

        self.retrieve_root = async_to_streamed_response_wrapper(
            client.retrieve_root,
        )


Client = NotDiamond

AsyncClient = AsyncNotDiamond
