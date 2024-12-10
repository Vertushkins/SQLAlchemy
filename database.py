from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine


engine = create_engine("sqlite:///data.db")
my_session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
