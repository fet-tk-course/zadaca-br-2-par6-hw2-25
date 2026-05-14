from sqlmodel import SQLModel, Field
from typing import Optional
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from pydantic import field_validator


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

    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError('Naziv dobavljača ne može biti prazan')
        return value.strip()


    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Neispravan email format')
            return value.strip()


    @field_validator('phone_number')
    @classmethod
    def validate_phone_number(cls, value):
        if not value.strip():
            raise ValueError('Broj telefona ne može biti prazan')
        return value.strip()


    @field_validator('min_order_amount')    
    @classmethod
    def validate_min_order_amount(cls, value):
        if value <= 0:
            raise ValueError('Minimalni iznos narudžbe ne može biti negativan')
        return value


    @field_validator('reliability_score')
    @classmethod
    def validate_reliability_score(cls, value):
        if not (0 <= value <= 5):
            raise ValueError('Ocjena pouzdanosti mora biti između 0 i 5')
        return value
    

    @field_validator('is_active')
    @classmethod
    def validate_is_active(cls, value):
        if not isinstance(value, bool):
            raise ValueError('is_active mora biti boolean vrijednost')
        return value
    

    @field_validator('supports_return')
    @classmethod
    def validate_supports_return(cls, value):
        if not isinstance(value, bool):
            raise ValueError('supports_return mora biti boolean vrijednost')
        return value


    @field_validator('last_delivery_date')
    @classmethod
    def validate_last_delivery_date(cls, value):
        if value is not None and value > datetime.now():
            raise ValueError('Datum zadnje isporuke ne može biti u budućnosti')
        return value


    @field_validator('discount_rate')
    @classmethod
    def validate_discount_rate(cls, value):
        if value is not None and not (0 <= value <= 100):
            raise ValueError('Stopa popusta mora biti između 0 i 100')
        return value
    

    


class SupplierUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    min_order_amount: Optional[int] = None
    reliability_score: Optional[float] = None
    is_active: Optional[bool] = None
    supports_return: Optional[bool] = None
    last_delivery_date: Optional[datetime] = None
    discount_rate: Optional[float] = None