from sqlalchemy import Column, String, BigInteger, Enum, Integer, Text, TIMESTAMP
from database import Base

class Product(Base):
    __tablename__ = "Product"

    ProductID = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    Category = Column(Enum('finished', 'semi-finished', 'raw'), nullable=False)
    Description = Column(String(250))
    ProductImage = Column(Text)
    SKU = Column(String(100), nullable=False)
    UnitOfMeasure = Column(Enum('mtr', 'mm', 'ltr', 'ml', 'cm', 'mg', 'gm', 'unit', 'pack'), nullable=False)
    LeadTime = Column(Integer, nullable=False)
    CreatedDate = Column(TIMESTAMP, nullable=False)
    UpdatedDate = Column(TIMESTAMP, nullable=False)
