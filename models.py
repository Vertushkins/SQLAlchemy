import datetime

from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, text
from typing import Annotated


idpk = Annotated[int, mapped_column(primary_key=True)]
created = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE ('utc', now())"))]
updated = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE ('utc', now())"),
                                                        onupdate=datetime.datetime.now())]


class WorkersORM(Base):
    __tablename__ = "workers"

    id: Mapped[idpk]
    name: Mapped[str]


class ResumesORM(Base):
    __tablename__ = "resumes"

    id: Mapped[idpk]
    title: Mapped[str]
    compensation: Mapped[int | None]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"))
    created_at: Mapped[created]
    updated_at: Mapped[updated]

