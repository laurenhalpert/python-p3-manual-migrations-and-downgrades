"""try again

Revision ID: acfee44a91da
Revises: c49b90c3610a
Create Date: 2023-05-10 09:30:49.959692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acfee44a91da'
down_revision = 'c49b90c3610a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("students", "birthday", new_column_name="date_of_birth")


def downgrade() -> None:
    op.alter_column("students", "date_of_birth", new_column_name="birthday")
