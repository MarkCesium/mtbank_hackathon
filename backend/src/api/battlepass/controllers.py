import logging
from typing import cast
from uuid import UUID

from dishka.integrations.fastapi import (  # pyright: ignore[reportUnknownVariableType]
    DishkaRoute,
    FromDishka,
)
from fastapi import APIRouter

from src.dependencies.auth import AuthenticatedUser
from src.schemas.base import AUTH_ERRORS
from src.services.battlepass import BattlepassService

from .schemas import BattlepassDayResponse, BattlepassStateResponse, RewardType

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/battlepass", tags=["battlepass"], route_class=DishkaRoute)


@router.get("/current", response_model=BattlepassStateResponse, responses={**AUTH_ERRORS})
async def get_current_battlepass(
    current_user: AuthenticatedUser,
    battlepass_service: FromDishka[BattlepassService],
) -> BattlepassStateResponse:
    state = await battlepass_service.get_current_state(UUID(current_user.user_id))
    return BattlepassStateResponse(
        year=state.year,
        month=state.month,
        month_days_count=state.month_days_count,
        today_day=state.today_day,
        is_frozen=state.is_frozen,
        days=[
            BattlepassDayResponse(
                day=d.day,
                state=d.state,
                reward_type=cast(RewardType, d.reward_type),
                reward_title=d.reward_title,
                reward_description=d.reward_description,
            )
            for d in state.days
        ],
    )
