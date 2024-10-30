from database import Database
from models.cards import Cards


def main():
    database = Database()
    
    user_id = int(1)
    
    if Cards.search_for_id(database.get_cursor(),user_id) :
        database.addPlayersPrice()
    else:
        database.addPlayerData()
        
    # database.add_or_update_player('Robert', 'Lewandowski', 19000)

    database.close()

    print("Database updated.")

main()
