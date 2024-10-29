# models/oth_statistics.py
def create_oth_statistics_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS oth_statistics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id INTEGER NOT NULL,
        weight REAL NOT NULL,
        height REAL NOT NULL,
        weak_foot_stars INTEGER NOT NULL,
        skill_moves_stars INTEGER NOT NULL,
        running_style TEXT NOT NULL,
        body_type TEXT NOT NULL,
        FOREIGN KEY (card_id) REFERENCES cards (id)
    )
    ''')