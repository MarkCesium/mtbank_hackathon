from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.db.models.refresh_token import RefreshToken

from .base import BaseRepository


class RefreshTokenRepository(BaseRepository[RefreshToken]):
    def __init__(self, session: AsyncSession):
        super().__init__(RefreshToken, session)

    async def get_by_token(self, token: str) -> RefreshToken | None:
        return await self.get_one_or_none(token=token)
