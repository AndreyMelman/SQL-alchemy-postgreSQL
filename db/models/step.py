from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from db.models import Base

if TYPE_CHECKING:
    from .buy_step import BuyStep


class Step(Base):
    __tablename__ = "step"

    name_step: Mapped[str] = mapped_column(String(50))

    buy_steps: Mapped[list["BuyStep"]] = relationship(back_populates="step")

    def __str__(self):
        return self.name_step

    def __repr__(self):
        return f"Step(id={self.id}, name_step={self.name_step})"
