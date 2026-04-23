from datetime import date, datetime
from zoneinfo import ZoneInfo

MINSK_TZ = ZoneInfo("Europe/Minsk")


def now_minsk() -> datetime:
    return datetime.now(MINSK_TZ)


def today_minsk() -> date:
    return now_minsk().date()
