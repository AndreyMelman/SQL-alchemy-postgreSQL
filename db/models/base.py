from sqlalchemy import MetaData, func
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped

from config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    id: Mapped[int] = mapped_column(default=None, primary_key=True)
