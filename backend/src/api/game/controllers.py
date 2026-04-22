import logging
from uuid import UUID

from dishka.integrations.fastapi import (  # pyright: ignore[reportUnknownVariableType]
    DishkaRoute,
    FromDishka,
)
from fastapi import APIRouter

from src.dependencies.auth import AuthenticatedUser
from src.schemas.base import AUTH_ERRORS
from src.services.game import GameService

from .schemas import FinishAttemptRequest, FinishAttemptResponse, StartAttemptResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/game", tags=["game"], route_class=DishkaRoute)


@router.post("/start", response_model=StartAttemptResponse, responses={**AUTH_ERRORS})
async def start_game(
    current_user: AuthenticatedUser,
    game_service: FromDishka[GameService],
) -> StartAttemptResponse:
    remaining = await game_service.start_attempt(UUID(current_user.user_id))
    return StartAttemptResponse(attempts_remaining=remaining)


@router.post("/finish", response_model=FinishAttemptResponse, responses={**AUTH_ERRORS})
async def finish_game(
    body: FinishAttemptRequest,
    current_user: AuthenticatedUser,
    game_service: FromDishka[GameService],
) -> FinishAttemptResponse:
    bonus, remaining, awarded = await game_service.finish_attempt(
        UUID(current_user.user_id),
        body.score,
        body.won,
    )
    return FinishAttemptResponse(
        bonus=bonus,
        attempts_remaining=remaining,
        awarded=awarded,
    )
