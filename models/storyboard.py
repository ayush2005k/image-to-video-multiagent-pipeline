from pydantic import BaseModel

class StoryboardScene(BaseModel):

    image:str

    duration:float

    caption:str

    transition:str