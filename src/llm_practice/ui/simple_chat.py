import gradio as gr

from llm_practice.llm.streaming import get_streaming_completion_from_messages
from llm_practice.constants.models import MODEL_OLLAMA_LLAMA3_2_3B, MODEL_GPT_4O_MINI


SYSTEM_MESSAGE = "You are a helpful assistant, always answer in a crisp and short manner"

def simple_chat(message, history, model, system_message: str = None):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    system_message = system_message if system_message else SYSTEM_MESSAGE
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    yield from get_streaming_completion_from_messages(messages, model)


def main():
    model_dropdown = gr.Dropdown(
        choices=[
            MODEL_GPT_4O_MINI,
            MODEL_OLLAMA_LLAMA3_2_3B
        ],
        label="Model",
        value=MODEL_GPT_4O_MINI,
    )

    view = gr.ChatInterface(
        fn=simple_chat,
        additional_inputs=[model_dropdown],
    )

    view.launch()