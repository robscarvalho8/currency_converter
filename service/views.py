from fastapi import Depends, HTTPException, APIRouter
from database import Session
from schemas import ErrorOutput, CurrencyOutput
from validator import CurrencyConvertService

converter_router = APIRouter(prefix='/converter')


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@converter_router.get("", response_model=CurrencyOutput,
                      responses={400: {'model': ErrorOutput}})
def converter(db: Session = Depends(get_db),
              coin_from: str = None, coin_to: str = None,
              amount: float = None):
    currency = CurrencyConvertService(db=db, coin_from=coin_from,
                                      coin_to=coin_to, amount=amount)
    try:
        return CurrencyOutput(name=currency.convert_to.name,
                              abbreviated=currency.convert_to.abbreviated,
                              amount=currency.amount_to,
                              date_quotation=currency.convert_to.date_quotation
                              )
    except Exception:
        raise HTTPException(400, currency.error)
