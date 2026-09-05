import base64
from io import BytesIO
from PIL import Image
from litellm import image_generation

from llm_practice.constants.models import MODEL_FLUX_2_KLIEN_4B, MODEL_GPT_IMAGE_1_MINI


DEFAULT_PROMPT = "A class of students learning AI engineering in a vibrant pop-art style"

def text_to_image(prompt: str | None = None):
    prompt = prompt or DEFAULT_PROMPT
    response = image_generation(
        model=MODEL_GPT_IMAGE_1_MINI,
        prompt=prompt,
        size="1024x1024",
    )

    image_base64 = response.data[0].b64_json
    image_data = base64.b64decode(image_base64)

    return Image.open(BytesIO(image_data))