from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.db.models import ShopItem
from src.schemas.shop import ShopCategory

from .base import BaseRepository


class ShopItemRepository(BaseRepository[ShopItem]):
    def __init__(self, session: AsyncSession):
        super().__init__(ShopItem, session)

    async def list_active(self, category: ShopCategory | None = None) -> Sequence[ShopItem]:
        stmt = select(ShopItem).where(ShopItem.is_active.is_(True))
        if category is not None:
            stmt = stmt.where(ShopItem.category == category)
        stmt = stmt.order_by(ShopItem.price)
        result = await self.session.scalars(stmt)
        return result.all()
