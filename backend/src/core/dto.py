from dataclasses import dataclass
from decimal import Decimal

from src.core.types import IDType


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
