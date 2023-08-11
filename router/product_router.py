from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from infra.db import get_session
from model.product_model import Product
from controller.product_controller import ProductController

router = APIRouter()
views = Jinja2Templates(directory="view/")

@router.get("/", tags=["products"])
async def display_products(request: Request, db: AsyncSession = Depends(get_session)):
    product_controller = ProductController(db)
    return views.TemplateResponse('products.html.j2', context={'request': request, 'products': await product_controller.get_products()})

@router.post("/")
async def create_product(new_product: Product.Model = Depends(Product.Model.as_form), db: AsyncSession = Depends(get_session)) -> Product.Model:
    product_controller = ProductController(db)
    return await product_controller.create_product(new_product)

@router.get("/{product_id}")
async def display_details(product_id, request: Request, db: AsyncSession = Depends(get_session)):
    product_controller = ProductController(db)
    return views.TemplateResponse('product.html.j2', context={'request': request, 'product': await product_controller.get_product_by_id(product_id)})