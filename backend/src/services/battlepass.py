import calendar
import logging

from src.core.dto import BattlepassDayDTO, BattlepassStateDTO, DayState
from src.core.time import today_minsk
from src.core.types import IDType
from src.infra.db.uow import UnitOfWork
from src.services.battlepass_config import BATTLEPASS_REWARDS, reward_for_day

logger = logging.getLogger(__name__)


class BattlepassService:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def get_current_state(self, user_id: IDType) -> BattlepassStateDTO:
        today = today_minsk()
        days_in_month = calendar.monthrange(today.year, today.month)[1]

        activations = await self.uow.battlepass_activation_repository.list_for_month(
            user_id, today.year, today.month
        )
        activated_days = {a.activated_date.day for a in activations}
        is_frozen = self._is_frozen(activated_days, today.day)

        days: list[BattlepassDayDTO] = []
        for day in range(1, days_in_month + 1):
            reward = reward_for_day(day)
            state = self._compute_state(day, today.day, activated_days, is_frozen)
            days.append(
                BattlepassDayDTO(
                    day=day,
                    state=state,
                    reward_type=reward.type.value,
                    reward_title=reward.title,
                    reward_description=reward.description,
                )
            )

        return BattlepassStateDTO(
            year=today.year,
            month=today.month,
            month_days_count=days_in_month,
            today_day=today.day,
            is_frozen=is_frozen,
            days=tuple(days),
        )

    async def activate_today(self, user_id: IDType) -> None:
        today = today_minsk()
        activations = await self.uow.battlepass_activation_repository.list_for_month(
            user_id, today.year, today.month
        )
        activated_days = {a.activated_date.day for a in activations}

        if self._is_frozen(activated_days, today.day):
            logger.info("Battlepass frozen for user %s, skipping activation", user_id)
            return

        if today.day in activated_days:
            return

        await self.uow.battlepass_activation_repository.create(
            user_id=user_id,
            activated_date=today,
        )

    @staticmethod
    def _is_frozen(activated_days: set[int], today_day: int) -> bool:
        if not activated_days:
            return False
        first = min(activated_days)
        return any(d not in activated_days for d in range(first + 1, today_day))

    @staticmethod
    def _compute_state(
        day: int, today_day: int, activated_days: set[int], is_frozen: bool
    ) -> DayState:
        if day in activated_days:
            return "completed"
        if day < today_day:
            return "missed"
        if is_frozen:
            return "locked"
        if day == today_day:
            return "active"
        return "available"


__all__ = ("BattlepassService", "BATTLEPASS_REWARDS")
