from pydantic import BaseModel

class ImageAnalysis(BaseModel):

    filename:str

    description:str

    emotion:str

    importance:int

    people:int