from flask import Blueprint, render_template
from app.models.transaction import Transaction

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    """首頁儀表板"""
    transactions = Transaction.get_all()
    
    # Calculate totals
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expense = sum(t.amount for t in transactions if t.type == 'expense')
    balance = total_income - total_expense

    return render_template('index.html', 
                           transactions=transactions, 
                           total_income=total_income,
                           total_expense=total_expense,
                           balance=balance)
