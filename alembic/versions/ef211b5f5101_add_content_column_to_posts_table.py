"""add content column to posts table

Revision ID: ef211b5f5101
Revises: dd882601923c
Create Date: 2023-01-27 00:56:37.519192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ef211b5f5101"
down_revision = "dd882601923c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
