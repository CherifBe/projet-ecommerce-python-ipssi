"""first migration

Revision ID: d06825e3a447
Revises: 
Create Date: 2023-08-10 15:55:23.601950

"""
from alembic import op
import sqlalchemy as sa
from model.user_model import User
# revision identifiers, used by Alembic.
revision = 'd06825e3a447'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        User,
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("firstname", sa.String(length=60), nullable=False),
        sa.Column("lastname", sa.String(length=60), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False)
    )


def downgrade():
    op.drop_table(
        User
    )
