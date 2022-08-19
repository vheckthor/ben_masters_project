import sqlite3

class UserRegNo:
    def __init__(self):
        self.con = sqlite3.connect('test.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        #self.cur.execute("""DROP TABLE user_reg_no""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS user_reg_no(
        date DATE PRIMARY KEY,
        category TEXT,
        name TEXT,
        reg_no REAL,
        link TEXT
        )""")

    def insert(self, item):
        self.cur.execute("""INSERT OR IGNORE INTO user_reg_no VALUES(?,?,?,?,?)""", item)
        self.con.commit()

    def read(self):
        self.cur.execute("""SELECT * FROM user_reg_no""")
        rows = self.cur.fetchall()
        print(rows)