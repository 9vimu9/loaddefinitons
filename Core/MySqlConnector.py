PORT = 33062
HOST = '0.0.0.0'
USER = 'root'
PASSWORD = 'password'
DATABASE = 'enhancer_db'

import mysql.connector


class MySQLConnector:
    connection = None
    cursor = None

    def __init__(self):
        self.connection = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        self.cursor = self.connection.cursor(dictionary=True)
