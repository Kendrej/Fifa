from database import Database  # Importuj klasę Database

def main():
    # 1. Inicjalizacja bazy danych
    db = Database()

    # 2. Dodanie przykładowego zawodnika
    db.add_or_update_player('Robert', 'Lewandowski', 160000)

    # 3. Wyświetlenie wszystkich cen zawodników
    prices = db.get_all_prices()
    for price in prices:
        print(price)

    # 4. Zamykanie połączenia z bazą danych
    db.close()

if __name__ == "__main__":
    main()
