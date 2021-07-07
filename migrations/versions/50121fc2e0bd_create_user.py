"""create-user

Revision ID: 50121fc2e0bd
Revises: 
Create Date: 2021-07-03 10:42:00.594383

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid


# revision identifiers, used by Alembic.
revision = '50121fc2e0bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    sa.Column('uuid', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('uuid', name=op.f('uq_users_uuid'))
    )
    op.create_table('portfolios',
    sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    sa.Column('portfolio_name', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_portfolios_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_portfolios'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolios')
    op.drop_table('users')
    # ### end Alembic commands ###
