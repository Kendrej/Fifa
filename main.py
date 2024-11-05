from database import Database
from models.cards import Cards


def main():
    database = Database()
    
    user_id = int(3)
    
    if database.check__if_id_card_existing(user_id) :
        #database.addPlayersPrice()
        print("Id karty jest juz w bazie danych")
    else:
        database.addPlayerData(user_id,"Cristiano","Ronaldo")
        database.addPlayerStatistics(user_id,87,76,88,76,67,33,73)
        print("Zawodnik dodany")
        
    database.close()

    print("Database updated.")

main()
