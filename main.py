from database import Database
from models.cards import Cards


def main():
    database = Database()
    
    user_id = int(2)
    
    if database.check__if_id_card_existing(user_id) :
        #database.addPlayersPrice()
        print("Id karty jest juz w bazie danych")
    else:
        database.addPlayerData(user_id,"Ewa","Pajor")
        print("Zawodnik dodany")
        
    database.close()

    print("Database updated.")

main()
