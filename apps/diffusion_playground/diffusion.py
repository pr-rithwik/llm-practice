from diffusers import AutoPipelineForText2Image, DiffusionPipeline
import torch


MODEL_SDXL_TURBO = "stabilityai/sdxl-turbo"
MODEL_SDXL_BASE = "stabilityai/stable-diffusion-xl-base-1.0"
MODEL_SDXL_REFINER = "stabilityai/stable-diffusion-xl-refiner-1.0"


turbo_pipe = None
base_pipe = None
refiner_pipe = None


def generate_turbo(prompt, num_inference_steps=4):
    global turbo_pipe

    if turbo_pipe is None:
        turbo_pipe = AutoPipelineForText2Image.from_pretrained(
            MODEL_SDXL_TURBO,
            variant="fp16",
            torch_dtype=torch.float16
        )
        turbo_pipe.enable_model_cpu_offload()

    image = turbo_pipe(
        prompt=prompt,
        num_inference_steps=num_inference_steps,
        guidance_scale=0.0
    ).images[0]

    return image


def generate_sdxl(prompt):
    global base_pipe

    if base_pipe is None:
        base_pipe = DiffusionPipeline.from_pretrained(
            MODEL_SDXL_BASE,
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
        )
        base_pipe.enable_model_cpu_offload()

    image = base_pipe(
        prompt=prompt,
        num_inference_steps=30
    ).images[0]

    return image


def generate_sdxl_refined(
    prompt,
    n_steps=40,
    high_noise_frac=0.8
):
    global base_pipe, refiner_pipe

    # Load base if necessary
    if base_pipe is None:
        base_pipe = DiffusionPipeline.from_pretrained(
            MODEL_SDXL_BASE,
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
        )
        base_pipe.enable_model_cpu_offload()

    # Load refiner if necessary
    if refiner_pipe is None:
        refiner_pipe = DiffusionPipeline.from_pretrained(
            MODEL_SDXL_REFINER,
            text_encoder_2=base_pipe.text_encoder_2,
            vae=base_pipe.vae,
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True,
        )
        refiner_pipe.enable_model_cpu_offload()

    latent = base_pipe(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_end=high_noise_frac,
        output_type="latent"
    ).images

    image = refiner_pipe(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_start=high_noise_frac,
        image=latent,
    ).images[0]

    return image