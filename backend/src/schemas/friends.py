from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class LeaderboardEntry(BaseModel):
    user_id: UUID
    username: str
    bonus: Decimal
    rank: int
    is_current_user: bool
