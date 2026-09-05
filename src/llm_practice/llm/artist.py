import base64
from io import BytesIO
from PIL import Image
from litellm import image_generation

from llm_practice.constants.models import MODEL_GPT_IMAGE_1_MINI


def artist(city: str):
    response = image_generation(
        model=MODEL_GPT_IMAGE_1_MINI,
        prompt=(
            f"An image representing a vacation in {city}, "
            "showing tourist spots and everything unique about "
            f"{city}, in a vibrant pop-art style"
        ),
        size="1024x1024",
    )

    image_base64 = response.data[0].b64_json
    image_data = base64.b64decode(image_base64)

    return Image.open(BytesIO(image_data))