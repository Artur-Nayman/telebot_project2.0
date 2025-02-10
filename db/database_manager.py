# db/database_manager.py
import mysql.connector

# Initialize the connection to the MySQL database
class DatabaseManager:
    def __init__(self, host, port, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, port=port, user=user, password=password, database=database
        )
        # Create a cursor object to interact with the database
        self.cursor = self.conn.cursor()

    def clear_xbox_table(self):
        # Execute a SQL command to delete all records from the 'xbox' table
        self.cursor.execute("DELETE FROM xbox")
        # Execute a SQL command to delete all records from the 'xbox' table
        self.conn.commit()

    def insert_game(self, title, price):
        # Define an SQL command to insert a new game record into the 'xbox' table
        sql = "INSERT INTO xbox (Title, Price) VALUES (%s, %s)"
        # Execute the SQL command with the provided title and price
        self.cursor.execute(sql, (title, price))
        self.conn.commit()# Commit the transaction to save changes

    def get_games(self):
        # Execute a SQL command to retrieve all game records from the 'xbox' table
        self.cursor.execute("SELECT Title, Price FROM xbox")
        # Fetch all the results and return them
        return self.cursor.fetchall()

    # Close the cursor and the database connection
    def close(self):
        self.cursor.close()
        self.conn.close()
