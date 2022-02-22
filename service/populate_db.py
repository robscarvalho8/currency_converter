from datetime import date
from models import Base, Currency
from database import Session, engine


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def create_currency():
    DATA_COIN = [
        {"name": "Dolar", "abbreviated": "USD", "dolar_quotation": 1.0,
         "date_quotation": date(2022, 2, 22)},
        {"name": "Real", "abbreviated": "BRL", "dolar_quotation": 5.1036,
         "date_quotation": date(2022, 2, 22)},
        {"name": "Euro", "abbreviated": "EUR", "dolar_quotation": 0.884,
         "date_quotation": date(2022, 2, 22)},
        {"name": "Bitcoin", "abbreviated": "BTC", "dolar_quotation": 0.0000270,
         "date_quotation": date(2022, 2, 22)},
        {"name": "Ethereum", "abbreviated": "ETH", "dolar_quotation": 0.000389,
         "date_quotation": date(2022, 2, 22)}
    ]
    db = Session()
    for coin in DATA_COIN:
        db_coin = Currency(**coin)
        db.add(db_coin)
        db.commit()
    db.close()


if __name__ == "__main__":
    create_currency()
