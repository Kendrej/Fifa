from datetime import datetime

class Price:
    def __init__(self, user_id, price, timestamp=None):
        self.user_id = user_id
        self.price = price
        self.timestamp = timestamp or datetime.now()
        
    # models/prices.py
    def create_prices_table(cursor):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_id INTEGER NOT NULL,
            price INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (card_id) REFERENCES cards (id)
        )
        ''')


