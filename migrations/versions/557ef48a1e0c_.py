"""empty message

Revision ID: 557ef48a1e0c
Revises: 
Create Date: 2019-03-18 13:49:34.590449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '557ef48a1e0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('address', sa.String(length=255), nullable=False))
    op.add_column('order', sa.Column('consignee', sa.String(length=68), nullable=False))
    op.add_column('order', sa.Column('phone', sa.String(length=11), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'phone')
    op.drop_column('order', 'consignee')
    op.drop_column('order', 'address')
    # ### end Alembic commands ###
