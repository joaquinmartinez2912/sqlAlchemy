"""create_table_provincias

Revision ID: 9e80dd2fa474
Revises: 5dd5963a27ed
Create Date: 2023-06-06 20:40:27.694984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e80dd2fa474'
down_revision = '5dd5963a27ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provincia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('pais', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pais'], ['pais.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('provincia')
    # ### end Alembic commands ###
