# NotDiamond

Types:

```python
from not_diamond.types import RetrieveRootResponse
```

Methods:

- <code title="get /">client.<a href="./src/not_diamond/_client.py">retrieve_root</a>() -> <a href="./src/not_diamond/types/retrieve_root_response.py">RetrieveRootResponse</a></code>

# ModelRouter

Methods:

- <code title="get /v2/modelRouter/health">client.model_router.<a href="./src/not_diamond/resources/model_router.py">check_health</a>() -> object</code>
- <code title="post /v2/modelRouter/modelSelect">client.model_router.<a href="./src/not_diamond/resources/model_router.py">select_model</a>(\*\*<a href="src/not_diamond/types/model_router_select_model_params.py">params</a>) -> object</code>
- <code title="post /v2/modelRouter/openHandsRouter">client.model_router.<a href="./src/not_diamond/resources/model_router.py">select_open_hands</a>(\*\*<a href="src/not_diamond/types/model_router_select_open_hands_params.py">params</a>) -> object</code>

# Evaluations

Methods:

- <code title="post /v2/evaluations/updateModelState">client.evaluations.<a href="./src/not_diamond/resources/evaluations.py">update_model_state</a>(\*\*<a href="src/not_diamond/types/evaluation_update_model_state_params.py">params</a>) -> object</code>

# Report

Methods:

- <code title="post /v2/report/hallucination">client.report.<a href="./src/not_diamond/resources/report/report.py">evaluate_hallucination</a>(\*\*<a href="src/not_diamond/types/report_evaluate_hallucination_params.py">params</a>) -> object</code>

## Metrics

Types:

```python
from not_diamond.types.report import (
    ArenaFeedback,
    FeedbackReport,
    RegenerationFeedback,
    RequestProvider,
    ThumbsUpDownFeedback,
)
```

Methods:

- <code title="post /v2/report/metrics/feedback">client.report.metrics.<a href="./src/not_diamond/resources/report/metrics.py">report_feedback</a>(\*\*<a href="src/not_diamond/types/report/metric_report_feedback_params.py">params</a>) -> object</code>
- <code title="post /v2/report/metrics/frontendArenaChoice">client.report.metrics.<a href="./src/not_diamond/resources/report/metrics.py">report_frontend_arena_choice</a>(\*\*<a href="src/not_diamond/types/report/metric_report_frontend_arena_choice_params.py">params</a>) -> object</code>
- <code title="post /v2/report/metrics/frontendRegenerated">client.report.metrics.<a href="./src/not_diamond/resources/report/metrics.py">report_frontend_regenerated</a>(\*\*<a href="src/not_diamond/types/report/metric_report_frontend_regenerated_params.py">params</a>) -> object</code>
- <code title="post /v2/report/metrics/frontendThumbsUpDown">client.report.metrics.<a href="./src/not_diamond/resources/report/metrics.py">report_frontend_thumbs</a>(\*\*<a href="src/not_diamond/types/report/metric_report_frontend_thumbs_params.py">params</a>) -> object</code>
- <code title="post /v2/report/metrics/latency">client.report.metrics.<a href="./src/not_diamond/resources/report/metrics.py">report_latency</a>(\*\*<a href="src/not_diamond/types/report/metric_report_latency_params.py">params</a>) -> object</code>

## Usage

Methods:

- <code title="post /v2/report/usage/reportLLMCosts">client.report.usage.<a href="./src/not_diamond/resources/report/usage.py">report_llm_costs</a>() -> object</code>
- <code title="post /v2/report/usage/reportUsage">client.report.usage.<a href="./src/not_diamond/resources/report/usage.py">report_usage</a>() -> object</code>
- <code title="get /v2/report/usage/testLLMReporting">client.report.usage.<a href="./src/not_diamond/resources/report/usage.py">test_llm_reporting</a>() -> object</code>

# Preferences

Methods:

- <code title="post /v2/preferences/preferenceCreate">client.preferences.<a href="./src/not_diamond/resources/preferences.py">create</a>(\*\*<a href="src/not_diamond/types/preference_create_params.py">params</a>) -> object</code>
- <code title="post /v2/preferences/update">client.preferences.<a href="./src/not_diamond/resources/preferences.py">update</a>(\*\*<a href="src/not_diamond/types/preference_update_params.py">params</a>) -> object</code>
- <code title="post /v2/preferences/preferenceDelete">client.preferences.<a href="./src/not_diamond/resources/preferences.py">delete</a>(\*\*<a href="src/not_diamond/types/preference_delete_params.py">params</a>) -> object</code>
- <code title="post /v2/preferences/userPreferenceCreate">client.preferences.<a href="./src/not_diamond/resources/preferences.py">create_user_preference</a>(\*\*<a href="src/not_diamond/types/preference_create_user_preference_params.py">params</a>) -> object</code>
- <code title="delete /v2/preferences/userPreferenceDelete/{preference_id}">client.preferences.<a href="./src/not_diamond/resources/preferences.py">delete_user_preference</a>(preference_id) -> object</code>
- <code title="get /v2/preferences/{user_id}">client.preferences.<a href="./src/not_diamond/resources/preferences.py">retrieve_user_preference</a>(user_id) -> object</code>
- <code title="get /v2/preferences/{user_id}/{preference_id}">client.preferences.<a href="./src/not_diamond/resources/preferences.py">retrieve_user_preference_by_id</a>(preference_id, \*, user_id) -> object</code>
- <code title="put /v2/preferences/userPreferenceUpdate">client.preferences.<a href="./src/not_diamond/resources/preferences.py">update_user_preference</a>(\*\*<a href="src/not_diamond/types/preference_update_user_preference_params.py">params</a>) -> object</code>

# Proxy

Methods:

- <code title="get /v2/proxy/auth">client.proxy.<a href="./src/not_diamond/resources/proxy/proxy.py">retrieve_auth</a>() -> object</code>
- <code title="get /v2/proxy/secrets/{user_id}">client.proxy.<a href="./src/not_diamond/resources/proxy/proxy.py">retrieve_secrets</a>(user_id) -> object</code>

## Secret

Methods:

- <code title="delete /v2/proxy/secret/delete/{user_id}/{provider}">client.proxy.secret.<a href="./src/not_diamond/resources/proxy/secret.py">delete</a>(provider, \*, user_id) -> object</code>
- <code title="post /v2/proxy/secret">client.proxy.secret.<a href="./src/not_diamond/resources/proxy/secret.py">upsert</a>(\*\*<a href="src/not_diamond/types/proxy/secret_upsert_params.py">params</a>) -> object</code>

# Prompt

Types:

```python
from not_diamond.types import (
    AdaptationRunResults,
    JobStatus,
    PromptAdaptResponse,
    PromptGetAdaptRunsResponse,
    PromptGetAdaptStatusResponse,
)
```

Methods:

- <code title="post /v2/prompt/adapt">client.prompt.<a href="./src/not_diamond/resources/prompt.py">adapt</a>(\*\*<a href="src/not_diamond/types/prompt_adapt_params.py">params</a>) -> <a href="./src/not_diamond/types/prompt_adapt_response.py">PromptAdaptResponse</a></code>
- <code title="get /v2/prompt/adaptResults/{adaptation_run_id}">client.prompt.<a href="./src/not_diamond/resources/prompt.py">get_adapt_results</a>(adaptation_run_id) -> <a href="./src/not_diamond/types/adaptation_run_results.py">AdaptationRunResults</a></code>
- <code title="get /v2/prompt/frontendAdaptRunResults/{user_id}/{adaptation_run_id}">client.prompt.<a href="./src/not_diamond/resources/prompt.py">get_adapt_run_results</a>(adaptation_run_id, \*, user_id) -> <a href="./src/not_diamond/types/adaptation_run_results.py">AdaptationRunResults</a></code>
- <code title="get /v2/prompt/frontendAdaptRuns/{user_id}">client.prompt.<a href="./src/not_diamond/resources/prompt.py">get_adapt_runs</a>(user_id) -> <a href="./src/not_diamond/types/prompt_get_adapt_runs_response.py">PromptGetAdaptRunsResponse</a></code>
- <code title="get /v2/prompt/adaptStatus/{adaptation_run_id}">client.prompt.<a href="./src/not_diamond/resources/prompt.py">get_adapt_status</a>(adaptation_run_id) -> <a href="./src/not_diamond/types/prompt_get_adapt_status_response.py">PromptGetAdaptStatusResponse</a></code>

# Pzn

Methods:

- <code title="post /v2/pzn/surveyResponse">client.pzn.<a href="./src/not_diamond/resources/pzn.py">create_survey_response</a>(\*\*<a href="src/not_diamond/types/pzn_create_survey_response_params.py">params</a>) -> object</code>
- <code title="post /v2/pzn/trainCustomRouter">client.pzn.<a href="./src/not_diamond/resources/pzn.py">train_custom_router</a>(\*\*<a href="src/not_diamond/types/pzn_train_custom_router_params.py">params</a>) -> object</code>

# Chat

Methods:

- <code title="post /v2/chat/modelSelect">client.chat.<a href="./src/not_diamond/resources/chat/chat.py">select_model</a>(\*\*<a href="src/not_diamond/types/chat_select_model_params.py">params</a>) -> object</code>

## Preferences

Methods:

- <code title="post /v2/chat/preferences/preferenceCreate">client.chat.preferences.<a href="./src/not_diamond/resources/chat/preferences.py">create</a>(\*\*<a href="src/not_diamond/types/chat/preference_create_params.py">params</a>) -> object</code>
- <code title="put /v2/chat/preferences/update">client.chat.preferences.<a href="./src/not_diamond/resources/chat/preferences.py">update</a>(\*\*<a href="src/not_diamond/types/chat/preference_update_params.py">params</a>) -> object</code>
- <code title="delete /v2/chat/preferences/preferenceDelete/{preference_id}">client.chat.preferences.<a href="./src/not_diamond/resources/chat/preferences.py">delete</a>(preference_id) -> object</code>

## Report

Methods:

- <code title="post /v2/chat/report/regenerated">client.chat.report.<a href="./src/not_diamond/resources/chat/report.py">report_regenerated</a>(\*\*<a href="src/not_diamond/types/chat/report_report_regenerated_params.py">params</a>) -> object</code>
- <code title="post /v2/chat/report/thumbsUpDown">client.chat.report.<a href="./src/not_diamond/resources/chat/report.py">report_thumbs</a>(\*\*<a href="src/not_diamond/types/chat/report_report_thumbs_params.py">params</a>) -> object</code>

## Arena

Methods:

- <code title="post /v2/chat/arena/arenaChoice">client.chat.arena.<a href="./src/not_diamond/resources/chat/arena.py">create_choice</a>(\*\*<a href="src/not_diamond/types/chat/arena_create_choice_params.py">params</a>) -> object</code>
- <code title="post /v2/chat/arena/arenaModels">client.chat.arena.<a href="./src/not_diamond/resources/chat/arena.py">create_models</a>(\*\*<a href="src/not_diamond/types/chat/arena_create_models_params.py">params</a>) -> object</code>

# Tt

Methods:

- <code title="post /v2/TT/translate">client.tt.<a href="./src/not_diamond/resources/tt.py">translate</a>(\*\*<a href="src/not_diamond/types/tt_translate_params.py">params</a>) -> object</code>

# Semihuman

Types:

```python
from not_diamond.types import SemihumanRouteResponse
```

Methods:

- <code title="post /v2/semihuman/modelSelect">client.semihuman.<a href="./src/not_diamond/resources/semihuman.py">route</a>(\*\*<a href="src/not_diamond/types/semihuman_route_params.py">params</a>) -> <a href="./src/not_diamond/types/semihuman_route_response.py">SemihumanRouteResponse</a></code>

# APIKeys

Methods:

- <code title="post /v2/api-keys/">client.api_keys.<a href="./src/not_diamond/resources/api_keys.py">create</a>(\*\*<a href="src/not_diamond/types/api_key_create_params.py">params</a>) -> object</code>
- <code title="get /v2/api-keys/{user_id}">client.api_keys.<a href="./src/not_diamond/resources/api_keys.py">retrieve</a>(user_id) -> object</code>
- <code title="patch /v2/api-keys/">client.api_keys.<a href="./src/not_diamond/resources/api_keys.py">update</a>(\*\*<a href="src/not_diamond/types/api_key_update_params.py">params</a>) -> object</code>
- <code title="delete /v2/api-keys/{user_id}/{api_key_id}">client.api_keys.<a href="./src/not_diamond/resources/api_keys.py">delete</a>(api_key_id, \*, user_id) -> object</code>

# LlmUsage

Types:

```python
from not_diamond.types import (
    LlmUsage,
    UsageSummary,
    LlmUsageRetrieveResponse,
    LlmUsageRetrieveDailyResponse,
    LlmUsageRetrieveMonthlyResponse,
)
```

Methods:

- <code title="get /v1/llm-usage">client.llm_usage.<a href="./src/not_diamond/resources/llm_usage.py">retrieve</a>(\*\*<a href="src/not_diamond/types/llm_usage_retrieve_params.py">params</a>) -> <a href="./src/not_diamond/types/llm_usage_retrieve_response.py">LlmUsageRetrieveResponse</a></code>
- <code title="get /v1/llm-usage/daily">client.llm_usage.<a href="./src/not_diamond/resources/llm_usage.py">retrieve_daily</a>(\*\*<a href="src/not_diamond/types/llm_usage_retrieve_daily_params.py">params</a>) -> <a href="./src/not_diamond/types/llm_usage_retrieve_daily_response.py">LlmUsageRetrieveDailyResponse</a></code>
- <code title="get /v1/llm-usage/monthly">client.llm_usage.<a href="./src/not_diamond/resources/llm_usage.py">retrieve_monthly</a>(\*\*<a href="src/not_diamond/types/llm_usage_retrieve_monthly_params.py">params</a>) -> <a href="./src/not_diamond/types/llm_usage_retrieve_monthly_response.py">LlmUsageRetrieveMonthlyResponse</a></code>
- <code title="get /v1/llm-usage/summary">client.llm_usage.<a href="./src/not_diamond/resources/llm_usage.py">retrieve_summary</a>(\*\*<a href="src/not_diamond/types/llm_usage_retrieve_summary_params.py">params</a>) -> <a href="./src/not_diamond/types/usage_summary.py">UsageSummary</a></code>

# AdaptationRuns

Types:

```python
from not_diamond.types import AdaptationRunRetrieveCostsResponse
```

Methods:

- <code title="get /v1/adaptation-runs/{adaptation_run_id}/costs">client.adaptation_runs.<a href="./src/not_diamond/resources/adaptation_runs.py">retrieve_costs</a>(adaptation_run_id) -> <a href="./src/not_diamond/types/adaptation_run_retrieve_costs_response.py">AdaptationRunRetrieveCostsResponse</a></code>

# Admin

## LlmUsage

Types:

```python
from not_diamond.types.admin import LlmUsageRetrieveDailyResponse
```

Methods:

- <code title="get /v1/admin/llm-usage/daily">client.admin.llm_usage.<a href="./src/not_diamond/resources/admin/llm_usage.py">retrieve_daily</a>(\*\*<a href="src/not_diamond/types/admin/llm_usage_retrieve_daily_params.py">params</a>) -> <a href="./src/not_diamond/types/admin/llm_usage_retrieve_daily_response.py">LlmUsageRetrieveDailyResponse</a></code>
- <code title="get /v1/admin/llm-usage/summary">client.admin.llm_usage.<a href="./src/not_diamond/resources/admin/llm_usage.py">retrieve_summary</a>(\*\*<a href="src/not_diamond/types/admin/llm_usage_retrieve_summary_params.py">params</a>) -> <a href="./src/not_diamond/types/usage_summary.py">UsageSummary</a></code>

# Health

Types:

```python
from not_diamond.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/not_diamond/resources/health.py">check</a>() -> <a href="./src/not_diamond/types/health_check_response.py">HealthCheckResponse</a></code>

# ErrorDebug

Methods:

- <code title="get /error-debug">client.error_debug.<a href="./src/not_diamond/resources/error_debug.py">trigger_error</a>() -> object</code>

# PosthogDebug

Methods:

- <code title="get /posthog-debug">client.posthog_debug.<a href="./src/not_diamond/resources/posthog_debug.py">trigger</a>() -> object</code>
