from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.db.models import Purchase

from .base import BaseRepository


class PurchaseRepository(BaseRepository[Purchase]):
    def __init__(self, session: AsyncSession):
        super().__init__(Purchase, session)
