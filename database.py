import sqlite3
from models.cards import Cards
from models.clubs import clubs
from models.leagues import leagues
from models.nationalities import nationalities
from models.positions import positions
from models.prices import Price
from models.statistics import statistics
from models.playstyles import playstyles
from models.oth_statistics import otherStatistics

class Database:
    def __init__(self, db_name='mydatabase.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def get_cursor(self):
        return self.cursor
    
    def _create_tables(self):
        clubs.create_clubs_table(self.cursor)
        leagues.create_leagues_table(self.cursor)
        nationalities.create_nationalities_table(self.cursor)
        positions.create_positions_table(self.cursor)
        Cards.create_cards_table(self.cursor)
        Price.create_prices_table(self.cursor)
        statistics.create_statistics_table(self.cursor)
        playstyles.create_playstyles_table(self.cursor)
        otherStatistics.create_oth_statistics_table(self.cursor)
        self.connection.commit()

    def close(self):
        self.connection.commit()
        self.connection.close()

    

    # --- Leagues Operations ---
    def check_if_id_league_exists(self,league:str):
        return leagues.getId_orReturnNone(self.get_cursor(),league) is not None
    
    def addLeague(self,league:str):
        leagues.add_league(self.get_cursor(),league)

    def getLeagueID(self,league:str):
        return leagues.getId_orReturnNone(self.get_cursor(),league)



    # --- Clubs Operations ---
    def check_if_club_exists(self,club:str):
        return clubs.GetId_orReturnNone(self.get_cursor(),club) is not None

    def getClubID(self,club:str):
        return clubs.GetId_orReturnNone(self.get_cursor(),club)
    
    def connectLeagueIDWithClubID(self,idLeague:int,idClub:int):
        clubs.addLeagueKey(self.get_cursor(),idLeague,idClub)

    def addClub(self,club:str):
        clubs.add_club(self.get_cursor(),club)


    
    # --- Nationalities Operations ---
    def check_if_nationality_exists(self,nationality:str):
        return nationalities.getId_orReturnNone(self.get_cursor(),nationality) is not None
    
    def getNationalityID(self,nationality:str):
        return nationalities.getId_orReturnNone(self.get_cursor(),nationality)

    def addNationality(self,nationality:str):
        nationalities.add_nationality(self.get_cursor(),nationality)



    # --- Cards Operations ---
    def addCard(self,idCard:int,firstName:str,secondName:str):
        Cards.addPlayersCard(self.get_cursor(),idCard,firstName,secondName)
        
    def check_if_id_card_exists(self,user_id:int):
        return Cards.search_for_id(self.get_cursor(),user_id)
    
    def connectNationalityIDWithCardID(self,idNationality:int,idCard:int):
        Cards.addNationalitykey(self.get_cursor(),idNationality,idCard)

    def connectClubIDWithCardID(self,idClub:int,idCard:int):
        Cards.addClubkey(self.get_cursor(),idClub,idCard)



    # --- Statistics Operations ---
    def addStatistics(self,id_card:int,overall:int,pace:int,shooting:int,passing:int,dribbling:int,defence:int,physical:int):
        statistics.add_statistics(self.get_cursor(),id_card,overall,pace,shooting,passing,dribbling,defence,physical)



    # --- Other Statistics Operations ---
    def addOtherStatistics(self,card_id, weight, height, weakFootStars, skillMovesStars, prefferedFoot, runningStyle, bodyType):
        otherStatistics.add_other_statistics(self.get_cursor(),card_id, weight, height, weakFootStars, skillMovesStars, prefferedFoot, runningStyle, bodyType)  


    
    # --- Playstyles Operations ---
    def addPlaystyle(self,playstyle:str):
        playstyles.add_playstyle(self.get_cursor(),playstyle)

    def getPlaystyleId(self,playstyle:str):
        return playstyles.GetId_or_ReturnNone(self.get_cursor(),playstyle)
    
    def check_if_id_playstyle_exists(self,playstyle:str):
        return playstyles.GetId_or_ReturnNone(self.get_cursor(),playstyle) is not None
    
    def assign_playstyle_to_Card(self,playstyle_id:int,card_id:int,is_plus:bool):
        playstyles.assign_playstyle_to_Card(self.get_cursor(),playstyle_id,card_id,is_plus)



    # --- Positions Operations ---
    def addPosition(self,position:str):
        positions.add_position(self.get_cursor(),position)

    def getPositionId(self,position:str):
        return positions.GetId_or_ReturnNone(self.get_cursor(),position)

    def check_if_id_position_exists(self,position:str):
        return positions.GetId_or_ReturnNone(self.get_cursor(),position) is not None
    
    def assign_position_to_Card(self,position_id:int,card_id:int):
        positions.assign_position_to_Card(self.get_cursor(),position_id,card_id)



    # --- Price Operations ---
    def addPlayersPrice(self,user_id,price,timestamp=None):
        Price.addPrice(self.get_cursor(),user_id,price,timestamp)