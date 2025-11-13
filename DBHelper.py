import sqlite3

class dbop:
    def __init__(self):
        self.conn = sqlite3.connect('appinstitute.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Table_User(
                user_id INTEGER PRIMARY KEY,
                user_name TEXT,
                password TEXT,
                state_user TEXT
                )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Table_Dawra (
                dawra_id INTEGER PRIMARY KEY,
                dawra_name TEXT,
                dawra_price TEXT            
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Table_Mutadrib (
                mutadrib_id INTEGER PRIMARY KEY,
                mutadrib_name TEXT,
                mutadrib_phone TEXT,
                mutadrib_addris TEXT,
                dawra_id INTEGER,
                FOREIGN KEY (dawra_id) REFERENCES Table_Dawra(dawra_id)
            )
        """)

        self.conn.commit()
        #self.cursor.close()
        print("Database and tables created successfully!")

    def check_user(self, name, password):
        self.cursor.execute("select * from Table_User where user_name=? and password=?", (name, password))
        return self.cursor.fetchone()

    def inse_user(self):
        users = [("Aziz", "123", "active")]
        self.cursor.executemany("insert into Table_User values(NULL,?,?,?)", users)
        self.conn.commit()

    def insert_user(self, name, pas, stat):
        self.cursor.execute("insert into Table_User values(NULL,?,?,?)", (name, pas, stat))
        self.conn.commit()

    def update_user(self, id, name, pas, stat):
        self.cursor.execute("update Table_User set user_name=?, password=?, state_user=? where user_id=?", (name, pas, stat, id))
        self.conn.commit()

    def delete_user(self, id):
        self.cursor.execute("delete from Table_User where user_id=?", (id))
        self.conn.commit()

    def fetch_user(self):
        self.cursor.execute("select * from Table_User")
        row = self.cursor.fetchall()
        return row

    def insert_dawra(self, name, price):
        self.cursor.execute("insert into Table_Dawra values(NULL,?,?)", (name, price))
        self.conn.commit()

    def update_dawra(self, id, name, price):
        self.cursor.execute("update Table_Dawra set dawra_name=?, dawra_price=? where dawra_id=?", (name, price, id))
        self.conn.commit()

    def delete_dawra(self, id):
        self.cursor.execute("delete from Table_Dawra where user_id=?", (id))
        self.conn.commit()

    def fetch_dawra(self):
        self.cursor.execute("select * from Table_Dawra")
        row = self.cursor.fetchall()
        return row

    def insert_mutadrib(self, name, phone, addris, dawra):
        self.cursor.execute("insert into Table_Mutadrib values(NULL,?,?,?,?)", (name, phone, addris, dawra))
        self.conn.commit()

    def update_mutadrib(self, id, name, phone, addris, dawra):
        self.cursor.execute("update Table_Mutandis set mutadrib_name=?, mutadrib_phone=?, mutadrib_addris=?, dawra_id where mutadrib_id=?", (name, phone, addris, dawra, id))
        self.conn.commit()

    def delete_mutadrib(self, id):
        self.cursor.execute("delete from Table_Mutadrib where mutadrib_id=?", (id))
        self.conn.commit()

    def fetch_mutadrib(self):
        self.cursor.execute("select * from Table_Mutadrib")
        row = self.cursor.fetchall()
        return row