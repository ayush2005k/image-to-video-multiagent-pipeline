import json

from google import genai

from PIL import Image

from config import settings

client = genai.Client(
    api_key=settings.GOOGLE_API_KEY
)

image = Image.open("assets/IMG_0704.jpg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        image,
        """
Describe this image in one sentence.
"""
    ]
)

print(response.text)