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

# GET /products/count
# Vraca ukupan broj podataka
@router.get("/count")
def count_products(
    session: Session=Depends(get_session)
):
    products=session.exec(select(Product)).all()
    return {
        "ukupno proizvoda":len(products)
    }
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

#POST /products
# Kreiraj novog proizvod
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_product(
    product_data: ProductCreate,
    session: Session = Depends(get_session)
):
    existing_field=session.exec(select(Product).where(Product.name==product_data.name)).first()
    if existing_field:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product with this id already exists")
    product=Product(**product_data.model_dump())
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

#PUT /products/{id}
# Ažuriraj postojeći proizvod
@router.put("/{product_id}")
def update_product(
    product_id: int,
    product_data: ProductCreate,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    for key, value in product_data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

#PATCH /products/{id}
# Ažuriraj postojeći proizvod (djelomično)
@router.patch("/{product_id}")
def patch_product(
    product_id: int,
    product_data: ProductUpdate,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    for key, value in product_data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

#DELETE /products/{id}
# Obriši proizvod po ID-u
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    session.delete(product)
    session.commit()
    return None