from pydantic import BaseModel


class Data(BaseModel):
    a: float
    b: float
    operator: str
    