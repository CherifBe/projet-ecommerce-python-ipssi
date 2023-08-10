from fastapi import APIRouter
from repository.user_repository import UserRepository 
# TODO: APPELER CONTROLLER A LA PLACE DE REPOSITORY

router = APIRouter()

@router.get("/", tags=["users"])
async def read_users():
    return UserRepository.get_all()