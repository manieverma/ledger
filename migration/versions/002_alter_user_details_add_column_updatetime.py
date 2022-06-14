from datetime import datetime
from uuid import uuid4

import pytz
from migrate import *
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.dialects.postgresql import UUID


tz = pytz.timezone('Asia/Kolkata')

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata = MetaData(bind=migrate_engine)
    user_detail = Table('user_details', metadata, autoload=True)
    created_col = Column('created', DateTime(timezone=True), nullable=False, default=datetime.now(tz))
    created_col.create(user_detail)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata = MetaData(bind=migrate_engine)
    user_detail = Table('user_details', metadata, autoload=True)
    user_detail.c.created.drop()
