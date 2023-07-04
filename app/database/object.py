from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.schema.user import Register
from app.schema.permission import PermissionSchema
from app.database.connect import session
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
        return await cls.crud.create(jsonable_encoder(data))
    

class ObjectInvalidToken:
    crud = CRUDInvalidToken(db=session, model=InvalidToken)

    @classmethod
    async def is_invalid(cls, token: str):
        return await cls.crud.get_by_token(token=token)
    
    @classmethod
    async def blacklist_token(cls, token: str):
        return await cls.crud.create({"token":token})


class Object:
    def __init__(self, model) -> None:
        self.crud = CRUD(db=session, model=model)
    
    async def get_all(self, *args, limit: int = None, offset: int = None):
        return await self.crud.get_all(*args, limit=limit, offset=offset)
    
    async def get_by_id(self, id: int):
        return await self.crud.get(id=id)
    
    async def create(self, data: dict):
        return self.crud.create(obj_in=data)

    async def update(self, id: int, data: dict):
        permission = await self.crud.get(id=id)
        return await self.crud.update(permission, jsonable_encoder(data))

    
    async def delete(self, id: int):
        permission = await self.crud.get(id=id)
        return await self.crud.delete(permission)