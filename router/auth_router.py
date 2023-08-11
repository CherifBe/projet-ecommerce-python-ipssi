from fastapi import APIRouter, Depends, Request
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