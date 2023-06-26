from pydantic import BaseModel


class UserSchema(BaseModel):
    pass


class Register(BaseModel):
    name: str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str