"""empty message

Revision ID: 2faba483e5e3
Revises: 
Create Date: 2020-12-04 03:33:42.083817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2faba483e5e3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Movies',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('genres', sa.String(), nullable=True),
    sa.Column('embedding', sa.PickleType(), nullable=True),
    sa.Column('release_date', sa.String(), nullable=True),
    sa.Column('runtime', sa.Float(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('movie', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('movie', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['movie'], ['Movies.id'], ),
    sa.ForeignKeyConstraint(['user'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Lists')
    op.drop_table('Users')
    op.drop_table('Movies')
    # ### end Alembic commands ###