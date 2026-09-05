from dotenv import load_dotenv

from llm_practice.ui.simple_query import main as simple_query_ui
from llm_practice.ui.simple_chat import main as simple_chat_ui
from llm_practice.ui.github_chat import main as github_chat_ui
from llm_practice.ui.multi_modal_chat import main as multi_modal_chat_ui

load_dotenv()

if __name__ == "__main__":
    # simple_query_ui()
    # simple_chat_ui()
    github_chat_ui()
    # multi_modal_chat_ui()