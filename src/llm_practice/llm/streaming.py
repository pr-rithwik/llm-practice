from litellm import completion
from collections.abc import Iterator

from llm_practice.constants.models import MODEL_GPT_4O_MINI

def get_completion_response(model, messages, tools=None, stream=True):
    response = completion(
        model=model,
        messages=messages,
        stream=stream,
        tools=tools
    )
    return response

def get_streaming_completion(prompt: str, model: str = MODEL_GPT_4O_MINI) -> Iterator[str]:
    messages=[{"role": "user", "content": prompt}]

    yield from get_streaming_completion_from_messages(
        messages=messages, model=model
    )


def get_streaming_completion_from_messages(messages, model: str = MODEL_GPT_4O_MINI,
        tools: list[dict] | None = None) -> Iterator[str]:
    # api_base = "http://localhost:11434" if use_ollama else None
    
    response = get_completion_response(model=model, messages=messages, tools=tools)
    
    result = ""
    for chunk in response:
        if content := chunk.choices[0].delta.content:
            result += content
            yield result
