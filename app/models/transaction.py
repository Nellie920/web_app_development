from app.database import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transaction'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50), nullable=False) # 'income' or 'expense'
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, type, amount, category, date, description=None):
        """
        新增一筆紀錄
        :param type: 'income' 或 'expense'
        :param amount: 金額
        :param category: 分類
        :param date: 日期
        :param description: 說明
        """
        try:
            new_tx = cls(
                type=type, 
                amount=amount, 
                category=category, 
                date=date, 
                description=description
            )
            db.session.add(new_tx)
            db.session.commit()
            return new_tx
        except Exception as e:
            db.session.rollback()
            print(f"Error creating transaction: {e}")
            raise

    @classmethod
    def get_all(cls):
        """取得所有記錄"""
        try:
            return cls.query.order_by(cls.date.desc()).all()
        except Exception as e:
            print(f"Error getting all transactions: {e}")
            return []

    @classmethod
    def get_by_id(cls, tx_id):
        """根據 ID 取得單筆記錄"""
        try:
            return cls.query.get(tx_id)
        except Exception as e:
            print(f"Error getting transaction by id: {e}")
            return None

    def update(self, **kwargs):
        """更新記錄"""
        try:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            print(f"Error updating transaction: {e}")
            raise

    def delete(self):
        """刪除記錄"""
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting transaction: {e}")
            raise
