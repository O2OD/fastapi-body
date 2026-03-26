from typing import Annotated, Optional
from enum import Enum

from pydantic import BaseModel, Field


class Data(BaseModel):
    a: float
    b: float
    operator: str


class ProductStatus(str, Enum):
    new: str = 'yangi'
    old: str = 'eski'
 

class ProductCreate(BaseModel):
    name: Annotated[str, Field(min_length=5, max_length=128)]
    descriptioin: Optional[str] = None
    price: Annotated[float, Field(ge=0, lt=100_000_000)]
    stock: Annotated[int, Field(ge=1)]
    status: ProductStatus


class ProductUpdate(BaseModel):
    name: Annotated[str | None, Field(min_length=5, max_length=128)] = None
    descriptioin: Optional[str] = None
    price: Annotated[float | None, Field(ge=0, lt=100_000_000)] = None
    stock: Annotated[int | None, Field(ge=1)] = None
    status: Optional[ProductStatus] = None
    