from dishka import Provider, Scope, provide  # pyright: ignore[reportUnknownVariableType]

from src.infra.db.uow import UnitOfWork
from src.services.game import GameService


class GameServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_game_service(self, uow: UnitOfWork) -> GameService:
        return GameService(uow)
