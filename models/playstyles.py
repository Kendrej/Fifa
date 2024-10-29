# models/playstyles.py
def create_playstyles_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS playstyles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INTEGER NOT NULL,
        style TEXT NOT NULL,
        is_plus BOOLEAN NOT NULL CHECK (is_plus IN (0, 1)),  -- 0 = zwykły, 1 = plus
        FOREIGN KEY (card_id) REFERENCES cards (id)
    )
    ''')
