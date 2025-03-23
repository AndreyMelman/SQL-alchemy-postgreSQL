from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from db.models import Base

if TYPE_CHECKING:
    from .client import Client
    from .buy_book import BuyBook
    from .buy_step import BuyStep
    from .book import Book


class Buy(Base):
    __tablename__ = "buy"

    buy_description: Mapped[str] = mapped_column(Text)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))

    client: Mapped["Client"] = relationship(back_populates="buy")
    buy_books: Mapped[list["BuyBook"]] = relationship(back_populates="buy")
    buy_steps: Mapped[list["BuyStep"]] = relationship(back_populates="buy")

    books: Mapped[list["Book"]] = relationship(
        secondary="buy_book",
        back_populates="buys",
        viewonly=True,
    )

    def __str__(self):
        return self.buy_description

    def __repr__(self):
        return f"Buy(id={self.id}, buy_description={self.buy_description})"
