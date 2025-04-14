import sqlite3
from entities.user_entity import User

class UsersDAO:

    def __init__(self, db_path='song_managing.db'):
        self.db_path = db_path
        
    def insert_user(self, username, email, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        user1 = User(username, email, password)
        cursor.execute('''
            INSERT INTO users (username, email, password) VALUES (?, ?, ?)
        ''', (user1.get_username(), user1.get_email(), user1.get_password()))
        conn.commit()
        conn.close()

    def get_user(self, username):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE username=?
        ''', (username,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    def get_all_users(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM users
        ''')
        users = cursor.fetchall()
        users = users[3:]
        conn.close()
        return users