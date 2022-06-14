from uuid import uuid4

from migrate import *
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

user = Table(
    'user_details', metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False),
    Column('empid', String(10), unique=True, nullable=False),
    Column('username', String(40), unique=True, nullable=False),
    Column('passwd', String(40), nullable=False, default="Welcome123"),
    Column('tenantid', String(10), unique=True, nullable=False)
)


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    user.create()


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    user.drop()