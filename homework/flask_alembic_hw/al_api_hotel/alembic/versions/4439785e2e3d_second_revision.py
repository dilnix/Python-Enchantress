"""Second revision

Revision ID: 4439785e2e3d
Revises: 8070904a4954
Create Date: 2021-03-18 17:48:51.593033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4439785e2e3d'
down_revision = '8070904a4954'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pet',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=True),
        sa.Column('owner_id', sa.INTEGER(), nullable=False),
        sa.Column('room_num', sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    pass
