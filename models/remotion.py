from pydantic import BaseModel


class RemotionScript(BaseModel):

    filename: str

    path: str

    code: str