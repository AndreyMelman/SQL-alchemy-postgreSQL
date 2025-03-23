from typing import TYPE_CHECKING

from db.models.base import Base
from sqlalchemy import (
    String,
    ForeignKey,
    DECIMAL,
    Integer,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

if TYPE_CHECKING:
    from .author import Author
    from .genre import Genre
    from .buy_book import BuyBook
    from .buy import Buy


class Book(Base):
    __tablename__ = "book"

    title: Mapped[str] = mapped_column(String(50))
    author_id: Mapped[int] = mapped_column(
        ForeignKey(
            "author.id",
            ondelete="CASCADE",
        ),
    )
    genre_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "genre.id",
            ondelete="SET NULL",
        ),
    )
    price: Mapped[DECIMAL] = mapped_column(DECIMAL(8, 2))
    amount: Mapped[int] = mapped_column(Integer)

    author: Mapped["Author"] = relationship(back_populates="books")
    genre: Mapped["Genre"] = relationship(back_populates="books")

    buy_books: Mapped[list["BuyBook"]] = relationship(back_populates="book")
    buys: Mapped[list["Buy"]] = relationship(
        secondary="buy_book",
        back_populates="books",
        viewonly=True,
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title})"
