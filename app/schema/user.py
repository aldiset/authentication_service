from datetime import date
from pydantic import BaseModel, EmailStr, validator

from app.security.password_hasher import PasswordHasher


class UserSchema(BaseModel):
    pass


class Register(BaseModel):
    name: str
    email: EmailStr
    password: str
    gender: str
    birth_of_day: date

    @validator("password")
    def password_validation(cls, value):
        return PasswordHasher.hash_password(password=value)

    @validator("gender")
    def gender_validation(cls, value):
        if value not in ["male", "female"]:
            raise ValueError("gender not valid")
        return value



class Login(BaseModel):
    email: str
    password: str