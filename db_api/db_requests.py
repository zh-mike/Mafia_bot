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
        admin_chat_id int,
        PRIMARY KEY (id_table)
        );
        """
        self.execute(sql, commit=True)


    def add_game_table(self, roles_list: str = '', chat_id: int = 0) -> int:
        data = True
        sql = "SELECT * FROM NewTable WHERE id_table=?"
        while data is not None:
            id_table = randint(1000, 9999)
            data = self.execute(sql, parameters=(id_table,), fetchone=True)
        sql = "INSERT INTO NewTable(id_table, roles_list, admin_chat_id) VALUES(?, ?, ?)"
        parameters = (id_table, roles_list, chat_id)
        self.execute(sql, parameters=parameters, commit=True)
        return id_table

    def search_table(self, id_table: int = 0):
        sql = "SELECT * FROM NewTable WHERE id_table=?"
        data = self.execute(sql, parameters=(id_table,), fetchone=True)
        return data

    def update_roles_user(self,id_table: int, roles_list: str):
        sql = "UPDATE NewTable SET roles_list=? WHERE id_table=?"
        return self.execute(sql, parameters=(roles_list, id_table), commit=True)


    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += " AND ".join([f"{item} = ?" for item in parameters])
        return sql, tuple(parameters.values())