class positions:
    def add_position(cursor,position:str):
        cursor.execute('''
        INSERT INTO positions (position)
        VALUES (?)
        ''', (position,))

    def GetId_or_ReturnNone(cursor,position:str):
        cursor.execute('SELECT id FROM positions WHERE position = ?', (position,))
        result = cursor.fetchone()
        return result[0] if result else None
    
    def assign_position_to_Card(cursor,position_id:int,card_id:int):
        cursor.execute('''
        INSERT INTO card_position(position_id,card_id)
        VALUES (?,?)
        ''', (position_id,card_id))

    def create_positions_table(cursor):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS positions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            position TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS card_position(
            card_position_id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_id INTEGER NOT NULL,
            position_id INTEGER NOT NULL,
            FOREIGN KEY (card_id) REFERENCES cards (id),
            FOREIGN KEY (position_id) REFERENCES positions (id)
        )
        ''')
