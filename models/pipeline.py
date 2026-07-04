from pydantic import BaseModel

class CompileResult(BaseModel):

    success:bool

    error:str=""