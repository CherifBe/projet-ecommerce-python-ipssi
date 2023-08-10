from fastapi import FastAPI
from infra.db import get_session
from router.auth_router import router as auth_router # TODO: update that

app = FastAPI()

app.include_router(auth_router, prefix="/auth")

@app.get("/")
def hello_world():
    return "Hello world!"

