import logging
from uuid import UUID

from src.core.exceptions import NotFoundError, ValidationError
from src.core.types import IDType
from src.infra.db.uow import UnitOfWork
from src.schemas.shop import PurchaseResult, ShopCategory, ShopItem

logger = logging.getLogger(__name__)


class ShopService:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def list_items(self, category: ShopCategory | None = None) -> list[ShopItem]:
        async with self.uow as uow:
            items = await uow.shop_item_repository.list_active(category)
            return [ShopItem.model_validate(item) for item in items]

    async def purchase(self, user_id: IDType, shop_item_id: UUID) -> PurchaseResult:
        async with self.uow as uow:
            user = await uow.user_repository.get_by_id(user_id)
            if user is None:
                raise NotFoundError("Пользователь не найден")

            item = await uow.shop_item_repository.get_by_id(shop_item_id)
            if item is None or not item.is_active:
                raise NotFoundError("Товар не найден")

            if user.bonus < item.price:
                raise ValidationError("Недостаточно баллов")

            new_balance = user.bonus - item.price
            await uow.user_repository.update(user_id, bonus=new_balance)

            purchase = await uow.purchase_repository.create(
                user_id=user_id,
                shop_item_id=shop_item_id,
                price_paid=item.price,
                payload_snapshot=item.payload,
            )

            logger.info(
                "User %s purchased item %s for %s points", user_id, shop_item_id, item.price
            )

            return PurchaseResult(
                purchase_id=purchase.id,
                shop_item_id=item.id,
                title=item.title,
                price_paid=item.price,
                payload=item.payload,
                purchased_at=purchase.purchased_at,
                new_balance=new_balance,
            )
