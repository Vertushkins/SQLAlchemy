from sqlalchemy import Table, Column, Integer, String, MetaData, insert
from sqlalchemy.orm import sessionmaker
from database import engine
from ORM import insert_data


def create_table(engine):
    metadata.drop_all(engine)
    metadata.create_all(engine)


# def insert_data():
#     with engine.connect() as connection:
#         statement = insert(user_table).values([
#             {"name": "Ivan"},
#             {"name": "Gosh"}
#         ])
#         connection.execute(statement)
#         connection.commit()


metadata = MetaData()

# user_table = Table(
#     "workers", metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String)
# )

insert_data()
