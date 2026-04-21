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
        """
        新增一筆股票記錄
        :param stock_symbol: 股票代號
        :param trade_type: 交易類型 ('buy' 或 'sell')
        :param price: 單價
        :param quantity: 股數
        :param trade_date: 交易日期
        """
        try:
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
        except Exception as e:
            db.session.rollback()
            print(f"Error creating stock transaction: {e}")
            raise

    @classmethod
    def get_all(cls):
        """取得所有股票記錄"""
        try:
            return cls.query.order_by(cls.trade_date.desc()).all()
        except Exception as e:
            print(f"Error getting all stock transactions: {e}")
            return []

    @classmethod
    def get_by_id(cls, st_id):
        """根據 ID 取得股票記錄"""
        try:
            return cls.query.get(st_id)
        except Exception as e:
            print(f"Error getting stock transaction by id: {e}")
            return None

    def update(self, **kwargs):
        """更新股票記錄"""
        try:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            print(f"Error updating stock transaction: {e}")
            raise

    def delete(self):
        """刪除股票記錄"""
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting stock transaction: {e}")
            raise
