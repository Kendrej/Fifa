def create_cards_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS players_card (
        id_card INTEGER PRIMARY KEY AUTOINCREMENT,
        id_nationality INTEGER,
        id_club INTEGER,
        id_playstyle INTEGER,
        id_position INTEGER,
        first_name VARCHAR(255) NOT NULL,
        second_name VARCHAR(255),
        FOREIGN KEY (id_nationality) REFERENCES nationalities(id),
        FOREIGN KEY (id_club) REFERENCES clubs(id),
        FOREIGN KEY (id_playstyle) REFERENCES playstyles(id),
        FOREIGN KEY (id_position) REFERENCES positions(id)
    )
    ''')
