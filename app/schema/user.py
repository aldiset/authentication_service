from pydantic import BaseModel, EmailStr

from app.utils.email_validation import EmailValidator


class UserSchema(BaseModel):
    pass


class Register(BaseModel):
    name: str
    email: EmailStr
    password: str


class Login(BaseModel):
    email: str
    password: str