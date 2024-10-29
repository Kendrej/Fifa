class Player:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

# models/cards.py
def create_cards_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        overall INTEGER NOT NULL,
        club_id INTEGER NOT NULL,
        nationality_id INTEGER NOT NULL,
        position_id INTEGER NOT NULL,
        FOREIGN KEY (club_id) REFERENCES clubs (id),
        FOREIGN KEY (nationality_id) REFERENCES nationalities (id),
        FOREIGN KEY (position_id) REFERENCES positions (id)
    )
    ''')
