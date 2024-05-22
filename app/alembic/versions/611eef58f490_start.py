"""start

Revision ID: 611eef58f490
Revises:
Create Date: 2024-05-22 16:51:21.274383

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "611eef58f490"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "username",
            sa.String(length=200),
            unique=True,
            nullable=False,
            index=True,
        ),
        sa.Column("password", sa.String(length=512), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime,
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    op.create_table(
        "locations",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "code",
            sa.String(length=150),
            index=True,
            unique=True,
            nullable=False,
        ),
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime,
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    op.create_table(
        "voyages",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "username",
            sa.String(length=200),
            index=True,
            nullable=False,
        ),
        sa.Column(
            "label",
            sa.String(length=150),
            index=True,
            unique=True,
            nullable=False,
        ),
        sa.Column("value", sa.Integer, nullable=False),
        sa.Column("lloc", sa.String(length=100), nullable=False),
        sa.Column("rloc", sa.String(length=100), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime,
            server_default=sa.func.now(),
            nullable=False,
        ),
    )


def downgrade() -> None:
    pass
