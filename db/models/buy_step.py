from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    Date,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from db.models import Base

if TYPE_CHECKING:
    from .buy import Buy
    from .step import Step


class BuyStep(Base):
    __tablename__ = "buy_step"

    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.id"))
    step_id: Mapped[int] = mapped_column(ForeignKey("step.id"))

    date_step_beg: Mapped[date | None] = mapped_column(Date)
    date_step_end: Mapped[date | None] = mapped_column(Date)

    buy: Mapped["Buy"] = relationship(back_populates="buy_steps")
    step: Mapped["Step"] = relationship(back_populates="buy_steps")

    def __repr__(self):
        return f"BuyStep(buy_step_id={self.id})"
