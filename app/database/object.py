from fastapi import HTTPException, status

from app.database.connect import session
from app.database.crud import CRUD, CRUDUser
from app.database.models import User, Role, Permission
from app.security.password_hasher import PasswordHasher

class Authentication:
    crud = CRUDUser(db=session, model=User)
    
    @classmethod
    async def authenticate(cls, email: str, password: str):
        user = cls.crud.get_by_email(email=email)
        if not user or not PasswordHasher.validate_password(password=password, hashed_password=user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid email or password")
        return user