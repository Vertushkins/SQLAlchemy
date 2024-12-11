import datetime

from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, text


class WorkersORM(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class ResumesORM(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    compensation: Mapped[int | None]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE ('utc', now())"))
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE ('utc', now())"),
                                                          onupdate=datetime.datetime.now())

