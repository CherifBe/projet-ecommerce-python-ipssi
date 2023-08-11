from typing import Optional

import sqlalchemy as sa
from pydantic.main import BaseModel
from infra.db import Base
from fastapi import Form
from typing import Type


class BaseModeledMixin:
    class Model(BaseModel):
        id: Optional[int]

    class Config:
        orm_mode = True

    def serialize(self):
        return self.to_model().dict()

    def to_model(self):
        return self.Model.from_orm(self)

class Product(BaseModeledMixin, Base):
    __tablename__ = "product"

    def __repr__(self):
        return f"{self.name}"

    class Model(BaseModel):
        name: str
        description: str
        image: str
        price: int
        stock: int

        class Config:
            orm_mode = True
        
        @classmethod
        def as_form(
            cls: Type[BaseModel],
            name: str = Form(), 
            description: str = Form(), 
            image: str = Form(),
            price: int = Form(),
            stock: int = Form()
            ):
            return cls(
                name = name,
                description = description,
                image = image,
                price = price,
                stock = stock
            )


    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(length=60), nullable=False)
    description = sa.Column(sa.String(length=255), nullable=False)
    image = sa.Column(sa.String(length=255), nullable=True)
    price = sa.Column(sa.Integer, nullable=False)
    stock = sa.Column(sa.Integer, nullable=False)