# ModelRouter

Types:

```python
from not_diamond.types import ModelRouterSelectModelResponse
```

Methods:

- <code title="post /v2/modelRouter/openHandsRouter">client.model_router.<a href="./src/not_diamond/resources/model_router.py">open_hands_select</a>(\*\*<a href="src/not_diamond/types/model_router_open_hands_select_params.py">params</a>) -> object</code>
- <code title="post /v2/modelRouter/modelSelect">client.model_router.<a href="./src/not_diamond/resources/model_router.py">select_model</a>(\*\*<a href="src/not_diamond/types/model_router_select_model_params.py">params</a>) -> <a href="./src/not_diamond/types/model_router_select_model_response.py">ModelRouterSelectModelResponse</a></code>

# Report

## Metrics

Types:

```python
from not_diamond.types.report import MetricSubmitFeedbackResponse
```

Methods:

- <code title="post /v2/report/metrics/feedback">client.report.metrics.<a href="./src/not_diamond/resources/report/metrics.py">submit_feedback</a>(\*\*<a href="src/not_diamond/types/report/metric_submit_feedback_params.py">params</a>) -> <a href="./src/not_diamond/types/report/metric_submit_feedback_response.py">MetricSubmitFeedbackResponse</a></code>

# Preferences

Types:

```python
from not_diamond.types import PreferenceCreateResponse
```

Methods:

- <code title="post /v2/preferences/userPreferenceCreate">client.preferences.<a href="./src/not_diamond/resources/preferences.py">create</a>(\*\*<a href="src/not_diamond/types/preference_create_params.py">params</a>) -> <a href="./src/not_diamond/types/preference_create_response.py">PreferenceCreateResponse</a></code>
- <code title="get /v2/preferences/{user_id}">client.preferences.<a href="./src/not_diamond/resources/preferences.py">retrieve</a>(user_id) -> object</code>
- <code title="put /v2/preferences/userPreferenceUpdate">client.preferences.<a href="./src/not_diamond/resources/preferences.py">update</a>(\*\*<a href="src/not_diamond/types/preference_update_params.py">params</a>) -> object</code>
- <code title="delete /v2/preferences/userPreferenceDelete/{preference_id}">client.preferences.<a href="./src/not_diamond/resources/preferences.py">delete</a>(preference_id) -> object</code>

# Prompt

Types:

```python
from not_diamond.types import JobStatus, PromptGetAdaptResultsResponse, PromptGetAdaptStatusResponse
```

Methods:

- <code title="get /v2/prompt/adaptResults/{adaptation_run_id}">client.prompt.<a href="./src/not_diamond/resources/prompt/prompt.py">get_adapt_results</a>(adaptation_run_id) -> <a href="./src/not_diamond/types/prompt_get_adapt_results_response.py">PromptGetAdaptResultsResponse</a></code>
- <code title="get /v2/prompt/adaptStatus/{adaptation_run_id}">client.prompt.<a href="./src/not_diamond/resources/prompt/prompt.py">get_adapt_status</a>(adaptation_run_id) -> <a href="./src/not_diamond/types/prompt_get_adapt_status_response.py">PromptGetAdaptStatusResponse</a></code>

## Adapt

Types:

```python
from not_diamond.types.prompt import (
    GoldenRecord,
    RequestProvider,
    AdaptCreateResponse,
    AdaptGetCostsResponse,
)
```

Methods:

- <code title="post /v2/prompt/adapt">client.prompt.adapt.<a href="./src/not_diamond/resources/prompt/adapt.py">create</a>(\*\*<a href="src/not_diamond/types/prompt/adapt_create_params.py">params</a>) -> <a href="./src/not_diamond/types/prompt/adapt_create_response.py">AdaptCreateResponse</a></code>
- <code title="get /v2/prompt/adapt/{adaptation_run_id}/costs">client.prompt.adapt.<a href="./src/not_diamond/resources/prompt/adapt.py">get_costs</a>(adaptation_run_id) -> <a href="./src/not_diamond/types/prompt/adapt_get_costs_response.py">AdaptGetCostsResponse</a></code>

# Pzn

Types:

```python
from not_diamond.types import PznTrainCustomRouterResponse
```

Methods:

- <code title="post /v2/pzn/surveyResponse">client.pzn.<a href="./src/not_diamond/resources/pzn.py">submit_survey_response</a>(\*\*<a href="src/not_diamond/types/pzn_submit_survey_response_params.py">params</a>) -> object</code>
- <code title="post /v2/pzn/trainCustomRouter">client.pzn.<a href="./src/not_diamond/resources/pzn.py">train_custom_router</a>(\*\*<a href="src/not_diamond/types/pzn_train_custom_router_params.py">params</a>) -> <a href="./src/not_diamond/types/pzn_train_custom_router_response.py">PznTrainCustomRouterResponse</a></code>

# Models

Types:

```python
from not_diamond.types import Model, ModelListResponse
```

Methods:

- <code title="get /v2/models">client.models.<a href="./src/not_diamond/resources/models.py">list</a>(\*\*<a href="src/not_diamond/types/model_list_params.py">params</a>) -> <a href="./src/not_diamond/types/model_list_response.py">ModelListResponse</a></code>
