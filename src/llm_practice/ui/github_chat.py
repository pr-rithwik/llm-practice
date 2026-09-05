import gradio as gr

from llm_practice.llm.streaming import get_completion_response
from llm_practice.tools.github import github_repo_tool
from llm_practice.constants.models import MODEL_GPT_4O_MINI, MODEL_OPEN_ROUTER_LLAMA_3_3_70B_INSTRUCT #, MODEL_OLLAMA_LLAMA3_2_3B, 
from llm_practice.tools.handle_tool_calls import handle_github_tool_calls


SYSTEM_MESSAGE = "You are a helpful assistant, always answer in a crisp and short manner"


def get_tools():
    tools = [github_repo_tool]

    return tools


def chat(message, history, model, system_message: str = None):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    system_message = system_message if system_message else SYSTEM_MESSAGE
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    tools = get_tools()
    response = get_completion_response(messages=messages, model=model, tools=tools, stream=False)

    counter = 0
    MAX_TOOL_CALLS = 5
    while response.choices[0].finish_reason=="tool_calls":
        counter += 1

        if counter > MAX_TOOL_CALLS:
            raise RuntimeError("Model exceeded maximum tool calls")
        
        message = response.choices[0].message
        messages.append(message)
        tool_responses = handle_github_tool_calls(message)

        messages.extend(tool_responses)
        response = get_completion_response(messages=messages, model=model, tools=tools, stream=False)
        
    return response.choices[0].message.content


def main():
    model_dropdown = gr.Dropdown(
        choices=[
            MODEL_GPT_4O_MINI,
            # MODEL_OLLAMA_LLAMA3_2_3B
            MODEL_OPEN_ROUTER_LLAMA_3_3_70B_INSTRUCT
        ],
        label="Model",
        value=MODEL_GPT_4O_MINI,
    )

    view = gr.ChatInterface(
        fn=chat,
        additional_inputs=[model_dropdown],
    )

    view.launch()