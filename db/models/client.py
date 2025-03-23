from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from db.models import Base

if TYPE_CHECKING:
    from .city import City
    from .buy import Buy


class Client(Base):
    __tablename__ = "client"

    name_client: Mapped[str] = mapped_column(String(30))
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    email: Mapped[str] = mapped_column(String(30), unique=True)

    city: Mapped["City"] = relationship(back_populates="clients")
    buy: Mapped[list["Buy"]] = relationship(back_populates="client")

    def __str__(self):
        return self.name_client

    def __repr__(self):
        return f"Client(id={self.id}, name_client={self.name_client})"
