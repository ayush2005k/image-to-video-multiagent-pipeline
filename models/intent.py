from pydantic import BaseModel

class VideoIntent(BaseModel):

    pacing:str

    visual_style:str

    caption_tone:str

    transition_style:str