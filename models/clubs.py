class clubs:
    def add_club(cursor,club:str):
        cursor.execute('''
        INSERT INTO clubs(name)
        VALUES (?)
        ''',(club,))

    def GetId_orReturnNone(cursor,club:str):
        cursor.execute('SELECT id FROM clubs WHERE name = ?', (club,))
        result = cursor.fetchone()
        return result[0] if result else None

    def addLeagueKey(cursor,idLeague:int,idClub:int):
        cursor.execute('''
        UPDATE clubs
        SET league_id = ?
        WHERE id = ?
        ''',(idLeague,idClub))

    def create_clubs_table(cursor):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS clubs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            league_id INTEGER,
            FOREIGN KEY (league_id) REFERENCES leagues(id)
        )
        ''')
