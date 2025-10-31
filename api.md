# Routing

Types:

```python
from not_diamond.types import RoutingSelectModelResponse, RoutingTrainCustomRouterResponse
```

Methods:

- <code title="post /v2/pzn/surveyResponse">client.routing.<a href="./src/not_diamond/resources/routing.py">create_survey_response</a>(\*\*<a href="src/not_diamond/types/routing_create_survey_response_params.py">params</a>) -> object</code>
- <code title="post /v2/modelRouter/modelSelect">client.routing.<a href="./src/not_diamond/resources/routing.py">select_model</a>(\*\*<a href="src/not_diamond/types/routing_select_model_params.py">params</a>) -> <a href="./src/not_diamond/types/routing_select_model_response.py">RoutingSelectModelResponse</a></code>
- <code title="post /v2/pzn/trainCustomRouter">client.routing.<a href="./src/not_diamond/resources/routing.py">train_custom_router</a>(\*\*<a href="src/not_diamond/types/routing_train_custom_router_params.py">params</a>) -> <a href="./src/not_diamond/types/routing_train_custom_router_response.py">RoutingTrainCustomRouterResponse</a></code>

# Preferences

Types:

```python
from not_diamond.types import PreferenceCreateUserPreferenceResponse
```

Methods:

- <code title="get /v2/preferences/{user_id}/{preference_id}">client.preferences.<a href="./src/not_diamond/resources/preferences.py">retrieve</a>(preference_id, \*, user_id) -> object</code>
- <code title="post /v2/preferences/userPreferenceCreate">client.preferences.<a href="./src/not_diamond/resources/preferences.py">create_user_preference</a>(\*\*<a href="src/not_diamond/types/preference_create_user_preference_params.py">params</a>) -> <a href="./src/not_diamond/types/preference_create_user_preference_response.py">PreferenceCreateUserPreferenceResponse</a></code>
- <code title="delete /v2/preferences/userPreferenceDelete/{preference_id}">client.preferences.<a href="./src/not_diamond/resources/preferences.py">delete_user_preference</a>(preference_id) -> object</code>
- <code title="put /v2/preferences/userPreferenceUpdate">client.preferences.<a href="./src/not_diamond/resources/preferences.py">update_user_preference</a>(\*\*<a href="src/not_diamond/types/preference_update_user_preference_params.py">params</a>) -> object</code>

# PromptAdaptation

Types:

```python
from not_diamond.types import (
    AdaptationRunResults,
    JobStatus,
    PromptAdaptationAdaptResponse,
    PromptAdaptationGetAdaptRunsResponse,
    PromptAdaptationGetAdaptStatusResponse,
    PromptAdaptationRetrieveCostsResponse,
)
```

Methods:

- <code title="post /v2/prompt/adapt">client.prompt_adaptation.<a href="./src/not_diamond/resources/prompt_adaptation.py">adapt</a>(\*\*<a href="src/not_diamond/types/prompt_adaptation_adapt_params.py">params</a>) -> <a href="./src/not_diamond/types/prompt_adaptation_adapt_response.py">PromptAdaptationAdaptResponse</a></code>
- <code title="get /v2/prompt/adaptResults/{adaptation_run_id}">client.prompt_adaptation.<a href="./src/not_diamond/resources/prompt_adaptation.py">get_adapt_results</a>(adaptation_run_id) -> <a href="./src/not_diamond/types/adaptation_run_results.py">AdaptationRunResults</a></code>
- <code title="get /v2/prompt/frontendAdaptRunResults/{user_id}/{adaptation_run_id}">client.prompt_adaptation.<a href="./src/not_diamond/resources/prompt_adaptation.py">get_adapt_run_results</a>(adaptation_run_id, \*, user_id) -> <a href="./src/not_diamond/types/adaptation_run_results.py">AdaptationRunResults</a></code>
- <code title="get /v2/prompt/frontendAdaptRuns/{user_id}">client.prompt_adaptation.<a href="./src/not_diamond/resources/prompt_adaptation.py">get_adapt_runs</a>(user_id) -> <a href="./src/not_diamond/types/prompt_adaptation_get_adapt_runs_response.py">PromptAdaptationGetAdaptRunsResponse</a></code>
- <code title="get /v2/prompt/adaptStatus/{adaptation_run_id}">client.prompt_adaptation.<a href="./src/not_diamond/resources/prompt_adaptation.py">get_adapt_status</a>(adaptation_run_id) -> <a href="./src/not_diamond/types/prompt_adaptation_get_adapt_status_response.py">PromptAdaptationGetAdaptStatusResponse</a></code>
- <code title="get /v1/adaptation-runs/{adaptation_run_id}/costs">client.prompt_adaptation.<a href="./src/not_diamond/resources/prompt_adaptation.py">retrieve_costs</a>(adaptation_run_id) -> <a href="./src/not_diamond/types/prompt_adaptation_retrieve_costs_response.py">PromptAdaptationRetrieveCostsResponse</a></code>

# Report

Types:

```python
from not_diamond.types import ReportSubmitFeedbackResponse
```

Methods:

- <code title="post /v2/report/hallucination">client.report.<a href="./src/not_diamond/resources/report.py">evaluate_hallucination</a>(\*\*<a href="src/not_diamond/types/report_evaluate_hallucination_params.py">params</a>) -> object</code>
- <code title="post /v2/report/metrics/latency">client.report.<a href="./src/not_diamond/resources/report.py">latency</a>(\*\*<a href="src/not_diamond/types/report_latency_params.py">params</a>) -> object</code>
- <code title="post /v2/report/metrics/feedback">client.report.<a href="./src/not_diamond/resources/report.py">submit_feedback</a>(\*\*<a href="src/not_diamond/types/report_submit_feedback_params.py">params</a>) -> <a href="./src/not_diamond/types/report_submit_feedback_response.py">ReportSubmitFeedbackResponse</a></code>

# Models

Types:

```python
from not_diamond.types import ModelListResponse
```

Methods:

- <code title="get /v2/models">client.models.<a href="./src/not_diamond/resources/models.py">list</a>(\*\*<a href="src/not_diamond/types/model_list_params.py">params</a>) -> <a href="./src/not_diamond/types/model_list_response.py">ModelListResponse</a></code>
