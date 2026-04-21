from flask import Blueprint, request, redirect, url_for, render_template

bp = Blueprint('stock', __name__, url_prefix='/stocks')

@bp.route('/new', methods=['GET'])
def new_stock():
    """
    新增股票頁面
    邏輯: 直接渲染新增表單頁面
    輸出: 渲染 templates/stocks/new.html
    """
    pass

@bp.route('', methods=['POST'])
def create_stock():
    """
    建立股票
    邏輯: 接收表單資料，驗證與執行 StockTransaction.create()，成功後重導向
    輸出: redirect('/')
    錯誤處理: 資料缺失時提示錯誤並重新渲染 new.html
    """
    pass

@bp.route('/<int:id>/edit', methods=['GET'])
def edit_stock(id):
    """
    編輯股票頁面
    邏輯: 根據 id 查詢 StockTransaction 並帶入預設值
    輸出: 渲染 templates/stocks/edit.html
    錯誤處理: 若 id 不存在則回傳 404
    """
    pass

@bp.route('/<int:id>/update', methods=['POST'])
def update_stock(id):
    """
    更新股票
    邏輯: 將更新後的表單內容套用至指定 StockTransaction 並儲存
    輸出: redirect('/')
    """
    pass

@bp.route('/<int:id>/delete', methods=['POST'])
def delete_stock(id):
    """
    刪除股票
    邏輯: 依據 id 刪除指定的 StockTransaction 紀錄
    輸出: redirect('/')
    """
    pass
