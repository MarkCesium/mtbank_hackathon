# ruff: noqa: E501
"""seed shop items

Revision ID: a3b4c5d6e7f8
Revises: f7469d98a2d3
Create Date: 2026-04-23 13:41:00.000000

"""

from collections.abc import Sequence

from alembic import op

revision: str = "a3b4c5d6e7f8"
down_revision: str | None = "f7469d98a2d3"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("""
        INSERT INTO shop_items (id, category, title, description, price, image_url, brand_name, payload, is_recommended, is_active) VALUES
        ('11111111-0000-0000-0000-000000000001', 'promo_code'::shop_category,  '-20% на такси',                   'Скидка 20% на первую поездку в Яндекс Go',            25.00, NULL, 'Яндекс Go',      'YAGO20PCT',                                                                   TRUE,  TRUE),
        ('11111111-0000-0000-0000-000000000002', 'promo_code'::shop_category,  '3 по цене 2',                      'Три напитка по цене двух в Cofix',                     15.00, NULL, 'Cofix',           'COFIX3FOR2',                                                                  TRUE,  TRUE),
        ('11111111-0000-0000-0000-000000000003', 'promo_code'::shop_category,  'Скидка 10%',                      'На заказ в Lamoda',                                    20.00, NULL, 'Lamoda',          'LAMODA10',                                                                    FALSE, TRUE),
        ('11111111-0000-0000-0000-000000000004', 'promo_code'::shop_category,  'Скидка 150 BYN',                   'На заказ от 400 BYN в Delivery Club',                  15.00, NULL, 'Delivery Club',   'DC150OFF',                                                                    FALSE, TRUE),
        ('11111111-0000-0000-0000-000000000005', 'promo_code'::shop_category,  'Скидка 200 BYN',                   'На заказ от 700 BYN в OZON',                           20.00, NULL, 'OZON',            'OZON200OFF',                                                                  FALSE, TRUE),
        ('22222222-0000-0000-0000-000000000001', 'subscription'::shop_category,'Яндекс Плюс 60 дней',              'Подписка на Яндекс Плюс на 60 дней',                   10.00, NULL, 'Яндекс Плюс',    'YPLUS60D',                                                                    TRUE,  TRUE),
        ('22222222-0000-0000-0000-000000000002', 'subscription'::shop_category,'Кинопоиск 30 дней',                'Подписка на Кинопоиск на 30 дней',                     10.00, NULL, 'Кинопоиск',      'KP30D',                                                                       FALSE, TRUE),
        ('22222222-0000-0000-0000-000000000003', 'subscription'::shop_category,'Spotify Premium 30 дней',          'Подписка на Spotify Premium на 30 дней',               10.00, NULL, 'Spotify',         'SPOTIFY30D',                                                                  FALSE, TRUE),
        ('33333333-0000-0000-0000-000000000001', 'bank_perk'::shop_category,   '+1% к кэшбеку на месяц',          'Увеличение кэшбека на 1% по всем категориям на 30 дней', 50.00, NULL, 'MTBank',       'Активируйте в приложении: раздел «Кэшбек» → «Мои бонусы»',                   FALSE, TRUE),
        ('33333333-0000-0000-0000-000000000002', 'bank_perk'::shop_category,   'Доп. категория кэшбека',           'Выберите ещё одну категорию для получения повышенного кэшбека', 80.00, NULL, 'MTBank', 'Активируйте в приложении: раздел «Кэшбек» → «Категории»',                    FALSE, TRUE),
        ('33333333-0000-0000-0000-000000000003', 'bank_perk'::shop_category,   'Бесплатный перевод на 24 часа',    'Переводы без комиссии в течение 24 часов',             20.00, NULL, 'MTBank',          'Активируйте в приложении: раздел «Переводы» → «Льготы»',                     FALSE, TRUE)
    """)


def downgrade() -> None:
    op.execute("DELETE FROM shop_items")
