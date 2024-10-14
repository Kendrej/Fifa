# database.py

print("Ładowanie modułu Database")  # Komunikat na początku pliku

import sqlite3
# from player import Player  # Importuj klasę Player
from price import Price  # Importuj klasę Price
from datetime import datetime

class Database:
    def __init__(self, db_name='mydatabase.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            price INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        ''')

    def add_or_update_player(self, first_name, last_name, price_value):
        self.cursor.execute('''
        SELECT id FROM users WHERE first_name = ? AND last_name = ?
        ''', (first_name, last_name))
        user = self.cursor.fetchone()

        if not user:
            self.cursor.execute('''
            INSERT INTO users (first_name, last_name)
            VALUES (?, ?)
            ''', (first_name, last_name))
            user_id = self.cursor.lastrowid
        else:
            user_id = user[0]

        price = Price(user_id, price_value)
        self.add_price(price)
        self.connection.commit()

    def add_price(self, price: Price):
        self.cursor.execute('''
        INSERT INTO prices (user_id, price, timestamp)
        VALUES (?, ?, ?)
        ''', (price.user_id, price.price, price.timestamp))

    def get_all_prices(self):
        self.cursor.execute('''
        SELECT users.first_name, users.last_name, prices.price, prices.timestamp
        FROM users
        JOIN prices ON users.id = prices.user_id
        ORDER BY prices.timestamp
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
