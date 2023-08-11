from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from infra.db import get_session
from repository.product_repository import ProductRepository
from model.product_model import Product

class ProductController():

    def __init__(self, db: AsyncSession = Depends(get_session)) -> None:
        super().__init__()
        self.product_repo = ProductRepository(db)
    
    async def create_product(self, new_product: Product.Model) -> Product.Model:
        #TODO: Vérifier si les champs sont correctes
        await self.product_repo.add_product(new_product) 
        return new_product
    
    async def get_products(self):
        return await self.product_repo.get_all()
    
    async def get_product_by_id(self, product_id):
        return await self.product_repo.get_product_by_id(product_id)