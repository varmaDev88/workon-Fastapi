"""add content column to posts table

Revision ID: 01501b24cea5
Revises: 54e9aea2c3b7
Create Date: 2024-07-11 17:04:26.466116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01501b24cea5'
down_revision = '54e9aea2c3b7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
