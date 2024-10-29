# models/clubs.py
def create_clubs_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clubs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        league_id INTEGER,
        FOREIGN KEY (league_id) REFERENCES leagues(id)
    )
    ''')
