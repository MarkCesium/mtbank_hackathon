from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.types import IDType
from src.infra.db.models import Friendship, User

from .base import BaseRepository


class FriendshipRepository(BaseRepository[Friendship]):
    def __init__(self, session: AsyncSession):
        super().__init__(Friendship, session)

    async def get_friends_with_users(self, user_id: IDType) -> Sequence[User]:
        stmt = (
            select(User)
            .join(Friendship, Friendship.friend_id == User.id)
            .where(Friendship.user_id == user_id)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def are_friends(self, user_id: IDType, friend_id: IDType) -> bool:
        stmt = select(Friendship).where(
            Friendship.user_id == user_id,
            Friendship.friend_id == friend_id,
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none() is not None
