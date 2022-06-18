from sqlalchemy import create_engine

from database.interface.database import Database


class PostgresDB(Database):
    __instance = None

    def __init__(self, **kwargs):
        super().__init__()

        db_details = kwargs

        self.__engine = create_engine(
            'postgresql://{}:{}@{}:{}/{}'.format(
                db_details["username"],
                db_details["password"],
                db_details["host"],
                db_details["port"],
                db_details["database"]
            )
        )

        PostgresDB.__instance = self.__engine

    def get_connection(self, **kwargs):
        if PostgresDB.__instance is None:
            PostgresDB(**kwargs)
        return PostgresDB.__instance

