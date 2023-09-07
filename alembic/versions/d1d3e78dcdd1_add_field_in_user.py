"""add field in user

Revision ID: d1d3e78dcdd1
Revises: e0172145eeb9
Create Date: 2023-09-07 12:21:52.316909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1d3e78dcdd1'
down_revision = 'e0172145eeb9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('users', sa.Column('birth_of_day', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'birth_of_day')
    op.drop_column('users', 'gender')
    # ### end Alembic commands ###
