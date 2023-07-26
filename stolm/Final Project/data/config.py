import os
from dotenv import load_dotenv
import sqlite3


load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins_id = []


class ConnectionToDB:
    """
    The class implements connecting to the database, working with it,
    and disconnecting from it after work. It was done to avoid
    the load on the database if the connection to it would be open
    for a long time.
    """

    def __init__(self):  # Connect to DB
        self.db = sqlite3.connect('main.db') # Path to our database
        self.cursor = self.db.cursor()
        print("Successfully Connected to SQLite")

    async def __aenter__(self):
        return self.cursor

    async def __aexit__(self, exc_type, exc_val, exc_tb):  # Disconnect from DB
        print("Successfully Disconnected from SQLite")
        self.cursor.close()
        self.db.close()

    def commit(self):  # Commit in DB
        self.db.commit()
