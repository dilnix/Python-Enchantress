"""Third revision

Revision ID: e0cd94a9f487
Revises: 4439785e2e3d
Create Date: 2021-03-18 17:59:58.479675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0cd94a9f487'
down_revision = '4439785e2e3d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'activity',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('pet_id', sa.INTEGER(), nullable=False),
        sa.Column('activity_type', sa.String(length=50), nullable=True),
        sa.Column('time', sa.Time(), nullable=True),
        sa.ForeignKeyConstraint(['pet_id'], ['pet.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    pass
