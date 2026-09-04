from dotenv import load_dotenv

from constants.models import MODEL_OLLAMA_QWEN3_4B, MODEL_OLLAMA_LLAMA3_2_3B
# from experiments import basic_completion, streaming
# from experiments.ollama import main as get_ollama_completion
from ui.simple_query import main as simple_query_ui
from ui.simple_chat import main as simple_chat_ui
from ui.tools_chat import main as tools_chat_ui

load_dotenv()

if __name__ == "__main__":
    # simple_query_ui()
    # simple_chat_ui()
    tools_chat_ui()