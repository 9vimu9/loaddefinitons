import mysql.connector

from Core.MySqlConnector import MySQLConnector

word_class_enum = dict(NOUN=1, VERB=2, ADJECTIVE=3, ADVERB=4, PREPOSITION=5, DETERMINER=6, PRONOUN=7, CONJUNCTION=8, INTERJECTION=9)


class Definition:
    db_connector = None

    def __init__(self):
        self.db_connector = MySQLConnector()

    def save(self, corpus_id, word_class, definition):
        definition = definition.replace("'", "\\'")
        word_class_id = word_class_enum[word_class.upper()]
        query = "INSERT INTO `definitions` (`definition`, `corpus_id`, `word_class`, `created_at`, `updated_at`) VALUES ('" + definition + "', " + str(
            corpus_id) + ", " + str(word_class_id) + ", now(), now())"
        try:
            self.db_connector.cursor.execute(query)
            self.db_connector.connection.commit()
            last_id = self.db_connector.cursor.lastrowid
            self.db_connector.cursor.execute("SELECT * FROM definitions WHERE id=" + str(last_id))
            rows = self.db_connector.cursor.fetchall()
            return rows[0]

        except mysql.connector.IntegrityError:
            return None
