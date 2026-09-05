import gradio as gr
from llm_practice.llm.text_to_image import text_to_image


def generate_image(message, history):
    image = text_to_image(prompt=message)
    history = history or []
    return history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": gr.Image(value=image)},
    ]


def main():
    with gr.Blocks() as ui:
        chatbot = gr.Chatbot(height=500)
        
        message = gr.Textbox(
            label="Your message:", 
            info="Give image description", 
            submit_btn=True
        )
        message.submit(
            generate_image, inputs=[message, chatbot], outputs=[chatbot]
        ).then(
            lambda: "", outputs=message
        )
    
    ui.launch()
