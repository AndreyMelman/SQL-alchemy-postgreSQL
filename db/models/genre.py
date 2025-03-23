from typing import TYPE_CHECKING

from db.models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

if TYPE_CHECKING:
    from .book import Book


class Genre(Base):
    __tablename__ = "genre"

    name_genre: Mapped[str] = mapped_column(String(50))
    books: Mapped[list["Book"]] = relationship(back_populates="author")

    def __str__(self):
        return self.name_genre

    def __repr__(self):
        return f"Genre(id={self.id}, name_genre={self.name_genre})"
