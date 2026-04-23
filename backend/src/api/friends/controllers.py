import logging
from uuid import UUID

from dishka.integrations.fastapi import (  # pyright: ignore[reportUnknownVariableType]
    DishkaRoute,
    FromDishka,
)
from fastapi import APIRouter

from src.dependencies.auth import AuthenticatedUser
from src.schemas.base import AUTH_ERRORS, CONFLICT_ERRORS, NOT_FOUND_ERRORS
from src.services.friends import FriendsService

from .schemas import AddFriendRequest, LeaderboardResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/friends", tags=["friends"], route_class=DishkaRoute)


@router.get(
    "/leaderboard",
    response_model=LeaderboardResponse,
    responses={**AUTH_ERRORS},
)
async def get_leaderboard(
    current_user: AuthenticatedUser,
    friends_service: FromDishka[FriendsService],
) -> LeaderboardResponse:
    entries = await friends_service.get_leaderboard(UUID(current_user.user_id))
    return LeaderboardResponse(entries=entries)


@router.post(
    "/add",
    status_code=204,
    responses={
        **AUTH_ERRORS,
        **NOT_FOUND_ERRORS,
        **CONFLICT_ERRORS,
        400: {"description": "Validation error"},
    },
)
async def add_friend(
    body: AddFriendRequest,
    current_user: AuthenticatedUser,
    friends_service: FromDishka[FriendsService],
) -> None:
    await friends_service.add_friend(UUID(current_user.user_id), body.friend_id)
