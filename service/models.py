from sqlalchemy import Column, Date, Integer, String, Float

from database import Base


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    abbreviated = Column(String)
    dolar_quotation = Column(Float)
    date_quotation = Column(Date)
