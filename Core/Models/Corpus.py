import mysql.connector

from Core.MySqlConnector import MySQLConnector


class Corpus:
    db_connector = None

    def __init__(self):
        self.db_connector = MySQLConnector()

    def save(self, word):
        query = "INSERT INTO `corpuses` (`word`, `created_at`, `updated_at`) VALUES ('" + word + "', now(), now())"
        try:
            self.db_connector.cursor.execute(query)
            self.db_connector.connection.commit()
            last_id = self.db_connector.cursor.lastrowid
            self.db_connector.cursor.execute("SELECT * FROM corpuses WHERE id=" + str(last_id))
            rows = self.db_connector.cursor.fetchall()
            return rows[0]

        except mysql.connector.IntegrityError:
            return None

    def delete(self, id):
        query = "DELETE FROM corpuses WHERE id=" + str(id)
        self.db_connector.cursor.execute(query)
        self.db_connector.connection.commit()

    def find_by_word(self, word):
        query = "SELECT * FROM corpuses WHERE word='" + word+"'"
        self.db_connector.cursor.execute(query)
        return self.db_connector.cursor.fetchall()

