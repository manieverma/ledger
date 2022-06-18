from sqlalchemy.orm import sessionmaker, Session

from database.db.postgresql import PostgresDB
from database.interface.sql_uow import SqlUow


class LedgerSqlUow(SqlUow):


    def __init__(self, session_factory=None):
        db_details = {
            "username": "postgres",
            "password": "root",
            "host": "localhost",
            "port": "5432",
            "database": "ledger"
        }
        DB_Engine = PostgresDB(db_details).get_connection()
        session_factory = sessionmaker(bind=DB_Engine)
        self.session_factory = session_factory


    def __enter__(self):
        self.session: Session = self.session_factory()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()