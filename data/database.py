import sqlite3


class Database:
    url_database = 'VirtualPet.db'

    def _create_connection(self):
        try:
            self.connection = sqlite3.connect(Database.url_database)
        except Exception as e:
            print(e)

    def _close_connection(self):
        self.connection.close()
        self.connection = None

    def execute_sql(self, sql, return_created_id=False):
        self._create_connection()
        cur = self.connection.cursor()
        cur.execute(sql)

        lines = cur.fetchall()

        if return_created_id:
            lines = cur.lastrowid

        self.connection.commit()
        self._close_connection()

        return lines
