import json

from google import genai

from PIL import Image


from config import settings

from prompts.vision_prompt import VISION_PROMPT

from models.image import ImageAnalysis


client = genai.Client(
    api_key=settings.GOOGLE_API_KEY
)


def analyze_image(image_path):
    
    from utils.image_utils import open_image

    image = Image.open(image_path)

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=[
            image,
            VISION_PROMPT
        ]

    )

    data = json.loads(response.text)

    data["filename"] = image_path.name

    data["emotion"] = data["emotion"].strip().lower()
    data["scene_type"] = data["scene_type"].strip().lower()

    return ImageAnalysis(**data)