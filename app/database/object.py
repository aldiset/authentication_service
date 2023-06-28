from fastapi import HTTPException, status

from app.schema.user import Register
from app.database.connect import session
from app.schema.invalid_token import BlacklistToken
from app.database.crud import CRUD, CRUDUser, CRUDInvalidToken
from app.database.models import User, Role, Permission, InvalidToken
from app.security.password_hasher import PasswordHasher

class Authentication:
    crud = CRUDUser(db=session, model=User)
    
    @classmethod
    async def authenticate(cls, email: str, password: str):
        user = cls.crud.get_by_email(email=email)
        if not user or not PasswordHasher.validate_password(password=password, hashed_password=user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid email or password")
        return user


class ObjectUser:
    crud = CRUDUser(db=session, model=User)

    @classmethod
    async def create_user(cls, data: Register):
        return await cls.crud.create(data)
    

class ObjectInvalidToken:
    crud = CRUDInvalidToken(db=session, model=InvalidToken)

    @classmethod
    async def is_invalid(cls, token: str):
        return await cls.crud.get_by_token(token=token)
    
    @classmethod
    async def blacklist_token(cls, data: BlacklistToken):
        return await cls.crud.create(data)