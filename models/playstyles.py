class playstyles:
    def add_playstyle(cursor,playstyle:str):
        cursor.execute('''
        INSERT INTO playstyles (style)
        VALUES (?)
        ''',(playstyle,))
         
    def GetId_or_ReturnNone(cursor,playstyle:str):
        cursor.execute('SELECT id FROM playstyles WHERE style = ?', (playstyle,))
        result = cursor.fetchone()
        return result[0] if result else None

    def assign_playstyle_to_Card(cursor,playstyle_id:int,card_id:int,plus:bool):
        try:
            plus_value = int(plus)

            cursor.execute('''
            INSERT INTO card_playstyle(playstyle_id,card_id,is_plus)
            VALUES (?,?,?)
            ''',(playstyle_id,card_id,plus_value))
        
        except Exception as db_error:
            print("Error while adding playstyle")
        

    def create_playstyles_table(cursor):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS playstyles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            style TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS card_playstyle (
            card_playstyle_id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_id INTEGER NOT NULL,
            playstyle_id INTEGER NOT NULL,
            is_plus BOOLEAN NOT NULL CHECK (is_plus IN (0, 1)),  -- 0 = zwykły, 1 = plus
            FOREIGN KEY (card_id) REFERENCES cards (id),
            FOREIGN KEY (playstyle_id) REFERENCES playstyles (id)
        )
        ''')
