from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    """
    首頁儀表板
    輸入: 無
    邏輯:
      - 從 Model 取得 Transaction 與 StockTransaction 的最新紀錄
      - 計算整體餘額與股票損益概況
    輸出: 渲染 templates/index.html
    """
    pass
