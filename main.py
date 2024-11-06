from database import Database
from models.cards import Cards


def main():
    database = Database("test.db")
    
    user_id = int(3)
    
    if database.check__if_id_card_existing(user_id) :
        #database.addPlayersPrice()
        print("Id karty jest juz w bazie danych")
    else:
        database.addCard(user_id,"Cristiano","Ronaldo")
        database.addStatistics(user_id,87,76,88,76,67,33,73)
        database.addOtherStatistics(user_id,57,168,3,4,"right","Mostly Explosive","Short & Normal")
        print("Zawodnik dodany")
        
    database.close()

    print("Database updated.")

main()
