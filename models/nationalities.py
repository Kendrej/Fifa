# models/nationalities.py
def create_nationalities_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS nationalities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')
