"""create account table

Revision ID: 10ffdc400730
Revises: None
Create Date: 2013-06-28 21:03:00.206000

"""

# revision identifiers, used by Alembic.
revision = '10ffdc400730'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')
