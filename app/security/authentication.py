from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


class TokenManager:
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf73b88e8d3e6"  # Just Example
    ALGORITHM = "HS256"
    EXPIRATION_TIME = timedelta(minutes=30)

    @classmethod
    async def create_token(cls, user_id: int):
        now = datetime.utcnow()
        payload = {
            "user_id": user_id,
            "iat": now,
            "exp": now + cls.EXPIRATION_TIME
        }
        token = jwt.encode(payload, cls.SECRET_KEY, algorithm=cls.ALGORITHM)
        return token

    @classmethod
    async def verify_token(cls, token: HTTPAuthorizationCredentials = Depends(security)):
        try:
            return jwt.decode(token.credentials, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])
        except:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
