import sqlite3
from models.cards import Cards
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

    def get_cursor(self):
        return self.cursor
    
    def addPlayerData():
        print()

    def addPlayersPrice():
        print()

    def _create_tables(self):
        create_clubs_table(self.cursor)
        create_leagues_table(self.cursor)
        create_nationalities_table(self.cursor)
        create_positions_table(self.cursor)
        Cards.create_cards_table(self.cursor)
        Price.create_prices_table(self.cursor)
        create_statistics_table(self.cursor)
        create_playstyles_table(self.cursor)
        create_oth_statistics_table(self.cursor)
        
        self.connection.commit()

    def close(self):
        self.connection.close()
