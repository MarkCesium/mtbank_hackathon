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
    2: Reward(RewardType.PROMO_SHOP, "-10% в 21vek.by", "Скидка на электронику"),
    3: Reward(RewardType.PROMO_SHOP, "-7% в Остров Чистоты", "Скидка на бытовую химию"),
    4: Reward(RewardType.PROMO_SHOP, "-5% в Соседи", "Скидка на весь чек"),
    5: Reward(RewardType.CASHBACK_BOOST, "+5% кэшбэка", "Следующий месяц"),
    6: Reward(RewardType.PROMO_SHOP, "-15% в Burger King", "Скидка на весь чек"),
    7: Reward(RewardType.PROMO_SHOP, "-20% в Domino's Pizza", "Скидка на весь чек"),
    8: Reward(RewardType.PROMO_SHOP, "-20% в HeroPark", "Скидка на развлечения"),
    9: Reward(RewardType.PROMO_SHOP, "-7% в Корона", "Скидка на весь чек"),
    10: Reward(RewardType.PROMO_SHOP, "-15% в Silver Screen", "Скидка на билеты в кино"),
    11: Reward(RewardType.PROMO_SHOP, "-6% в Mile", "Скидка на одежду"),
    12: Reward(RewardType.PROMO_SHOP, "-10% в Adidas", "Скидка на спортивную одежду"),
    13: Reward(RewardType.PROMO_SHOP, "-10% в I-Store", "Скидка на технику Apple"),
    14: Reward(RewardType.PROMO_SHOP, "-8% в 5 элемент", "Скидка на электронику"),
    15: Reward(RewardType.CASHBACK_BOOST, "+7% кэшбэка", "Следующий месяц"),
    16: Reward(RewardType.PROMO_SHOP, "-15% в Яндекс Go", "Скидка на поездки"),
    17: Reward(RewardType.PROMO_SHOP, "-7% в Green", "Скидка на весь чек"),
    18: Reward(RewardType.PROMO_SUB, "BelkaCar — поездка", "Бесплатная первая поездка"),
    19: Reward(RewardType.PROMO_SHOP, "-10% в Доктор Вет", "Скидка на товары для питомцев"),
    20: Reward(RewardType.PROMO_SHOP, "-10% в АЛЛО", "Скидка на технику"),
    21: Reward(RewardType.PROMO_SHOP, "-5% в Mark Formelle", "Скидка на одежду"),
    22: Reward(RewardType.PROMO_SHOP, "-10% в Reebok", "Скидка на спортивную одежду"),
    23: Reward(RewardType.PROMO_SHOP, "-5% в Алми", "Скидка на весь чек"),
    24: Reward(RewardType.PROMO_SHOP, "-5% в Onliner", "Скидка в каталоге Clover"),
    25: Reward(RewardType.CASHBACK_BOOST, "+10% кэшбэка", "Следующий месяц"),
    26: Reward(RewardType.PROMO_SHOP, "-10% в Планета Здоровья", "Скидка на аптечные товары"),
    27: Reward(RewardType.PROMO_SHOP, "-8% в Электросила", "Скидка на электронику"),
    28: Reward(RewardType.PROMO_SHOP, "-6% в Мила", "Скидка на косметику"),
    29: Reward(RewardType.PROMO_SUB, "Яндекс Плюс — месяц", "Бесплатная подписка"),
    30: Reward(
        RewardType.PACKAGE_MONTH,
        "Пакет решений бесплатно",
        "Бесплатное обслуживание на следующий месяц",
    ),
    31: Reward(RewardType.PROMO_SHOP, "-30% в Буль-Буль", "Скидка на бабл-ти"),
}


def reward_for_day(day: int) -> Reward:
    return BATTLEPASS_REWARDS[day]
