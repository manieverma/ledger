from database.interface.sql_uow import SqlUow


class MessageBus:
    def __init__(self, uow: SqlUow):
        self.uow = uow
