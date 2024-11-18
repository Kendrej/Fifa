class leagues:
    def add_league(cursor,league:str):
        cursor.execute('''
        INSERT INTO leagues(name)
        VALUES (?)
        ''',(league,))
    
    def getId_orReturnNone(cursor,league:str):
        cursor.execute('SELECT id FROM leagues WHERE name = ?',(league,))
        result = cursor.fetchone()
        return result[0] if result else None

    def create_leagues_table(cursor):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS leagues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')
