from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.schema.user import Register
from app.database.object import ObjectUser
from app.security.authentication import TokenManager
from app.database.object import Authentication

router = APIRouter()

@router.post("/me")
async def me(credential: str = Depends(TokenManager.verify_token)):
    user = await ObjectUser.get_user_by_id(id=credential.get("user_id"))
    return JSONResponse(content={"message":"success", "data":user}, status_code=status.HTTP_200_OK)

@router.post("/login")
async def login(email: str, password: str):
    user = await Authentication.authenticate(email=email, password=password)
    token = await TokenManager.create_token(user_id=user.id)
    return JSONResponse(content={"message":"success", "token":token}, status_code=status.HTTP_200_OK)

@router.post("/secret")
async def secret(credential: str = Depends(TokenManager.verify_token)):
    return JSONResponse(content={"message":"success"})

@router.post("/logout")
async def logout(credentials: str = Depends(TokenManager.logout)):
    # Implementation for logout route
    return JSONResponse(content={"message":"success"}, status_code=status.HTTP_200_OK)

@router.post("/register")
async def register(data: Register):
    return await ObjectUser.create_user(data=data)