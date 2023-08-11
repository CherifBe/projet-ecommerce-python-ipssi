from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Depends
from infra.db import get_session
from model.product_model import Product

class ProductRepository():

    def __init__(self, db: AsyncSession = Depends(get_session)) -> None:
        super().__init__()
        self.db = db

    async def add_product(self, product: Product.Model):
        new_product = Product()
        new_product.name = product.name
        new_product.description = product.description
        new_product.image = product.image
        new_product.price = product.price
        new_product.stock = product.stock
        self.db.add(new_product)
        await self.db.commit()
        return new_product

    async def get_product_by_id(self, id):
        query = select(Product).where(Product.id == id)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def get_all(self):
        query = select(Product)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def update_product(self, id, updated_product: Product):
        product: Product
        product = await self.get_product_by_id(id)
        product.name = updated_product.name
        product.description = updated_product.description
        product.image = updated_product.image
        product.price = updated_product.price
        product.stock = updated_product.stock
        await self.db.commit()
        return product