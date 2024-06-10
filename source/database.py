import sqlite3


class Database:

    def __init(self, db_name):
        self.db_name = db_name

    def connect(self):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        return connection
