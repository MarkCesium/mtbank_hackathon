"""Add bonus and game attempts to user

Revision ID: a1b2c3d4e5f6
Revises: 136c558c6e81
Create Date: 2026-04-22 14:00:00.000000

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a1b2c3d4e5f6"
down_revision: str | None = "136c558c6e81"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "bonus",
            sa.Numeric(precision=10, scale=2),
            nullable=False,
            server_default=sa.text("0.00"),
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "game_attempts_used",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("0"),
        ),
    )
    op.add_column(
        "users",
        sa.Column("game_attempts_reset_date", sa.Date(), nullable=True),
    )
    op.alter_column("users", "bonus", server_default=None)
    op.alter_column("users", "game_attempts_used", server_default=None)


def downgrade() -> None:
    op.drop_column("users", "game_attempts_reset_date")
    op.drop_column("users", "game_attempts_used")
    op.drop_column("users", "bonus")
