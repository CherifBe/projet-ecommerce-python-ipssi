from datetime import datetime
from typing import Dict, List, Optional
from xmlrpc.client import boolean

import sqlalchemy as sa
from pydantic.main import BaseModel
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import text
from sqlalchemy.orm import relationship
from infra.db import Base

class BaseModeledMixin:
    class Model(BaseModel):
        id: Optional[int]

    class Config:
        orm_mode = True

    def serialize(self):
        return self.to_model().dict()

    def to_model(self):
        return self.Model.from_orm(self)

class User(BaseModeledMixin, Base):
    __tablename__ = "user"

    def __repr__(self):
        return f"{self.username}>"

    class Model(BaseModel):
        id: Optional[int]
        firstname: str
        lastname: str
        email: str
        password: str

        class Config:
            orm_mode = True

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    firstname = sa.Column(sa.String(length=60), nullable=False)
    lastname = sa.Column(sa.String(length=60), nullable=False)
    email = sa.Column(sa.String(length=255), nullable=False)
    password = sa.Column(sa.String(length=255), nullable=False) #TODO: Don't forget to hash password
