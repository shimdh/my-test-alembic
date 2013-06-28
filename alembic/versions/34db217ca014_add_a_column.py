"""Add a column

Revision ID: 34db217ca014
Revises: 10ffdc400730
Create Date: 2013-06-28 21:10:01.870000

"""

# revision identifiers, used by Alembic.
revision = '34db217ca014'
down_revision = '10ffdc400730'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account', 'last_transaction_date')
