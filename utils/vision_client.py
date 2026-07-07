from google import genai

from config import settings

client = genai.Client(
    api_key=settings.GOOGLE_API_KEY
)