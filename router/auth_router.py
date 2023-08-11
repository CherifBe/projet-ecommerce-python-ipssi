from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from repository.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from infra.db import get_session
import json
from model.user_model import User
# TODO: APPELER CONTROLLER A LA PLACE DE REPOSITORY

router = APIRouter()
views = Jinja2Templates(directory="view/")

#@router.get("/", tags=["users"])
#async def read_users(db: AsyncSession = Depends(get_session)):
#    user_repo = UserRepository(db)
#    return await user_repo.get_all()

@router.get("/", tags=["authentication"])
async def display_form_signup(request: Request):
    return views.TemplateResponse('form_signup.html.j2', context={'request': request})

@router.post("/")
async def create_user(new_user: User.Model = Depends(User.Model.as_form), db: AsyncSession = Depends(get_session)) -> User.Model:
    user_repo = UserRepository(db)
    await user_repo.add_user(new_user)
    return new_user

@router.get("/login")
async def display_form_login(request: Request):
    return views.TemplateResponse('form_login.html.j2', context={'request': request})

@router.post("/login")
async def login_user(email: str = Form(), password: str = Form(), db: AsyncSession = Depends(get_session)):
    user_repo = UserRepository(db)
    user = await user_repo.get_user_by_email(email)
    if(user == None):
        return "une erreur, l'utilisateur n'existe pas"
    if(user.password != password):
        return "une erreur, les mots de passe ne correspondent pas"
    return user