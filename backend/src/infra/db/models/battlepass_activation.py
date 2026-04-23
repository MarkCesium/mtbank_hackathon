from datetime import date, datetime

from sqlalchemy import UUID, Date, DateTime, ForeignKey, Index, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from src.core.types import IDType

from .base import Base


class BattlepassActivation(Base):
    __tablename__ = "battlepass_activations"

    user_id: Mapped[IDType] = mapped_column(
        UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    activated_date: Mapped[date] = mapped_column(Date, nullable=False)
    activated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    __table_args__ = (
        UniqueConstraint("user_id", "activated_date", name="uq_battlepass_activations_user_date"),
        Index("ix_battlepass_activations_user_date", "user_id", "activated_date"),
    )
