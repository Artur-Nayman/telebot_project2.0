# db/database_manager.py
import mysql.connector

class DatabaseManager:
    def __init__(self, host, port, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, port=port, user=user, password=password, database=database
        )
        self.cursor = self.conn.cursor()

    def clear_xbox_table(self):
        self.cursor.execute("DELETE FROM xbox")
        self.conn.commit()

    def insert_game(self, title, price):
        sql = "INSERT INTO xbox (Title, Price) VALUES (%s, %s)"
        self.cursor.execute(sql, (title, price))
        self.conn.commit()

    def get_games(self):
        self.cursor.execute("SELECT Title, Price FROM xbox")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
