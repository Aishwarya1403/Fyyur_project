"""empty message

Revision ID: 6acad7d52248
Revises: 0dfccd1849a2
Create Date: 2020-05-19 01:52:41.390112

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6acad7d52248'
down_revision = '0dfccd1849a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Show', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('Show', 'artist_name')
    op.drop_column('Show', 'image_link')
    op.drop_column('Show', 'venue_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('venue_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Show', sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.add_column('Show', sa.Column('artist_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.alter_column('Show', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###
