from dishka import Provider, Scope, provide  # pyright: ignore[reportUnknownVariableType]

from src.infra.db.uow import UnitOfWork
from src.services.battlepass import BattlepassService
from src.services.game import GameService


class GameServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_game_service(
        self, uow: UnitOfWork, battlepass_service: BattlepassService
    ) -> GameService:
        return GameService(uow, battlepass_service)
