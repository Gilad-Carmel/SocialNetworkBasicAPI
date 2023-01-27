"""add columns to post table

Revision ID: b21ab3093ce4
Revises: 616d4fba3bc9
Create Date: 2023-01-27 01:10:49.319404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b21ab3093ce4'
down_revision = '616d4fba3bc9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'is_published',
        sa.Boolean, server_default="TRUE", nullable=False
    ))
    op.add_column('posts', sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")
    ))

def downgrade() -> None:
    op.drop_column('posts', 'is_published')
    op.drop_column('posts', 'created_at')
    pass
