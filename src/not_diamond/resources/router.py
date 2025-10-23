# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, Optional, cast

import httpx

from ..types import router_select_model_params, router_train_custom_router_params, router_create_survey_response_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["RouterResource", "AsyncRouterResource"]


class RouterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RouterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return RouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return RouterResourceWithStreamingResponse(self)

    def create_survey_response(
        self,
        *,
        constraint_priorities: str,
        email: str,
        llm_providers: str,
        use_case_desc: str,
        user_id: str,
        x_token: str,
        additional_preferences: Optional[str] | Omit = omit,
        dataset_file: Optional[FileTypes] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt_file: Optional[FileTypes] | Omit = omit,
        prompts: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Survey Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "constraint_priorities": constraint_priorities,
                "email": email,
                "llm_providers": llm_providers,
                "use_case_desc": use_case_desc,
                "user_id": user_id,
                "additional_preferences": additional_preferences,
                "dataset_file": dataset_file,
                "name": name,
                "prompt_file": prompt_file,
                "prompts": prompts,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["prompt_file"], ["dataset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            "/v2/pzn/surveyResponse",
            body=maybe_transform(body, router_create_survey_response_params.RouterCreateSurveyResponseParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def select_model(
        self,
        *,
        llm_providers: Iterable[router_select_model_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        type: Optional[str] | Omit = omit,
        hash_content: bool | Omit = omit,
        max_model_depth: Optional[int] | Omit = omit,
        metric: str | Omit = omit,
        preference_id: Optional[str] | Omit = omit,
        previous_session: Optional[str] | Omit = omit,
        tools: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        tradeoff: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Token Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/modelRouter/modelSelect",
            body=maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "hash_content": hash_content,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                router_select_model_params.RouterSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, router_select_model_params.RouterSelectModelParams),
            ),
            cast_to=object,
        )

    def train_custom_router(
        self,
        *,
        dataset_file: FileTypes,
        language: str,
        llm_providers: str,
        maximize: bool,
        prompt_column: str,
        override: Optional[bool] | Omit = omit,
        preference_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        preference_id: if specified, update the topic + topic embedding entries in db

        language: either "english" or "multilingual". If "english", use
        "embed-english-v3.0" embedding model If "multilingual", use
        "embed-multilingual-v3.0" embedding model.

        llm_providers: a JSONified string in the form '[{ "provider": "openai", "model":
        "gpt-3.5"}, { "provider": "openai", "model": "gpt-4"}]' which you can load as
        JSON

        prompt_column: column in the dataset_file that corresponds to the prompt each
        LLM is evaluated on

        dataset_file: will be a csv containing:

        1. prompt_column is the column containing the prompt used to call the LLM
        2. A column for each <provider>/<model>/score (as passed in llm_providers param)
           indicating the score achieved by the LLM
        3. A column for each <provider>/<model>/response (as passed in llm_providers
           param) indicating the response given by the LLM

        maximize: whether score higher is better. If False, then apply negative sign to
        all scores as the LLMTopicMaximalMarginalRelevance class assumes higher score is
        better

        Run BERTopic algo on Modal (run 10 times to get the best result) If
        preference_id is specified, update existing topic + embeddings If no
        preference_id, create a new preference and store topic + topic embeddings in db

        Store each prompt as an entry in the LLMPipeline table Create a result entry in
        LLMPipelineResults for each model in llm_providers Each result entry will also
        store the LLM response (db migration script pending)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "dataset_file": dataset_file,
                "language": language,
                "llm_providers": llm_providers,
                "maximize": maximize,
                "prompt_column": prompt_column,
                "override": override,
                "preference_id": preference_id,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["dataset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v2/pzn/trainCustomRouter",
            body=maybe_transform(body, router_train_custom_router_params.RouterTrainCustomRouterParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRouterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRouterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRouterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRouterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Not-Diamond/not-diamond-python#with_streaming_response
        """
        return AsyncRouterResourceWithStreamingResponse(self)

    async def create_survey_response(
        self,
        *,
        constraint_priorities: str,
        email: str,
        llm_providers: str,
        use_case_desc: str,
        user_id: str,
        x_token: str,
        additional_preferences: Optional[str] | Omit = omit,
        dataset_file: Optional[FileTypes] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt_file: Optional[FileTypes] | Omit = omit,
        prompts: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Survey Response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-token": x_token, **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "constraint_priorities": constraint_priorities,
                "email": email,
                "llm_providers": llm_providers,
                "use_case_desc": use_case_desc,
                "user_id": user_id,
                "additional_preferences": additional_preferences,
                "dataset_file": dataset_file,
                "name": name,
                "prompt_file": prompt_file,
                "prompts": prompts,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["prompt_file"], ["dataset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            "/v2/pzn/surveyResponse",
            body=await async_maybe_transform(
                body, router_create_survey_response_params.RouterCreateSurveyResponseParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def select_model(
        self,
        *,
        llm_providers: Iterable[router_select_model_params.LlmProvider],
        messages: Union[Iterable[Dict[str, Union[str, Iterable[object]]]], str],
        type: Optional[str] | Omit = omit,
        hash_content: bool | Omit = omit,
        max_model_depth: Optional[int] | Omit = omit,
        metric: str | Omit = omit,
        preference_id: Optional[str] | Omit = omit,
        previous_session: Optional[str] | Omit = omit,
        tools: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        tradeoff: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Token Model Select

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/modelRouter/modelSelect",
            body=await async_maybe_transform(
                {
                    "llm_providers": llm_providers,
                    "messages": messages,
                    "hash_content": hash_content,
                    "max_model_depth": max_model_depth,
                    "metric": metric,
                    "preference_id": preference_id,
                    "previous_session": previous_session,
                    "tools": tools,
                    "tradeoff": tradeoff,
                },
                router_select_model_params.RouterSelectModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, router_select_model_params.RouterSelectModelParams),
            ),
            cast_to=object,
        )

    async def train_custom_router(
        self,
        *,
        dataset_file: FileTypes,
        language: str,
        llm_providers: str,
        maximize: bool,
        prompt_column: str,
        override: Optional[bool] | Omit = omit,
        preference_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        preference_id: if specified, update the topic + topic embedding entries in db

        language: either "english" or "multilingual". If "english", use
        "embed-english-v3.0" embedding model If "multilingual", use
        "embed-multilingual-v3.0" embedding model.

        llm_providers: a JSONified string in the form '[{ "provider": "openai", "model":
        "gpt-3.5"}, { "provider": "openai", "model": "gpt-4"}]' which you can load as
        JSON

        prompt_column: column in the dataset_file that corresponds to the prompt each
        LLM is evaluated on

        dataset_file: will be a csv containing:

        1. prompt_column is the column containing the prompt used to call the LLM
        2. A column for each <provider>/<model>/score (as passed in llm_providers param)
           indicating the score achieved by the LLM
        3. A column for each <provider>/<model>/response (as passed in llm_providers
           param) indicating the response given by the LLM

        maximize: whether score higher is better. If False, then apply negative sign to
        all scores as the LLMTopicMaximalMarginalRelevance class assumes higher score is
        better

        Run BERTopic algo on Modal (run 10 times to get the best result) If
        preference_id is specified, update existing topic + embeddings If no
        preference_id, create a new preference and store topic + topic embeddings in db

        Store each prompt as an entry in the LLMPipeline table Create a result entry in
        LLMPipelineResults for each model in llm_providers Each result entry will also
        store the LLM response (db migration script pending)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "dataset_file": dataset_file,
                "language": language,
                "llm_providers": llm_providers,
                "maximize": maximize,
                "prompt_column": prompt_column,
                "override": override,
                "preference_id": preference_id,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["dataset_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v2/pzn/trainCustomRouter",
            body=await async_maybe_transform(body, router_train_custom_router_params.RouterTrainCustomRouterParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RouterResourceWithRawResponse:
    def __init__(self, router: RouterResource) -> None:
        self._router = router

        self.create_survey_response = to_raw_response_wrapper(
            router.create_survey_response,
        )
        self.select_model = to_raw_response_wrapper(
            router.select_model,
        )
        self.train_custom_router = to_raw_response_wrapper(
            router.train_custom_router,
        )


class AsyncRouterResourceWithRawResponse:
    def __init__(self, router: AsyncRouterResource) -> None:
        self._router = router

        self.create_survey_response = async_to_raw_response_wrapper(
            router.create_survey_response,
        )
        self.select_model = async_to_raw_response_wrapper(
            router.select_model,
        )
        self.train_custom_router = async_to_raw_response_wrapper(
            router.train_custom_router,
        )


class RouterResourceWithStreamingResponse:
    def __init__(self, router: RouterResource) -> None:
        self._router = router

        self.create_survey_response = to_streamed_response_wrapper(
            router.create_survey_response,
        )
        self.select_model = to_streamed_response_wrapper(
            router.select_model,
        )
        self.train_custom_router = to_streamed_response_wrapper(
            router.train_custom_router,
        )


class AsyncRouterResourceWithStreamingResponse:
    def __init__(self, router: AsyncRouterResource) -> None:
        self._router = router

        self.create_survey_response = async_to_streamed_response_wrapper(
            router.create_survey_response,
        )
        self.select_model = async_to_streamed_response_wrapper(
            router.select_model,
        )
        self.train_custom_router = async_to_streamed_response_wrapper(
            router.train_custom_router,
        )
