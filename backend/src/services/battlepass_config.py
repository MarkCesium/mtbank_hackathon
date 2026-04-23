from dataclasses import dataclass
from enum import StrEnum


class RewardType(StrEnum):
    PROMO_SHOP = "promo_shop"
    PROMO_SUB = "promo_sub"
    CASHBACK_BOOST = "cashback_boost"
    PACKAGE_MONTH = "package_month"


@dataclass(frozen=True, slots=True)
class Reward:
    type: RewardType
    title: str
    description: str


BATTLEPASS_REWARDS: dict[int, Reward] = {
    1: Reward(RewardType.PROMO_SHOP, "-5% в Евроопт", "Скидка на весь чек"),
    2: Reward(RewardType.PROMO_SHOP, "-10% в 21 век", "Скидка на электронику"),
    3: Reward(RewardType.PROMO_SHOP, "-7% в Остров Чистоты", "Скидка на бытовую химию"),
    4: Reward(RewardType.PROMO_SHOP, "-5% в Соседи", "Скидка на весь чек"),
    5: Reward(RewardType.CASHBACK_BOOST, "+5% кэшбэка", "Следующий месяц"),
    6: Reward(RewardType.PROMO_SHOP, "-8% в Белмаркет", "Скидка на весь чек"),
    7: Reward(RewardType.PROMO_SHOP, "-10% в OZ.by", "Скидка на книги"),
    8: Reward(RewardType.PROMO_SHOP, "-5% в Доброном", "Скидка на весь чек"),
    9: Reward(RewardType.PROMO_SHOP, "-7% в Корона", "Скидка на весь чек"),
    10: Reward(RewardType.PROMO_SUB, "Netflix — месяц", "Бесплатная подписка"),
    11: Reward(RewardType.PROMO_SHOP, "-6% в Mile", "Скидка на одежду"),
    12: Reward(RewardType.PROMO_SHOP, "-10% в Буслик", "Скидка на детские товары"),
    13: Reward(RewardType.PROMO_SHOP, "-5% в Rublevsky", "Скидка на весь чек"),
    14: Reward(RewardType.PROMO_SHOP, "-8% в 5 элемент", "Скидка на электронику"),
    15: Reward(RewardType.CASHBACK_BOOST, "+7% кэшбэка", "Следующий месяц"),
    16: Reward(RewardType.PROMO_SHOP, "-5% в МираМан", "Скидка на весь чек"),
    17: Reward(RewardType.PROMO_SHOP, "-7% в Green", "Скидка на весь чек"),
    18: Reward(RewardType.PROMO_SHOP, "-10% в Санта", "Скидка на весь чек"),
    19: Reward(RewardType.PROMO_SHOP, "-5% в Виталюр", "Скидка на весь чек"),
    20: Reward(RewardType.PROMO_SUB, "Spotify — месяц", "Бесплатная подписка"),
    21: Reward(RewardType.PROMO_SHOP, "-6% в Гиппо", "Скидка на весь чек"),
    22: Reward(RewardType.PROMO_SHOP, "-8% в Белорусочка", "Скидка на одежду"),
    23: Reward(RewardType.PROMO_SHOP, "-5% в Алми", "Скидка на весь чек"),
    24: Reward(RewardType.PROMO_SHOP, "-7% в Копеечка", "Скидка на весь чек"),
    25: Reward(RewardType.CASHBACK_BOOST, "+10% кэшбэка", "Следующий месяц"),
    26: Reward(RewardType.PROMO_SHOP, "-5% в Престон", "Скидка на весь чек"),
    27: Reward(RewardType.PROMO_SHOP, "-8% в Электросила", "Скидка на электронику"),
    28: Reward(RewardType.PROMO_SHOP, "-6% в Мила", "Скидка на косметику"),
    29: Reward(RewardType.PROMO_SHOP, "-10% в Свитанак", "Скидка на весь чек"),
    30: Reward(
        RewardType.PACKAGE_MONTH,
        "Пакет решений бесплатно",
        "Бесплатное обслуживание на следующий месяц",
    ),
    31: Reward(RewardType.PROMO_SHOP, "-15% бонус", "Скидка дня"),
}


def reward_for_day(day: int) -> Reward:
    return BATTLEPASS_REWARDS[day]
