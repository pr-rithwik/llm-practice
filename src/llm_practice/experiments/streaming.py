from llm_practice.constants.models import MODEL_GPT_4O_MINI
from llm_practice.llm.streaming import get_streaming_completion



def main():
    question = "Explain what an LLM is in simple terms."
    model = MODEL_GPT_4O_MINI
    for chunk in get_streaming_completion(question, model):
        print(chunk, end="", flush=True)
    print()



if __name__ == "__main__":
    main()