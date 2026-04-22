import logging
from typing import Annotated

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.dependencies.auth import AuthenticatedUser
from src.schemas.base import AUTH_ERRORS, CONFLICT_ERRORS, SuccessResponse
from src.services.auth import AuthService

from .schemas import (
    LogoutRequest,
    RefreshRequest,
    RegisterRequest,
    RegisterResponse,
    TokenResponse,
    UserResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"], route_class=DishkaRoute)


@router.post(
    "/register", status_code=201, response_model=RegisterResponse, responses={**CONFLICT_ERRORS}
)
async def register(
    body: RegisterRequest, auth_service: FromDishka[AuthService]
) -> RegisterResponse:
    user_id = await auth_service.register(body.username, body.email, body.password)
    return RegisterResponse(user_id=user_id)


@router.post("/login", response_model=TokenResponse, responses={**AUTH_ERRORS})
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)],
    auth_service: FromDishka[AuthService],
) -> TokenResponse:
    access_token, refresh_token = await auth_service.login(form_data.username, form_data.password)
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.post("/refresh", response_model=TokenResponse, responses={**AUTH_ERRORS})
async def refresh(body: RefreshRequest, auth_service: FromDishka[AuthService]) -> TokenResponse:
    access_token, refresh_token = await auth_service.refresh_tokens(body.refresh_token)
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.post("/logout", response_model=SuccessResponse)
async def logout(body: LogoutRequest, auth_service: FromDishka[AuthService]) -> SuccessResponse:
    success = await auth_service.logout(body.refresh_token)
    return SuccessResponse(success=success)


@router.get("/me", response_model=UserResponse, responses={**AUTH_ERRORS})
async def get_me(
    current_user: AuthenticatedUser,
    auth_service: FromDishka[AuthService],
) -> UserResponse:
    user = await auth_service.get_me(current_user.user_id)
    return UserResponse(
        user_id=user.id,
        username=user.username,
        email=user.email,
    )
