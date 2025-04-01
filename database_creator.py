import sqlite3

class Database:
    def setup_database(self):
        conn = sqlite3.connect('song_managing.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE songs (
	    song_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	    Artist TEXT,
	    Album TEXT,
	    Title TEXT NOT NULL,
	    Year INTEGER,
	    Genre TEXT
        );
        ''')


        cursor.execute('''
        CREATE TABLE trash (
	    song_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	    Artist TEXT,
	    Album TEXT,
	    Title TEXT NOT NULL,
	    Year INTEGER,
	    Genre TEXT
        );
        ''')

        cursor.execute('''
        CREATE TABLE admins (
	    admin_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	    username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
        );
        ''')

        cursor.execute('''
        CREATE TABLE user (
	    user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	    username TEXT NOT NULL,
        password TEXT NOT NULL
        );
        ''')

        conn.commit()
        conn.close()

if __name__ == "__main__":
    db = Database()
    db.setup_database()