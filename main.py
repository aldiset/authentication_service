from uvicorn import run
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.routes.auth import router as auth
from app.routes.role import router as role
from app.routes.user_role import router as user_role
from app.routes.permission import router as permission
from app.routes.role_permission import router as role_permission

app = FastAPI(title="Authentication Service")
app.include_router(router=role, prefix="/role", tags=["Role"])
app.include_router(router=auth, prefix="/auth", tags=["Authentication"])
app.include_router(router=user_role, prefix="/user-role", tags=["User Role"])
app.include_router(router=permission, prefix="/permission", tags=["Permission"])
app.include_router(router=role_permission, prefix="/role-permission", tags=["Role Permission"])


@app.get("/")
async def read_items():
    return HTMLResponse(content='<a href="/docs"> clickMe! </a>')


if __name__=='__main__':
    run(app=app)