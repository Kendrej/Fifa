class nationalities:
    def add_nationality(cursor,nationality:str):
        cursor.execute('''
        INSERT INTO nationalities(nationality)
        VALUES (?)
        ''',(nationality,))

    def getId_orReturnNone(cursor,nationality:str):
        cursor.execute('SELECT id FROM nationalities WHERE nationality = ?', (nationality,))
        result = cursor.fetchone()
        return result[0] if result else None
    
    def create_nationalities_table(cursor):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS nationalities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nationality TEXT NOT NULL
        )
        ''')
