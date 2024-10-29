# models/leagues.py
def create_leagues_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS leagues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')
