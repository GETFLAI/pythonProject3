import sqlite3

class Table_SQLite(): # бд sql

    def __init__(self):
        self.con = sqlite3.connect("BD_SQLite\db_ds.sqlite")
        self.cur = self.con.cursor()

    def claim_name(self, name): # изменение имени
        result = self.cur.execute("""SELECT name_player FROM player""").fetchone()
        if result == None:
            self.cur.execute("""INSERT INTO player (name_player) VALUES(?)""", (name,))
        else:
            print(result)
            self.cur.execute("""DELETE from player""")
            self.cur.execute("""INSERT INTO player (name_player) VALUES(?)""", (name,))
        self.con.commit()
        self.con.close()

    def get_name(self): # получение имени
        result = self.cur.execute("""SELECT name_player FROM player""").fetchone()
        if result == None:
            return None
        else:
            return result[0]