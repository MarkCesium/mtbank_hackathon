import logging
from decimal import Decimal

from src.core.exceptions import DailyLimitExceededError, NotFoundError
from src.core.time import today_minsk
from src.core.types import IDType
from src.infra.db.models import User
from src.infra.db.uow import UnitOfWork
from src.services.battlepass import BattlepassService

logger = logging.getLogger(__name__)

DAILY_LIMIT = 3
WIN_THRESHOLD = 1000
WIN_BONUS = Decimal("0.05")


class GameService:
    def __init__(self, uow: UnitOfWork, battlepass_service: BattlepassService) -> None:
        self.uow = uow
        self.battlepass_service = battlepass_service

    async def start_attempt(self, user_id: IDType) -> int:
        user = await self.uow.user_repository.get_by_id(user_id)
        if user is None:
            raise NotFoundError("User not found")

        used = self._effective_used(user)
        if used >= DAILY_LIMIT:
            raise DailyLimitExceededError()

        today = today_minsk()
        await self.uow.user_repository.update(
            user_id,
            game_attempts_used=used + 1,
            game_attempts_reset_date=today,
        )
        return DAILY_LIMIT - (used + 1)

    async def finish_attempt(
        self,
        user_id: IDType,
        score: int,
        won: bool,
    ) -> tuple[Decimal, int, Decimal]:
        user = await self.uow.user_repository.get_by_id(user_id)
        if user is None:
            raise NotFoundError("User not found")

        awarded = Decimal("0.00")
        new_bonus = user.bonus
        if won and score >= WIN_THRESHOLD:
            awarded = WIN_BONUS
            new_bonus = user.bonus + WIN_BONUS
            await self.uow.user_repository.update(user_id, bonus=new_bonus)
            await self.battlepass_service.activate_today(user_id)

        remaining = DAILY_LIMIT - self._effective_used(user)
        return new_bonus, remaining, awarded

    @staticmethod
    def _effective_used(user: User) -> int:
        if user.game_attempts_reset_date != today_minsk():
            return 0
        return user.game_attempts_used
