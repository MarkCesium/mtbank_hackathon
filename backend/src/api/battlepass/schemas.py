from typing import Literal

from pydantic import BaseModel

DayState = Literal["completed", "active", "available", "missed", "locked"]
RewardType = Literal["promo_shop", "promo_sub", "cashback_boost", "package_month"]


class BattlepassDayResponse(BaseModel):
    day: int
    state: DayState
    reward_type: RewardType
    reward_title: str
    reward_description: str


class BattlepassStateResponse(BaseModel):
    year: int
    month: int
    month_days_count: int
    today_day: int
    is_frozen: bool
    days: list[BattlepassDayResponse]
