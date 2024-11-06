class otherStatistics:
    def add_other_statistics(cursor,card_id:int , weight:int,height:int,weakFootStars:int, skillMovesStars:int, prefferedFoot:str, runningStyle:str, bodyType:str):
        cursor.execute('''
    INSERT INTO oth_statistics (card_id, weight, height, weak_foot_stars, skill_moves_stars, preferred_foot, running_style, body_type)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    ''',(card_id, weight, height, weakFootStars, skillMovesStars, prefferedFoot, runningStyle, bodyType))

    def create_oth_statistics_table(cursor):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS oth_statistics (
            card_id INTEGER PRIMARY KEY,
            weight INTEGER NOT NULL,
            height INTEGER NOT NULL,
            weak_foot_stars INTEGER NOT NULL,
            skill_moves_stars INTEGER NOT NULL,
            preferred_foot TEXT NOT NULL,
            running_style TEXT NOT NULL,
            body_type TEXT NOT NULL,
            FOREIGN KEY (card_id) REFERENCES cards (id)
        )
        ''')
