from fastapi import FastAPI
from infra.db import get_session
from router.auth_router import router as auth_router # TODO: update that
from router.product_router import router as product_router
from router.admin_router import router as admin_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(product_router, prefix="/product")
app.include_router(admin_router, prefix="/admin")

@app.get("/")
def hello_world():
    return "Hello world!"

