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


@router.get("/{supplier_id}", response_model=Supplier)
def read_supplier(supplier_id: int, session: Session = Depends(get_session)):
    supplier = session.get(Supplier, supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Dobavljač nije pronađen")
    return supplier


@router.patch("/{supplier_id}", response_model=Supplier)
def update_supplier(
    supplier_id: int, 
    supplier_data: SupplierUpdate, 
    session: Session = Depends(get_session)
):
    db_supplier = session.get(Supplier, supplier_id)
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Dobavljač nije pronađen")
    
    # Konverzija u rječnik uz ignorisanje polja koja nisu poslana
    data = supplier_data.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(db_supplier, key, value)
    
    session.add(db_supplier)
    session.commit()
    session.refresh(db_supplier)
    return db_supplier


@router.delete("/{supplier_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplier(supplier_id: int, session: Session = Depends(get_session)):
    supplier = session.get(Supplier, supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Dobavljač nije pronađen")
    
    session.delete(supplier)
    session.commit()
    return None