import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv('DB_PORT')
HOST = os.getenv('DB_HOST')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DB_DATABASE')

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
