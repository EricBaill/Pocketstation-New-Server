"""empty message

Revision ID: 4b6b10bbe9f3
Revises: a39a3a6934cf
Create Date: 2019-03-12 10:41:23.828411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b6b10bbe9f3'
down_revision = 'a39a3a6934cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('number', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'number')
    # ### end Alembic commands ###
