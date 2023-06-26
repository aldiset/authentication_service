from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_items():
    return "<h1>Hello World</h1>"