from models import WorkersORM
from database import my_session


def insert_data():
    with my_session() as session:
        worker = WorkersORM(name="Vlad")
        session.add(worker)
        session.commit()
