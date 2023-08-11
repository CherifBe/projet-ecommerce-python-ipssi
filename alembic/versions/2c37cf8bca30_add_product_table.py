"""add product table

Revision ID: 2c37cf8bca30
Revises: d06825e3a447
Create Date: 2023-08-11 11:55:05.025679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c37cf8bca30'
down_revision = 'd06825e3a447'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'product',
        sa.Column('id',sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=60), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=False),
        sa.Column('image', sa.String(length=255), nullable=True),
        sa.Column('price', sa.Integer, nullable=False),
        sa.Column('stock', sa.Integer, nullable=False)
    )

def downgrade():
    op.drop_table(
        'product'
    )