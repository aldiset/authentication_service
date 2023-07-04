from uvicorn import run
from fastapi import FastAPI
from app.routes.auth import router as auth
from app.routes.permission import router as permission
from app.routes.role import router as role
from app.routes.user_role import router as user_role
from fastapi.responses import HTMLResponse

app = FastAPI(title="Authentication Service")
app.include_router(router=auth, prefix="/auth", tags=["Authentication"])
app.include_router(router=permission, prefix="/permission", tags=["Permission"])
app.include_router(router=role, prefix="/role", tags=["Role"])
app.include_router(router=user_role, prefix="/user_role", tags=["User Role"])


@app.get("/")
async def read_items():
    return HTMLResponse(content='<a href="/docs"> clickMe! </a>')


if __name__=='__main__':
    run(app=app)