# models/playstyles.py
def create_playstyles_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS playstyles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INTEGER NOT NULL,
        style TEXT NOT NULL,
        FOREIGN KEY (card_id) REFERENCES cards (id)
    )
    ''')
