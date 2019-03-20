"""empty message

Revision ID: 2e23c4f64919
Revises: 4b1192c9a860
Create Date: 2019-03-12 11:25:31.081167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e23c4f64919'
down_revision = '4b1192c9a860'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('toolnumber', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'toolnumber')
    # ### end Alembic commands ###
