from decimal import Decimal

from pydantic import BaseModel, Field


class StartAttemptResponse(BaseModel):
    attempts_remaining: int


class FinishAttemptRequest(BaseModel):
    score: int = Field(ge=0)
    won: bool


class FinishAttemptResponse(BaseModel):
    bonus: Decimal
    attempts_remaining: int
    awarded: Decimal
