class Cards:
    def search_for_id(cursor, id_card):
        cursor.execute('SELECT id_card FROM players_card WHERE id_card = ?', (id_card,))
        return cursor.fetchone() is not None

    def addPlayersCard(cursor,idCard,firstName,secondName):
        cursor.execute('''
    INSERT INTO players_card (id_card,first_name, second_name)
    VALUES (?, ?, ?)
    ''', (idCard,firstName,secondName))
        
    def addNationalitykey(cursor,idNationality:int,idCard:int):
        cursor.execute('''
    UPDATE players_card
    SET id_nationality = ?
    WHERE id_card = ?
    ''', (idNationality, idCard))

    def addClubkey(cursor,idClub:int,idCard:int):
        cursor.execute('''
        UPDATE players_card
        SET id_club = ?
        WHERE id_card = ?
        ''', (idClub,idCard))

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
