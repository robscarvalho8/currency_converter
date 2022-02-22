from sql_app.models import Currency
from sql_app.database import Session


class CurrencyConvertService():
    def __init__( self, db: Session, coin_from: str, coin_to: str, amount: float ):
        self.db = db
        self.__coin_from = coin_from
        self.__coin_to = coin_to
        self.__convert_from = ""
        self.__convert_to = ""
        self.__amount_from = amount
        self.__amount_to = ""
        self.error = []
        self.start()

    def start( self ):
        self.get_convert_from()
        self.get_convert_to()
        if not self.error:
            self.convert_amount()

    @property
    def coin_from( self ):
        return self.__coin_from

    @property
    def coin_to( self ):
        return self.__coin_to

    @property
    def convert_from( self ):
        return self.__convert_from

    @convert_from.setter
    def convert_from( self, value ):
        self.__convert_from = value

    @property
    def convert_to( self ):
        return self.__convert_to

    @convert_to.setter
    def convert_to( self, value ):
        self.__convert_to = value

    @property
    def amount_from( self ):
        return self.__amount_from

    @amount_from.setter
    def amount_from( self, value ):
        self.__amount_from = value

    @property
    def amount_to( self ):
        return self.__amount_to

    @amount_to.setter
    def amount_to( self, value ):
        self.__amount_to = value

    def get_convert_from( self ):
        self.convert_from = self.db.query(Currency).filter(Currency.abbreviated == self.coin_from).first()
        if not self.convert_from:
            return self.error.append({"detail": f"{self.coin_from} is not a valid coin."})

    def get_convert_to( self ):
        self.convert_to = self.db.query(Currency).filter(Currency.abbreviated == self.coin_to).first()
        if not self.convert_to:
            return self.error.append({"detail": f"{self.coin_to} is not a valid coin."})

    def convert_amount( self ):
        if not self.amount_from:
            return self.error.append({"detail": f"Amount is required."})
        else:
            self.amount_to = round(
                (self.amount_from / self.convert_from.dolar_quotation) * self.convert_to.dolar_quotation, 8)

