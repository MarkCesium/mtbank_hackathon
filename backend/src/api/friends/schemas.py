from uuid import UUID

from pydantic import BaseModel

from src.schemas.friends import LeaderboardEntry


class AddFriendRequest(BaseModel):
    friend_id: UUID


class LeaderboardResponse(BaseModel):
    entries: list[LeaderboardEntry]
