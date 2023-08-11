from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from infra.db import get_session
from model.user_model import User
from controller.auth_controller import AuthController
from controller.product_controller import ProductController

router = APIRouter()
views = Jinja2Templates(directory="view/")

@router.get("/", tags=["admin"])
async def display_administration(request: Request, db: AsyncSession = Depends(get_session)):
    auth_controller = AuthController(db)
    product_controller = ProductController(db)

    return views.TemplateResponse(
        'administration.html.j2', 
        context={'request': request, 
                 'users': await auth_controller.get_users(),
                 'products': await product_controller.get_products()
                 })

#@router.post("/")
#async def create_user(new_user: User.Model = Depends(User.Model.as_form), db: AsyncSession = Depends(get_session)) -> User.Model:
#    auth_controller = AuthController(db)
#    return await auth_controller.create_user(new_user)
