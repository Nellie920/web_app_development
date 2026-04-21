CREATE TABLE "transaction" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(50) NOT NULL,
    amount REAL NOT NULL,
    category VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stock_transaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_symbol VARCHAR(20) NOT NULL,
    trade_type VARCHAR(50) NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    trade_date DATE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
