from bootstrap.bus.message_bus import MessageBus
from database.interface.sql_uow import SqlUow
from database.uow.ledger_sql_uow import LedgerSqlUow


def bootstrap() -> MessageBus:
    uow: SqlUow = LedgerSqlUow()
    return MessageBus(
        uow
    )