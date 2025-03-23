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


class Author(Base):
    __tablename__ = "author"

    name_author: Mapped[str] = mapped_column(String(50))

    books: Mapped[list["Book"]] = relationship(
        back_populates="author", cascade="all, delete"
    )

    def __str__(self):
        return self.name_author

    def __repr__(self):
        return f"Author(id={self.id}, name_author={self.name_author})"
