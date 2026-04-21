# 路由設計文件 (API Design)

根據產品需求文件 (PRD)、系統架構 (ARCHITECTURE) 與資料庫設計 (DB_DESIGN)，在此定義系統所有頁面及 API 的路由對照表與邏輯說明。為符合 HTML 表單操作限制，刪除與更新動作皆採用 `POST` 方法實作。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| **首頁儀表板** | GET | `/` | `templates/index.html` | 呈現包含最新餘額估算、近期的收支列表與股票紀錄 |
| **新增收支頁面** | GET | `/transactions/new` | `templates/transactions/new.html` | 顯示新增收支紀列表單 |
| **建立收支** | POST | `/transactions` | — | 接收新增收支表單並建立，完成後重導至首頁 |
| **編輯收支頁面** | GET | `/transactions/<id>/edit` | `templates/transactions/edit.html` | 顯示指定收支的修改表單 |
| **更新收支** | POST | `/transactions/<id>/update` | — | 接收並更新指定收支的資料，完成後重導至首頁 |
| **刪除收支** | POST | `/transactions/<id>/delete` | — | 刪除單一收支紀錄，完成後重導至首頁 |
| **新增股票頁面** | GET | `/stocks/new` | `templates/stocks/new.html` | 顯示新增股票紀錄表單 |
| **建立股票** | POST | `/stocks` | — | 接收新增表單並建立股票紀錄，完成後重導至首頁 |
| **編輯股票頁面** | GET | `/stocks/<id>/edit` | `templates/stocks/edit.html` | 顯示指定股票的修改表單 |
| **更新股票** | POST | `/stocks/<id>/update` | — | 接收並更新指定股票的資料，完成後重導至首頁 |
| **刪除股票** | POST | `/stocks/<id>/delete` | — | 刪除單一股票紀錄，完成後重導至首頁 |

## 2. 每個路由的詳細說明

### 2.1 首頁儀表板 (`app/routes/main.py`)
- **GET `/`**: 
  - **輸入**: 無
  - **處理邏輯**: 透過 `Transaction.get_all()` 與 `StockTransaction.get_all()` 取出所有紀錄。並加總這之間的數據估算「總餘額」。
  - **輸出**: 綁定運算後的參數與資料並渲染 `templates/index.html`。
  - **錯誤處理**: 資料庫讀取失敗應提供基本錯誤訊息並以適當 HTTP 代碼回應。

### 2.2 收支管理 (`app/routes/transaction.py`)
- **GET `/transactions/new`**: 返回 `new.html` 表單供填寫。
- **POST `/transactions`**: 從 HTTP 請求表單取值，呼叫 `Transaction.create()`。成功則 `redirect('/')` 重導向首頁；少填必填項目或是資料格式有誤，則重新渲染 `new.html` 並提示錯誤訊息。
- **GET `/transactions/<id>/edit`**: 呼叫 `Transaction.get_by_id(id)` 帶入 `edit.html` 給使用者修改，如果查無特定 ID，回傳 404 Not Found 錯誤。
- **POST `/transactions/<id>/update`**: 收到表單異動後存入資料實體並進行 Update。
- **POST `/transactions/<id>/delete`**: 抓出對應 ID 後執行 `Delete` 手段。

### 2.3 股票管理 (`app/routes/stock.py`)
- **GET `/stocks/new`**: 返回股票 `new.html` 買/賣表單供填寫。
- **POST `/stocks`**: 接收代號、買賣類型、價格、股數參數。執行 `StockTransaction.create()` 後回首頁，驗證失敗重回表單並反饋錯誤。
- **GET `/stocks/<id>/edit`**: 取得 `StockTransaction.get_by_id(id)` 後將內容印在編輯頁面，如果查無此 ID 則回傳 404 錯誤。
- **POST `/stocks/<id>/update`**: 將最新的表單內容變更傳入 update() 送出至資料庫。
- **POST `/stocks/<id>/delete`**: 從資料庫移除該股票操作紀錄。

## 3. Jinja2 模板清單

此專案的模板將遵循「圓潤可愛」精神繼承統一設計語言。
- **`templates/base.html`**: 設計總框架。注入可愛圓角 CSS、主色系主題與所有頁面共用 Header、Footer。
- **`templates/index.html`**: 首頁總覽，繼承自 base.html。
- **`templates/transactions/new.html`**: 新增收支表單，繼承自 base.html。
- **`templates/transactions/edit.html`**: 編輯特定收支表單，繼承自 base.html。
- **`templates/stocks/new.html`**: 新增股票紀錄表單，繼承自 base.html。
- **`templates/stocks/edit.html`**: 編輯特定股票紀錄表單，繼承自 base.html。

## 4. 路由骨架程式碼

在此技能的操作下，後端目錄 `app/routes/` 內建立了：
- `main.py`
- `transaction.py` 
- `stock.py` 

他們分別以 Flask Blueprint 模組獨立封裝，僅實作路由對照與註解（骨架）。
