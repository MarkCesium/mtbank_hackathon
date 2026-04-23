from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ShopCategory(StrEnum):
    promo_code = "promo_code"
    subscription = "subscription"
    bank_perk = "bank_perk"


class ShopItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    category: ShopCategory
    title: str
    description: str
    price: Decimal
    image_url: str | None
    brand_name: str | None
    is_recommended: bool


class PurchaseResult(BaseModel):
    purchase_id: UUID
    shop_item_id: UUID
    title: str
    price_paid: Decimal
    payload: str
    purchased_at: datetime
    new_balance: Decimal
