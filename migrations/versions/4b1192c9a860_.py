"""empty message

Revision ID: 4b1192c9a860
Revises: d03209c2f8f2
Create Date: 2019-03-12 11:24:05.087218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b1192c9a860'
down_revision = 'd03209c2f8f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('resnumber', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'resnumber')
    # ### end Alembic commands ###
