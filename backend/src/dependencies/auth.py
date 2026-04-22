from typing import Annotated

import jwt
from dishka import Provider, Scope, provide  # pyright: ignore[reportUnknownVariableType]
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.core.config import Settings, settings
from src.infra.db.uow import UnitOfWork
from src.schemas.auth import CurrentUser
from src.services.auth import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


class AuthServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_auth_service(self, uow: UnitOfWork, settings: Settings) -> AuthService:
        return AuthService(uow, settings.jwt)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> CurrentUser:
    try:
        payload = jwt.decode(token, settings.jwt.secret, algorithms=["HS256"])
        return CurrentUser(
            user_id=payload["sub"],
            email=payload["email"],
            username=payload["username"],
        )
    except jwt.InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e


AuthenticatedUser = Annotated[CurrentUser, Depends(get_current_user)]
