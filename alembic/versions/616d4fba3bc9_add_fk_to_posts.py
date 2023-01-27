"""add fk to posts

Revision ID: 616d4fba3bc9
Revises: 1c07cd19157e
Create Date: 2023-01-27 01:05:53.861547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "616d4fba3bc9"
down_revision = "1c07cd19157e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts','owner_id')
    pass
