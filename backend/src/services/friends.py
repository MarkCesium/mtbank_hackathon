import logging
from uuid import UUID

from src.core.exceptions import AlreadyExistsError, NotFoundError, ValidationError
from src.core.types import IDType
from src.infra.db.uow import UnitOfWork
from src.schemas.friends import LeaderboardEntry

logger = logging.getLogger(__name__)


class FriendsService:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def get_leaderboard(self, current_user_id: IDType) -> list[LeaderboardEntry]:
        async with self.uow as uow:
            current_user = await uow.user_repository.get_by_id(current_user_id)
            if current_user is None:
                raise NotFoundError("Пользователь не найден")

            friends = await uow.friendship_repository.get_friends_with_users(current_user_id)
            all_users = [current_user, *friends]
            all_users.sort(key=lambda u: u.bonus, reverse=True)

            return [
                LeaderboardEntry(
                    user_id=user.id,
                    username=user.username,
                    bonus=user.bonus,
                    rank=rank,
                    is_current_user=user.id == current_user_id,
                )
                for rank, user in enumerate(all_users, start=1)
            ]

    async def add_friend(self, current_user_id: IDType, friend_id: UUID) -> None:
        async with self.uow as uow:
            if current_user_id == friend_id:
                raise ValidationError("Нельзя добавить себя в друзья")

            friend = await uow.user_repository.get_by_id(friend_id)
            if friend is None:
                raise NotFoundError("Пользователь не найден")

            already_friends = await uow.friendship_repository.are_friends(
                current_user_id, friend_id
            )
            if already_friends:
                raise AlreadyExistsError("Вы уже друзья")

            await uow.friendship_repository.create(user_id=current_user_id, friend_id=friend_id)
            await uow.friendship_repository.create(user_id=friend_id, friend_id=current_user_id)

            logger.info("Friendship created: %s <-> %s", current_user_id, friend_id)
