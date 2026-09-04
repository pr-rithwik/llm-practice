from dotenv import load_dotenv
from llm_practice.llm.completion import get_completion
from llm_practice.constants.models import MODEL_GPT_4O_MINI

def main():
    response = get_completion(
        prompt="Explain what an LLM is in simple terms.",
        model=MODEL_GPT_4O_MINI,
    )

    print(response)


if __name__ == "__main__":
    main()