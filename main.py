from database import Database

def main():
    # 1. Inicjalizacja bazy danych
    database = Database()

    # 2. Dodanie przykładowego zawodnika
    database.add_or_update_player('Robert', 'Lewandowski', 17000)

    # 4. Zamykanie połączenia z bazą danych
    database.close()

    print("Database updated.")

main()
