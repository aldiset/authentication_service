from jose import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer

security = HTTPBearer()
secret_key = "your-secret-key"
algorithm = "HS256"

def verify_token(token: str = Depends(security)):
    try:
        return jwt.decode(token=token, key=secret_key, algorithms=[algorithm])
    except jwt.JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
