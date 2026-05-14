from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator

#Model proizvoda koji predstavlja tabelu u bazi podataka
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: str
    quantity: int
    price: float
    available: bool
    supplier_id: int

#Model za kreiranje proizvoda   
class ProductCreate(SQLModel):
    name: str
    category: str
    quantity: int
    price: float
    available: bool
    supplier_id: int
    @field_validator("name")
    @classmethod
    def naziv_ne_smije_biti_prazan(cls,v):
        if not v.strip():
            raise ValueError("Naziv proizvoda ne smije biti prazan")
        return v.strip() 
    @field_validator("quantity")
    @classmethod 
    def kolicina_mora_biti_pozitivna(cls,v):
        if v<=0:
            raise ValueError("Kolicina mora biti veca od nule")
        return v
    
#Model za ažuriranje proizvoda
class ProductUpdate(SQLModel):
    name: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    available: Optional[bool] = None
    supplier_id: Optional[int] = None

