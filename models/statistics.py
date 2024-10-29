# models/statistics.py
def create_statistics_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS statistics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INTEGER NOT NULL,
        goals INTEGER NOT NULL,
        assists INTEGER NOT NULL,
        matches INTEGER NOT NULL,
        FOREIGN KEY (card_id) REFERENCES cards (id)
    )
    ''')
