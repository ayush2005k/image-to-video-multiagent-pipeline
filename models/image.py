from pydantic import BaseModel, Field


class ImageAnalysis(BaseModel):

    filename: str

    description: str

    emotion: str

    scene_type: str

    people_count: int = Field(ge=0)

    importance: int = Field(
        ge=1,
        le=10
    )