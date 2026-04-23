from dishka import Provider, Scope, provide  # pyright: ignore[reportUnknownVariableType]

from src.infra.db.uow import UnitOfWork
from src.services.friends import FriendsService


class FriendsServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_friends_service(self, uow: UnitOfWork) -> FriendsService:
        return FriendsService(uow)
