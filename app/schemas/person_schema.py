from pydantic import BaseModel

class PersonBase(BaseModel):
    id: int
    username: str
    email: str