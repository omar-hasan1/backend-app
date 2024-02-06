from pydantic import BaseModel

class User(BaseModel):
    username: str
    phone_number: str
