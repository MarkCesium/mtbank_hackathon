import logging
from uuid import UUID

from dishka.integrations.fastapi import (  # pyright: ignore[reportUnknownVariableType]
    DishkaRoute,
    FromDishka,
)
from fastapi import APIRouter

from src.dependencies.auth import AuthenticatedUser
from src.schemas.base import AUTH_ERRORS, NOT_FOUND_ERRORS
from src.schemas.shop import PurchaseResult, ShopCategory
from src.services.shop import ShopService

from .schemas import ListShopItemsResponse, PurchaseRequest

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/shop", tags=["shop"], route_class=DishkaRoute)


@router.get(
    "/items",
    response_model=ListShopItemsResponse,
    responses={**AUTH_ERRORS},
)
async def list_shop_items(
    current_user: AuthenticatedUser,
    shop_service: FromDishka[ShopService],
    category: ShopCategory | None = None,
) -> ListShopItemsResponse:
    items = await shop_service.list_items(category)
    return ListShopItemsResponse(items=items)


@router.post(
    "/purchase",
    response_model=PurchaseResult,
    responses={**AUTH_ERRORS, **NOT_FOUND_ERRORS, 400: {"description": "Insufficient balance"}},
)
async def purchase_item(
    body: PurchaseRequest,
    current_user: AuthenticatedUser,
    shop_service: FromDishka[ShopService],
) -> PurchaseResult:
    return await shop_service.purchase(UUID(current_user.user_id), body.shop_item_id)
