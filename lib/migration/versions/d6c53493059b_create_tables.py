"""create tables

Revision ID: d6c53493059b
Revises: 
Create Date: 2024-09-22 18:41:47.340785

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6c53493059b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('real_estate',
    sa.Column('estate_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('property_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('estate_id')
    )
    op.create_table('property_managers',
    sa.Column('manager_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('contact', sa.String(length=20), nullable=True),
    sa.Column('estate_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['estate_id'], ['real_estate.estate_id'], ),
    sa.PrimaryKeyConstraint('manager_id')
    )
    op.create_table('land_owners',
    sa.Column('owner_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('phone_number', sa.String(length=30), nullable=True),
    sa.Column('date_of_acquisition', sa.String(length=45), nullable=True),
    sa.Column('manager_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['manager_id'], ['property_managers.manager_id'], ),
    sa.PrimaryKeyConstraint('owner_id')
    )
    op.create_table('lands',
    sa.Column('land_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('place', sa.String(length=30), nullable=True),
    sa.Column('size', sa.String(length=20), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['land_owners.owner_id'], ),
    sa.PrimaryKeyConstraint('land_id'),
    sa.UniqueConstraint('owner_id')
    )
    op.create_table('lands_managers',
    sa.Column('lm_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('land_id', sa.Integer(), nullable=True),
    sa.Column('manager_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['land_id'], ['lands.land_id'], ),
    sa.ForeignKeyConstraint(['manager_id'], ['property_managers.manager_id'], ),
    sa.PrimaryKeyConstraint('lm_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lands_managers')
    op.drop_table('lands')
    op.drop_table('land_owners')
    op.drop_table('property_managers')
    op.drop_table('real_estate')
    # ### end Alembic commands ###
