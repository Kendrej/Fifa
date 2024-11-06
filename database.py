import sqlite3
from models.cards import Cards
from models.clubs import create_clubs_table
from models.leagues import create_leagues_table
from models.nationalities import nationalities
from models.positions import create_positions_table
from models.prices import Price
from models.statistics import statistics
from models.playstyles import create_playstyles_table
from models.oth_statistics import otherStatistics

class Database:
    def __init__(self, db_name='mydatabase.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def get_cursor(self):
        return self.cursor
    
    def check_if_id_card_exists(self,user_id:int):
        return Cards.search_for_id(self.get_cursor(),user_id)
    
    def check_if_nationality_exists(self,nationality:str):
        if nationalities.getId_orReturnNone(self.get_cursor(),nationality) is None:
            return False
        else:
            return True
    
    def getNationalityID(self,nationality:str):
        return nationalities.getId_orReturnNone(self.get_cursor(),nationality)

    def connectNationalityIDWithCardID(self,idNationality:int,idCard:int):
        Cards.addNationalitykey(self.get_cursor(),idNationality,idCard)

    def addNationality(self,nationality:str):
        nationalities.add_nationality(self.get_cursor(),nationality)

    def addCard(self,idCard:int,firstName:str,secondName:str):
        Cards.addPlayersCard(self.get_cursor(),idCard,firstName,secondName)

    def addStatistics(self,id_card:int,overall:int,pace:int,shooting:int,passing:int,dribbling:int,defence:int,physical:int):
        statistics.add_statistics(self.get_cursor(),id_card,overall,pace,shooting,passing,dribbling,defence,physical)

    def addOtherStatistics(self,card_id, weight, height, weakFootStars, skillMovesStars, prefferedFoot, runningStyle, bodyType):
        otherStatistics.add_other_statistics(self.get_cursor(),card_id, weight, height, weakFootStars, skillMovesStars, prefferedFoot, runningStyle, bodyType)
    def addPlayersPrice():
        print()

    def _create_tables(self):
        create_clubs_table(self.cursor)
        create_leagues_table(self.cursor)
        nationalities.create_nationalities_table(self.cursor)
        create_positions_table(self.cursor)
        Cards.create_cards_table(self.cursor)
        Price.create_prices_table(self.cursor)
        statistics.create_statistics_table(self.cursor)
        create_playstyles_table(self.cursor)
        otherStatistics.create_oth_statistics_table(self.cursor)
        
        self.connection.commit()

    def close(self):
        self.connection.commit()
        self.connection.close()
