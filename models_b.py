from sqlmodel import SQLModel, Field
from typing import Optional
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Supplier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    name: str # Naziv dobavljača
    email: str # Email adresa
    phone_number: str # Broj telefona kao string
    min_order_amount: int # Minimalni iznos narudžbe
    reliability_score: float # Ocjena pouzdanosti
    is_active: bool = True # Da li je dobavljač aktivan
    supports_return: bool = False # Da li podržava povrat robe
    
    last_delivery_date: Optional[datetime] = None # Datum zadnje isporuke
    discount_rate: Optional[float] = None # Stopa popusta (ako postoji)


class SupplierCreate(SQLModel):
    name: str
    email: str
    phone_number: str
    min_order_amount: int
    reliability_score: float
    is_active: bool = True
    supports_return: bool = False
    last_delivery_date: Optional[datetime] = None
    discount_rate: Optional[float] = None