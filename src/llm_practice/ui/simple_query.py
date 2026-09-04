import gradio as gr
from llm_practice.llm.streaming import get_streaming_completion
from llm_practice.constants.models import MODEL_OLLAMA_LLAMA3_2_3B, MODEL_GPT_4O_MINI


def main():
    message_input = gr.Textbox(
        label="Your message:", 
        info="Ask your query", 
        lines=7
    )
    model_dropdown = gr.Dropdown(
        choices=[
            MODEL_GPT_4O_MINI,
            MODEL_OLLAMA_LLAMA3_2_3B
        ],
        label="Model",
        value=MODEL_GPT_4O_MINI,
    )

    message_output = gr.Markdown(label="Response:")

    view = gr.Interface(
        fn=get_streaming_completion,
        title="Simple Chat", 
        inputs=[message_input, model_dropdown], 
        outputs=[message_output], 
        examples=[
            ["What is an LLM", MODEL_GPT_4O_MINI],
            ["What is Transformer architecture", MODEL_OLLAMA_LLAMA3_2_3B]
        ], 
        flagging_mode="never"
    )
    view.launch()

