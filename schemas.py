from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    Name: str
    Category: str
    Description: Optional[str]
    ProductImage: Optional[str]
    SKU: str
    UnitOfMeasure: str
    LeadTime: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    ProductID: int
    CreatedDate: datetime
    UpdatedDate: datetime

    class Config:
        from_attributes = True  # Replace orm_mode with from_attributes
