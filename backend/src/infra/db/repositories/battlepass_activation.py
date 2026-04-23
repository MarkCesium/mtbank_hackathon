from sqlalchemy import extract, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.types import IDType
from src.infra.db.models import BattlepassActivation

from .base import BaseRepository


class BattlepassActivationRepository(BaseRepository[BattlepassActivation]):
    def __init__(self, session: AsyncSession):
        super().__init__(BattlepassActivation, session)

    async def list_for_month(
        self, user_id: IDType, year: int, month: int
    ) -> list[BattlepassActivation]:
        stmt = select(BattlepassActivation).where(
            BattlepassActivation.user_id == user_id,
            extract("year", BattlepassActivation.activated_date) == year,
            extract("month", BattlepassActivation.activated_date) == month,
        )
        result = await self.session.scalars(stmt)
        return list(result.all())
