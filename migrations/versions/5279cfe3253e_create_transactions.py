"""create-transactions

Revision ID: 5279cfe3253e
Revises: 50121fc2e0bd
Create Date: 2021-07-05 00:19:57.192169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5279cfe3253e'
down_revision = '50121fc2e0bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('purchase_date', sa.DateTime(), nullable=False),
    sa.Column('coinAmount', sa.Float(), nullable=False),
    sa.Column('spot_price', sa.Float(), nullable=False),
    sa.Column('exchange', sa.String(length=40), nullable=False),
    sa.Column('fiat', sa.String(length=40), nullable=False),
    sa.Column('coin_id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolios.id'], name=op.f('fk_transactions_portfolio_id_portfolios')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_transactions'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###