"""empty message

Revision ID: 39e6c3a64bfb
Revises: a9f04a71997f
Create Date: 2024-07-13 14:22:11.990073

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39e6c3a64bfb'
down_revision: Union[str, None] = 'a9f04a71997f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
