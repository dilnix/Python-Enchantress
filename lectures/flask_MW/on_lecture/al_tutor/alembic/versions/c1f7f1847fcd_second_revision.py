"""Second revision

Revision ID: c1f7f1847fcd
Revises: 7ed0be111ce9
Create Date: 2021-03-11 19:59:26.765895

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'c1f7f1847fcd'
down_revision = '7ed0be111ce9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pets',
        sa.Column('id', postgresql.INTEGER(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('owner', sa.String(200))
    )


def downgrade():
    op.drop_table('pets')
