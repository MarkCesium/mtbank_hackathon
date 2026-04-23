from decimal import Decimal

from sqlalchemy import Boolean, Index, Numeric, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from src.schemas.shop import ShopCategory

from .base import Base


class ShopItem(Base):
    __tablename__ = "shop_items"

    category: Mapped[ShopCategory] = mapped_column(
        SQLEnum(ShopCategory, name="shop_category"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    brand_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    payload: Mapped[str] = mapped_column(String(500), nullable=False)
    is_recommended: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    __table_args__ = (Index("ix_shop_items_category_active", "category", "is_active"),)
