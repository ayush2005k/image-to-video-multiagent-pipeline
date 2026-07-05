from typing import Literal
from pydantic import BaseModel


class VideoIntent(BaseModel):
    pacing: Literal["slow", "medium", "fast"]

    visual_style: Literal[
        "cinematic",
        "upbeat",
        "corporate",
        "modern",
        "luxury",
        "documentary"
    ]

    caption_tone: Literal[
        "minimal",
        "bold",
        "emotional",
        "professional"
    ]

    transition_style: Literal[
        "fade",
        "cut",
        "zoom",
        "crossfade",
        "slide"
    ]