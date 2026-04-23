from .auth import AuthServiceProvider
from .battlepass import BattlepassServiceProvider
from .config import ConfigProvider
from .db import DBProvider
from .friends import FriendsServiceProvider
from .game import GameServiceProvider
from .shop import ShopServiceProvider

__all__ = (
    "AuthServiceProvider",
    "BattlepassServiceProvider",
    "ConfigProvider",
    "DBProvider",
    "FriendsServiceProvider",
    "GameServiceProvider",
    "ShopServiceProvider",
)
