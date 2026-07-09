from pydantic import BaseModel, Field


class StoryboardScene(BaseModel):

    image: str

    start_time: float = Field(ge=0)

    duration: float = Field(gt=0)

    caption: str

    transition: str

    reason: str


class Storyboard(BaseModel):

    title: str

    total_duration: float

    scenes: list[StoryboardScene]