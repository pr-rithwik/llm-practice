from litellm import speech
from llm_practice.constants.models import MODEL_GPT_4O_MINI_TTS


def talker(message: str):
    response = speech(
        model=MODEL_GPT_4O_MINI_TTS,
        voice="onyx",
        input=message,
    )

    return response.content