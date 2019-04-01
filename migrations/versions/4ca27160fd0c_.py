"""empty message

Revision ID: 4ca27160fd0c
Revises: e3c45106b25d
Create Date: 2019-03-20 10:01:45.772571

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4ca27160fd0c'
down_revision = 'e3c45106b25d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('points', 'sumprice',
               existing_type=mysql.FLOAT(),
               nullable=False)
    op.alter_column('points', 'total_points',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('points', 'total_points',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('points', 'sumprice',
               existing_type=mysql.FLOAT(),
               nullable=True)
    # ### end Alembic commands ###