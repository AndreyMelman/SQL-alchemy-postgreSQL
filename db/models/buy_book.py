from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from db.models import Base

if TYPE_CHECKING:
    from .buy import Buy
    from .book import Book


class BuyBook(Base):
    __tablename__ = "buy_book"

    amount: Mapped[int] = mapped_column(Integer)

    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"))

    buy: Mapped["Buy"] = relationship(back_populates="buy_books")
    book: Mapped["Book"] = relationship(back_populates="buy_books")

    def __str__(self):
        return self.amount

    def __repr__(self):
        return f"BuyBook(buy_book_id={self.id}, amount={self.amount})"
