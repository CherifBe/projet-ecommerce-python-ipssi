from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from infra.db import get_session
from repository.user_repository import UserRepository
from model.user_model import User

class AuthController():

    def __init__(self, db: AsyncSession = Depends(get_session)) -> None:
        super().__init__()
        self.user_repo = UserRepository(db)
    
    async def create_user(self, new_user: User.Model) -> User.Model:
        await self.user_repo.add_user(new_user)
        return new_user
    
    async def login_user(self, email, password):
        user = await self.user_repo.get_user_by_email(email)
        if(user == None):
            return "une erreur, l'utilisateur n'existe pas"
        if(user.password != password):
            return "une erreur, les mots de passe ne correspondent pas"
        return user
    

