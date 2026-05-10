from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from database import get_session
from models_a import Product, ProductCreate, ProductUpdate

router = APIRouter(prefix="/products", tags=["Products"])

# GET /products
# Lista svih proizvoda + filter po kategoriji
@router.get("/")
def get_products(
    category:str = None,
    session: Session = Depends(get_session)
):
    statement = select(Product)
    if category:
        statement = statement.where(Product.category == category)
    products = session.exec(statement).all()
    return products

# GET /products/{id}
# Dohvati proizvod po ID-u
@router.get("/{product_id}")
def get_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


