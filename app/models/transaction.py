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

    @classmethod
    def get_all(cls):
        return cls.query.order_by(cls.date.desc()).all()

    @classmethod
    def get_by_id(cls, tx_id):
        return cls.query.get(tx_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
