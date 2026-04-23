from datetime import datetime

from sqlalchemy import UUID, DateTime, ForeignKey, Index, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.core.types import IDType

from .base import Base


class Purchase(Base):
    __tablename__ = "purchases"

    user_id: Mapped[IDType] = mapped_column(
        UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    shop_item_id: Mapped[IDType] = mapped_column(
        UUID, ForeignKey("shop_items.id", ondelete="RESTRICT"), nullable=False
    )
    price_paid: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    payload_snapshot: Mapped[str] = mapped_column(nullable=False)
    purchased_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default="now()"
    )

    __table_args__ = (Index("ix_purchases_user_id", "user_id"),)
