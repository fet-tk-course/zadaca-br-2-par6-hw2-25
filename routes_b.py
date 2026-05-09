from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional
from database import get_session
from models_b import Supplier, SupplierCreate, SupplierUpdate

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.post("/", response_model=Supplier, status_code=status.HTTP_201_CREATED)
def create_supplier(supplier: SupplierCreate, session: Session = Depends(get_session)):
    # Kreiranje instance modela iz primljenih podataka
    db_supplier = Supplier.model_validate(supplier)
    session.add(db_supplier)
    session.commit()
    session.refresh(db_supplier)
    return db_supplier


@router.get("/", response_model=List[Supplier])
def read_suppliers(
    is_active: Optional[bool] = None, 
    session: Session = Depends(get_session)
):
    statement = select(Supplier)
    if is_active is not None:
        statement = statement.where(Supplier.is_active == is_active)
    
    results = session.exec(statement).all()
    return results