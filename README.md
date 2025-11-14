# Notdiamond Python API library

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/notdiamond.svg?label=pypi%20(stable))](https://pypi.org/project/notdiamond/)

The Notdiamond Python library provides convenient access to the Notdiamond REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## What is Prompt Adaptation?

Not Diamond specializes in **Prompt Adaptation** - automatically optimizing your prompts to work optimally across different LLMs. Each language model has unique characteristics, instruction-following patterns, and preferred prompt formats. A prompt that works perfectly for GPT-5 might perform poorly on Claude or Gemini.
Manually rewriting prompts for each model is time-consuming and requires deep expertise in each model's quirks.

**The Solution**: Not Diamond automatically adapts your prompts with:
- Automatic optimization of both system and user prompts
- Built-in evaluation metrics
- Minimum 25 training examples recommended
- Processing time: typically 10–30 minutes

## Documentation

The REST API documentation can be found on [docs.notdiamond.ai](https://docs.notdiamond.ai). The full API of this library can be found in [api.md](api.md).

## Installation

```sh
# install from PyPI
pip install --pre notdiamond
```

## Usage

#### Quick Start

```python
import os
from notdiamond import Notdiamond

client = Notdiamond(
    api_key=os.environ.get("NOT_DIAMOND_API_KEY"),  # This is the default and can be omitted
)

# Step 1: Start a prompt adaptation job
adaptation = client.prompt.adapt.create(
    fields=["question"],
    system_prompt="You are a helpful assistant that answers questions accurately.",
    target_models=[
        {
            "model": "claude-sonnet-4-5-20250929",
            "provider": "anthropic",
        },
        {
            "model": "gemini-2.5-flash",
            "provider": "google",
        },
    ],
    template="Question: {question}\nAnswer:",
    train_goldens=[
        {"fields": {"question": "What is 2+2?"}, "answer": "4"},
        {"fields": {"question": "What is the capital of France?"}, "answer": "Paris"},
        {"fields": {"question": "Who wrote Romeo and Juliet?"}, "answer": "William Shakespeare"},
        # Add at least 25 training examples for best results
        # More examples = better adaptation quality
    ],
    test_goldens=[
        {"fields": {"question": "What is 3*3?"}, "answer": "9"},
        {"fields": {"question": "What is the largest ocean?"}, "answer": "Pacific Ocean"},
        # Add test examples to validate performance
    ],
    evaluation_metric="LLMaaJ:Sem_Sim_1",  # Or use custom evaluation
)

print(f"Adaptation started: {adaptation.adaptation_run_id}")

# Step 2: Poll for completion (typically takes 10-30 minutes)
while True:
    status = client.prompt.get_adapt_status(adaptation.adaptation_run_id)
    print(f"Status: {status.status}")
    
    if status.status == "queued":
        print(f"Queue position: {status.queue_position}")
    
    if status.status in ["completed", "failed"]:
        break
    
    time.sleep(30)  # Poll every 30 seconds

# Step 3: Get the optimized prompts
if status.status == "completed":
    results = client.prompt.get_adapt_results(adaptation.adaptation_run_id)
    
    print(f"\nOrigin model baseline: {results.origin_model.score:.2f}")
    
    for target in results.target_models:
        print(f"\n{'='*50}")
        print(f"Model: {target.model.model} ({target.model.provider})")
        print(f"Optimized System Prompt:\n{target.system_prompt}")
        print(f"Optimized Template:\n{target.user_message_template}")
        print(f"Pre-optimization score: {target.pre_optimization_score:.2f}")
        print(f"Post-optimization score: {target.post_optimization_score:.2f}")
        print(f"Improvement: {((target.post_optimization_score / target.pre_optimization_score - 1) * 100):.1f}%")
        print(f"Cost: ${target.cost:.4f}")
```

For more details, see the [Prompt Adaptation documentation](https://docs.notdiamond.ai/docs/adapting-prompts-to-new-models).

### Model Routing

Select the best model automatically:

```python
import os
from notdiamond import NotDiamond

client = NotDiamond(
    api_key=os.environ.get("NOT_DIAMOND_API_KEY"),  # This is the default and can be omitted
)

response = client.model_router.select_model(
    llm_providers=[
        {"model": "gpt-4o", "provider": "openai"},
        {"model": "claude-sonnet-4-5-20250929", "provider": "anthropic"},
        {"model": "gemini-2.5-flash", "provider": "google"},
    ],
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms"},
    ],
)
print(response.providers)
```

### Train Custom Router

For even better performance, you can train a custom router on your own dataset. This allows the router to learn the specific patterns and preferences of your use case:

```python
from pathlib import Path
from notdiamond import NotDiamond

client = NotDiamond(
    api_key=os.environ.get("NOT_DIAMOND_API_KEY"),  # This is the default and can be omitted
)

client.pzn.train_custom_router(
    dataset_file=Path("/path/to/file"),
    language="english",
    llm_providers='[{"provider": "openai", "model": "gpt-4o"}, {"provider": "anthropic", "model": "claude-sonnet-4-5-20250929"}]',
    maximize=True,
    prompt_column="prompt",
)
```

## Async usage

Simply import `AsyncNotdiamond` instead of `Notdiamond` and use `await` with each API call:

```python
import os
import asyncio
from notdiamond import AsyncNotdiamond

client = AsyncNotdiamond(
    api_key=os.environ.get("NOT_DIAMOND_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    # Start a prompt adaptation job
    response = await client.prompt.adapt.create(
        fields=["question"],
        system_prompt="You are a helpful assistant that answers questions accurately.",
        target_models=[
            {
                "model": "claude-sonnet-4-5-20250929",
                "provider": "anthropic",
            },
            {
                "model": "gemini-2.5-flash",
                "provider": "google",
            },
        ],
        template="Question: {question}\nAnswer:",
        train_goldens=[
            {"fields": {"question": "What is 2+2?"}, "answer": "4"},
            {"fields": {"question": "What is the capital of France?"}, "answer": "Paris"},
            # Add at least 25 examples for best results
        ],
        test_goldens=[
            {"fields": {"question": "What is 3*3?"}, "answer": "9"},
        ],
    )
    
    adaptation_run_id = response.adaptation_run_id
    print(f"Adaptation started: {adaptation_run_id}")
    
    # Check status
    status = await client.prompt.get_adapt_status(adaptation_run_id)
    print(f"Status: {status.job_status}")


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install --pre notdiamond[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import asyncio
from notdiamond import DefaultAioHttpClient
from notdiamond import AsyncNotdiamond


async def main() -> None:
    async with AsyncNotdiamond(
        api_key="My API Key",
        http_client=DefaultAioHttpClient(),
    ) as client:
        response = await client.prompt.adapt.create(
            fields=["question"],
            system_prompt="You are a helpful assistant that answers questions accurately.",
            target_models=[
                {
                    "model": "claude-sonnet-4-5-20250929",
                    "provider": "anthropic",
                },
                {
                    "model": "gemini-2.5-flash",
                    "provider": "google",
                },
            ],
            template="Question: {question}\nAnswer:",
            train_goldens=[
                {"fields": {"question": "What is 2+2?"}, "answer": "4"},
                {"fields": {"question": "What is the capital of France?"}, "answer": "Paris"},
                # Add at least 25 examples for best results
            ],
            test_goldens=[
                {"fields": {"question": "What is 3*3?"}, "answer": "9"},
            ],
        )
        print(f"Adaptation started: {response.adaptation_run_id}")


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from notdiamond import Notdiamond

client = Notdiamond()

response = client.prompt.adapt.create(
    fields=["question", "context"],
    system_prompt="You are a helpful assistant.",
    target_models=[
        {
            "model": "claude-sonnet-4-5-20250929",
            "provider": "anthropic",
        },
    ],
    template="Context: {context}\nQuestion: {question}\nAnswer:",
    train_goldens=[
        {
            "fields": {
                "question": "What is 2+2?",
                "context": "Basic arithmetic",
            },
            "answer": "4",
        },
        # Add at least 25 examples for best results
    ],
    test_goldens=[
        {
            "fields": {
                "question": "What is 3*3?",
                "context": "Basic arithmetic",
            },
            "answer": "9",
        },
    ],
)
print(response.adaptation_run_id)
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `notdiamond.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `notdiamond.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `notdiamond.APIError`.

```python
import notdiamond
from notdiamond import Notdiamond

client = Notdiamond()

try:
    client.prompt.adapt.create(
        fields=["question"],
        system_prompt="You are a helpful assistant.",
        target_models=[
            {
                "model": "claude-sonnet-4-5-20250929",
                "provider": "anthropic",
            },
            {
                "model": "gemini-2.5-flash",
                "provider": "google",
            },
        ],
        template="Question: {question}\nAnswer:",
        train_goldens=[
            {"fields": {"question": "What is 2+2?"}, "answer": "4"},
            # Add at least 25 examples...
        ],
        test_goldens=[
            {"fields": {"question": "What is 3*3?"}, "answer": "9"},
        ],
    )
except notdiamond.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except notdiamond.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except notdiamond.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from notdiamond import Notdiamond

# Configure the default for all requests:
client = Notdiamond(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Notdiamond(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request (note: prompt adaptation may take 10-30 minutes, so increase timeout accordingly):
client.with_options(timeout=120.0).prompt.get_adapt_status(
    adaptation_run_id="your-adaptation-run-id"
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `NOTDIAMOND_LOG` to `info`.

```shell
$ export NOTDIAMOND_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from notdiamond import Notdiamond

client = Notdiamond()
response = client.prompt.adapt.with_raw_response.create(
    fields=["question"],
    system_prompt="You are a helpful assistant.",
    target_models=[
        {
            "model": "claude-sonnet-4-5-20250929",
            "provider": "anthropic",
        },
        {
            "model": "gemini-2.5-flash",
            "provider": "google",
        },
    ],
    template="Question: {question}\nAnswer:",
    train_goldens=[
        {"fields": {"question": "What is 2+2?"}, "answer": "4"},
        # Add at least 25 examples...
    ],
    test_goldens=[
        {"fields": {"question": "What is 3*3?"}, "answer": "9"},
    ],
)
print(response.headers.get('X-My-Header'))

adapt_response = response.parse()  # get the object that `prompt.adapt.create()` would have returned
print(adapt_response.adaptation_run_id)
```

These methods return an [`APIResponse`](https://github.com/Not-Diamond/not-diamond-python/tree/main/src/notdiamond/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/Not-Diamond/not-diamond-python/tree/main/src/notdiamond/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.prompt.adapt.with_streaming_response.create(
    fields=["question"],
    system_prompt="You are a helpful assistant.",
    target_models=[
        {
            "model": "claude-sonnet-4-5-20250929",
            "provider": "anthropic",
        },
        {
            "model": "gemini-2.5-flash",
            "provider": "google",
        },
    ],
    template="Question: {question}\nAnswer:",
    train_goldens=[
        {"fields": {"question": "What is 2+2?"}, "answer": "4"},
        # Add at least 25 examples...
    ],
    test_goldens=[
        {"fields": {"question": "What is 3*3?"}, "answer": "9"},
    ],
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from notdiamond import Notdiamond, DefaultHttpxClient

client = Notdiamond(
    # Or use the `NOTDIAMOND_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from notdiamond import Notdiamond

with Notdiamond() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/Not-Diamond/not-diamond-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import notdiamond
print(notdiamond.__version__)
```

## Requirements

Python 3.9 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).

