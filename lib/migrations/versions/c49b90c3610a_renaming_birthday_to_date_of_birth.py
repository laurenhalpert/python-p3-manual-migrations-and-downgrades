"""Renaming birthday to date of birth

Revision ID: c49b90c3610a
Revises: 427e50c91617
Create Date: 2023-05-10 09:15:48.355663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c49b90c3610a'
down_revision = '427e50c91617'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("students", "birthday", "date_of_birth")


def downgrade() -> None:
    op.alter_column("students", "date_of_birth", "birthday")
