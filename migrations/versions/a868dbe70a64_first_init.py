"""first init

Revision ID: a868dbe70a64
Revises: 
Create Date: 2021-10-23 11:47:55.399148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a868dbe70a64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room', sa.String(length=256), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('company', sa.String(length=256), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('adress', sa.String(length=128), nullable=False),
    sa.Column('zip_code', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=64), nullable=False),
    sa.Column('land', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    # ### end Alembic commands ###
