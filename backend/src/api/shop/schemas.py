from uuid import UUID

from pydantic import BaseModel

from src.schemas.shop import ShopItem


class ListShopItemsResponse(BaseModel):
    items: list[ShopItem]


class PurchaseRequest(BaseModel):
    shop_item_id: UUID
