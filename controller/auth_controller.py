from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from infra.db import get_session
from repository.user_repository import UserRepository
from model.user_model import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

class AuthController():

    def __init__(self, db: AsyncSession = Depends(get_session)) -> None:
        super().__init__()
        self.user_repo = UserRepository(db)
    
    async def create_user(self, new_user: User.Model) -> User.Model:
        new_user.password = get_password_hash(new_user.password)
        await self.user_repo.add_user(new_user)
        return new_user
    
    async def login_user(self, email, password):
        user = await self.user_repo.get_user_by_email(email)
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        return user
    

