# ruff: noqa: E501
"""update shop items

Revision ID: c6d7e8f9a0b1
Revises: b225929d4ae9
Create Date: 2026-04-24 15:00:00.000000

"""

from collections.abc import Sequence

from alembic import op

revision: str = "c6d7e8f9a0b1"
down_revision: str | None = "b225929d4ae9"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Delete items with no purchases (safe)
    op.execute("""
        DELETE FROM shop_items WHERE id IN (
            '11111111-0000-0000-0000-000000000003',
            '11111111-0000-0000-0000-000000000004',
            '11111111-0000-0000-0000-000000000005'
        )
    """)

    # Spotify has purchases — can only deactivate
    op.execute("""
        UPDATE shop_items SET is_active = FALSE
        WHERE id = '22222222-0000-0000-0000-000000000003'
    """)

    op.execute("""
        INSERT INTO shop_items (id, category, title, description, price, image_url, brand_name, payload, is_recommended, is_active) VALUES
        ('11111111-0000-0000-0000-000000000005', 'promo_code'::shop_category,  'Скидка 50 BYN',         'На заказ от 150 BYN в OZON',          20.00, NULL, 'OZON',          'OZON50OFF',  FALSE, TRUE),
        ('11111111-0000-0000-0000-000000000006', 'promo_code'::shop_category,  '-15% в Burger King',   'Скидка на весь чек',                  20.00, NULL, 'Burger King',   'BK15OFF',    TRUE,  TRUE),
        ('11111111-0000-0000-0000-000000000007', 'promo_code'::shop_category,  '-15% в KFC',           'Скидка на весь чек',                  20.00, NULL, 'KFC',           'KFC15OFF',   FALSE, TRUE),
        ('11111111-0000-0000-0000-000000000008', 'promo_code'::shop_category,  '-20% в Mac By',        'Скидка на весь чек',                  25.00, NULL, 'Mac By',        'MACBY20',    TRUE,  TRUE),
        ('11111111-0000-0000-0000-000000000009', 'promo_code'::shop_category,  '-20% в Tapioca',       'Скидка на все напитки',               15.00, NULL, 'Tapioca',       'TAPIOCA20',  TRUE,  TRUE),
        ('22222222-0000-0000-0000-000000000004', 'subscription'::shop_category,'Яндекс Музыка 30 дней', 'Подписка на Яндекс Музыку на 30 дней', 8.00, NULL, 'Яндекс Музыка', 'YMUSIC30D', FALSE, TRUE)
    """)


def downgrade() -> None:
    op.execute("""
        DELETE FROM shop_items WHERE id IN (
            '11111111-0000-0000-0000-000000000005',
            '11111111-0000-0000-0000-000000000006',
            '11111111-0000-0000-0000-000000000007',
            '11111111-0000-0000-0000-000000000008',
            '11111111-0000-0000-0000-000000000009',
            '22222222-0000-0000-0000-000000000004'
        )
    """)

    op.execute("""
        INSERT INTO shop_items (id, category, title, description, price, image_url, brand_name, payload, is_recommended, is_active) VALUES
        ('11111111-0000-0000-0000-000000000003', 'promo_code'::shop_category,  'Скидка 10%',    'На заказ в Lamoda',                   20.00, NULL, 'Lamoda',        'LAMODA10',   FALSE, TRUE),
        ('11111111-0000-0000-0000-000000000004', 'promo_code'::shop_category,  'Скидка 150 BYN', 'На заказ от 400 BYN в Delivery Club', 15.00, NULL, 'Delivery Club', 'DC150OFF',   FALSE, TRUE),
        ('11111111-0000-0000-0000-000000000005', 'promo_code'::shop_category,  'Скидка 200 BYN', 'На заказ от 700 BYN в OZON',          20.00, NULL, 'OZON',          'OZON200OFF', FALSE, TRUE)
    """)

    op.execute("""
        UPDATE shop_items SET is_active = TRUE
        WHERE id = '22222222-0000-0000-0000-000000000003'
    """)
