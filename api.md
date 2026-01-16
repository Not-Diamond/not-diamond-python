# ModelRouter

Types:

```python
from notdiamond.types import ModelRouterSelectModelResponse
```

Methods:

- <code title="post /v2/modelRouter/modelSelect">client.model_router.<a href="./src/notdiamond/resources/model_router.py">select_model</a>(\*\*<a href="src/notdiamond/types/model_router_select_model_params.py">params</a>) -> <a href="./src/notdiamond/types/model_router_select_model_response.py">ModelRouterSelectModelResponse</a></code>

# Preferences

Types:

```python
from notdiamond.types import PreferenceCreateResponse
```

Methods:

- <code title="post /v2/preferences/userPreferenceCreate">client.preferences.<a href="./src/notdiamond/resources/preferences.py">create</a>(\*\*<a href="src/notdiamond/types/preference_create_params.py">params</a>) -> <a href="./src/notdiamond/types/preference_create_response.py">PreferenceCreateResponse</a></code>
- <code title="put /v2/preferences/userPreferenceUpdate">client.preferences.<a href="./src/notdiamond/resources/preferences.py">update</a>(\*\*<a href="src/notdiamond/types/preference_update_params.py">params</a>) -> object</code>
- <code title="delete /v2/preferences/userPreferenceDelete/{preference_id}">client.preferences.<a href="./src/notdiamond/resources/preferences.py">delete</a>(preference_id) -> object</code>

# PromptOptimization

Types:

```python
from notdiamond.types import (
    GoldenRecord,
    JobStatus,
    RequestProvider,
    PromptOptimizationGetOptimizationResultsResponse,
    PromptOptimizationGetOptimziationStatusResponse,
    PromptOptimizationOptimizeResponse,
    PromptOptimizationRetrieveCostsResponse,
)
```

Methods:

- <code title="get /v2/prompt/optimizeResults/{optimization_run_id}">client.prompt_optimization.<a href="./src/notdiamond/resources/prompt_optimization.py">get_optimization_results</a>(optimization_run_id) -> <a href="./src/notdiamond/types/prompt_optimization_get_optimization_results_response.py">PromptOptimizationGetOptimizationResultsResponse</a></code>
- <code title="get /v2/prompt/optimizeStatus/{optimization_run_id}">client.prompt_optimization.<a href="./src/notdiamond/resources/prompt_optimization.py">get_optimziation_status</a>(optimization_run_id) -> <a href="./src/notdiamond/types/prompt_optimization_get_optimziation_status_response.py">PromptOptimizationGetOptimziationStatusResponse</a></code>
- <code title="post /v2/prompt/optimize">client.prompt_optimization.<a href="./src/notdiamond/resources/prompt_optimization.py">optimize</a>(\*\*<a href="src/notdiamond/types/prompt_optimization_optimize_params.py">params</a>) -> <a href="./src/notdiamond/types/prompt_optimization_optimize_response.py">PromptOptimizationOptimizeResponse</a></code>
- <code title="get /v2/prompt/optimize/{optimization_run_id}/costs">client.prompt_optimization.<a href="./src/notdiamond/resources/prompt_optimization.py">retrieve_costs</a>(optimization_run_id) -> <a href="./src/notdiamond/types/prompt_optimization_retrieve_costs_response.py">PromptOptimizationRetrieveCostsResponse</a></code>

# CustomRouter

Types:

```python
from notdiamond.types import CustomRouterTrainCustomRouterResponse
```

Methods:

- <code title="post /v2/pzn/trainCustomRouter">client.custom_router.<a href="./src/notdiamond/resources/custom_router.py">train_custom_router</a>(\*\*<a href="src/notdiamond/types/custom_router_train_custom_router_params.py">params</a>) -> <a href="./src/notdiamond/types/custom_router_train_custom_router_response.py">CustomRouterTrainCustomRouterResponse</a></code>

# Models

Types:

```python
from notdiamond.types import Model, ModelListResponse
```

Methods:

- <code title="get /v2/models">client.models.<a href="./src/notdiamond/resources/models.py">list</a>(\*\*<a href="src/notdiamond/types/model_list_params.py">params</a>) -> <a href="./src/notdiamond/types/model_list_response.py">ModelListResponse</a></code>
