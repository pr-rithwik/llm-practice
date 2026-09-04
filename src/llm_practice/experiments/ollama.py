from dotenv import load_dotenv
from llm_practice.llm.completion import get_completion
from llm_practice.constants.models import MODEL_OLLAMA_LLAMA3_2_3B

def main():
    print("Using Ollama: ")
    response = get_completion(
        prompt="Explain what an LLM is in simple terms.",
        model=MODEL_OLLAMA_LLAMA3_2_3B,
        use_ollama=True
    )

    print(response)


if __name__ == "__main__":
    main()