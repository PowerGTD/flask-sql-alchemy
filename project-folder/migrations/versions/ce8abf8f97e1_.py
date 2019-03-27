"""empty message

Revision ID: ce8abf8f97e1
Revises: 1095dacb282c
Create Date: 2019-03-26 18:51:51.904848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce8abf8f97e1'
down_revision = '1095dacb282c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('member', 'course_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('member', 'course_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
