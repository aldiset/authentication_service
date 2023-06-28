from pydantic import BaseModel

class BlacklistToken(BaseModel):
    token: str