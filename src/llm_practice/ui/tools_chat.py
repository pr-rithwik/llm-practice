import gradio as gr
import json

from llm_practice.services.github_api import get_github_repo_stats
from llm_practice.llm.streaming import get_completion_response
from llm_practice.tools.github import github_repo_tool
from llm_practice.constants.models import MODEL_OLLAMA_LLAMA3_2_3B, MODEL_GPT_4O_MINI


SYSTEM_MESSAGE = "You are a helpful assistant, always answer in a crisp and short manner"


def get_tools():
    tools = [github_repo_tool]

    return tools


def handle_tool_calls(message):
    responses = []
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_github_repo_stats":
            arguments = json.loads(tool_call.function.arguments)
            github_url = arguments.get('repo_url')
            github_details = get_github_repo_stats(repo_url=github_url)
            responses.append({
                "role": "tool",
                "content": json.dumps(github_details),
                "tool_call_id": tool_call.id
            })
    return responses


def chat(message, history, model, system_message: str = None):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    system_message = system_message if system_message else SYSTEM_MESSAGE
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    tools = get_tools()
    response = get_completion_response(messages=messages, model=model, tools=tools, stream=False)

    while response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        messages.append(message)
        
        tool_responses = handle_tool_calls(message)
        messages.extend(tool_responses)
        response = get_completion_response(messages=messages, model=model, tools=tools, stream=False)
    
    return response.choices[0].message.content


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
        fn=chat,
        additional_inputs=[model_dropdown],
    )

    view.launch()