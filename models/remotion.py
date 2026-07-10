from pydantic import BaseModel


class RemotionScript(BaseModel):

    filename: str

    code: str