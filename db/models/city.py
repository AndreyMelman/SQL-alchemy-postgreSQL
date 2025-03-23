from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    Integer,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from db.models import Base


if TYPE_CHECKING:
    from .client import Client


class City(Base):
    __tablename__ = "city"

    name_city: Mapped[str] = mapped_column(String(50))
    days_delivery: Mapped[int] = mapped_column(Integer)

    clients: Mapped[list["Client"]] = relationship(back_populates="city")

    def __str__(self):
        return self.name_city

    def __repr__(self):
        return f"City(id={self.id}, name_city={self.name_city})"
