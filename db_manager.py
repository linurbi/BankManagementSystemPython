import sqlite3


class DbManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def execute_query(self, query, params=None, return_selection=False, return_last_command=False,
                      return_only_one=False):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if not params:
                cursor.execute(query)
                self.db_commit()
            else:
                cursor.execute(query, params)
                self.db_commit()
            if return_selection:
                return cursor.fetchall()
            if return_last_command:
                return cursor.lastrowid
            if return_only_one:
                return cursor.fetchone()

    def db_commit(self):
        db = sqlite3.connect(self.db_path)
        db.commit()
