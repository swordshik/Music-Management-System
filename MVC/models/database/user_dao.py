import sqlite3

class UserDAO:
    def __init__(self, conn):
        self.conn = conn

    def create_user(self, name, email, password, is_admin=0):
        try:
            self.conn.execute(
                "INSERT INTO user_table (name, email, password, is_admin) VALUES (?, ?, ?, ?)",
                (name, email, password, is_admin)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_user(self, email, password):
        cursor = self.conn.execute(
            "SELECT user_id, name, email, is_admin FROM user_table WHERE email = ? AND password = ?",
            (email, password)
        )
        return cursor.fetchone()