from flask import Blueprint, request, redirect, url_for, render_template, flash
from app.models.transaction import Transaction
from datetime import datetime

bp = Blueprint('transaction', __name__, url_prefix='/transactions')

@bp.route('/new', methods=['GET'])
def new_transaction():
    """顯示新增收支表單"""
    return render_template('transactions/new.html')

@bp.route('', methods=['POST'])
def create_transaction():
    """處理新增收支"""
    type = request.form.get('type')
    amount_str = request.form.get('amount')
    category = request.form.get('category')
    date_str = request.form.get('date')
    description = request.form.get('description')

    if not type or not amount_str or not category or not date_str:
        flash('請填寫所有必填欄位 (類型、金額、分類、日期)', 'danger')
        return render_template('transactions/new.html', **request.form)

    try:
        amount = float(amount_str)
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        Transaction.create(
            type=type,
            amount=amount,
            category=category,
            date=date,
            description=description
        )
        flash('收支紀錄新增成功！', 'success')
        return redirect(url_for('main.index'))
    except ValueError:
        flash('金額格式錯誤或日期格式不正確', 'danger')
        return render_template('transactions/new.html', **request.form)
    except Exception as e:
        flash(f'新增失敗: {str(e)}', 'danger')
        return render_template('transactions/new.html', **request.form)

@bp.route('/<int:id>/edit', methods=['GET'])
def edit_transaction(id):
    """編輯收支頁面"""
    tx = Transaction.get_by_id(id)
    if not tx:
        flash('找不到該筆紀錄', 'danger')
        return redirect(url_for('main.index'))
    return render_template('transactions/edit.html', transaction=tx)

@bp.route('/<int:id>/update', methods=['POST'])
def update_transaction(id):
    """更新收支"""
    tx = Transaction.get_by_id(id)
    if not tx:
        flash('找不到該筆紀錄', 'danger')
        return redirect(url_for('main.index'))

    type = request.form.get('type')
    amount_str = request.form.get('amount')
    category = request.form.get('category')
    date_str = request.form.get('date')
    description = request.form.get('description')

    if not type or not amount_str or not category or not date_str:
        flash('請填寫所有必填欄位', 'danger')
        return render_template('transactions/edit.html', transaction=tx)

    try:
        amount = float(amount_str)
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        tx.update(
            type=type,
            amount=amount,
            category=category,
            date=date,
            description=description
        )
        flash('紀錄更新成功！', 'success')
    except ValueError:
        flash('金額格式錯誤或日期格式不正確', 'danger')
        return render_template('transactions/edit.html', transaction=tx)
    except Exception as e:
        flash(f'更新失敗: {str(e)}', 'danger')
        
    return redirect(url_for('main.index'))

@bp.route('/<int:id>/delete', methods=['POST'])
def delete_transaction(id):
    """刪除收支"""
    tx = Transaction.get_by_id(id)
    if not tx:
        flash('找不到該筆紀錄', 'danger')
    else:
        try:
            tx.delete()
            flash('紀錄已刪除', 'success')
        except Exception as e:
            flash(f'刪除失敗: {str(e)}', 'danger')
    return redirect(url_for('main.index'))
