from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    bonus: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=Decimal("67.00"), server_default="67.00")
    game_attempts_used: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    game_attempts_reset_date: Mapped[date | None] = mapped_column(Date, nullable=True, default=None)
