from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Depends
from infra.db import get_session
from model import User

class UserRepository():

    def __init__(self, db: AsyncSession = Depends(get_session)) -> None:
        super().__init__()
        self.db = db

    async def add_user(self, user: User.Model):
        new_user = User()
        new_user.firstname = user.firstname
        new_user.lastname = user.lastname
        new_user.email = user.email
        new_user.password = user.password
        self.db.add(new_user)
        await self.db.commit()
        return new_user

    async def get_user_by_id(self, id):
        query = select(User).where(User.id == id)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def get_all(self):
        query = select(User)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def update_user(self, id, updated_user: User):
        user: User
        user = await self.get_user_by_id(id)
        user.firstname = updated_user.firstname
        user.lastname = updated_user.lastname
        user.email = updated_user.email
        user.password = updated_user.password
        await self.db.commit()
        return user