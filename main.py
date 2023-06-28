from uvicorn import run
from fastapi import FastAPI
from app.routes.auth import router as auth
from fastapi.responses import HTMLResponse

app = FastAPI(title="Authentication Service")
app.include_router(router=auth, prefix="/auth", tags=["Authentication"])


@app.get("/")
async def read_items():
    return HTMLResponse(content='<a href="/docs"> clickMe! </a>')


if __name__=='__main__':
    run(app=app)