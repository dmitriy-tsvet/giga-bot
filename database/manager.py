from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine
import typing
from . import base
from sqlalchemy import MetaData
metadata_obj = MetaData()
from sqlalchemy import Table, Column, Integer, String, BigInteger, Float, Boolean


async def create_async_session(database: base.AsyncDatabase, *args, **kwargs):
    engine = create_async_engine(str(database), *args, **kwargs)
    Session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    return Session



# user_table = Table(
#     "user",
#     metadata_obj,
#     Column("index", Integer, primary_key=True),
#     Column("id", BigInteger),
#     Column("username", String),
#     Column("fullname", String),
#     Column("created_at", String),
# )

user_table = Table(
    "item_image",
    metadata_obj,
    Column("index", Integer, primary_key=True),
    Column("item_id", String),
    Column("url", String),
)

#
# order_table = Table(
#     "order",
#     metadata_obj,
#     Column("index", Integer, primary_key=True),
#     Column("id", String),
#     Column("user_id", BigInteger),
#     Column("fullname", String),
#     Column("phone", String),
#     Column("text", String),
#     Column("created_at", String),
# )


def create_session(database: typing.Union[base.TransactionDatabase, base.FileDatabase], *args, **kwargs):
    engine = create_engine(url=str(database), future=True, *args, **kwargs)
    Session = sessionmaker(bind=engine)

    metadata_obj.create_all(bind=engine)
    return Session
