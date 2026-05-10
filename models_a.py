from sqlmodel import SQLModel, Field
from typing import Optional

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: str
    quantity: int
    price: float
    available: bool
    supplier_id: int
    
class ProductCreate(SQLModel):
    name: str
    category: str
    quantity: int
    price: float
    available: bool
    supplier_id: int
    
class ProductUpdate(SQLModel):
    name: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    available: Optional[bool] = None
    supplier_id: Optional[int] = None

