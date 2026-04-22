import logging
from datetime import UTC, datetime, timedelta
from uuid import UUID

from src.core.config import JWTConfig
from src.core.dto import TokenClaims, UserDTO
from src.core.exceptions import (
    AlreadyExistsError,
    InvalidCredentialsError,
    NotFoundError,
)
from src.core.security import (
    create_access_token,
    create_refresh_token,
    decode_access_token,
    hash_password,
    verify_password,
)
from src.core.types import IDType
from src.infra.db.uow import UnitOfWork

logger = logging.getLogger(__name__)


class AuthService:
    def __init__(self, uow: UnitOfWork, jwt_config: JWTConfig) -> None:
        self.uow = uow
        self.jwt_config = jwt_config

    async def register(self, username: str, email: str, password: str) -> IDType:
        existing = await self.uow.user_repository.get_one_or_none(email=email)
        if existing:
            raise AlreadyExistsError("Email already registered")

        existing_username = await self.uow.user_repository.get_one_or_none(username=username)
        if existing_username:
            raise AlreadyExistsError("Username already taken")

        hashed = await hash_password(password)
        user = await self.uow.user_repository.create(
            username=username,
            email=email,
            password=hashed,
        )
        return user.id

    async def login(self, email: str, password: str) -> tuple[str, str]:
        user = await self.uow.user_repository.get_one_or_none(email=email)
        if not user or not await verify_password(password, user.password):
            raise InvalidCredentialsError("Invalid email or password")

        access_token = create_access_token(str(user.id), user.email, user.username, self.jwt_config)
        refresh_token = await self._create_refresh_token(user.id)
        return access_token, refresh_token

    async def refresh_tokens(self, refresh_token: str) -> tuple[str, str]:
        token_record = await self.uow.refresh_token_repository.get_by_token(refresh_token)
        if not token_record:
            raise InvalidCredentialsError("Invalid refresh token")
        if token_record.is_revoked:
            raise InvalidCredentialsError("Refresh token has been revoked")
        if token_record.expires_at < datetime.now(UTC):
            raise InvalidCredentialsError("Refresh token has expired")

        await self.uow.refresh_token_repository.update(token_record.id, is_revoked=True)

        user = await self.uow.user_repository.get_by_id(token_record.user_id)
        if not user:
            raise NotFoundError("User not found")

        new_access_token = create_access_token(
            str(user.id), user.email, user.username, self.jwt_config
        )
        new_refresh_token = await self._create_refresh_token(user.id)
        return new_access_token, new_refresh_token

    async def logout(self, refresh_token: str) -> bool:
        token_record = await self.uow.refresh_token_repository.get_by_token(refresh_token)
        if not token_record:
            return False
        await self.uow.refresh_token_repository.update(token_record.id, is_revoked=True)
        return True

    async def get_me(self, user_id: str) -> UserDTO:
        user = await self.uow.user_repository.get_by_id(UUID(user_id))
        if not user:
            raise NotFoundError("User not found")
        return UserDTO(id=user.id, username=user.username, email=user.email)

    async def get_user_by_email(self, email: str) -> UserDTO:
        user = await self.uow.user_repository.get_one_or_none(email=email)
        if not user:
            raise NotFoundError("User not found")
        return UserDTO(id=user.id, username=user.username, email=user.email)

    async def validate_token(self, access_token: str) -> TokenClaims:
        return decode_access_token(access_token, self.jwt_config)

    async def _create_refresh_token(self, user_id: IDType) -> str:
        token = create_refresh_token()
        expires_at = datetime.now(UTC) + timedelta(days=self.jwt_config.refresh_token_expire_days)
        await self.uow.refresh_token_repository.create(
            token=token,
            user_id=user_id,
            expires_at=expires_at,
        )
        return token
