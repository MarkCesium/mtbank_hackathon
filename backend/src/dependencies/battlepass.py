from dishka import Provider, Scope, provide  # pyright: ignore[reportUnknownVariableType]

from src.infra.db.uow import UnitOfWork
from src.services.battlepass import BattlepassService


class BattlepassServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_battlepass_service(self, uow: UnitOfWork) -> BattlepassService:
        return BattlepassService(uow)
