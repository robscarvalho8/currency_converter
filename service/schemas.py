from datetime import date

from pydantic import BaseModel


class CurrencyOutput(BaseModel):
    name: str
    abbreviated: str
    amount: float
    date_quotation: date


class ErrorOutput(BaseModel):
    error: dict
