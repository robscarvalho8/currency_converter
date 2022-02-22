from datetime import date
from sql_app.models import Base, Currency
from sql_app.database import Session, engine

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def create_currency():
    DATA_COIN = [
        {"name": "Dolar", "abbreviated": "USD", "dolar_quotation": 1.0, "date_quotation": date(2022, 2, 20)},
        {"name": "Real", "abbreviated": "BRL", "dolar_quotation": 5.0988, "date_quotation": date(2022, 2, 20)},
        {"name": "Euro", "abbreviated": "EUR", "dolar_quotation": 0.8837, "date_quotation": date(2022, 2, 20)},
        {"name": "Bitcoin", "abbreviated": "BTC", "dolar_quotation": 0.0000261, "date_quotation": date(2022, 2, 20)},
        {"name": "Ethereum", "abbreviated": "ETH", "dolar_quotation": 0.000381, "date_quotation": date(2022, 2, 20)}
    ]
    db = Session()
    for coin in DATA_COIN:
        db_coin = Currency(**coin)
        db.add(db_coin)
        db.commit()
    db.close()


if __name__ == "__main__":
    create_currency()
