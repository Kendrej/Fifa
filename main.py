from database import Database

def main():
    database = Database()
    
    user_id = int(1)

    # database.add_or_update_player('Robert', 'Lewandowski', 19000)

    database.close()

    print("Database updated.")

main()
