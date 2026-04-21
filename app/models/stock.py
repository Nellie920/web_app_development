from app.database import db
from datetime import datetime

class StockTransaction(db.Model):
    __tablename__ = 'stock_transaction'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_symbol = db.Column(db.String(20), nullable=False)
    trade_type = db.Column(db.String(50), nullable=False) # 'buy' or 'sell'
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    trade_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, stock_symbol, trade_type, price, quantity, trade_date):
        new_st = cls(
            stock_symbol=stock_symbol,
            trade_type=trade_type,
            price=price,
            quantity=quantity,
            trade_date=trade_date
        )
        db.session.add(new_st)
        db.session.commit()
        return new_st

    @classmethod
    def get_all(cls):
        return cls.query.order_by(cls.trade_date.desc()).all()

    @classmethod
    def get_by_id(cls, st_id):
        return cls.query.get(st_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
