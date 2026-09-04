from litellm import completion
from llm_practice.constants.models import MODEL_GPT_4O_MINI


def get_completion(prompt: str, model: str = MODEL_GPT_4O_MINI, use_ollama: bool = False) -> str:
    api_base = "http://localhost:11434" if use_ollama else None

    response = completion(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        api_base=api_base,
    )

    return response.choices[0].message.content if response.choices else None
