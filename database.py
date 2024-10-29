import sqlite3
from models.cards import create_cards_table
from models.clubs import create_clubs_table
from models.leagues import create_leagues_table
from models.nationalities import create_nationalities_table
from models.positions import create_positions_table
from models.prices import Price
from models.statistics import create_statistics_table
from models.playstyles import create_playstyles_table
from models.oth_statistics import create_oth_statistics_table

class Database:
    def __init__(self, db_name='mydatabase.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        create_clubs_table(self.cursor)
        create_leagues_table(self.cursor)
        create_nationalities_table(self.cursor)
        create_positions_table(self.cursor)
        create_cards_table(self.cursor)
        Price.create_prices_table(self.cursor)
        create_statistics_table(self.cursor)
        create_playstyles_table(self.cursor)
        create_oth_statistics_table(self.cursor)
        
        self.connection.commit()

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

    def close(self):
        self.connection.close()
