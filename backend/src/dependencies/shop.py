from dishka import Provider, Scope, provide  # pyright: ignore[reportUnknownVariableType]

from src.infra.db.uow import UnitOfWork
from src.services.shop import ShopService


class ShopServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_shop_service(self, uow: UnitOfWork) -> ShopService:
        return ShopService(uow)
