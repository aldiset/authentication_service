from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.database.object import ObjectInvalidToken


security = HTTPBearer()


class TokenManager:
    SECRET_KEY = "e6fa79b6b8d2e1a87177d0e5bf9e7c83ea6106748b1b9d7253ac743c4bbc4e5c"  # Just Example
    ALGORITHM = "HS256"
    EXPIRATION_TIME = timedelta(minutes=30)
    NOW = datetime.utcnow()

    @classmethod
    async def create_token(cls, user_id: int, permissions: list = []):
        payload = {
            "user_id": user_id,
            "permissions": permissions,
            "iat": cls.NOW,
            "exp": cls.NOW + cls.EXPIRATION_TIME
        }
        token = jwt.encode(payload, cls.SECRET_KEY, algorithm=cls.ALGORITHM)
        return token

    @classmethod
    async def verify_token(cls, token: HTTPAuthorizationCredentials = Depends(security)):
        try:
            if await ObjectInvalidToken.is_invalid(token=token.credentials):
                raise
            return jwt.decode(token.credentials, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])
        except:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    @classmethod
    async def logout(cls, token: HTTPAuthorizationCredentials = Depends(security)):
        await cls.verify_token(token=token)
        return await ObjectInvalidToken.blacklist_token(token=token.credentials)