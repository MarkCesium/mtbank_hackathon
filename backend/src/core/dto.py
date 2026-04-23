from dataclasses import dataclass
from decimal import Decimal
from typing import Literal

from src.core.types import IDType

DayState = Literal["completed", "active", "available", "missed", "locked"]


@dataclass(frozen=True, slots=True)
class TokenClaims:
    sub: str
    email: str
    username: str


@dataclass(frozen=True, slots=True)
class UserDTO:
    id: IDType
    username: str
    email: str
    bonus: Decimal
    attempts_remaining: int


@dataclass(frozen=True, slots=True)
class BattlepassDayDTO:
    day: int
    state: DayState
    reward_type: str
    reward_title: str
    reward_description: str


@dataclass(frozen=True, slots=True)
class BattlepassStateDTO:
    year: int
    month: int
    month_days_count: int
    today_day: int
    is_frozen: bool
    days: tuple[BattlepassDayDTO, ...]
