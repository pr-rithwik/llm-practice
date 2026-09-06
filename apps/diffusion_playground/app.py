import gradio as gr

from apps.diffusion_playground.diffusion import (
    generate_turbo,
    generate_sdxl,
    generate_sdxl_refined
)


SDXL_TURBO = "SDXL Turbo"
SDXL_BASE = "SDXL Base"
SDXL_BASE_REFINED = "SDXL Base + Refined"


def get_image(radio, prompt):
    if radio == SDXL_TURBO:
        image = generate_turbo(prompt)

    elif radio == SDXL_BASE:
        image = generate_sdxl(prompt)

    elif radio == SDXL_BASE_REFINED:
        image = generate_sdxl_refined(prompt)

    return image, prompt, ""


def main():
    with gr.Blocks() as ui:
        message = gr.TextBox(
            label="Description of Image",
            submit_btn=True
        )

        image_output = gr.Image(
            height=500,
            interactive=False
        )

        radio = gr.Radio(
            choices=[
                SDXL_TURBO,
                SDXL_BASE,
                SDXL_BASE_REFINED
            ],
            value=SDXL_TURBO,
            label="Choose an option",
        )

        submit_btn = gr.Button("Submit Selection")

        output = gr.Textbox(label="Output")

        submit_btn.click(
            fn=get_image,
            inputs=[radio, message],
            outputs=[image_output, output, message],
        )

    ui.launch()


if __name__ == "__main__":
    main()