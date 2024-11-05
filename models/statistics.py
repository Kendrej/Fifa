class statistics:
    # def add_statistics(cursor,int(overall),int(pace),int(shooting),int(passing),int(dribbling),int(defence),int(physical)):
    #     print()

    def create_statistics_table(cursor):
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS statistics (
            card_id INTEGER PRIMARY KEY,
            overall INTEGER NOT NULL,
            pace INTEGER NOT NULL,
            dribbling INTEGER NOT NULL,
            shooting INTEGER NOT NULL,
            defense INTEGER NOT NULL,
            passing INTEGER NOT NULL,
            physical INTEGER NOT NULL,
            FOREIGN KEY (card_id) REFERENCES cards (id)
        )
        ''')
