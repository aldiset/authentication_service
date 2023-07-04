from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.database.object import Object
from app.database.models import Role
from app.schema.role import RoleSchema
from app.security.authentication import TokenManager

router = APIRouter()
objects = Object(model=Role)

@router.get("/")
async def get_all(
        limit: int = None,
        offset: int = None,
        credentials: str = Depends(TokenManager.verify_token)
    ):
    filters = []
    data = await objects.get_all(*filters, limit=limit, offset=offset)
    return JSONResponse(content={"message":"success","data":data}, status_code=status.HTTP_200_OK)@router.get("/")

@router.get("/{id}")
async def get_detail(id: int, credentials: str = Depends(TokenManager.verify_token)):
    data = await objects.get_by_id(id=id)
    return JSONResponse(content={"message":"success","data":data}, status_code=status.HTTP_200_OK)

@router.post("/")
async def create_role(data: RoleSchema, credentials: str = Depends(TokenManager.verify_token)):
    data = await objects.create(data=data.dict())
    return JSONResponse(content={"message":"success","data":data}, status_code=status.HTTP_201_CREATED)

@router.put("/{id}")
async def update_role(id: int, data: RoleSchema, credentials: str = Depends(TokenManager.verify_token)):
    data = await objects.update(id=id, data=data.dict())
    return JSONResponse(content={"message":"success","data":data}, status_code=status.HTTP_200_OK)

@router.delete("/{id}")
async def delete_role(id: int, data: RoleSchema, credentials: str = Depends(TokenManager.verify_token)):
    data = await objects.delete(id=id)
    return JSONResponse(content={"message":"success","data":data}, status_code=status.HTTP_200_OK)