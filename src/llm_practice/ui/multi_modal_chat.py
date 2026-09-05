import gradio as gr

from llm_practice.tools.handle_tool_calls import handle_multi_modal_tool_calls
from llm_practice.llm.streaming import get_completion_response
from llm_practice.tools.artist import artist
from llm_practice.tools.talker import talker
from llm_practice.constants.models import MODEL_GPT_4O_MINI


SYSTEM_MESSAGE = "You are a helpful assistant, always answer in a crisp and short manner"

def put_message_in_chatbot(message, history):
    return "", history + [{"role":"user", "content":message}]


def chat(history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + history

    tools = [artist, talker]
    all_details = {}
    response = get_completion_response(
        messages=messages, model=MODEL_GPT_4O_MINI, tools=tools, stream=False
    )
    
    counter, MAX_TOOL_CALLS = 0, 5
    while response.choices[0].finish_reason=="tool_calls":
        counter += 1

        if counter > MAX_TOOL_CALLS:
            raise RuntimeError("Model exceeded maximum tool calls")
        message = response.choices[0].message
        messages.append(message)
        
        tool_responses, details = handle_multi_modal_tool_calls(message)
        all_details.update({k: v for k, v in details.items() if v is not None})
        
        messages.extend(tool_responses)
        response = get_completion_response(
            messages=messages, model=MODEL_GPT_4O_MINI, tools=tools, stream=False)
    
    reply = response.choices[0].message.content
    history += [{"role":"assistant", "content":reply}]

    voice = all_details.get("voice", None)
    image = all_details.get("image", None)
    
    return history, voice, image


def main():
    with gr.Blocks() as ui:
        with gr.Row():
            chatbot = gr.Chatbot(height=500)
            image_output = gr.Image(height=500, interactive=False)
        with gr.Row():
            audio_output = gr.Audio(autoplay=True)
        with gr.Row():
            message = gr.Textbox(label="Chat with our AI Assistant:")

        message.submit(
            put_message_in_chatbot, inputs=[message, chatbot], outputs=[message, chatbot]
        ).then(
            chat, inputs=chatbot, outputs=[chatbot, audio_output, image_output]
        ) # can i stack multiple thens - subsequent actions

    ui.launch()