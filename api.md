# ModelRouter

Methods:

- <code title="post /v2/modelRouter/modelSelect">client.model_router.<a href="./src/not_diamond/resources/model_router.py">select_model</a>(\*\*<a href="src/not_diamond/types/model_router_select_model_params.py">params</a>) -> object</code>

# Preferences

Methods:

- <code title="post /v2/preferences/preferenceCreate">client.preferences.<a href="./src/not_diamond/resources/preferences.py">create</a>(\*\*<a href="src/not_diamond/types/preference_create_params.py">params</a>) -> object</code>
- <code title="post /v2/preferences/update">client.preferences.<a href="./src/not_diamond/resources/preferences.py">update</a>(\*\*<a href="src/not_diamond/types/preference_update_params.py">params</a>) -> object</code>
- <code title="post /v2/preferences/preferenceDelete">client.preferences.<a href="./src/not_diamond/resources/preferences.py">delete</a>(\*\*<a href="src/not_diamond/types/preference_delete_params.py">params</a>) -> object</code>
- <code title="post /v2/preferences/userPreferenceCreate">client.preferences.<a href="./src/not_diamond/resources/preferences.py">create_user_preference</a>(\*\*<a href="src/not_diamond/types/preference_create_user_preference_params.py">params</a>) -> object</code>
- <code title="delete /v2/preferences/userPreferenceDelete/{preference_id}">client.preferences.<a href="./src/not_diamond/resources/preferences.py">delete_user_preference</a>(preference_id) -> object</code>
- <code title="get /v2/preferences/{user_id}">client.preferences.<a href="./src/not_diamond/resources/preferences.py">retrieve_user_preference</a>(user_id) -> object</code>
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
