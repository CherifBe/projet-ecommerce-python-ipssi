from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from infra.db import get_session
from model.user_model import User
from controller.auth_controller import AuthController

router = APIRouter()
views = Jinja2Templates(directory="view/")

@router.get("/", tags=["authentication"])
async def display_form_signup(request: Request):
    return views.TemplateResponse('form_signup.html.j2', context={'request': request})

@router.post("/")
async def create_user(request: Request, new_user: User.Model = Depends(User.Model.as_form), db: AsyncSession = Depends(get_session)) -> User.Model:
    auth_controller = AuthController(db)
    await auth_controller.create_user(new_user)
    return views.TemplateResponse('form_login.html.j2', context={'request': request})

@router.get("/login")
async def display_form_login(request: Request):
    return views.TemplateResponse('form_login.html.j2', context={'request': request})

@router.post("/login")
async def login_user(email: str = Form(), password: str = Form(), db: AsyncSession = Depends(get_session)):
    auth_controller = AuthController(db)
    return await auth_controller.login_user(email, password)

@router.post('/delete/{user_id}', tags=["delete_user"])
async def delete_user(user_id, db: AsyncSession = Depends(get_session)):
    auth_controller = AuthController(db)
    return await auth_controller.delete_user(user_id)
