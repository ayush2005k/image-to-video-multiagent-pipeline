import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    RETRY_LIMIT = 3

    CHROMA_PATH = "./chroma_db"

    IMAGE_FOLDER = "./assets"

    OUTPUT_FOLDER = "./sample_output"

settings = Settings()