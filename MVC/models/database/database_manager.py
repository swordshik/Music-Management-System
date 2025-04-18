import sqlite3

class DatabaseManager:
    def __init__(self, db_name="music_database.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS user_table (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0
            )
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS songs (
                song_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                artist TEXT NOT NULL,
                album TEXT NOT NULL,
                song TEXT NOT NULL,
                genre TEXT,
                year TEXT,
                lyrics TEXT,
                FOREIGN KEY(user_id) REFERENCES user_table(user_id)
            )
        """)
        self.conn.commit()

    def get_connection(self):
        return self.conn

    def close(self):
        self.conn.close()