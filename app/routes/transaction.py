from flask import Blueprint, request, redirect, url_for, render_template

bp = Blueprint('transaction', __name__, url_prefix='/transactions')

@bp.route('/new', methods=['GET'])
def new_transaction():
    """
    新增收支頁面
    邏輯: 直接渲染新增表單頁面
    輸出: 渲染 templates/transactions/new.html
    """
    pass

@bp.route('', methods=['POST'])
def create_transaction():
    """
    建立收支
    邏輯: 接收表單資料，驗證與執行 Transaction.create()，成功後重導向
    輸出: redirect('/')
    錯誤處理: 資料缺失時提示錯誤並重新渲染 new.html
    """
    pass

@bp.route('/<int:id>/edit', methods=['GET'])
def edit_transaction(id):
    """
    編輯收支頁面
    邏輯: 根據 id 查詢 Transaction 並帶入預設值
    輸出: 渲染 templates/transactions/edit.html
    錯誤處理: 若 id 不存在則回傳 404
    """
    pass

@bp.route('/<int:id>/update', methods=['POST'])
def update_transaction(id):
    """
    更新收支
    邏輯: 將更新後的表單內容套用至指定 Transaction 實體並儲存
    輸出: redirect('/')
    """
    pass

@bp.route('/<int:id>/delete', methods=['POST'])
def delete_transaction(id):
    """
    刪除收支
    邏輯: 依據 id 刪除指定的 Transaction 紀錄
    輸出: redirect('/')
    """
    pass
