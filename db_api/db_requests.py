import sqlite3

from random import randint

class Database:
    def __init__(self, db_path: str = "mafia_database.db"):
        self.db_path = db_path

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            data = None
            cursor.execute(sql, parameters)
            if commit:
                conn.commit()
            if fetchone:
                data = cursor.fetchone()
            if fetchall:
                data = cursor.fetchall()
            return data

#########################################################################################

    def create_table_new_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS NewTable(
        id_table int NOT NULL,
        roles_list text,
        PRIMARY KEY (id_table)
        );
        """
        self.execute(sql, commit=True)


    def add_game_table(self, roles_list: str = ''):
        data = True
        sql = "SELECT * FROM NewTable WHERE id_table=?"
        while data is not None:
            id_table = randint(1000, 9999)
            data = self.execute(sql, parameters=(id_table,), fetchone=True)
        sql = "INSERT INTO NewTable(id_table, roles_list) VALUES(?, ?)"
        parameters = (id_table, roles_list)
        self.execute(sql, parameters=parameters, commit=True)
        return id_table

        # sql = "INSERT INTO NewTable(id_table, roles_list) VALUES(?, ?)"
        # parameters = (id_table, roles_list)
        # self.execute(sql, parameters=parameters, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += " AND ".join([f"{item} = ?" for item in parameters])
        return sql, tuple(parameters.values())