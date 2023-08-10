from fastapi import APIRouter, Depends
from repository.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from infra.db import get_session
import json
from model.user_model import User
# TODO: APPELER CONTROLLER A LA PLACE DE REPOSITORY

router = APIRouter()

@router.get("/", tags=["users"])
async def read_users(db: AsyncSession = Depends(get_session)):
    user_repo = UserRepository(db)
    return await user_repo.get_all()

@router.post("/")
async def create_user(new_user: User.Model, db: AsyncSession = Depends(get_session)) -> User.Model:
    user_repo = UserRepository(db)
    await user_repo.add_user(new_user)
    return new_user