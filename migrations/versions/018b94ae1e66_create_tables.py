"""create-tables

Revision ID: 018b94ae1e66
Revises: 
Create Date: 2021-07-08 09:46:35.056459

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '018b94ae1e66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('device_id', sa.String(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('device_id', name=op.f('uq_users_device_id'))
    )
    op.create_table('portfolios',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('portfolio_name', sa.String(length=80), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_portfolios_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_portfolios'))
    )
    op.create_table('transactions',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('purchase_date', sa.DateTime(), nullable=False),
    sa.Column('coin_amount', sa.Float(), nullable=False),
    sa.Column('spot_price', sa.Float(), nullable=False),
    sa.Column('exchange', sa.String(length=40), nullable=False),
    sa.Column('fiat', sa.String(length=40), nullable=False),
    sa.Column('coin_id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolios.id'], name=op.f('fk_transactions_portfolio_id_portfolios')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_transactions_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_transactions'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('portfolios')
    op.drop_table('users')
    # ### end Alembic commands ###